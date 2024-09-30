import socketio

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
    partida_id = int(data.get('partida_id'))
    print('prevsid', prevsid)
    print('sid', sid)
    print('partida_id', partida_id)
    print('rooms', rooms)
    
    if partida_id not in rooms:
        rooms[partida_id] = []

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
    
    print('rooms', rooms)