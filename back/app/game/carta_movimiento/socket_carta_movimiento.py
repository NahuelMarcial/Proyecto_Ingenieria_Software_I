from fastapi import APIRouter, Depends

from app.game.carta_movimiento.schemas import *
from app.sockets.socket_connection import sio,rooms
from app.game.fichas.schemas import *
from app.home.schemas import *

router = APIRouter()

@sio.on("movimiento_usado")
async def movimiento_usado(data):
    await sio.emit("movimiento_realizado",room=data['partida_id'])

@sio.on("movimiento_desecho")
async def movimiento_desecho(data):
    await sio.emit("deshizo_movimiento",room=data['partida_id'])

@sio.on("set_creado_cartas_movimiento")
async def set_creado(partida_id):
    await sio.emit("set_cartas_movimiento_creado", room=partida_id)

