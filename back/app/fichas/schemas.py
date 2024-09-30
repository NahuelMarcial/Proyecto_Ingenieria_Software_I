from pydantic import BaseModel

class FichaData(BaseModel):
    id_ficha: int
    pos_x: int
    pos_y: int
    color: str