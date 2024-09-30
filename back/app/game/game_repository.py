from sqlalchemy.orm import Session
from fastapi import HTTPException

import app.partida.partida_repository as partida_repository
import app.game.utils as game_utils
import app.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.carta_figura.carta_figura_repository as carta_figura_repository
import app.fichas.fichas_repository as fichas_repository

def pasar_turno(db: Session, partida_id: int):
    
    partida = partida_repository.get_partida_db(db, partida_id)
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    turno = game_utils.pasar_turno(partida, jugadores)
    partida.turno = turno

    db.commit()
    db.refresh(partida)
    return partida

def abandonar_partida_ini(db: Session, partida_id: int, id_player: str):
    partida = partida_repository.get_partida_db(db, partida_id)
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    partida = game_utils.abandonar_partida_ini(partida, jugadores, id_player)

    db.commit()
    db.refresh(partida)
    return partida

def eliminar_partida_db(partida_id, db):
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    carta_movimiento_repository.delete_cartas_movimiento_db(db, partida_id)
    carta_figura_repository.delete_cartas_figura_db(db, partida_id)
    fichas_repository.delete_fichas_db(db, partida_id)
    db.delete(partida)
    db.commit()
    return partida