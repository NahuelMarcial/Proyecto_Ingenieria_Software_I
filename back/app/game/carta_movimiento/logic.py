from fastapi import HTTPException
import random

import app.home.home_repository as home_repository
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.game_repository as game_repository
import app.game.fichas.logic as fichas_logic
import app.game.fichas.fichas_repository as fichas_repository

movimientos_array = []

def validar_partida(partida_id , db) :
   error = False
   partida = home_repository.get_partida_db(db, partida_id)
   if not partida:
       error = True
       raise HTTPException(status_code=404, detail="Partida no encontrada")
   if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
   cartas = carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
   if cartas:
       error = True
       raise HTTPException(status_code=400, detail="Ya se asignaron las cartas movimiento a esta partida")
   return error

def validar_partida_ini(partida_id , db) :
   error = False
   partida = home_repository.get_partida_db(db, partida_id)
   if not partida:
       error = True
       raise HTTPException(status_code=404, detail="Partida no encontrada")
   if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
   cartas = carta_movimiento_repository.get_cartas_movimiento_db(db, partida_id)
   if not cartas:
       error = True
       raise HTTPException(status_code=400, detail="La partida no tiene cartas asignadas")
   return error

def validar_jugador(id_partida: int, player_id: str, db):
    error = False
    partida = home_repository.get_partida_db(db, id_partida)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    cartas = carta_movimiento_repository.get_cartas_movimiento_db(db, id_partida)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="La partida no tiene cartas asignadas")
    jugadores = home_repository.get_jugadores_db(db, id_partida)
    if player_id not in jugadores:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no pertenece a la partida")
    return  error

def validar_carta_movimiento(id_partida: int, id_carta: int, id_jugador:int, db):
    error = False
    carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, id_partida, id_carta)
    if not carta:
        error = True
        raise HTTPException(status_code=404, detail="Carta de movimiento no encontrada")
    if carta.id_player != id_jugador:
        error = True
        raise HTTPException(status_code=400, detail="La carta no pertenece al jugador")
    if carta.gastada:
        error = True
        raise HTTPException(status_code=400, detail="La carta ya fue utilizada")
    if carta.descartada:
        error = True
        raise HTTPException(status_code=400, detail="La carta fue descartada")
    partida = home_repository.get_partida_db(db, id_partida)
    if not game_repository.es_turno_del_jugador(partida, id_jugador):
        error = True 
        raise HTTPException(status_code=400, detail="No es el turno del jugador")
    return error

def validar_carta_movimiento_existe(id_partida: int, id_carta: int, db):
    error = False
    carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, id_partida, id_carta)
    if not carta:
        error = True
        raise HTTPException(status_code=404, detail="Carta de movimiento no encontrada")
    return error

def validar_turno (id_partida: int, id_jugador: int, db):
    partida = home_repository.get_partida_db(db, id_partida)
    error= False
    if not game_repository.es_turno_del_jugador(partida, id_jugador):
        error = True
        raise HTTPException(status_code=400, detail="No es el turno del jugador")
    return error

def asignar_cartas_movimiento(cartas, player_id):  
    cartas_del_jugador = [carta for carta in cartas if carta.id_player == player_id and (carta.descartada == False and carta.gastada == False)] 
    cartas_disponibles = [carta for carta in cartas if carta.id_player == "" and carta.descartada == False]
    while len(cartas_del_jugador) < 3 and len(cartas_disponibles) > 0:
        carta = random.choice(cartas_disponibles)
        carta.id_player = player_id
        cartas_disponibles.remove(carta)
        cartas_del_jugador.append(carta)
    return cartas

def usar_carta_movimiento(db, partida_id: int, id_carta: int, id_ficha1: int, id_ficha2: int):
    ficha1 = fichas_repository.get_ficha_partida_db(db , id_ficha1, partida_id )
    ficha2 = fichas_repository.get_ficha_partida_db(db , id_ficha2, partida_id )
    carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, partida_id, id_carta)

    ficha1,ficha2 = fichas_logic.swap_fichas(ficha1,ficha2) 
    carta.gastada = True
    db.commit()
    return 


def deshacer_carta_movimiento(db, partida_id: int):
    mov = carta_movimiento_repository.get_ultimo_movimiento_con_carta_db(db, partida_id)
    if mov:
        carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, partida_id, mov.id_carta_mov)
        ficha1 = fichas_repository.get_ficha_partida_db(db , mov.id_ficha1, partida_id )
        ficha2 = fichas_repository.get_ficha_partida_db(db , mov.id_ficha2, partida_id )
    
        ficha1,ficha2 = fichas_logic.swap_fichas(ficha1,ficha2)
        carta.gastada = False
        return mov.id_mov
    else:
        raise HTTPException(status_code=400, detail="No hay movimientos para deshacer")

def deshacer_todos_movimientos(db, partida_id: int):
    cantidad_movimientos = carta_movimiento_repository.get_cantidad_movimientos_db(db, partida_id)
    for _ in range(cantidad_movimientos):
        carta_movimiento_repository.deshacer_carta_movimiento_db(db, partida_id)
        db.commit()
    return

