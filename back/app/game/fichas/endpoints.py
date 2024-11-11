from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db

from app.game.fichas.schemas import *
import app.game.fichas.logic as ficha_logic
import app.game.carta_figura.logic as carta_figura_logic
import app.game.fichas.fichas_repository as ficha_repository
import app.game.fichas.socket_fichas as socket_fichas
import app.game.game_repository as game_repository

router = APIRouter()

@router.post("/crear",response_model= list [FichaData])
async def create_set_fichas(partida_id: int, db: Session = Depends(get_db)):
    error = ficha_logic.validar_partida(partida_id, db)
    if not error:
        ficha_repository.create_fichas_db(db, partida_id)
        ficha_repository.assign_random_positions_db(db, partida_id)
        await socket_fichas.set_creado(partida_id)
        return ficha_repository.get_fichas_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al crear las fichas")
    
@router.get("/listar",response_model= list [FichaData])
def get_fichas(partida_id: int, db: Session = Depends(get_db)):
    error = ficha_logic.validar_partida_exist(partida_id, db)
    if not error:
        return ficha_repository.get_fichas_db(db, partida_id)
    else:
        raise HTTPException(status_code=400, detail="Error al listar las fichas")
    
@router.get("/buscar_figuras_formadas",response_model= list [FigFormada])
def get_figuras_formadas(partida_id: int, db: Session = Depends(get_db)):
    error = ficha_logic.validar_partida_exist(partida_id, db)
    if not error:
        if not game_repository.get_dificultad_db(db, partida_id):
            return ficha_logic.get_figuras_formadas_db(db, partida_id)
        else: 
            return [] 
    else:
        raise HTTPException(status_code=400, detail="Error al buscar figuras formadas")
    
@router.get("/get_sugerencias/{player_id}", response_model=SugerenciaData)
def get_sugerencias(partida_id: int, player_id: str, db: Session = Depends(get_db)):
    error = ficha_logic.validar_partida_exist(partida_id, db)
    error = carta_figura_logic.validar_jugador_exist(partida_id, player_id, db)
    if not error:
        if not game_repository.get_dificultad_db(db, partida_id):
            sugerencia = ficha_logic.get_sugerencia(partida_id, player_id, db)
            if sugerencia:
                return sugerencia
            else:
                return SugerenciaData(id_ficha1=-1, id_ficha2=-1, id_carta=-1)
        else:
            return SugerenciaData(id_ficha1=-1, id_ficha2=-1, id_carta=-1)
    else:
        raise HTTPException(status_code=400, detail="Error al obtener sugerencias")
    