from sqlalchemy.orm import Session
from fastapi import HTTPException
import json
import random

from app.carta_figura.models import Carta_Figura
from app.carta_figura.schemas import *
import app.carta_figura.utils as carta_figura_utils
import app.partida.partida_repository as partida_repository 

with open('app/carta_figura/cartas_figura.json', 'r') as file:
    cartas_figura_data = json.load(file)

def create_set_carta_figuras_db(db: Session, id_partida_in: int):
    cartas_figura = []
    for carta_figura in cartas_figura_data:
        db_carta_figura = Carta_Figura(
            id_carta=carta_figura["id_carta"],
            nombre=carta_figura["nombre"],
            color=carta_figura["color"],
            id_partida=id_partida_in,
            id_player="",
            mostrar=False,
            descartada=False,
            bloqueada=False,
            reponer=False
        )
        db.add(db_carta_figura)
        cartas_figura.append(db_carta_figura)
    db.commit()
    return cartas_figura

def get_cartas_figura_db(db: Session, id_partida_in: int):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida_in).all()

def get_cartas_figura_mostradas_db(db: Session, id_partida_in: int):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida_in, Carta_Figura.mostrar == True).all()

def asignar_cartas_figura(db: Session, id_partida: int):
    cartas_figura = get_cartas_figura_db(db, id_partida)
    players = partida_repository.get_jugadores_db(db, id_partida)
    cartas_figura = carta_figura_utils.asignar_cartas_figura(cartas_figura, players)
    db.commit()
    return cartas_figura

def get_cartas_jugador_nodescartadas_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player, Carta_Figura.descartada == False).all()

def get_cartas_jugador_mostradas_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player, Carta_Figura.mostrar == True).all()



def reponer_cartas_jugador_db(db: Session, partida_id: int, player_id: str):
    cartas_figura = get_cartas_jugador_nodescartadas_db(db, partida_id, player_id)
    mostradas = get_cartas_jugador_mostradas_db(db, partida_id, player_id)

    
    while len(mostradas) < 3:
        if not cartas_figura:
            break
        carta_random = random.choice(cartas_figura)
        carta_random.mostrar = True
        mostradas.append(carta_random)
        cartas_figura.remove(carta_random)
    
    db.commit()
    return mostradas
def delete_cartas_figura_db(db: Session, id_partida: int):
    db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida).delete()
    db.commit()
    return None
