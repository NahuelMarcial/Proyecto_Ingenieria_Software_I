from fastapi import APIRouter, Depends

from app.sockets.socket_connection import sio, rooms 
from app.home.schemas import *

router = APIRouter()

@sio.on("set_creado_cartas_figura")
async def set_creado(partida_id):
    await sio.emit("set_cartas_figura_creado", room=partida_id)

@sio.on("carta_jugada_figura")
async def carta_jugada_figura(partida_id):
    await sio.emit("carta_figura_jugada", room=partida_id)