from fastapi import HTTPException
from app.partida.schemas import PartidaData
import app.partida.partida_repository as partida_repository



def verificar_iniciar_partida(partida_id, jugador, db):
    partida = partida_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if not partida.owner == jugador:
        raise HTTPException(status_code=400, detail="Solo el owner puede iniciar la partida")
    if partida.cantidad_jugadores < 2:
        raise HTTPException(status_code=400, detail="No hay suficientes jugadores para iniciar la partida")
    if partida.iniciada:
        raise HTTPException(status_code=400, detail="La partida ya ha sido iniciada")
    return

def eliminar_jugador(partida, jugador, jugadores):
    
    jugador_encontrado = False

    for i in range(len(jugadores)):
        if (jugadores[i] == jugador) and jugador_encontrado == False:
            jugadores[i] = ""
            jugador_encontrado = True
            partida.cantidad_jugadores -= 1
            break
    
    if not jugador_encontrado:
        raise HTTPException(status_code=404, detail="Jugador no encontrado en la partida")
    return jugadores