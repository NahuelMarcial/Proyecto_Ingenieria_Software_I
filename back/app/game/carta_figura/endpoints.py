from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db

from app.game.carta_figura.schemas import *
import app.lobby.app as lobby_app
import app.game.carta_figura.carta_figura_repository as carta_figura_repository
import app.game.carta_figura.logic as carta_figura_logic
import app.game.carta_figura.socket_carta_figura as socket_carta_figura
import app.game.logic as game_logic
import app.game.socket_game as socket_game
import app.game.game_repository as game_repository
import app.home.home_repository as home_repository
router = APIRouter()

@router.post("/set", response_model= list [Carta_Figura_new])
async def create_set_carta_figuras(partida_id: int, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_partida_crear_set(partida_id, db)
    if not error:
        carta_figura_repository.create_set_carta_figuras_db(db, partida_id)
        carta_figura_repository.asignar_cartas_figura(db, partida_id)
        carta_figura_logic.reponer_cartas_ini(partida_id, db)
        await socket_carta_figura.set_creado(partida_id)
        return carta_figura_repository.get_cartas_figura_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al crear el set de cartas figura")
    
@router.patch("/reponer_cartas_ini", response_model= list [Carta_Figura_new])
def reponer_cartas_ini(partida_id: int, db: Session = Depends(get_db)):
    carta_figura_logic.reponer_cartas_ini(partida_id, db)
    return carta_figura_repository.get_cartas_figura_mostradas_db(db, partida_id)

    
@router.patch("/reponer_cartas_jugador", response_model= list [Carta_Figura_new])
def reponer_cartas_jugador (partida_id: int, player_id: PlayerId, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_reponer_cartas_jugador(partida_id, player_id.id_player, db)
    if not error:
        carta_figura_repository.reponer_cartas_jugador_db(db, partida_id, player_id.id_player)
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, player_id.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al reponer cartas jugador")
    
@router.get("/mano", response_model= list [Carta_Figura_new])
def get_cartas_figura(partida_id: int, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_partida_exist(partida_id, db)
    if not error:
        return carta_figura_repository.get_cartas_figura_mostradas_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas figura")
    
@router.get("/mano_jugador/{jugador_id}", response_model= list [Carta_Figura_new])
def get_cartas_figura_jugador(partida_id: int, jugador_id: str, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_partida_exist(partida_id, db) or carta_figura_logic.validar_jugador_exist(partida_id, jugador_id, db)
    if not error:
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, jugador_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas figura")
    
@router.patch("/jugar_carta", response_model= list [Carta_Figura_new])
async def jugar_carta(partida_id: int, data: JugarCarta, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_jugar_carta(partida_id, data.id_carta, data.id_player, db)
    if not error:
        carta_figura_repository.jugar_carta_db(db, partida_id, data.id_carta, data.id_ficha)
        await socket_carta_figura.carta_jugada_figura(partida_id)
        cartas_en_mano=carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, data.id_player)

        if len(cartas_en_mano) == 1:
            carta_figura_repository.desbloquear_carta_db(db, partida_id, cartas_en_mano)
        
        ganador = game_logic.verificar_ganador(db, partida_id)
        if ganador != "":
            jugadores = await lobby_app.get_jugadores(partida_id, db)
            data_s = {'partida_id': partida_id, 'jugadores': jugadores}
            await socket_game.jugador_gana(data_s)
            
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, data.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al jugar carta")
    
@router.patch("/cheat_descartar", response_model= list [Carta_Figura_new])
async def cheat_descartar(partida_id: int, data: PlayerId, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_partida_exist(partida_id, db) or carta_figura_logic.validar_jugador_exist(partida_id, data.id_player, db)
    if not error:
        carta_figura_repository.cheat_descartar_db(db, partida_id, data.id_player)
        await socket_carta_figura.carta_jugada_figura(partida_id)
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, data.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al usar el cheat")
    

@router.patch("/bloquear_carta", response_model= list [Carta_Figura_new])
async def bloquear_carta(partida_id: int, data: BloquearCarta, db: Session = Depends(get_db)):
    
    error = carta_figura_logic.validar_bloquear_carta(partida_id, data.id_bloqueador, data.id_carta, data.id_ficha, db)
    if not error:
        bloqueado = carta_figura_repository.get_carta_id_db(db, partida_id, data.id_carta)
        bloqueado = bloqueado.id_player
        carta_figura_repository.bloquear_carta_db(db, partida_id, data.id_carta, data.id_ficha)
        await socket_carta_figura.carta_jugada_figura(partida_id)
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, bloqueado)
    else:
        raise HTTPException(status_code=400, detail="Error al bloquear carta")

@router.get("/cartas_restantes_jugador/{jugador_id}", response_model= Cantidad_Cartas)
def get_cartas_restantes(partida_id: int, jugador_id: str, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_partida_exist(partida_id, db) or carta_figura_logic.validar_jugador_exist(partida_id, jugador_id, db)
    if not error:
        if not game_repository.get_dificultad_db(db, partida_id):
            cantidad = carta_figura_repository.get_cartas_restantes_db(db, partida_id, jugador_id)
            return Cantidad_Cartas(cantidad=cantidad)
        else :
            cantidad = 0
            return Cantidad_Cartas(cantidad=cantidad)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas restantes")

@router.get("/cartas_restantes", response_model= list [CantidadCartasJugador])
def get_cartas_restantes_all(partida_id: int, db: Session = Depends(get_db)):
    error = carta_figura_logic.validar_partida_exist(partida_id, db)
    if not error:
        partida= home_repository.get_partida_db(db, partida_id)
        jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
        cantidad_ret = [] 
        for jugador in jugadores:
            print(jugador)
            if jugador != "":
                cantidad = get_cartas_restantes(partida_id, jugador, db)
                cantidad_ret.append(CantidadCartasJugador(cantidad=cantidad.cantidad, jugador=jugador))
        return cantidad_ret
    
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas restantes")
