from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base

class Partida(Base):
    __tablename__ = "partidas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), index=True)
    owner = Column(String(30), index=True)
    iniciada = Column(Boolean, default=False)
    cantidad_jugadores = Column(Integer, default=1)
    color_bloqueado = Column(String(10), default="")
    turno = Column(Integer, default=1)
    jugador1 = Column(String(30), default="")
    jugador2 = Column(String(30), default="")
    jugador3 = Column(String(30), default="")
    jugador4 = Column(String(30), default="")
    max_jugadores = Column(Integer, default=4)