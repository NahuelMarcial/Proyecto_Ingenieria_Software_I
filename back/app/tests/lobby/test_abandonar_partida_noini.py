import pytest
from app.home.models import Partida
def test_abandonar_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2="Jugador2", jugador3= "Jugador3", iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/{partidavalida.id}/abandonar", json={"jugador": "Jugador3", "sid": "back"})
    assert response.status_code == 200 ,"Error al abandonar partida no iniciada"
    assert response.json() == {"id": partidavalida.id, "nombre": "Partida Valida", "owner": "Jugador1", "iniciada": False, 
                               "cantidad_jugadores": 3, "color_bloqueado": "", "turno": 1, "jugador1": "Jugador1", 
                               "jugador2": "Jugador2", "jugador3": "", "jugador4": "",
                                 "max_jugadores": 4}, "La partida no coincide con la esperada"
    

def test_owner_puede_abandonar(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2="Jugador2", jugador3= "Jugador3", iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/{partidavalida.id}/abandonar", json={"jugador": "Jugador1", "sid": "back"})
    assert response.status_code == 200 ,"Error al abandonar owner partida no iniciada"
    assert response.json() == {"id": partidavalida.id, "nombre": "Partida Valida", "owner": "Jugador1", "iniciada": True, 
                               "cantidad_jugadores": 3, "color_bloqueado": "", "turno": 1, "jugador1": "", 
                               "jugador2": "Jugador2", "jugador3": "Jugador3", "jugador4": "",
                                 "max_jugadores": 4}, "La partida no coincide con la esperada"


def test_id_partida_no_existe(test_client, init_db):
    response = test_client.patch("/99999999/abandonar", json={"jugador": "Jugador2", "sid": "back"})
    assert response.status_code == 404 

def test_jugador_no_en_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1",iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/{partidavalida.id}/abandonar", json={"jugador": "Jugador2", "sid": "back"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Jugador no encontrado en la partida"}


