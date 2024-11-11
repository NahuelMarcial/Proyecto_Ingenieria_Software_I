from pydantic import BaseModel

class Carta_Movimiento_new(BaseModel):
   id : int 
   id_partida: int
   id_carta: int
   tipo_movimiento : str
   descartada: bool
   id_player : str
   gastada :bool 

class JugadorID(BaseModel):
   id_player: str

class movimientoData(BaseModel):    
   id_carta : int 
   id_jugador : str
   id_ficha1 : int 
   id_ficha2 : int

class movimiento_posible_data(BaseModel):
   id_ficha1 : int
   id_carta : int 