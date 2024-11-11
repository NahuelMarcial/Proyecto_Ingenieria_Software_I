from pydantic import BaseModel

class PlayerId(BaseModel):
    id_player: str

class JugadorData(BaseModel):
    id_player: str
    sid: str

class PartidaData(BaseModel):
    id: int
    nombre: str
    owner: str
    iniciada: bool
    cantidad_jugadores: int
    color_bloqueado: str
    turno: int
    jugador1: str
    jugador2: str
    jugador3: str
    jugador4: str
    max_jugadores: int

class sidplayer(BaseModel):
    sid: str

class ColorProhibido(BaseModel):
    color: str

class Ganador(BaseModel):
    id_player: str
    name: str