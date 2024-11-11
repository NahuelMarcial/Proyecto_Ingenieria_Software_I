from pydantic import BaseModel

class Carta_Figura_new(BaseModel):
    id: int
    id_carta: int
    nombre: str
    color: str
    id_partida: int
    id_player: str
    mostrar: bool
    descartada: bool
    bloqueada: bool
    reponer: bool

class PlayerId(BaseModel):
    id_player: str

class JugarCarta(BaseModel):
    id_carta: int
    id_ficha: int
    id_player: str


class BloquearCarta(BaseModel):
    id_bloqueador: str
    id_carta: int
    id_ficha: int

class Cantidad_Cartas(BaseModel):
    cantidad: int

class CantidadCartasJugador(BaseModel):
    cantidad: int
    jugador: str
    

