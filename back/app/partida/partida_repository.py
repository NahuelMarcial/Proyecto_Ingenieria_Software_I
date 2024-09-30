from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.partida.models import Partida
from app.partida.schemas import *
import app.partida.utils as utils
from app.carta_movimiento import carta_movimiento_repository as carta_movimiento_repository
from app.carta_figura import carta_figura_repository as carta_figura_repository
from app.fichas import fichas_repository as fichas_repository
def create_new_partida_db(db: Session, partida: PartidaCreate):
    db_partida = Partida(
        nombre=partida.nombre,
        owner=partida.owner,
        max_jugadores=partida.max_jugadores,
        jugador1=partida.owner
    )
    db.add(db_partida)
    db.commit()
    db.refresh(db_partida)
    return db_partida

def get_partida_db(db: Session, partida_id: int):
    partida = db.query(Partida).filter(Partida.id == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    return partida

def get_partidas_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Partida).filter(Partida.cantidad_jugadores < Partida.max_jugadores,
                                    Partida.iniciada == False).limit(limit).all()

def get_all_partidas_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Partida).offset(skip).limit(limit).all()

def get_jugadores_db(db: Session, partida_id: int):
    partida = get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    return jugadores


def agregar_jugador_db(partida_id, jugador, db):

    partida = get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]

    utils.validar_unirse(partida)
    jugadores = utils.agregar_jugador(jugadores, jugador, partida)

    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores

    db.commit()
    db.refresh(partida)

    return partida

