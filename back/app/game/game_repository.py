from sqlalchemy.orm import Session
from fastapi import HTTPException

import app.home.home_repository as home_repository
import app.game.carta_movimiento.logic as carta_mov_logic
import app.game.logic as game_logic
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.carta_figura.carta_figura_repository as carta_figura_repository
import app.game.fichas.fichas_repository as fichas_repository
from app.home.models import Partida


def pasar_turno(db: Session, partida_id: int):
    partida = home_repository.get_partida_db(db, partida_id)
    jugadores = home_repository.get_jugadores_db(db, partida_id)
    turno = game_logic.pasar_turno(partida, jugadores)
    partida.turno = turno

    db.commit()
    db.refresh(partida)
    return partida

def es_turno_del_jugador(partida: Partida, jugador_id: str):
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    jugador_actual = jugadores[partida.turno - 1] 
    return jugador_actual == jugador_id

async def abandonar_partida_ini(db: Session, partida_id: int, id_player: str):
    partida = home_repository.get_partida_db(db, partida_id)
    jugadores = home_repository.get_jugadores_db(db, partida_id)
    partida = await game_logic.abandonar_partida_ini(partida, jugadores, id_player)

    db.commit()
    db.refresh(partida)
    return partida

def eliminar_partida_db(partida_id, db):
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    carta_movimiento_repository.delete_cartas_movimiento_db(db, partida_id)
    carta_figura_repository.delete_cartas_figura_db(db, partida_id)
    fichas_repository.delete_fichas_db(db, partida_id)
    carta_movimiento_repository.delete_movimientos_db(db, partida_id)
    db.delete(partida)
    db.commit()
    return partida

def get_color_prohibido_db(partida_id, db):
    partida = home_repository.get_partida_db(db, partida_id)
    error = game_logic.verificar_partida_ini(db, partida_id)
    if not error:
        color = partida.color_bloqueado
    return color

def get_dificultad_db(db: Session, partida_id: int):
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    return partida.dificil

def update_ganador_partida_db(db, partida_id, ganador):
    partida = home_repository.get_partida_db(db, partida_id)
    partida.ganador = ganador
    db.commit()
    db.refresh(partida)
    return partida
