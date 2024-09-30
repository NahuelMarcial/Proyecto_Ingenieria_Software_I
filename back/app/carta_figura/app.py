from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db

from app.carta_figura.schemas import *
import app.carta_figura.carta_figura_repository as carta_figura_repository
import app.carta_figura.utils as carta_figura_utils

router = APIRouter()

@router.post("/set/{partida_id}", response_model= list [Carta_Figura_new])
def create_set_carta_figuras(partida_id: int, db: Session = Depends(get_db)):
    error = carta_figura_utils.validar_partida_crear_set(partida_id, db)
    if not error:
        carta_figura_repository.create_set_carta_figuras_db(db, partida_id)
        carta_figura_repository.asignar_cartas_figura(db, partida_id)
        carta_figura_utils.reponer_cartas_ini(partida_id, db)
        return carta_figura_repository.get_cartas_figura_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al crear el set de cartas figura")
    
@router.patch("/reponer_cartas_ini/{partida_id}", response_model= list [Carta_Figura_new])
def reponer_cartas_ini(partida_id: int, db: Session = Depends(get_db)):
    carta_figura_utils.reponer_cartas_ini(partida_id, db)
    return carta_figura_repository.get_cartas_figura_mostradas_db(db, partida_id)

    
@router.patch("/reponer_cartas_jugador/{partida_id}", response_model= list [Carta_Figura_new])
def reponer_cartas_jugador (partida_id: int, player_id: PlayerId, db: Session = Depends(get_db)):
    error = carta_figura_utils.validar_reponer_cartas_jugador(partida_id, player_id.id_player, db)
    if not error:
        carta_figura_repository.reponer_cartas_jugador_db(db, partida_id, player_id.id_player)
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, player_id.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al reponer cartas jugador")
    
@router.get("/mano/{partida_id}", response_model= list [Carta_Figura_new])
def get_cartas_figura(partida_id: int, db: Session = Depends(get_db)):
    error = carta_figura_utils.validar_partida_exist(partida_id, db)
    if not error:
        return carta_figura_repository.get_cartas_figura_mostradas_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas figura")
    
@router.get("/mano_jugador/{partida_id}/{jugador_id}", response_model= list [Carta_Figura_new])
def get_cartas_figura_jugador(partida_id: int, jugador_id: str, db: Session = Depends(get_db)):
    error = carta_figura_utils.validar_partida_exist(partida_id, db) or carta_figura_utils.validar_jugador_exist(partida_id, jugador_id, db)
    if not error:
        return carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, jugador_id)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener las cartas figura")