import pytest
from app.home.models import Partida
def test_get_turno_nro_correctamente(test_client, init_db):
    # Creamos una partida iniciada con 2 jugadores y turno 1
    partida = Partida(
        nombre="Partida Test Turno", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2",
        iniciada=True, 
        turno=3, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()
    
    # Solicitamos el número de turno
    response = test_client.get(f"/game/{partida.id}/turno_nro")
    assert response.status_code == 200 ,"Error al obtener el turno"
    assert response.json() == 3 , f"Se esperaba el turno 3 pero se obtuvo: {response.json()}"

def test_get_turno_nro_partida_no_iniciada(test_client, init_db):
    # Creamos una partida que no ha sido iniciada
    partida = Partida(
        nombre="Partida No Iniciada", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2", 
        iniciada=False, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/turno_nro")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

def test_get_turno_nro_partida_no_existe(test_client, init_db):
    response = test_client.get("/game/999999/turno_nro")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_get_turno_jugador_correctamente(test_client, init_db):
    # Creamos una partida iniciada con 3 jugadores y el turno en 2
    partida = Partida(
        nombre="Partida Turno Jugador", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2",
        jugador3="Jugador3",
        iniciada=True, 
        turno=2, 
        cantidad_jugadores=3, 
        max_jugadores=3
    )
    db = init_db
    db.add(partida)
    db.commit()
    
    # Solicitamos el jugador que tiene el turno
    response = test_client.get(f"/game/{partida.id}/turno_jugador")
    assert response.status_code == 200
    assert response.json() == {"id_player": "Jugador2"}

def test_get_turno_jugador_partida_no_iniciada(test_client, init_db):
    # Creamos una partida que no ha sido iniciada
    partida = Partida(
        nombre="Partida No Iniciada Turno Jugador", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2", 
        iniciada=False, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/turno_jugador")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

def test_get_turno_jugador_partida_no_existe(test_client, init_db):
    response = test_client.get("/game/99999999/turno_jugador")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
