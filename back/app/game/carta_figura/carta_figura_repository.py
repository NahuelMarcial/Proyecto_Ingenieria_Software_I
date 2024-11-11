from sqlalchemy.orm import Session
from fastapi import HTTPException
import json
import random

from app.game.carta_figura.models import Carta_Figura
from app.game.carta_figura.schemas import *
import app.game.carta_figura.logic as carta_figura_logic
import app.game.carta_movimiento.logic as carta_movimiento_logic
import app.home.home_repository as home_repository
import app.game.fichas.fichas_repository as fichas_repository
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository


with open('app/game/carta_figura/cartas_figura.json', 'r') as file:
    cartas_figura_data = json.load(file)

def create_set_carta_figuras_db(db: Session, id_partida_in: int):
    cartas_figura = []
    for carta_figura in cartas_figura_data:
        db_carta_figura = Carta_Figura(
            id_carta=carta_figura["id_carta"],
            nombre=carta_figura["nombre"],
            color=carta_figura["color"],
            id_partida=id_partida_in,
            id_player="",
            mostrar=False,
            descartada=False,
            bloqueada=False,
            reponer=True
        )
        db.add(db_carta_figura)
        cartas_figura.append(db_carta_figura)
    db.commit()
    return cartas_figura

def get_cartas_figura_db(db: Session, id_partida_in: int):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida_in).all()

def get_cartas_figura_mostradas_db(db: Session, id_partida_in: int):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida_in, Carta_Figura.mostrar == True).all()

def asignar_cartas_figura(db: Session, id_partida: int):
    cartas_figura = get_cartas_figura_db(db, id_partida)
    players = home_repository.get_jugadores_db(db, id_partida)
    cartas_figura = carta_figura_logic.asignar_cartas_figura(cartas_figura, players)
    db.commit()
    return cartas_figura

def get_cartas_jugador_nodescartadas_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player, Carta_Figura.descartada == False).all()

def get_cartas_jugador_descartadas_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player, Carta_Figura.descartada == True).all()

def get_cartas_jugador_mostradas_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player, Carta_Figura.mostrar == True).all()

def get_cartas_jugador_mostradas_no_bloqu_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player, Carta_Figura.mostrar == True, Carta_Figura.bloqueada == False).all()

def get_cartas_jugador_db(db: Session, id_partida: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_player == id_player).all()

def get_carta_id_db(db: Session, id_partida: int, id_carta: int):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida, Carta_Figura.id_carta == id_carta).first()

def reponer_cartas_jugador_db(db: Session, partida_id: int, player_id: str):
    cartas_figura = get_cartas_jugador_nodescartadas_db(db, partida_id, player_id)
    mostradas = get_cartas_jugador_mostradas_db(db, partida_id, player_id)
    reponer = True
    for carta in mostradas:
        if carta.reponer == 0:
            reponer = False
            break
        
    if reponer:
        while len(mostradas) < 3:
            if not cartas_figura:
                break
            carta_random = random.choice(cartas_figura)
            carta_random.mostrar = True
            mostradas.append(carta_random)
            cartas_figura.remove(carta_random)
    db.commit()
    return mostradas

def delete_cartas_figura_db(db: Session, id_partida: int):
    db.query(Carta_Figura).filter(Carta_Figura.id_partida == id_partida).delete()
    db.commit()
    return None

def get_ganador_carta_figura_db(db: Session, id_partida: int):
    ganador = ""
    jugadores = home_repository.get_jugadores_db(db, id_partida)
    jugadores_validos = [jugador for jugador in jugadores if jugador != ""]
    for jugador in jugadores_validos:
        cartas_jugador = get_cartas_jugador_descartadas_db(db, id_partida, jugador)
        cartas_totales = get_cartas_jugador_db(db, id_partida, jugador)
        if len(cartas_jugador) == len(cartas_totales):
            ganador = jugador
            return ganador
    return ganador

def jugar_carta_db(db: Session, id_partida: int, id_carta: int, id_ficha: int):
    
    find = carta_figura_logic.ficha_pertenece_figura(id_partida, id_carta, id_ficha, db)
    if find:
        carta = get_carta_id_db(db, id_partida, id_carta)
        partida = home_repository.get_partida_db(db, id_partida)
        ficha = fichas_repository.get_ficha_partida_db(db, id_ficha, id_partida)
        carta.descartada = True
        carta.mostrar = False
        partida.color_bloqueado = ficha.color.value
        db.commit()
        
        carta_figura_logic.eliminar_movimientos_utiles(find, id_partida, db)
        db.commit()
        carta_movimiento_logic.deshacer_todos_movimientos(db, id_partida)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="La ficha no pertenece a la figura de la carta")
    
    return

def cheat_descartar_db(db, partida_id, id_player):
    cartas_jugador = get_cartas_jugador_db(db, partida_id, id_player)
    if len(cartas_jugador) > 1:
        for carta in cartas_jugador[:-1]:
            carta.descartada = True
            carta.mostrar = False
    db.commit()
    return

def bloquear_carta_db(db, id_partida, id_carta, id_ficha):
    find = carta_figura_logic.ficha_pertenece_figura(id_partida, id_carta, id_ficha, db)
    if find:
        carta = get_carta_id_db(db, id_partida, id_carta)
        partida = home_repository.get_partida_db(db, id_partida)
        ficha = fichas_repository.get_ficha_partida_db(db, id_ficha, id_partida)
        carta.bloqueada = True
        carta.reponer = False
        partida.color_bloqueado = ficha.color.value
        db.commit()
        
        carta_figura_logic.eliminar_movimientos_utiles(find, id_partida, db)
        db.commit()
        carta_movimiento_logic.deshacer_todos_movimientos(db, id_partida)
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="La ficha no pertenece a la figura de la carta")
    
    return


def get_cartas_restantes_db(db: Session, partida_id: int, id_player: str):
    return db.query(Carta_Figura).filter(Carta_Figura.id_partida == partida_id,
                                          Carta_Figura.id_player == id_player,
                                          Carta_Figura.descartada == False,
                                          Carta_Figura.mostrar == False).count()


def desbloquear_carta_db(db: Session, partida_id: int, cartas_en_mano):
    carta = cartas_en_mano[0]
    carta.bloqueada = False
    db.commit()
    return
