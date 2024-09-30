from fastapi import APIRouter, Depends

from app.sockets.socket_connection import sio, rooms  # Importar sio y rooms
from app.partida.schemas import *
import app.partida.partida_repository as partida_repository
import app.lobby.utils as utils
import app.lobby.lobby_repository as lobby_repository

router = APIRouter()


@sio.on("pasar_turno")
async def pasar_turno(data):
    partida_id: int = data['partida_id']
    jugador: str = data['playerId']
    await sio.emit("turno_pasado", {"player_id":jugador} ,room=partida_id)

@sio.on("abandonar_partida_ini")
async def abandonar_partida_ini(data, sid):
    partida_id: int = data['partida_id']
    await sio.emit("jugador_abandona_ini" ,room=partida_id)
    await sio.leave_room(sid, partida_id)
    await sio.enter_room(sid, '/')
    
    # Eliminar el jugador de la room en el diccionario compartido
    if partida_id in rooms and sid in rooms[partida_id]:
        rooms[partida_id].remove(sid)

@sio.on("fin_partida")
async def fin_partida(data):
    partida_id: int = data['partida_id']
    await sio.emit("partida_finalizada" ,room=partida_id)

