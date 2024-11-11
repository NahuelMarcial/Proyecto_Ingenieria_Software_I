from fastapi import APIRouter, Depends

from app.sockets.socket_connection import sio, rooms 
from app.home.schemas import *
from app.home.sid_dict import sid_dict

router = APIRouter()

# Diccionario para rastrear eventos emitidos
eventos_emitidos = {}


@sio.on("pasar_turno")
async def pasar_turno(data):
    partida_id: int = data['partida_id']
    turno_previo = data.get('turno_previo', None)
    turno_actual = data.get('turno_actual', None)

    if turno_previo is not None:
        await sio.emit("actualizar_partidas_activas", {"player_id" : turno_previo})
    
    if turno_actual is not None:
        await sio.emit("actualizar_partidas_activas", {"player_id" : turno_actual})
    
    await sio.emit("turno_pasado", room=partida_id)

@sio.on("abandonar_partida_ini")
async def abandonar_partida_ini(data, sid):
    partida_id: int = data['partida_id']
    player_id: int = data['playerId']
    
    await sio.leave_room(sid, partida_id)
    await sio.emit("jugador_abandona_ini", {"player_id" : player_id} ,room=partida_id)
    await sio.enter_room(sid, '/')
    
    # Eliminar el jugador de la room en el diccionario compartido
    if partida_id in rooms and sid in rooms[partida_id]:
        rooms[partida_id].remove(sid)

@sio.on("fin_partida")
async def fin_partida(data, sid):
    partida_id: int = data['partida_id']
    await sio.leave_room(sid, partida_id)
    await sio.emit("partida_borrada")
    await sio.enter_room(sid, '/')
    if partida_id in eventos_emitidos:
        eventos_emitidos[partida_id]['jugador_gana'] = False


@sio.on("jugador_gana")
async def jugador_gana(data):
    partida_id: int = data['partida_id']
    jugadores_data = data['jugadores']
    jugadores = [jugadores_data.jugador1, jugadores_data.jugador2, jugadores_data.jugador3, jugadores_data.jugador4]
    # Verificar si el evento ya ha sido emitido
    if partida_id not in eventos_emitidos:
        eventos_emitidos[partida_id] = {'jugador_gana': False}
    
    if not eventos_emitidos[partida_id]['jugador_gana']:
        await sio.emit("jugador_gana", room=partida_id)
        
        # Actualizar el diccionario
        eventos_emitidos[partida_id]['jugador_gana'] = True

    for jugador in jugadores:
        if jugador:  # Asegurarse de que el jugador no esté vacío
            await sio.emit("actualizar_partidas_activas", {"player_id": jugador})
