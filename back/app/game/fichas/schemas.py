from pydantic import BaseModel
from typing import List, Tuple

class FichaData(BaseModel):
    id_ficha: int
    pos_x: int
    pos_y: int
    color: str

class FigFormada(BaseModel):
    figura: str
    fichas: List[set[Tuple[int, int]]]

class SugerenciaData(BaseModel):
   id_ficha1 : int
   id_ficha2 : int
   id_carta : int