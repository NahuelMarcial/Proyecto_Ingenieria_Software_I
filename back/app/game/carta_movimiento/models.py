from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from app.database.database import Base


class Carta_Movimiento(Base) :
   __tablename__ = 'cartas_movimiento'
   id = Column(Integer, primary_key=True, index=True)
   id_partida = Column(Integer, ForeignKey('partidas.id'))
   id_carta = Column(Integer)
   tipo_movimiento = Column(String)
   descartada = Column(Boolean , default=False)
   id_player = Column(String,default="")
   gastada = Column(Boolean,default=False)

class movimientos(Base):
   __tablename__ = 'movimientos'
   id = Column(Integer, primary_key=True, index=True)
   id_mov = Column(Integer)
   id_partida = Column(Integer, ForeignKey('partidas.id'))
   id_carta_mov = Column(Integer)
   id_ficha1 = Column(Integer)
   id_ficha2 = Column(Integer)

