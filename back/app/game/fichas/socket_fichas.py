from fastapi import APIRouter, Depends

from app.sockets.socket_connection import sio, rooms 
from app.home.schemas import *

router = APIRouter()

@sio.on("set_creado_fichas")
async def set_creado(partida_id):
    await sio.emit("set_fichas_creado", room=partida_id)