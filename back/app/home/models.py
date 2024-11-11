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
    password = Column(String(60), default="")
    dificil = Column(Boolean, default=False)
    ganador = Column(String(30), default="")

class Info_Jugador(Base):
    __tablename__ = "info_jugadores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    player_id = Column(String(30), index=True)
    nombre = Column(String(30), index=True)