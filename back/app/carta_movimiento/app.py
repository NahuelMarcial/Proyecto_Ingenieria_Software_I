from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db


from app.carta_movimiento.schemas import *
import app.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.carta_movimiento.utils as carta_movimiento_utils
import app.partida.partida_repository as partida_repository

router = APIRouter()


@router.post("/set/{partida_id}", response_model= list [Carta_Movimiento_new])
def create_set_carta_movimiento(partida_id: int , db : Session =Depends(get_db)):
   error = carta_movimiento_utils.validar_partida(partida_id, db) 
   if not error :
       carta_movimiento_repository.create_set_cartas_movimiento_db(db, partida_id)
       carta_movimiento_repository.asignar_cartas_movimiento(db, partida_id)
       return carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
   else : 
       raise HTTPException(status_code=400, detail="Error al crear el set de cartas movimiento")

@router.get("/get/{partida_id}", response_model= list [Carta_Movimiento_new])
def get_cartas_movimiento(partida_id: int, db: Session = Depends(get_db)):
    error = carta_movimiento_utils.validar_partida_ini(partida_id, db)
    if not error:
        return carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas movimiento de la partida")
       

@router.get("/get_cartas_jugador/{partida_id}/{player_id}", response_model=list[Carta_Movimiento_new])
def get_carta_movimiento(partida_id: int, player_id: str, db: Session = Depends(get_db)):
    error = carta_movimiento_utils.validar_jugador(partida_id, player_id, db)
    if not error:
        return carta_movimiento_repository.get_carta_movimiento_db(db, partida_id, player_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas movimiento del jugador")
    
    

@router.patch("/reponer_ini/{partida_id}", response_model= list [Carta_Movimiento_new])
def asignar_cartas_movimiento(partida_id: int, db: Session = Depends(get_db)):
    error = carta_movimiento_utils.validar_partida_ini(partida_id, db)
    if not error:
        carta_movimiento_repository.asignar_cartas_movimiento(db, partida_id)
        return carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al reponer las cartas movimiento")
    

@router.patch("/reponer_jugador/{partida_id}", response_model= list [Carta_Movimiento_new])
def asignar_cartas_movimiento_1(partida_id: int, jugador: JugadorID, db: Session = Depends(get_db)):
    error = carta_movimiento_utils.validar_jugador(partida_id, jugador.id_player, db)
    if not error:
        carta_movimiento_repository.get_cartas_movimiento_db(db,partida_id)
        carta_movimiento_repository.asignar_cartas_movimiento_1(db, partida_id, jugador.id_player)
        return carta_movimiento_repository.get_carta_movimiento_db(db, partida_id, jugador.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al reponer las cartas movimiento")

