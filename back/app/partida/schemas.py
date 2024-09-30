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

class PartidaId(BaseModel):
    id: int

class PartidaCreate(BaseModel):
    nombre: str
    owner: str
    max_jugadores: int
    sid: str

class JoinRequest(BaseModel):
    jugador: str
    sid: str