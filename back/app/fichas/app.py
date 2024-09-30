from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db

from app.fichas.schemas import *
import app.fichas.utils as ficha_utils
import app.fichas.fichas_repository as ficha_repository

router = APIRouter()

@router.post("/crear/{partida_id}",response_model= list [FichaData])
def create_set_fichas(partida_id: int, db: Session = Depends(get_db)):
    error = ficha_utils.validar_partida(partida_id, db)
    if not error:
        ficha_repository.create_fichas_db(db, partida_id)
        ficha_repository.assign_random_positions_db(db, partida_id)
        return ficha_repository.get_fichas_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al crear las fichas")
    
@router.get("/listar/{partida_id}",response_model= list [FichaData])
def get_fichas(partida_id: int, db: Session = Depends(get_db)):
    error = ficha_utils.validar_partida_exist(partida_id, db)
    if not error:
        return ficha_repository.get_fichas_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al listar las fichas")