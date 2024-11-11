from fastapi import APIRouter, Depends

from app.sockets.socket_connection import sio, rooms 
from app.home.schemas import *

router = APIRouter()


@sio.on("abandonar_noini")
async def abandonar_noiniciada(sid, data):
    partida_id: int = data['partida_id']

    await sio.leave_room(sid, partida_id)
    await sio.emit("jugador_abandona_lobby_noini", room=partida_id)
    await sio.emit("jugador_abandona")
    await sio.enter_room(sid, '/')
    
    # Eliminar el jugador de la room en el diccionario compartido
    if partida_id in rooms and sid in rooms[partida_id]:
        rooms[partida_id].remove(sid)


@sio.on("iniciar_partida")
async def iniciar_partida(data):
    partida_id: int = data['partida_id']

    await sio.emit("partida_iniciada_lobby", {"partida_id":partida_id} ,room=partida_id)
    await sio.emit("partida_iniciada")

@sio.on("owner_abandona")
async def owner_abandona_lobby(data):
    partida_id: int = data['partida_id']
    
    await sio.emit("owner_abandona_lobby", room=partida_id)
    



