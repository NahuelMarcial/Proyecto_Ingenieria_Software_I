from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.sockets.socket_connection import sio, rooms  # Importar sio y rooms
from app.partida.schemas import *
import app.partida.partida_repository as partida_repository
import app.lobby.utils as utils
import app.lobby.lobby_repository as lobby_repository

router = APIRouter()


@sio.on("abandonar_noini")
async def abandonar_noiniciada(sid, data):
    partida_id: int = data['partida_id']
    jugador: str = data['playerId']

    await sio.leave_room(sid, partida_id)
    await sio.emit("jugador_abandona_lobby_noini", {"jugadorId": sid}, room=partida_id)
    await sio.emit("jugador_abandona", {"jugadorId": sid})
    await sio.enter_room(sid, '/')
    
    # Eliminar el jugador de la room en el diccionario compartido
    if partida_id in rooms and sid in rooms[partida_id]:
        rooms[partida_id].remove(sid)
    
    print(f"Jugador {jugador} ha abandonado la partida")


@sio.on("iniciar_partida")
async def iniciar_partida(data):
    partida_id: int = data['partida_id']

    await sio.emit("partida_iniciada_lobby", room=partida_id)
    await sio.emit("partida_iniciada")
    print(f"Partida {partida_id} iniciada")


    



