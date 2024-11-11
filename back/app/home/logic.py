from fastapi import HTTPException
import re

from app.home.schemas import PartidaActiva, PartidaGet
import app.home.home_repository as home_repository
import app.lobby.lobby_repository as lobby_repository

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

#verificar la contrseña de la partida
def validar_password(password):
    # Verificar que la longitud de la contraseña sea exactamente 4 caracteres
    if len(password) != 4 and len(password) != 0 :
        raise HTTPException(status_code=422, detail="Contraseña de partida invalida, debe tener exactamente 4 caracteres numericos")
    # Verificar que la contraseña contenga solo dígitos
    if len(password)== 4 and not re.match(r'^\d{4}$', password):
        raise HTTPException(status_code=422, detail="Contraseña de partida debe contener solo números enteros")

# Verifica que la partida exista, no este llena y no haya iniciado    
def validar_unirse(partida):
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if partida.cantidad_jugadores == partida.max_jugadores:
        raise HTTPException(status_code=400, detail="Partida llena")
    if partida.iniciada:
        raise HTTPException(status_code=400, detail="No se puede unir a una partida iniciada")
    
def validar_no_pertenece(partida_id, jugador, db):
    jugadores = home_repository.get_jugadores_db(db, partida_id)
    if jugador in jugadores:
        return True
    return False

# Agrega un jugador a la partida, asignandole el primer lugar vacio    
def agregar_jugador(jugadores, jugador, partida):
    for i in range(len(jugadores)):
        if jugadores[i] == "":
            jugadores[i] = jugador
            partida.cantidad_jugadores += 1
            break
    return jugadores

def filtrar_partidas_activas(db, partidas, player_id):
    partidas_activas = []
    for partida in partidas:
        jugadores = home_repository.get_jugadores_db(db, partida.id)
        if player_id in jugadores:
            turno = partida.turno
            turno = jugadores[turno - 1]
            turno = turno == player_id
            ganador = partida.ganador != ""
            owner = lobby_repository.get_owner_db(db, partida.id)

            partida_activa = PartidaActiva(
                id=partida.id,
                nombre=partida.nombre,
                owner=owner,
                iniciada=partida.iniciada,
                cantidad_jugadores=partida.cantidad_jugadores,
                tu_turno=turno,
                max_jugadores=partida.max_jugadores,
                ganador=ganador
            )
            partidas_activas.append(partida_activa)
    return partidas_activas

def get_partidas(db, player_id):
    partidas = home_repository.get_partidas_db(db, player_id)
    partidas_return = []
    for partida in partidas:
        if partida.password == "":
            password_b = False
        else:
            password_b = True
        
        partida_return = PartidaGet(
                id=partida.id,
                nombre=partida.nombre,
                owner=partida.owner,
                iniciada=partida.iniciada,
                cantidad_jugadores=partida.cantidad_jugadores,
                color_bloqueado=partida.color_bloqueado,
                turno=partida.turno,
                jugador1=partida.jugador1,
                jugador2=partida.jugador2,
                jugador3=partida.jugador3,
                jugador4=partida.jugador4,
                max_jugadores=partida.max_jugadores,
                password=password_b,
                dificil=partida.dificil 
            )       
        partidas_return.append(partida_return)
    return partidas_return
