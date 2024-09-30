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