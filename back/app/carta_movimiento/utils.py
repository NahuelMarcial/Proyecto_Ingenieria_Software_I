from fastapi import HTTPException
import random

from app.partida.models import Partida
import app.partida.partida_repository as partida_repository
import app.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository


def validar_partida(partida_id , db) :
   error = False
   partida = partida_repository.get_partida_db(db, partida_id)
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
   partida = partida_repository.get_partida_db(db, partida_id)
   if not partida:
       error = True
       raise HTTPException(status_code=404, detail="No se encontro partida")
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
    partida = partida_repository.get_partida_db(db, id_partida)
    if not partida:
        error = True
        raise HTTPException(status_code=404, detail="No se encontro partida")
    if not partida.iniciada:
        error = True
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    cartas = carta_movimiento_repository.get_cartas_movimiento_db(db, id_partida)
    if not cartas:
        error = True
        raise HTTPException(status_code=400, detail="La partida no tiene cartas asignadas")
    jugadores = partida_repository.get_jugadores_db(db, id_partida)
    if player_id not in jugadores:
        error = True
        raise HTTPException(status_code=400, detail="El jugador no pertenece a la partida")

def asignar_cartas_movimiento(cartas, player_id):  
    cartas_del_jugador = [carta for carta in cartas if carta.id_player == player_id and (carta.descartada == False and carta.gastada == False)] 
    cartas_disponibles = [carta for carta in cartas if carta.id_player == "" and carta.descartada == False]
    while len(cartas_del_jugador) < 3 and len(cartas_disponibles) > 0:
        carta = random.choice(cartas_disponibles)
        carta.id_player = player_id
        cartas_disponibles.remove(carta)
        cartas_del_jugador.append(carta)
    return cartas