from sqlalchemy.orm import Session
from fastapi import HTTPException
import random

import app.partida.partida_repository as partida_repository
from app.lobby import utils

# Reordenamiento de los jugadores
def ini_random_jugadores_db(data):
    db: Session = data['db']
    partida_id: int = data['partida_id']
    jugador: str = data['playerId']
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    jugadores = random.sample(jugadores, len(jugadores))
    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores

    db.commit()
    db.refresh(partida)
    print(f"Jugadores de la partida {partida_id} reordenados aleatoriamente")
    return partida


# Actualizar el estado de la partida a iniciada
def iniciar_partida_db(partida_id, db):
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    partida.iniciada = True
    db.commit()
    db.refresh(partida)
    return partida

def eliminar_jugador_db(partida_id, jugador, db):
    partida = partida_repository.get_partida_db(db, partida_id)
    error = False 
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if jugador == partida.owner:
        #TODO: owner abandona
        error = True
        raise HTTPException(status_code=400, detail="Owner abandona no implementado")
    if partida.iniciada:
        error = True
        #TODO: abandonar partida iniciada
        raise HTTPException(status_code=400, detail="Abandonar partida iniciada no implementado")

    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    jugadores = utils.eliminar_jugador(partida, jugador, jugadores)
    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores

    db.commit()
    db.refresh(partida)
    return error

def get_owner_db(db, partida_id):
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    return partida.owner

def arreglar_turno_db(partida_id, db):
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    turno = partida.turno
    while True:
        turno += 1
        if turno > 4:
            turno = 1
        if jugadores[turno - 1] != "":
            break
    partida.turno = turno
    db.commit()
    db.refresh(partida)
    return partida