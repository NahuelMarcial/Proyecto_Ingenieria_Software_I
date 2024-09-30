from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter
from app.sockets.socket_connection import sio, rooms  # Importar sio y rooms

import app.partida.partida_repository as repository
import app.partida.utils as utils
from app.partida.models import Partida

router = APIRouter()

@sio.on("crear_partida")
async def crear_partida(sid, partida_id):
    if partida_id not in rooms:
        rooms[partida_id] = []
    rooms[partida_id].append(sid)
    await sio.enter_room(sid, partida_id)
    await sio.emit("partida_creada", {"partida_id": partida_id})
    print(f"Partida {partida_id} creada con sid {sid}")
    print('rooms', rooms)
    return {"message": f"Partida {partida_id} creada"}

@sio.on("unirse")
async def unirse_partida(sid, data):
    db: Session = data['db']
    partida_id: int = data['partida_id']
    jugador: str = data['playerId']
    sid: str = sid

    if partida_id not in rooms:
        rooms[partida_id] = []
    rooms[partida_id].append(sid)
  
    await sio.enter_room(sid, partida_id)
    await sio.emit("jugador_unido_lobby", {"jugadorId": jugador}, room=partida_id)
    await sio.emit("jugador_unido", {"jugadorId": jugador})
    
    print(f"Jugador {jugador} con sid {sid} se ha unido a la partida {partida_id}")
    print('rooms', rooms)
    
    return {"message": f"El jugador {jugador} se ha unido a la partida {partida_id}"}
