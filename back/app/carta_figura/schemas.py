from pydantic import BaseModel
from typing import Optional

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


