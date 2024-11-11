from app.game.fichas.models import *
from app.game.carta_movimiento.models import *
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.fichas.fichas_repository as fichas_repository
from fastapi import HTTPException

def movimiento(db, partida_id:int, carta_id:int, ficha1_id:int, ficha2_id:int):
    ficha1 = fichas_repository.get_ficha_partida_db(db, ficha1_id, partida_id)
    if ficha1 is None :
        raise HTTPException(status_code=400, detail="Ficha 1 no encontrada")
    ficha2 = fichas_repository.get_ficha_partida_db(db, ficha2_id, partida_id)
    if ficha2 is None :
        raise HTTPException(status_code=400, detail="Ficha 2 no encontrada")
    carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, partida_id, carta_id)
    if carta is None : 
        raise HTTPException(status_code=404, detail="Carta de movimiento no encontrada")
    nombre = carta.tipo_movimiento
    if nombre == "cruce en linea contiguo":
        return cruce_linea_contigua(ficha1, ficha2)
    if nombre == "cruce en linea con un espacio": 
        return cruce_linea_espacio(ficha1, ficha2)
    if nombre == "cruce diagonal contiguo" : 
        return cruce_diagonal_contigua(ficha1, ficha2)
    if nombre == "cruce diagonal con un espacio":
        return cruce_diagonal_espacio(ficha1, ficha2)
    if nombre == "cruce en L derecha":
        return cruce_L_derecha(ficha1, ficha2)
    if nombre == "cruce en L izquierda":
        return cruce_L_izquierda(ficha1, ficha2)
    if nombre == "cruce en linea lateral":
        return cruce_linea_lateral(ficha1, ficha2)

def cruce_linea_contigua(ficha1: Ficha, ficha2: Ficha):
    cambio_linea_cont = False 
    if ficha1.pos_x == ficha2.pos_x and ficha1.pos_y == ficha2.pos_y + 1 \
    or ficha1.pos_x == ficha2.pos_x and ficha1.pos_y == ficha2.pos_y - 1 \
    or ficha1.pos_x == ficha2.pos_x + 1 and ficha1.pos_y == ficha2.pos_y \
    or ficha1.pos_x == ficha2.pos_x - 1 and ficha1.pos_y == ficha2.pos_y:
        cambio_linea_cont = True
    return cambio_linea_cont

def cruce_linea_espacio(ficha1: Ficha, ficha2: Ficha):
    cambio_linea_esp = False
    if ficha1.pos_x == ficha2.pos_x and ficha1.pos_y == ficha2.pos_y + 2 \
    or ficha1.pos_x == ficha2.pos_x and ficha1.pos_y == ficha2.pos_y - 2 \
    or ficha1.pos_x == ficha2.pos_x + 2 and ficha1.pos_y == ficha2.pos_y \
    or ficha1.pos_x == ficha2.pos_x - 2 and ficha1.pos_y == ficha2.pos_y:
        cambio_linea_esp = True
    return cambio_linea_esp

def cruce_diagonal_contigua(ficha1: Ficha, ficha2: Ficha):
    cambio_diagonal_cont = False
    if ficha1.pos_x == ficha2.pos_x + 1 and ficha1.pos_y == ficha2.pos_y + 1\
    or ficha1.pos_x == ficha2.pos_x + 1 and ficha1.pos_y == ficha2.pos_y - 1\
    or ficha1.pos_x == ficha2.pos_x - 1 and ficha1.pos_y == ficha2.pos_y + 1\
    or ficha1.pos_x == ficha2.pos_x - 1 and ficha1.pos_y == ficha2.pos_y - 1:
        cambio_diagonal_cont = True
    return cambio_diagonal_cont

def cruce_diagonal_espacio(ficha1: Ficha, ficha2: Ficha):
    cambio_diagonal_esp = False
    if ficha1.pos_x == ficha2.pos_x + 2 and ficha1.pos_y == ficha2.pos_y + 2 \
    or ficha1.pos_x == ficha2.pos_x + 2 and ficha1.pos_y == ficha2.pos_y - 2 \
    or ficha1.pos_x == ficha2.pos_x - 2 and ficha1.pos_y == ficha2.pos_y + 2 \
    or ficha1.pos_x == ficha2.pos_x - 2 and ficha1.pos_y == ficha2.pos_y - 2:
        cambio_diagonal_esp = True
    return cambio_diagonal_esp

def cruce_L_derecha(ficha1: Ficha, ficha2: Ficha):
    cambio_L_der = False
    if ficha1.pos_x == ficha2.pos_x + 1 and ficha1.pos_y == ficha2.pos_y - 2 \
    or ficha1.pos_x == ficha2.pos_x + 2 and ficha1.pos_y == ficha2.pos_y + 1 \
    or ficha1.pos_x == ficha2.pos_x - 1 and ficha1.pos_y == ficha2.pos_y + 2 \
    or ficha1.pos_x == ficha2.pos_x - 2 and ficha1.pos_y == ficha2.pos_y - 1:
        cambio_L_der = True
    return cambio_L_der

def cruce_L_izquierda(ficha1: Ficha, ficha2: Ficha):
    cambio_L_izq = False
    if ficha1.pos_x == ficha2.pos_x - 1 and ficha1.pos_y == ficha2.pos_y - 2\
    or ficha1.pos_x == ficha2.pos_x + 2 and ficha1.pos_y == ficha2.pos_y - 1\
    or ficha1.pos_x == ficha2.pos_x + 1 and ficha1.pos_y == ficha2.pos_y + 2\
    or ficha1.pos_x == ficha2.pos_x - 2 and ficha1.pos_y == ficha2.pos_y + 1:
        cambio_L_izq = True
    return cambio_L_izq

def cruce_linea_lateral(ficha1: Ficha, ficha2: Ficha):
    cambio_linea_lat = False
    if ficha1.id_ficha != ficha2.id_ficha:
        if ficha1.pos_x == ficha2.pos_x and (ficha2.pos_y == 1 or ficha2.pos_y == 6):
            cambio_linea_lat = True
        if ficha1.pos_x == ficha2.pos_x and (ficha1.pos_y == 1 or ficha1.pos_y == 6):
            cambio_linea_lat = True
        if ficha1.pos_y == ficha2.pos_y and (ficha2.pos_x == 1 or ficha2.pos_x == 6):
            cambio_linea_lat = True
        if ficha1.pos_y == ficha2.pos_y and (ficha1.pos_x == 1 or ficha1.pos_x == 6):
            cambio_linea_lat = True
    return cambio_linea_lat


def movimientos_posibles(db, partida_id : int, carta_id: int, ficha_id: int):
    ficha = fichas_repository.get_ficha_partida_db(db, ficha_id, partida_id)
    if not ficha :
        raise HTTPException(status_code=400, detail="Ficha no encontrada")
    
    carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, partida_id, carta_id)
    if not carta :
        raise HTTPException(status_code=400, detail="Carta de movimiento no encontrada")
    
    nombre = carta.tipo_movimiento
    if nombre == "cruce en linea contiguo":
        return cruce_linea_contiguo_mov(db, partida_id, ficha)
    if nombre == "cruce en linea con un espacio":
        return cruce_linea_espacio_mov(db, partida_id, ficha)
    if nombre == "cruce diagonal contiguo":
        return cruce_diagonal_contiguo_mov(db, partida_id, ficha)
    if nombre == "cruce diagonal con un espacio":
        return cruce_diagonal_espacio_mov(db, partida_id, ficha)
    if nombre == "cruce en L derecha":
        return cruce_L_derecha_mov(db, partida_id, ficha)
    if nombre == "cruce en L izquierda":
        return cruce_L_izquierda_mov(db, partida_id, ficha)
    if nombre == "cruce en linea lateral":
        return cruce_linea_lateral_mov(db, partida_id, ficha)
    
def cruce_linea_contiguo_mov(db, partida_id: int, ficha: Ficha):
    desplazamientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x + dx, ficha.pos_y + dy)
        for dx, dy in desplazamientos
        if 0< ficha.pos_x + dx <= 6 and 0 < ficha.pos_y + dy <= 6
    ]
    return movimientos_posibles

def cruce_linea_espacio_mov(db, partida_id: int, ficha: Ficha):
    desplazamientos = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x + dx, ficha.pos_y + dy)
        for dx, dy in desplazamientos
        if 0< ficha.pos_x + dx <= 6 and 0 < ficha.pos_y + dy <= 6
    ]
    return movimientos_posibles           

def cruce_diagonal_contiguo_mov(db, partida_id: int, ficha: Ficha):
    desplazamientos = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x + dx, ficha.pos_y + dy)
        for dx, dy in desplazamientos
        if 0< ficha.pos_x + dx <= 6 and 0 < ficha.pos_y + dy <= 6
    ]
    return movimientos_posibles

def cruce_diagonal_espacio_mov(db, partida_id: int, ficha: Ficha):
    desplazamientos = [(2, 2), (-2, 2), (2, -2), (-2, -2)]
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x + dx, ficha.pos_y + dy)
        for dx, dy in desplazamientos
        if 0< ficha.pos_x + dx <= 6 and 0 < ficha.pos_y + dy <= 6
    ]
    return movimientos_posibles

def cruce_L_derecha_mov(db, partida_id: int, ficha: Ficha):
    desplazamientos = [(1, -2), (2, 1), (-1, 2), (-2, -1)]
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x + dx, ficha.pos_y + dy)
        for dx, dy in desplazamientos
        if 0< ficha.pos_x + dx <= 6 and 0 < ficha.pos_y + dy <= 6
    ]
    return movimientos_posibles

def cruce_L_izquierda_mov(db, partida_id: int, ficha: Ficha):
    desplazamientos = [(-1, -2), (2, -1), (1, 2), (-2, 1)]
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x + dx, ficha.pos_y + dy)
        for dx, dy in desplazamientos
        if 0< ficha.pos_x + dx <= 6 and 0 < ficha.pos_y + dy <= 6
    ]
    return movimientos_posibles

def cruce_linea_lateral_mov(db, partida_id: int, ficha: Ficha):
    #agregar todos los movimientos posibles
    #caso general 
    movimientos_posibles = [
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x, 1),
        fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x, 6),
        fichas_repository.get_ficha_pos_db(db, partida_id, 1, ficha.pos_y),
        fichas_repository.get_ficha_pos_db(db, partida_id, 6, ficha.pos_y)
    ]   
    #casos especiales 
    #caso borde x 
    if ficha.pos_x == 1 or ficha.pos_x == 6:
        movimientos_posibles = [
            fichas_repository.get_ficha_pos_db(db, partida_id, x, ficha.pos_y)
            for x in range(1, 7)
        ] + [
            fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x, 1),
            fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x, 6),
        ]
    
    #caso borde y
    if ficha.pos_y == 1 or ficha.pos_y == 6:
        movimientos_posibles = [
            fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x, y)
            for y in range(1, 7)
        ] + [
            fichas_repository.get_ficha_pos_db(db, partida_id, 1, ficha.pos_y),
            fichas_repository.get_ficha_pos_db(db, partida_id, 6, ficha.pos_y),
        ]

    #caso esquina
    esquinas= [(1,1),(1,6), (6,1), (6,6)]
    if (ficha.pos_x, ficha.pos_y) in esquinas:
        movimientos_posibles = [
            fichas_repository.get_ficha_pos_db(db, partida_id, x, ficha.pos_y)
            for x in range(1, 7)
        ] + [
            fichas_repository.get_ficha_pos_db(db, partida_id, ficha.pos_x, y)
            for y in range(1, 7)
        ]

    #eliminar la ficha actual
    movimientos_posibles = [
        mov for mov in movimientos_posibles
        if not (mov.pos_x == ficha.pos_x and mov.pos_y == ficha.pos_y)
    ]
    return movimientos_posibles