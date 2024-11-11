from sqlalchemy.orm import Session
import json

from app.game.carta_movimiento.models import Carta_Movimiento, movimientos
from app.game.carta_movimiento.schemas import *
import app.home.home_repository as home_repository
import app.game.carta_movimiento.logic as carta_movimiento_logic

with open('app/game/carta_movimiento/cartas_movimiento.json', 'r') as file:
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
    create_movimientos_db(db, id_partida_in)
    return cartas_movimiento

def create_movimientos_db(db: Session, id_partida_in: int):

    mov = []
    for i in range(1, 4):
        db_movimiento = movimientos(
            id_mov=i,
            id_partida=id_partida_in,
            id_carta_mov=0,
            id_ficha1=0,
            id_ficha2=0,
        )
        db.add(db_movimiento)
        mov.append(db_movimiento)
        db.commit()
    return mov

def get_cartas_movimiento_db(db: Session, id_partida_in: int):
    return db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida_in).all()

def get_carta_movimiento_db(db: Session, id_partida: int, player_id: str):
    return db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida, Carta_Movimiento.id_player == player_id).all()

def get_carta_movimiento_id_db(db: Session, id_partida: int, id_carta: int):
    return db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida, Carta_Movimiento.id_carta == id_carta).first()   

def get_movimientos_db(db: Session, id_partida: int):
    return db.query(movimientos).filter(movimientos.id_partida == id_partida).all()

def get_ultimo_movimiento_con_carta_db(db: Session, id_partida_in: int):
    return db.query(movimientos).filter(movimientos.id_carta_mov != 0, movimientos.id_partida == id_partida_in).order_by(movimientos.id.desc()).first()

def get_cantidad_movimientos_db(db, partida_id: int) -> int:
    return db.query(movimientos).filter(movimientos.id_partida == partida_id, movimientos.id_carta_mov !=0).count()

def get_mano_cartas_movimiento_db(db: Session, id_partida: int, player_id: str):
    return db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida, Carta_Movimiento.id_player == player_id, Carta_Movimiento.gastada == False).all()

def reset_movimientos_db(db: Session, id_partida: int):
    movimientos = get_movimientos_db(db, id_partida)
    for movimiento in movimientos:
        movimiento.id_carta_mov = 0
        movimiento.id_ficha1 = 0
        movimiento.id_ficha2 = 0
    db.commit()

def asignar_cartas_movimiento(db: Session, id_partida: int):
    cartas_movimiento = get_cartas_movimiento_db(db, id_partida)
    players = home_repository.get_jugadores_db(db, id_partida)
    players_utiles = [player for player in players if player != ""]
    for player in players_utiles:
        cartas_movimiento = carta_movimiento_logic.asignar_cartas_movimiento(cartas_movimiento, player) 
    db.commit()
    return cartas_movimiento

def asignar_cartas_movimiento_1(db: Session, id_partida: int, player_id: str):
    cartas_movimiento = get_cartas_movimiento_db(db, id_partida)
    cartas_movimiento = carta_movimiento_logic.asignar_cartas_movimiento(cartas_movimiento, player_id)   
    db.commit()
    return cartas_movimiento

def desasignar_cartas_movimiento(db: Session, id_partida: int, player_id: str):
    cartas_movimiento = get_carta_movimiento_db(db, id_partida, player_id)
    carta_movimiento_logic.validar_jugador(id_partida, player_id, db)
    for carta_movimiento in cartas_movimiento:
        carta_movimiento.id_player = ""
    db.commit()
    return cartas_movimiento

def delete_cartas_movimiento_db(db: Session, id_partida: int):
    db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == id_partida).delete()
    db.commit()
    return None

def usar_carta_movimiento_db(db: Session, id_carta: int, id_ficha1: int, id_ficha2: int, partida_id: int):
    carta_movimiento_logic.usar_carta_movimiento(db, partida_id, id_carta, id_ficha1, id_ficha2)
    agregar_movimiento_db(db, id_carta, id_ficha1, id_ficha2, partida_id)
    db.commit()
    return

def agregar_movimiento_db(db: Session, id_carta: int, id_ficha1: int, id_ficha2: int, partida_id: int):
    movimientos = get_movimientos_db(db, partida_id)
    for movimiento in movimientos:
        if movimiento.id_carta_mov == 0:
            movimiento.id_carta_mov = id_carta
            movimiento.id_ficha1 = id_ficha1
            movimiento.id_ficha2 = id_ficha2
            break
    db.commit()
    return

def sacar_mov_db(db: Session, id_partida: int, mov_id: int):
    mov = db.query(movimientos).filter(movimientos.id_partida == id_partida, movimientos.id_mov == mov_id).first()
    mov.id_carta_mov = 0
    mov.id_ficha1 = 0
    mov.id_ficha2 = 0
    db.commit()
    return

def deshacer_carta_movimiento_db(db: Session, partida_id: int):
    movimientos = carta_movimiento_logic.deshacer_carta_movimiento(db,partida_id)
    sacar_mov_db(db, partida_id, movimientos)
    db.commit()
    return

def aplicar_movimiento_db(db: Session, id_partida_in: int, id_carta_in: int):
    carta_movimiento = get_carta_movimiento_id_db(db, id_partida_in, id_carta_in)
    if carta_movimiento is None:
        return
    carta_movimiento.gastada = False
    carta_movimiento.id_player = ""
    db.commit()
    return

def delete_movimientos_db(db, partida_id):
    db.query(movimientos).filter(movimientos.id_partida == partida_id).delete()
    db.commit()
    return None