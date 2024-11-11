from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db

from app.game.fichas.schemas import *
from app.game.carta_movimiento.schemas import *
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.carta_movimiento.logic as carta_movimiento_logic
import app.game.carta_movimiento.socket_carta_movimiento as socket_carta_movimiento
import app.game.carta_movimiento.movimientos_logic as movimientos_logic
import app.game.fichas.logic as fichas_logic
import app.game.game_repository as game_repository
import app.game.fichas.fichas_repository as fichas_repository
router = APIRouter()


@router.post("/set", response_model= list [Carta_Movimiento_new])
async def create_set_carta_movimiento(partida_id: int , db : Session =Depends(get_db)):
   error = carta_movimiento_logic.validar_partida(partida_id, db) 
   if not error :
        carta_movimiento_repository.create_set_cartas_movimiento_db(db, partida_id)
        carta_movimiento_repository.asignar_cartas_movimiento(db, partida_id)
        await socket_carta_movimiento.set_creado(partida_id)
        return carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
   else : 
        raise HTTPException(status_code=400, detail="Error al crear el set de cartas movimiento")

@router.get("/get", response_model= list [Carta_Movimiento_new])
def get_cartas_movimiento(partida_id: int, db: Session = Depends(get_db)):
    error = carta_movimiento_logic.validar_partida_ini(partida_id, db)
    if not error:
        return carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas movimiento de la partida")

@router.get("/get_cartas_jugador/{player_id}", response_model=list[Carta_Movimiento_new])
def get_carta_movimiento(partida_id: int, player_id: str, db: Session = Depends(get_db)):
    error = carta_movimiento_logic.validar_jugador(partida_id, player_id, db)
    if not error:
        return carta_movimiento_repository.get_carta_movimiento_db(db, partida_id, player_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas movimiento del jugador")

@router.patch("/reponer_ini", response_model= list [Carta_Movimiento_new])
def asignar_cartas_movimiento(partida_id: int, db: Session = Depends(get_db)):
    error = carta_movimiento_logic.validar_partida_ini(partida_id, db)
    if not error:
        carta_movimiento_repository.asignar_cartas_movimiento(db, partida_id)
        return carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al reponer las cartas movimiento")
    

@router.patch("/reponer_jugador", response_model= list [Carta_Movimiento_new])
def asignar_cartas_movimiento_1(partida_id: int, jugador: JugadorID, db: Session = Depends(get_db)):
    error = carta_movimiento_logic.validar_jugador(partida_id, jugador.id_player, db)
    if not error:
        carta_movimiento_repository.get_cartas_movimiento_db(db,partida_id)
        carta_movimiento_repository.asignar_cartas_movimiento_1(db, partida_id, jugador.id_player)
        return carta_movimiento_repository.get_carta_movimiento_db(db, partida_id, jugador.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al reponer las cartas movimiento")

@router.patch("/usar_carta_movimiento", response_model= list [Carta_Movimiento_new])
async def usar_carta_movimiento(partida_id : int ,request: movimientoData ,db: Session = Depends(get_db)):
    error_partida= carta_movimiento_logic.validar_partida_ini(partida_id, db)
    error_mov = (not movimientos_logic.movimiento(db, partida_id, request.id_carta, request.id_ficha1, request.id_ficha2))
    if error_mov:
        raise HTTPException(status_code=400, detail="Movimiento no coincide con las fichas")
    error_jug = carta_movimiento_logic.validar_jugador(partida_id, request.id_jugador, db)
    error_carta = carta_movimiento_logic.validar_carta_movimiento(partida_id, request.id_carta, request.id_jugador, db)
    error_fichas = fichas_logic.validar_fichas(db, partida_id, request.id_ficha1, request.id_ficha2)
    error = error_partida or  error_carta or error_mov or error_jug or  error_fichas

    if not error:
        carta_movimiento_repository.usar_carta_movimiento_db(db,request.id_carta ,request.id_ficha1, request.id_ficha2, partida_id)
        data = {"partida_id": partida_id} 
        await socket_carta_movimiento.movimiento_usado(data)
        return carta_movimiento_repository.get_carta_movimiento_db(db,partida_id,request.id_jugador )
    else:
        raise HTTPException(status_code=400, detail="Movimiento invalido")
    
@router.patch("/deshacer_movimiento", response_model= list [Carta_Movimiento_new])
async def deshacer_movimiento(partida_id : int ,jugador_id: JugadorID, db: Session = Depends(get_db)):
    error_jugador = carta_movimiento_logic.validar_jugador(partida_id, jugador_id.id_player, db)
    error_turno = carta_movimiento_logic.validar_turno(partida_id, jugador_id.id_player, db)
    error_fichas = fichas_logic.validar_partida_exist(partida_id, db)
    error = error_jugador or error_turno or error_fichas
    if not error:
    
        carta_movimiento_repository.deshacer_carta_movimiento_db(db, partida_id)
        await socket_carta_movimiento.movimiento_desecho({"partida_id": partida_id})
        return carta_movimiento_repository.get_carta_movimiento_db(db,partida_id,jugador_id.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al deshacer el movimiento")
    
@router.get("/get_movimientos_posibles/{id_carta}/{id_ficha}", response_model= list[FichaData])
def get_movimientos_posibles(partida_id : int, id_carta:int, id_ficha:int, db: Session = Depends(get_db)):
    error_partida= carta_movimiento_logic.validar_partida_ini(partida_id, db)
    error_ficha= fichas_logic.validar_ficha(db, partida_id, id_ficha)
    error_carta = carta_movimiento_logic.validar_carta_movimiento_existe(partida_id, id_carta, db)
    error = error_partida or error_carta or error_ficha
    if not error:
        if not game_repository.get_dificultad_db(db, partida_id):
            return movimientos_logic.movimientos_posibles(db, partida_id, id_carta, id_ficha)
        else : 
            return fichas_repository.get_fichas_db(db, partida_id)        
    else:
        raise HTTPException(status_code=400, detail="Error al obtener los movimientos posibles")
