from pydantic import BaseModel

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
    password: str
    dificil : bool
    
class PartidaGet(BaseModel):
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
    password: bool
    dificil : bool

class PartidaActiva(BaseModel):
    id: int
    nombre: str
    owner: str
    iniciada: bool
    cantidad_jugadores: int
    tu_turno: int
    max_jugadores: int
    ganador: bool

class PartidaId(BaseModel):
    id: int

class PartidaCreate(BaseModel):
    nombre: str
    owner: str
    max_jugadores: int
    sid: str
    password : str
    dificil : bool

class JoinRequest(BaseModel):
    jugador: str
    sid: str
    password: str

class NombreJugadorData(BaseModel):
    player_id: str
    nombre: str
    sid: str
