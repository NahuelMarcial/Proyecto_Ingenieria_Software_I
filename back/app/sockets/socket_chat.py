from app.sockets.socket_connection import sio

@sio.on("chat_message")
async def handle_chat_message(sid, data):  
    mensaje: str = data['message']
    jugador: str = data['playerId']
    time : str = data['time']
    partida_id: int = data['partida_id']
    is_log_system : bool = data['isLogSystem']
    
    # Emitir el mensaje a todos los clientes conectados
    await sio.emit("receive_chat_message", data={"playerId": jugador, "message": mensaje, "time": time, "partida_id": partida_id, "isLogSystem": is_log_system})
