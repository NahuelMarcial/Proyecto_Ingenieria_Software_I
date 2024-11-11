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

class JugadoresData(BaseModel):
    jugador1: str
    jugador2: str
    jugador3: str
    jugador4: str

class JugadorData(BaseModel):
    jugador: str
    sid: str

class JugadorID(BaseModel):
    jugador: str

class OwnerID(BaseModel):
    owner: str

class NombresData(BaseModel):
    jugador1: str
    jugador2: str
    jugador3: str
    jugador4: str
