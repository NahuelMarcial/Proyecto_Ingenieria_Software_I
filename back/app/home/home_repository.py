from sqlalchemy.orm import Session
from fastapi import HTTPException
import bcrypt
from app.home.models import Partida, Info_Jugador
from app.home.schemas import *
import app.home.logic as home_logic
from app.game.carta_movimiento import carta_movimiento_repository as carta_movimiento_repository
from app.game.carta_figura import carta_figura_repository as carta_figura_repository
from app.game.fichas import fichas_repository as fichas_repository
from app.home.sid_dict import sid_dict

def create_new_partida_db(db: Session, partida: PartidaCreate):
    if partida.password == "":
        db_partida = Partida(
        nombre=partida.nombre,
        owner=partida.owner,
        max_jugadores=partida.max_jugadores,
        jugador1=partida.owner,
        password=partida.password,
        dificil = partida.dificil
    )
    else:
        hashed_password = bcrypt.hashpw(partida.password.encode('utf-8'), bcrypt.gensalt())
        db_partida = Partida(
            nombre=partida.nombre,
            owner=partida.owner,
            max_jugadores=partida.max_jugadores,
            jugador1=partida.owner,
            password=hashed_password.decode('utf-8'),
            dificil = partida.dificil
        )
    db.add(db_partida)
    db.commit()
    db.refresh(db_partida)
    return db_partida


def get_partida_db(db: Session, partida_id: int):
    partida = db.query(Partida).filter(Partida.id == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    return partida

def get_partidas_db(db: Session, player_id: str, skip: int = 0, limit: int = 100):
    return db.query(Partida).filter(
        Partida.cantidad_jugadores < Partida.max_jugadores,
        Partida.iniciada == False,
        Partida.jugador1 != player_id,
        Partida.jugador2 != player_id,
        Partida.jugador3 != player_id,
        Partida.jugador4 != player_id
    ).limit(limit).all()

def get_all_partidas_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Partida).offset(skip).limit(limit).all()

def get_jugadores_db(db: Session, partida_id: int):
    partida = get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    return jugadores

def agregar_jugador_db(partida_id, jugador, password_jugador, db):

    partida = get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if partida.password != "":
        if not bcrypt.checkpw(password_jugador.encode('utf-8'), partida.password.encode('utf-8')):
            raise HTTPException(status_code=422, detail="Contraseña incorrecta")
    
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]

    home_logic.validar_unirse(partida)
    jugadores = home_logic.agregar_jugador(jugadores, jugador, partida)

    partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4 = jugadores

    db.commit()
    db.refresh(partida)

    return partida

def asignar_nombre_db(request: NombreJugadorData, db: Session):
    db_jugador = db.query(Info_Jugador).filter(Info_Jugador.player_id == request.player_id).first()
    if db_jugador:
        raise HTTPException(status_code=400, detail="Jugador ya tiene nombre")
    else:
        db_jugador = Info_Jugador(player_id=request.player_id, nombre=request.nombre)
        db.add(db_jugador)
        sid_dict[request.player_id] = request.sid
    db.commit()
    db.refresh(db_jugador)
    jugador = NombreJugadorData(player_id=db_jugador.player_id, nombre=db_jugador.nombre, sid=request.sid)    
    return jugador

def get_nombre_jugador_db(player_id: str, db: Session):
    db_jugador = db.query(Info_Jugador).filter(Info_Jugador.player_id == player_id).first()
    if not db_jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    sid_jugador = sid_dict.get(player_id,"back")
    jugador = NombreJugadorData(player_id=db_jugador.player_id, nombre=db_jugador.nombre, sid=sid_jugador)
    return jugador

