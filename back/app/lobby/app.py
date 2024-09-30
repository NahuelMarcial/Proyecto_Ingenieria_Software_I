from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.partida.schemas import *
from app.database.database import get_db
import app.partida.partida_repository as partida_repository
from app.lobby.schemas import *
import app.lobby.socket_lobby as socket_lobby
import app.lobby.lobby_repository as lobby_repository
import app.lobby.utils as utils


router = APIRouter()


@router.patch("/abandonar/{partida_id}", response_model=PartidaData)
async def abandonar_partida(partida_id: int, request: JugadorData, db: Session = Depends(get_db)):
    if request.sid == 'back':
        lobby_repository.eliminar_jugador_db(partida_id, request.jugador, db)
        return partida_repository.get_partida_db(db, partida_id)
    else:
        data = {'db': db, 'partida_id': partida_id, 'playerId': request.jugador}
        error = lobby_repository.eliminar_jugador_db(partida_id, request.jugador, db)
        if not error:
            await socket_lobby.abandonar_noiniciada(request.sid, data)
        return partida_repository.get_partida_db(db, partida_id)
    
@router.patch("/iniciar/{partida_id}", response_model=PartidaData)
async def iniciar_partida(partida_id: int, request: JugadorID, db: Session = Depends(get_db)):
    data = {'db': db, 'partida_id': partida_id, 'playerId': request.jugador}
    utils.verificar_iniciar_partida(partida_id, request.jugador, db)
    lobby_repository.ini_random_jugadores_db(data)
    lobby_repository.iniciar_partida_db(partida_id, db)
    lobby_repository.arreglar_turno_db(partida_id, db)
    await socket_lobby.iniciar_partida(data)
    return partida_repository.get_partida_db(db, partida_id)

@router.get("/jugadores/{partida_id}", response_model=JugadoresData)
async def get_jugadores(partida_id: int, db: Session = Depends(get_db)):
    jugadores = partida_repository.get_jugadores_db(db, partida_id)
    jugadoresout = JugadoresData
    jugadoresout.jugador1 = jugadores[0]
    jugadoresout.jugador2 = jugadores[1]
    jugadoresout.jugador3 = jugadores[2]
    jugadoresout.jugador4 = jugadores[3]

    return jugadoresout

@router.get("/owner/{partida_id}", response_model=OwnerID)
def get_owner(partida_id: int, db: Session = Depends(get_db)):
    owner = lobby_repository.get_owner_db(db, partida_id)
    ret = OwnerID(owner=owner)
    return ret