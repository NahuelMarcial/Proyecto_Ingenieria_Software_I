from fastapi import HTTPException
import random

from app.partida.models import Partida
import app.partida.partida_repository as partida_repository
import app.fichas.fichas_repository as fichas_repository

def validar_partida(partida_id, db):
    error = False
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="No se encontro partida")
    if not partida.iniciada :
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    fichas = fichas_repository.get_fichas_db(db, partida_id)
    if fichas:
        raise HTTPException(status_code=400, detail="Ya se asignaron las fichas a esta partida")
    return error

def validar_partida_exist(partida_id, db):
    error = False
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="No se encontro partida")
    if not partida.iniciada :
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    fichas = fichas_repository.get_fichas_db(db, partida_id)
    if not fichas:
        raise HTTPException(status_code=400, detail="No hay fichas asignadas a esta partida")
    return error    
    