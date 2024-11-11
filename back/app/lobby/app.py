from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
import time

from app.home.schemas import *
from app.database.database import get_db
import app.home.home_repository as home_repository
from app.lobby.schemas import *
import app.lobby.socket_lobby as socket_lobby
import app.lobby.lobby_repository as lobby_repository
import app.lobby.logic as lobby_logic


router = APIRouter()

start_turn_time = {}

@router.patch("/abandonar", response_model=PartidaData)
async def abandonar_partida(partida_id: int, request: JugadorData, db: Session = Depends(get_db)):
    if request.sid == 'back':
        await lobby_repository.eliminar_jugador_db(partida_id, request.jugador, db)
        return home_repository.get_partida_db(db, partida_id)
    else:
        data = {'db': db, 'partida_id': partida_id, 'playerId': request.jugador}
        await lobby_repository.eliminar_jugador_db(partida_id, request.jugador, db)
        await socket_lobby.abandonar_noiniciada(request.sid, data)
        return home_repository.get_partida_db(db, partida_id)
    
@router.patch("/iniciar", response_model=PartidaData)
async def iniciar_partida(partida_id: int, request: JugadorID, db: Session = Depends(get_db)):
    data = {'db': db, 'partida_id': partida_id, 'playerId': request.jugador}
    lobby_logic.verificar_iniciar_partida(partida_id, request.jugador, db)
    lobby_repository.ini_random_jugadores_db(data)
    lobby_repository.iniciar_partida_db(partida_id, db)
    lobby_repository.arreglar_turno_db(partida_id, db)
    await socket_lobby.iniciar_partida(data)
    start_turn_time[partida_id] = int(time.time() * 1000)
    return home_repository.get_partida_db(db, partida_id)

@router.get("/jugadores", response_model=JugadoresData)
async def get_jugadores(partida_id: int, db: Session = Depends(get_db)):
    jugadores = home_repository.get_jugadores_db(db, partida_id)
    jugadoresout = JugadoresData(
        jugador1=jugadores[0],
        jugador2=jugadores[1],
        jugador3=jugadores[2],
        jugador4=jugadores[3]
    )
    return jugadoresout

@router.get("/nombres", response_model=NombresData)
async def get_nombres(partida_id: int, db: Session = Depends(get_db)):
    nombres = lobby_repository.get_nombres_db(db, partida_id)
    nombresout = NombresData
    nombresout.jugador1 = nombres[0]
    nombresout.jugador2 = nombres[1]
    nombresout.jugador3 = nombres[2]
    nombresout.jugador4 = nombres[3]

    return nombresout

@router.get("/owner", response_model=OwnerID)
def get_owner(partida_id: int, db: Session = Depends(get_db)):
    owner = lobby_repository.get_owner_db(db, partida_id)
    ret = OwnerID(owner=owner)
    return ret