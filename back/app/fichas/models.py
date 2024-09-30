from sqlalchemy import Column, Integer, Enum
from app.database.database import Base
import enum

class Color(enum.Enum):
    azul = "azul"
    rojo = "rojo"
    verde = "verde"
    amarillo = "amarillo"

class Ficha(Base):
    __tablename__ = "Fichas"

    id = Column(Integer, primary_key=True, index=True)
    id_ficha = Column(Integer, index=True)  #va del 1 al 36
    id_partida = Column(Integer, index=True)
    pos_x = Column(Integer, default=0) #va del 1 al 6
    pos_y = Column(Integer, default=0) #va del 1 al 6
    color = Column(Enum(Color))