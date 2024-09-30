from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.database import Base

class Carta_Figura(Base):
    __tablename__ = 'cartas_figura'

    id = Column(Integer, primary_key=True, index=True)
    id_carta = Column(Integer)
    nombre = Column(String)
    color = Column(String)
    id_partida = Column(Integer, ForeignKey('partidas.id'))
    id_player = Column(String, default="")
    mostrar = Column(Boolean, default=False)
    descartada = Column(Boolean, default=False)
    bloqueada = Column(Boolean, default=False)
    reponer = Column(Boolean, default=False)
    