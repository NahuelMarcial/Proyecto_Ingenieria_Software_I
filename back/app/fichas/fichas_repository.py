from sqlalchemy.orm import Session
from fastapi import HTTPException
from random import randint

from app.fichas.models import Ficha ,Color
from app.fichas.schemas import *



def create_fichas_db(db: Session, partida_id: int):
    colores = [Color.azul, Color.rojo, Color.verde, Color.amarillo]
    id=0
    for color in colores:
        for _ in range(9):
            ficha = Ficha(
                id_ficha=id,  # O cualquier lógica que uses para el ID
                id_partida=partida_id,
                color=color,  # Ajusta según sea necesario
                pos_x=0,
                pos_y=0
            )
            db.add(ficha)
            id += 1
    db.commit()


def assign_random_positions_db(db: Session, partida_id: int):
    fichas = db.query(Ficha).filter(Ficha.id_partida == partida_id).all()
    
    posiciones = [(x, y) for x in range(1, 7) for y in range(1, 7)]
    
    for ficha in fichas:
        if posiciones:
            pos = posiciones.pop(randint(0, len(posiciones) - 1))
            ficha.pos_x, ficha.pos_y = pos
    db.commit()


def get_fichas_db(db: Session, id_partida_in: int):
    return db.query(Ficha).filter(Ficha.id_partida == id_partida_in).all()

def delete_fichas_db(db: Session, id_partida: int):
    db.query(Ficha).filter(Ficha.id_partida == id_partida).delete()
    db.commit()
    return None