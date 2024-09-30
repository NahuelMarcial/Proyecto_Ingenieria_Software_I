from fastapi import HTTPException
import random

from app.partida.models import Partida
import app.partida.partida_repository as partida_repository
import app.carta_figura.carta_figura_repository as carta_figura_repository
import app.carta_figura.app as carta_figura_app
from app.carta_figura.schemas import *

def validar_partida_crear_set(partida_id, db):
    error = False
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="No se encontro partida")
    cartas = carta_figura_repository.get_cartas_figura_db(db, partida_id)
    if cartas:
        error = True
        raise HTTPException(status_code=400, detail="Ya se asignaron las cartas figura a esta partida")
    return error

def validar_partida_exist(partida_id, db):
    error = False
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="No se encontro partida")
    cartas = carta_figura_repository.get_cartas_figura_db(db, partida_id)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="No hay cartas asignadas a la partida")
    return error

def validar_jugador_exist(partida_id, jugador_id, db):
    error = False
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="No se encontro partida")
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    if jugador_id not in jugadores:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no pertenece a la partida")
    return error

def validar_reponer_cartas_jugador(partida_id, player_id, db):
    error = False
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="No se encontro partida")
    if partida.iniciada == False:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    cartas = carta_figura_repository.get_cartas_jugador_nodescartadas_db(db, partida_id, player_id)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no tiene cartas para reponer")
    return error

def reponer_cartas_ini(partida_id, db):
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    jugadores_utiles = [jugador for jugador in jugadores if jugador != ""]
    for jugador in jugadores_utiles:
        jugadorin = PlayerId(id_player=jugador)
        carta_figura_app.reponer_cartas_jugador(partida_id, jugadorin, db)
    return carta_figura_repository.get_cartas_figura_mostradas_db(db, partida_id)

# 7 figuras azul y 18 blanca y de cada una hay 2
# Cantidad de cartas figura por jugador

# Diccionarios para la cantidad de cartas a asignar según el número de jugadores
figura_bancas = {4: 36 // 4, 3: 36 // 3, 2: 36 // 2}
figura_azul = {4: 14 // 4, 3: 14 // 3, 2: 14 // 2}


def asignar_cartas_figura(cartas_figura, players):
    # Filtrar los jugadores que tienen un ID válido
    players_utiles = [player for player in players if player != ""]
    cant_players = len(players_utiles)

    if cant_players < 2 or cant_players > 4:
        raise HTTPException(status_code = 400 ,detail= "El número de jugadores debe ser entre 2 y 4")

    # Función auxiliar para asignar cartas a los jugadores
    def asignar(cartas, cantidad_por_jugador):
        cartas_asignadas = 0
        for player in players_utiles:
            for _ in range(cantidad_por_jugador):
                if cartas_asignadas < len(cartas):
                    carta = random.choice(cartas)
                    carta.id_player = player
                    cartas.remove(carta)
                else:
                    break

    # Asignar las cartas de color azul y blancas
    cartas_azules = [carta for carta in cartas_figura if carta.color == "azul"]
    cartas_blancas = [carta for carta in cartas_figura if carta.color == "blanca"]

    asignar(cartas_azules, figura_azul[cant_players])
    asignar(cartas_blancas, figura_bancas[cant_players])

    return cartas_figura