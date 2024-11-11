from sqlalchemy.orm import Session
from fastapi import HTTPException
import random

import app.home.home_repository as home_repository
import app.lobby.logic as lobby_logic
import app.lobby.socket_lobby as socket_lobby

# Reordenamiento de los jugadores
def ini_random_jugadores_db(data):
    db: Session = data['db']
    partida_id: int = data['partida_id']
    jugador: str = data['playerId']
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    jugadores = random.sample(jugadores, len(jugadores))
    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores

    db.commit()
    db.refresh(partida)
    return partida


# Actualizar el estado de la partida a iniciada
def iniciar_partida_db(partida_id, db):
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    partida.iniciada = True
    db.commit()
    db.refresh(partida)
    return partida

async def eliminar_jugador_db(partida_id, jugador, db):
    partida = home_repository.get_partida_db(db, partida_id)
    error = False 
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if jugador == partida.owner:
        partida.iniciada = True
        data = {'db': db, 'partida_id': partida_id, 'playerId': jugador}
        await socket_lobby.owner_abandona_lobby(data)

    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    jugadores = lobby_logic.eliminar_jugador(partida, jugador, jugadores)
    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores

    db.commit()
    db.refresh(partida)
    return error

def get_owner_db(db, partida_id):
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if partida.owner in [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]:
        return partida.owner
    else:
        return ""

def arreglar_turno_db(partida_id, db):
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    jugadores = home_repository.get_jugadores_db(db, partida_id)
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

def get_nombres_db(db, partida_id):
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    nombres = []
    for jugador in jugadores:
        if jugador == "":
            nombres.append("")
        else:
            nombre = home_repository.get_nombre_jugador_db(jugador, db)
            nombres.append(nombre.nombre)
            
    return nombres