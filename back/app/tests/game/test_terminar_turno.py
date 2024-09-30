import pytest 
from app.partida.models import Partida
def test_pasar_turno_correctamente(test_client, init_db):
    # Creamos una partida iniciada con 2 jugadores
    partida = Partida(
        nombre="Partida Test", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="",
        jugador3="Jugador3",
        iniciada=True, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()
    test_client.post(f"/carta_movimiento/set/{partida.id}")
    test_client.post(f"/carta_figura/set/{partida.id}")
    # Terminamos el turno del jugador1
    response = test_client.patch(f"/game/terminar_turno/{partida.id}", json={"id_player": "Jugador1"})
    assert response.status_code == 200
    
    # Verificamos que el turno pasó correctamente al siguiente jugador
    assert response.json() == {"id_player": "Jugador3"}

    # Testeamos que de la vuelta completa correctamente
    response = test_client.patch(f"/game/terminar_turno/{partida.id}", json={"id_player": "Jugador3"})
    assert response.status_code == 200
    assert response.json() == {"id_player": "Jugador1"}

def test_pasar_turno_partida_no_iniciada(test_client, init_db):
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

    response = test_client.patch(f"/game/terminar_turno/{partida.id}", json={"id_player": "Jugador1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

def test_jugador_no_pertenece_a_partida(test_client, init_db):
    # Creamos una partida iniciada con un jugador
    partida = Partida(
        nombre="Partida Test", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        iniciada=True, 
        turno=1, 
        cantidad_jugadores=1, 
        max_jugadores=1
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.patch(f"/game/terminar_turno/{partida.id}", json={"id_player": "JugadorDesconocido"})
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

def test_no_es_el_turno_del_jugador(test_client, init_db):
    # Creamos una partida con dos jugadores y el turno es del jugador 1
    partida = Partida(
        nombre="Partida Test", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2", 
        iniciada=True, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.patch(f"/game/terminar_turno/{partida.id}", json={"id_player": "Jugador2"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No es tu turno"}

def test_partida_no_existe(test_client, init_db):
    response = test_client.patch("/game/terminar_turno/999999", json={"id_player": "Jugador1"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}