import pytest
from app.partida.models import Partida
def test_abandonar_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2="Jugador2", jugador3= "Jugador3", iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/abandonar/{partidavalida.id}", json={"jugador": "Jugador3", "sid": "back"})
    assert response.status_code == 200
    assert response.json() == {"id": partidavalida.id, "nombre": "Partida Valida", "owner": "Jugador1", "iniciada": False, "cantidad_jugadores": 3, "color_bloqueado": "", "turno": 1, "jugador1": "Jugador1", "jugador2": "Jugador2", "jugador3": "", "jugador4": "", "max_jugadores": 4}

def test_owner_no_puede_abandonar(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/abandonar/{partidavalida.id}", json={"jugador": "Jugador1", "sid": "back"})
    assert response.status_code == 400 
    assert response.json() == {"detail": "Owner abandona no implementado"}

def test_id_partida_no_existe(test_client, init_db):
    response = test_client.patch("/abandonar/99999999", json={"jugador": "Jugador2", "sid": "back"})
    assert response.status_code == 404 

def test_jugador_no_en_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1",iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/abandonar/{partidavalida.id}", json={"jugador": "Jugador2", "sid": "back"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Jugador no encontrado en la partida"}

def test_no_se_puede_abandonar_partida_iniciada(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1",jugador2= 'Jugador2', iniciada=True, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.patch(f"/lobby/abandonar/{partidavalida.id}", json={"jugador": "Jugador2", "sid": "back"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Abandonar partida iniciada no implementado"}

