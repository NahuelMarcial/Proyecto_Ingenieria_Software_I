from fastapi import HTTPException
import re

from app.partida.models import Partida

# Verifica que la cantidad de jugadores este entre 2 y 4
def validar_cantidad_jugadores(max_jugadores):
    if max_jugadores < 2 or max_jugadores > 4:
        raise HTTPException(status_code=422, detail="Cantidad de jugadores invalida, debe ser entre 2 y 4")

# Verifica que el nombre no sea nulo, sea demasiado largo y no contenga caracteres especiales
def validar_nombre(nombre, tipo):
    if not nombre or len(nombre) > 30:
        raise HTTPException(status_code=422, detail=f"Nombre de {tipo} invalido, debe ser entre 1 y 30 caracteres")
    if re.search(r'[\/:;?*><%+=!@#_\[\]{}()]', nombre):
        raise HTTPException(status_code=422, detail=f"Nombre de {tipo} contiene caracteres inválidos")

# Verifica que la partida exista, no este llena y no haya iniciado    
def validar_unirse(partida):
    if not partida:
        raise HTTPException(status_code=404, detail="No se encontro partida")
    if partida.cantidad_jugadores == partida.max_jugadores:
        raise HTTPException(status_code=400, detail="Partida llena")
    if partida.iniciada:
        raise HTTPException(status_code=400, detail="No se puede unir a una partida iniciada")

# Agrega un jugador a la partida, asignandole el primer lugar vacio    
def agregar_jugador(jugadores, jugador, partida):
    for i in range(len(jugadores)):
        if jugadores[i] == "":
            jugadores[i] = jugador
            partida.cantidad_jugadores += 1
            break
    return jugadores
