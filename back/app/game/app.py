from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db

from app.game.schemas import *
import app.game.utils as game_utils
import app.carta_movimiento.app as carta_movimiento_app
import app.carta_figura.app as carta_figura_app
import app.game.game_repository as game_repository
import app.partida.partida_repository as partida_repository
import app.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.socket_game as socket_game


router = APIRouter()

@router.patch("/terminar_turno/{partida_id}", response_model=None)
async def terminar_turno(partida_id: int, player:PlayerId, db: Session = Depends(get_db)):
    error = game_utils.verificar_pasar_turno(db, partida_id, player.id_player)
    if not error:
        carta_movimiento_app.asignar_cartas_movimiento_1(partida_id, player, db)
        carta_figura_app.reponer_cartas_jugador(partida_id, player, db)
        partida = game_repository.pasar_turno(db, partida_id)
        data = {'db': db, 'partida_id': partida_id, 'playerId': player.id_player}
        await socket_game.pasar_turno(data)
        jugadores = partida_repository.get_jugadores_db(db, partida_id)
        return {"id_player": jugadores[partida.turno - 1]}
    else:
        raise HTTPException(status_code=400, detail="Error al pasar el turno")

@router.get("/turno_nro/{partida_id}", response_model=int)
async def get_turno_nro(partida_id: int, db: Session = Depends(get_db)):
    error = game_utils.verificar_partida_exist(partida_id, db)
    if not error:
        partida = partida_repository.get_partida_db(db, partida_id)
        return partida.turno
    else:
        raise HTTPException(status_code=400, detail="Error al obtener el turno")
    
@router.get("/turno_jugador/{partida_id}", response_model=PlayerId)
async def get_turno_jugador(partida_id: int, db: Session = Depends(get_db)):
    error = game_utils.verificar_partida_exist(partida_id, db)
    if not error:
        partida = partida_repository.get_partida_db(db, partida_id)
        jugadores = partida_repository.get_jugadores_db(db, partida_id)
        turno = partida.turno
        return {"id_player": jugadores[turno - 1]}
    else:
        raise HTTPException(status_code=400, detail="Error al obtener el turno")
    
@router.patch("/abandonar_partida_ini/{partida_id}", response_model=PartidaData)
async def abandonar_partida_ini(partida_id: int, request:JugadorData, db: Session = Depends(get_db)):
    error = game_utils.verificar_abandonar_partida_ini(db, partida_id, request.id_player)
    if not error:
        carta_movimiento_repository.desasignar_cartas_movimiento(db, partida_id, request.id_player)
        game_repository.abandonar_partida_ini(db, partida_id, request.id_player)
    else:
        raise HTTPException(status_code=400, detail="Error al abandonar la partida")
    
    if request.sid != 'back':
        data = {'db': db, 'partida_id': partida_id}
        await socket_game.abandonar_partida_ini(data,request.sid)
    
    ganador = game_utils.verificar_ganador(db, partida_id)

    if ganador != "":
        data = {'db': db, 'partida_id': partida_id}
        await socket_game.fin_partida(data)
    
    return partida_repository.get_partida_db(db, partida_id)

@router.get("/ganador/{partida_id}", response_model=PlayerId)
def ganador(partida_id: int, db: Session = Depends(get_db)):
    ganador = game_utils.verificar_ganador(db, partida_id)
    ganadorID = PlayerId(id_player=ganador)
    return ganadorID

@router.delete("/eliminar/{partida_id}/{sid}", response_model=PartidaData)
async def eliminar_partida(partida_id: int, sid: str, db: Session = Depends(get_db)):
    partida = partida_repository.get_partida_db(db, partida_id)
    game_repository.eliminar_partida_db(partida_id, db)
    if sid != "back":
        data = {'db': db, 'partida_id': partida_id}
        await socket_game.abandonar_partida_ini(data,sid)
    return partida