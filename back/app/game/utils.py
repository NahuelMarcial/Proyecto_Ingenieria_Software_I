from fastapi import HTTPException

from app.partida.models import Partida
import app.partida.partida_repository as partida_repository

def verificar_pasar_turno(db, partida_id, player_id):
    partida = partida_repository.get_partida_db(db, partida_id)
    error = False
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    if player_id not in jugadores:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no pertenece a la partida")
    turno_jugador = 5
    for i in range(len(jugadores)):
        if jugadores[i] == player_id:
            turno_jugador = i+1
            break
    if partida.turno != turno_jugador:
        error = True
        raise HTTPException(status_code=400, detail="No es tu turno")
    return error

def pasar_turno(partida, jugadores):
    turno = partida.turno
    while True:
        turno += 1
        if turno > 4:
            turno = 1
        if jugadores[turno - 1] != "":
            break
    return turno

def verificar_partida_exist(partida_id, db):
    partida = partida_repository.get_partida_db(db, partida_id)
    error = False
    if not partida:
        error = True
        raise HTTPException(status_code=400, detail="Partida no encontrada")
    if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")

    return error

def verificar_abandonar_partida_ini(db, partida_id, player_id):
    partida = partida_repository.get_partida_db(db, partida_id)
    error = False
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    if player_id not in jugadores:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no pertenece a la partida")
    return error

def abandonar_partida_ini(partida, jugadores, id_player):
    turno_act = partida.turno
    turno_act = jugadores[turno_act - 1]
    for i in range(len(jugadores)):
        if jugadores[i] == id_player:
            jugadores[i] = ""
            if  turno_act == id_player:
                partida.turno = pasar_turno(partida, jugadores) 
            break
    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores
    partida.cantidad_jugadores = partida.cantidad_jugadores - 1
    return partida

def verificar_ganador(db, partida_id):
    partida = partida_repository.get_partida_db(db, partida_id)
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    
    ganador = ""
    if partida.cantidad_jugadores == 1:
        ganador = [jugador for jugador in jugadores if jugador != ""][0]

    # TODO: Verificar cuando alguien forma una carta de figura si le quedan cartas dispoinibles
    
    return ganador