from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db
import time

from app.game.schemas import *
import app.lobby.app as lobby_app
import app.game.logic as game_logic
import app.game.carta_movimiento.endpoints as carta_movimiento_app
import app.game.carta_figura.endpoints as carta_figura_app
import app.game.game_repository as game_repository
import app.home.home_repository as home_repository
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.socket_game as socket_game
import app.game.carta_movimiento.logic as carta_movimiento_logic

from app.lobby.app import start_turn_time
from app.game.carta_figura.endpoints import router as carta_figura_router
from app.game.carta_movimiento.endpoints import router as carta_movimiento_router
from app.game.fichas.endpoints import router as fichas_router


router = APIRouter()

router.include_router(carta_figura_router, prefix="/carta_figura")
router.include_router(carta_movimiento_router, prefix="/carta_movimiento")
router.include_router(fichas_router, prefix="/fichas")

@router.patch("/terminar_turno", response_model=None)
async def terminar_turno(partida_id: int, player:PlayerId, db: Session = Depends(get_db)):
    error = game_logic.verificar_pasar_turno(db, partida_id, player.id_player)
    if not error:
        if start_turn_time is not None:
            start_turn_time[partida_id] = int(time.time() * 1000)
        turno_previo = get_turno_jugador(partida_id, db)
        carta_movimiento_logic.deshacer_todos_movimientos(db, partida_id)
        carta_movimiento_repository.reset_movimientos_db(db, partida_id)
        carta_movimiento_app.asignar_cartas_movimiento_1(partida_id, player, db)
        carta_figura_app.reponer_cartas_jugador(partida_id, player, db)
        partida = game_repository.pasar_turno(db, partida_id)
        turno_actual = get_turno_jugador(partida_id, db)
        data = {'db': db, 'partida_id': partida_id, 'playerId': player.id_player, 'turno_previo': turno_previo, 'turno_actual': turno_actual}
        await socket_game.pasar_turno(data)
        jugadores = home_repository.get_jugadores_db(db, partida_id)
        return {"id_player": jugadores[partida.turno - 1]}
    else:
        raise HTTPException(status_code=400, detail="Error al pasar el turno")
    
@router.patch("/terminar_turno_timeout", response_model=None)
async def terminar_turno_timeout(partida_id: int, db: Session = Depends(get_db)):
    player_id = get_turno_jugador(partida_id, db)
    player = PlayerId(id_player=player_id["id_player"])
    time_actual = int(time.time() * 1000)
    time_lapsed = time_actual - start_turn_time[partida_id]
    if  121 * 1000 - time_lapsed < 900:
        await terminar_turno(partida_id, player, db)
        
        return
    else:
        raise HTTPException(status_code=400, detail="Error al pasar el turno")
    

@router.get("/start_turn_time", response_model=int)
def start_time(partida_id: int):
    return start_turn_time[partida_id]
    

@router.get("/turno_nro", response_model=int)
async def get_turno_nro(partida_id: int, db: Session = Depends(get_db)):
    error = game_logic.verificar_partida_exist(partida_id, db)
    if not error:
        partida = home_repository.get_partida_db(db, partida_id)
        return partida.turno
    else:
        raise HTTPException(status_code=400, detail="Error al obtener el turno")
    
@router.get("/turno_jugador", response_model=PlayerId)
def get_turno_jugador(partida_id: int, db: Session = Depends(get_db)):
    error = game_logic.verificar_partida_exist(partida_id, db)
    if not error:
        partida = home_repository.get_partida_db(db, partida_id)
        jugadores = home_repository.get_jugadores_db(db, partida_id)
        turno = partida.turno
        return {"id_player": jugadores[turno - 1]}
    else:
        raise HTTPException(status_code=400, detail="Error al obtener el turno")
    
@router.patch("/abandonar_partida_ini", response_model=PartidaData)
async def abandonar_partida_ini(partida_id: int, request:JugadorData, db: Session = Depends(get_db)):
    error = game_logic.verificar_abandonar_partida_ini(db, partida_id, request.id_player)
    if not error:
        carta_movimiento_repository.desasignar_cartas_movimiento(db, partida_id, request.id_player)
        await game_repository.abandonar_partida_ini(db, partida_id, request.id_player)
        if request.sid != 'back':
            data = {'db': db, 'partida_id': partida_id, 'playerId': request.id_player}
            await socket_game.abandonar_partida_ini(data,request.sid)

        ganador = game_logic.verificar_ganador(db, partida_id)

        if ganador != "":
            jugadores = await lobby_app.get_jugadores(partida_id, db)
            data = {'partida_id': partida_id, 'jugadores': jugadores}
            await socket_game.jugador_gana(data)

        return home_repository.get_partida_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al abandonar la partida")

@router.get("/ganador", response_model=Ganador)
def ganador(partida_id: int, db: Session = Depends(get_db)):
    partida = home_repository.get_partida_db(db, partida_id)
    ganador_id = partida.ganador
    if (partida.ganador != ""):
        ganador_name = home_repository.get_nombre_jugador_db(ganador_id, db)
        ganador_name = ganador_name.nombre
        ganador = Ganador(id_player=ganador_id, name=ganador_name)
    else :
        ganador = Ganador(id_player="", name="")
    return ganador

@router.delete("/eliminar/{sid}", response_model=PartidaData)
async def eliminar_partida(partida_id: int, sid: str, db: Session = Depends(get_db)):
    partida = home_repository.get_partida_db(db, partida_id)
    game_repository.eliminar_partida_db(partida_id, db)
    if sid != "back":
        data = {'db': db, 'partida_id': partida_id}
        await socket_game.fin_partida(data, sid)
    if start_turn_time is not None:
        start_turn_time.pop(partida_id, None)
    return partida

@router.get("/color_prohido", response_model=ColorProhibido) 
def color_prohibido(partida_id: int, db: Session = Depends(get_db)):
    color = game_repository.get_color_prohibido_db(partida_id, db)
    color = ColorProhibido(color=color)
    return color
