from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.partida.schemas import *
from app.database.database import get_db
import app.partida.socket_partida as socket_partida
import app.partida.utils as utils
import app.partida.partida_repository as repository

router = APIRouter()

@router.post("/crear/", response_model=PartidaData)
async def create_partida(partida: PartidaCreate, db: Session = Depends(get_db)):
    utils.validar_cantidad_jugadores(partida.max_jugadores)
    utils.validar_nombre(partida.nombre, "partida")
    utils.validar_nombre(partida.owner, "jugador")
    partida_out = repository.create_new_partida_db(db, partida)
    
    # Verificar si el sid está conectado
    if partida.sid == 'back':
        return repository.get_partida_db(db, partida_out.id)
    else:
        await socket_partida.crear_partida(partida.sid, partida_out.id)
        return repository.get_partida_db(db, partida_out.id)

    

@router.get("/partidas/", response_model= list [PartidaData])
def mostar_partidas(db: Session = Depends(get_db)):
    return repository.get_partidas_db(db)

@router.get("/partidas/{partida_id}", response_model=PartidaData)
def mostrar_partida(partida_id: int, db: Session = Depends(get_db)):
    return repository.get_partida_db(db, partida_id)
    
@router.patch("/unirse/{partida_id}", response_model=PartidaData)
async def unirse_partida(partida_id: int, request: JoinRequest, db: Session = Depends(get_db)):
    if request.sid == 'back':
        repository.agregar_jugador_db(partida_id, request.jugador, db)
        return repository.get_partida_db(db, partida_id)
    else:
        data = {'db': db, 'partida_id': partida_id, 'playerId': request.jugador}
        repository.agregar_jugador_db(partida_id, request.jugador, db)
        await socket_partida.unirse_partida(request.sid, data)
        return repository.get_partida_db(db, partida_id)
    

