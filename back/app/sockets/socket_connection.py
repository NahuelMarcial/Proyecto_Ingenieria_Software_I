import socketio
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.home.models import Info_Jugador


sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=[])
sio_app = socketio.ASGIApp(socketio_server=sio, socketio_path='/sockets/socket_connection')

rooms = {}  # Definir el diccionario rooms

@sio.event
async def connect(sid, environ):
    print('connect ', sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)


@sio.on('connect_player')
async def connect_player(sid, data):
    prevsid = data.get('prevsid')
    if data.get('partida_id') != '/':
        partida_id = int(data.get('partida_id'))
    else:
        partida_id = '/'
        if partida_id not in rooms:
            rooms[partida_id] = []
        
    player_id = data.get('player_id')
    db = next(get_db())
    actualizar_SID_db(player_id, sid, db)


    if prevsid in rooms[partida_id]:
        # Reemplaza prevsid por sid en la room existente
        await sio.enter_room(sid, partida_id)
        await sio.leave_room(prevsid, partida_id)
        rooms[partida_id].remove(prevsid)
        rooms[partida_id].append(sid)
    else:
        # Asigna a la room con partida_id
        await sio.enter_room(sid, partida_id)
        rooms[partida_id].append(sid)

def actualizar_SID_db(player_id_in: str, sid_in: str, db: Session):
    from app.home.sid_dict import sid_dict
    db_jugador = db.query(Info_Jugador).filter(Info_Jugador.player_id == player_id_in).first()
    if db_jugador:
        # Actualizar el SID en el diccionario
        sid_dict[player_id_in] = sid_in
    return
    