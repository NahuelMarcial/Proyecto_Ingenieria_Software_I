from sqlalchemy.orm import Session
from fastapi import HTTPException
import json

from app.carta_movimiento.models import Carta_Movimiento
from app.partida.models import Partida
from app.carta_movimiento.schemas import *
import app.partida.partida_repository as partida_repository
import app.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.carta_movimiento.utils as carta_movimiento_utils

with open('app/carta_movimiento/cartas_movimiento.json', 'r') as file:
    cartas_movimiento_data = json.load(file)
def create_set_cartas_movimiento_db(db:Session , id_partida_in: int): 
    cartas_movimiento = []
    for carta_movimiento in cartas_movimiento_data:
        db_carta_movimiento = Carta_Movimiento(
            id_partida=id_partida_in,
            id_carta=carta_movimiento["id_carta"],
            tipo_movimiento=carta_movimiento["tipo_movimiento"],
            descartada=False,
            id_player=""
        )
        db.add(db_carta_movimiento)
        cartas_movimiento.append(db_carta_movimiento)
    db.commit()
    return cartas_movimiento

def get_cartas_movimiento_db(db: Session, id_partida_in: int):
    return db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida_in).all()

def get_carta_movimiento_db(db: Session, id_partida: int, player_id: str):
    return db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida, Carta_Movimiento.id_player == player_id).all()
    
def asignar_cartas_movimiento(db: Session, id_partida: int):
    cartas_movimiento = get_cartas_movimiento_db(db, id_partida)
    players = partida_repository.get_jugadores_db(db, id_partida)
    players_utiles = [player for player in players if player != ""]
    for player in players_utiles:
        cartas_movimiento = carta_movimiento_utils.asignar_cartas_movimiento(cartas_movimiento, player) 
    db.commit()
    return cartas_movimiento

def asignar_cartas_movimiento_1(db: Session, id_partida: int, player_id: str):
    cartas_movimiento = get_cartas_movimiento_db(db, id_partida)
    cartas_movimiento = carta_movimiento_utils.asignar_cartas_movimiento(cartas_movimiento, player_id)   
    db.commit()
    return cartas_movimiento

def desasignar_cartas_movimiento(db: Session, id_partida: int, player_id: str):
    cartas_movimiento = get_carta_movimiento_db(db, id_partida, player_id)
    carta_movimiento_utils.validar_jugador(id_partida, player_id, db)
    for carta_movimiento in cartas_movimiento:
        carta_movimiento.id_player = ""
    db.commit()
    return cartas_movimiento
def delete_cartas_movimiento_db(db: Session, id_partida: int):
    db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida).delete()
    db.commit()
    return None