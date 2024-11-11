from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.home.schemas import *
from app.database.database import get_db
import app.home.socket_home as socket_home
import app.home.logic as home_logic
import app.home.home_repository as home_repository

router = APIRouter()

@router.post("/crear/", response_model=PartidaData)
async def create_partida(partida: PartidaCreate, db: Session = Depends(get_db)):
    home_logic.validar_cantidad_jugadores(partida.max_jugadores)
    home_logic.validar_nombre(partida.nombre, "partida")
    home_logic.validar_nombre(partida.owner, "jugador")
    home_logic.validar_password(partida.password)
    partida_out = home_repository.create_new_partida_db(db, partida)
    
    # Verificar si el sid está conectado
    if partida.sid == 'back':
        return home_repository.get_partida_db(db, partida_out.id)
    else:
        await socket_home.crear_partida(partida.sid, partida_out.id)
        return home_repository.get_partida_db(db, partida_out.id)

@router.get("/partidas/{player_id}", response_model= list [PartidaGet])
def mostar_partidas(player_id: str, db: Session = Depends(get_db)):
    return home_logic.get_partidas(db, player_id)

@router.get("/partida/{partida_id}", response_model=PartidaData)
def mostrar_partida(partida_id: int, db: Session = Depends(get_db)):
    return home_repository.get_partida_db(db, partida_id)
    
@router.patch("/unirse/{partida_id}", response_model=PartidaData)
async def unirse_partida(partida_id: int, request: JoinRequest, db: Session = Depends(get_db)):
    error = home_logic.validar_no_pertenece(partida_id, request.jugador, db)
    if not error:
        home_repository.agregar_jugador_db(partida_id, request.jugador, request.password, db)
        if request.sid != 'back':
            data = {'db': db, 'partida_id': partida_id, 'playerId': request.jugador}
            await socket_home.unirse_partida(request.sid, data)
            
        return home_repository.get_partida_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al unirse") 
    
@router.post("/asignar_nombre/", response_model=NombreJugadorData)
def asignar_nombre(request: NombreJugadorData, db: Session = Depends(get_db)):
    home_logic.validar_nombre(request.nombre, "jugador")
    return home_repository.asignar_nombre_db(request, db)

@router.get("/nombre_jugador/{player_id}", response_model=NombreJugadorData)
def get_nombre_jugador(player_id: str, db: Session = Depends(get_db)):
    return home_repository.get_nombre_jugador_db(player_id, db)

@router.get("/partidas_activas/{player_id}", response_model= list [PartidaActiva])
def get_partidas_activas(player_id: str, db: Session = Depends(get_db)):
    Partidas = home_repository.get_all_partidas_db(db)
    Partidas_activas = home_logic.filtrar_partidas_activas(db, Partidas, player_id)
    return Partidas_activas
    

