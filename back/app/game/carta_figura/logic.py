from fastapi import HTTPException
import random
from sqlalchemy.orm import Session

import app.home.home_repository as home_repository
import app.game.carta_figura.carta_figura_repository as carta_figura_repository
import app.game.fichas.fichas_repository as fichas_repository
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.game_repository as game_repository
import app.game.carta_movimiento.logic as carta_movimiento_logic
import app.game.fichas.endpoints as fichas_app
import app.game.carta_figura.endpoints as carta_figura_app
from app.game.carta_figura.schemas import *

def validar_partida_crear_set(partida_id, db):
    error = False
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    cartas = carta_figura_repository.get_cartas_figura_db(db, partida_id)
    if cartas:
        error = True
        raise HTTPException(status_code=400, detail="Ya se asignaron las cartas figura a esta partida")
    return error

def validar_partida_exist(partida_id, db):
    error = False
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    cartas = carta_figura_repository.get_cartas_figura_db(db, partida_id)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="No hay cartas asignadas a la partida")
    return error

def validar_jugador_exist(partida_id, jugador_id, db):
    error = False
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    jugadores = home_repository.get_jugadores_db(db, partida_id)
    if jugador_id not in jugadores:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no pertenece a la partida")
    return error

def validar_reponer_cartas_jugador(partida_id, player_id, db):
    error = False
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if partida.iniciada == False:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    cartas = carta_figura_repository.get_cartas_jugador_nodescartadas_db(db, partida_id, player_id)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no tiene cartas para reponer")
    return error

def validar_jugar_carta(partida_id, carta_id, player_id, db):
    error = False
    error = validar_partida_exist(partida_id, db)
    if error:
        return error
    error = validar_jugador_exist(partida_id, player_id, db)
    if error:
        return error
    cartas = carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, player_id)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no tiene cartas para jugar")
    for carta in cartas:
        if carta.descartada == True:
            error = True
            raise HTTPException(status_code=400, detail="La carta ya fue jugada")
    cartas_ids = [carta.id_carta for carta in cartas]
    if carta_id not in cartas_ids:
        error = True
        raise HTTPException(status_code=400, detail="La carta no pertenece al jugador")
    error_turno = carta_movimiento_logic.validar_turno(partida_id, player_id, db)
    if error_turno:
        error = True
    return error

def validar_bloquear_carta(partida_id, bloqueador_id, carta_id, ficha_id, db):
    error = False
    error = validar_partida_exist(partida_id, db)
    if error:
        return error
    partida = home_repository.get_partida_db(db, partida_id)
    if partida.iniciada == False:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    error = validar_jugador_exist(partida_id, bloqueador_id, db)
    if error:
        return error
    carta = carta_figura_repository.get_carta_id_db(db, partida_id, carta_id)
    if not carta:
        error = True
        raise HTTPException(status_code=400, detail="La carta no existe")
    bloqueado_id = carta_figura_repository.get_carta_id_db(db, partida_id, carta_id)
    bloqueado_id = bloqueado_id.id_player
    error = validar_jugador_exist(partida_id, bloqueado_id, db)
    if error:
        return error
    if bloqueador_id == bloqueado_id:
        error = True
        raise HTTPException(status_code=400, detail="No se puede bloquear a uno mismo")
    es_turno = game_repository.es_turno_del_jugador(partida, bloqueador_id)
    if not es_turno:
        error = True
        raise HTTPException(status_code=400, detail="No es el turno del jugador")
    if carta.id_player != bloqueado_id:
        error = True
        raise HTTPException(status_code=400, detail="La carta no pertenece al jugador")
    if carta.bloqueada == True:
        error = True
        raise HTTPException(status_code=400, detail="La carta ya está bloqueada")
    cartas_mano = carta_figura_repository.get_cartas_jugador_mostradas_db(db, partida_id, bloqueado_id)
    if carta not in cartas_mano:
        error = True
        raise HTTPException(status_code=400, detail="La carta no está en la mano del jugador")
    for carta in cartas_mano:
        if carta.bloqueada == True:
            error = True
            raise HTTPException(status_code=400, detail="El jugador ya tiene una carta bloqueada")
    if len(cartas_mano) == 1:
        error = True
        raise HTTPException(status_code=400, detail="No se puede bloquear la última carta")
    ficha = fichas_repository.get_ficha_partida_db(db, ficha_id, partida_id)
    if not ficha:
        error = True
        raise HTTPException(status_code=400, detail="La ficha no existe")
    fichas = fichas_repository.get_fichas_db(db, partida_id)
    if not fichas:
        error = True
        raise HTTPException(status_code=400, detail="No hay fichas asignadas a esta partida")
    return error

def reponer_cartas_ini(partida_id, db):
    jugadores = home_repository.get_jugadores_db(db, partida_id)
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

def ficha_pertenece_figura(partida_id, id_carta, id_ficha, db: Session):
    carta = carta_figura_repository.get_carta_id_db(db, partida_id, id_carta)
    ficha = fichas_repository.get_ficha_partida_db(db, id_ficha, partida_id)
    figuras_formadas = fichas_app.get_figuras_formadas(partida_id, db)

    for figura in figuras_formadas:
        if figura.figura == carta.nombre:
            for ficha_figura in figura.fichas:
                if (ficha.pos_x, ficha.pos_y) in ficha_figura:
                    return figura
    figura = None
    return figura

def eliminar_movimientos_utiles(figura, id_partida, db):

    movimientos_db = carta_movimiento_repository.get_movimientos_db(db, id_partida)

    for ficha in figura.fichas:
        for posx, posy in ficha:
            x = posx
            y = posy
            break
        break

    fichas_figura = set()

    for ficha in figura.fichas:
        for posx, posy in ficha:
            fichas_figura.add((posx, posy))

  
    aux = fichas_repository.get_ficha_pos_db(db, id_partida, x, y)
    color_fig = aux.color.value
    mov_validos = []

    for mov in reversed(movimientos_db):
        if mov.id_carta_mov == 0:
            continue
        ficha1 = fichas_repository.get_ficha_partida_db(db, mov.id_ficha1, id_partida)
        ficha2 = fichas_repository.get_ficha_partida_db(db, mov.id_ficha2, id_partida)
        aplicar = False

        if ficha1.color.value != color_fig and ficha2.color.value != color_fig:
            continue
        
        if (ficha1.pos_x, ficha1.pos_y) in fichas_figura or (ficha2.pos_x, ficha2.pos_y) in fichas_figura:
            aplicar = True
        if (ficha1.pos_x+1, ficha1.pos_y) in fichas_figura or (ficha2.pos_x+1, ficha2.pos_y) in fichas_figura:
            aplicar = True
        if (ficha1.pos_x-1, ficha1.pos_y) in fichas_figura or (ficha2.pos_x-1, ficha2.pos_y) in fichas_figura:
            aplicar = True
        if (ficha1.pos_x, ficha1.pos_y+1) in fichas_figura or (ficha2.pos_x, ficha2.pos_y+1) in fichas_figura:
            aplicar = True
        if (ficha1.pos_x, ficha1.pos_y-1) in fichas_figura or (ficha2.pos_x, ficha2.pos_y-1) in fichas_figura:
            aplicar = True
        if (ficha1.color.value == ficha2.color.value):
            aplicar = False
        for auxmov in reversed(movimientos_db):
            if auxmov.id_mov in mov_validos:
                if auxmov.id_ficha1 == mov.id_ficha1 or auxmov.id_ficha1 == mov.id_ficha2 or auxmov.id_ficha2 == mov.id_ficha1 or auxmov.id_ficha2 == mov.id_ficha2:
                    aplicar = True
        if aplicar:
            mov_validos.append(mov.id_mov)
    
    for mov in movimientos_db:
        if mov.id_mov in mov_validos:
            carta_movimiento_repository.aplicar_movimiento_db(db, id_partida, mov.id_carta_mov)
            carta_movimiento_repository.sacar_mov_db(db, id_partida, mov.id_mov)

    return movimientos_db
