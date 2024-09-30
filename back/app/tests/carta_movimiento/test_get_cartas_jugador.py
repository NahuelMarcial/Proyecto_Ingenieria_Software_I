import pytest
from app.partida.models import Partida
from app.carta_movimiento.models import Carta_Movimiento

#caso exitoso traer cartas de movimiento de un jugador de una partida

def test_get_carta_movimiento(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    response= test_client.get(f"/carta_movimiento/get_cartas_jugador/{partida_set_movimiento.id}/Jugador1")
    print (response.json())
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["id_player"] == "Jugador1"
    assert response.json()[1]["id_player"] == "Jugador1"
    assert response.json()[2]["id_player"] == "Jugador1"

#caso fallido traer cartas de movimiento de un jugador de una partida
def test_get_carta_movimiento_fallido(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    test_client.patch(f"/carta_movimiento/asignar/{partida_set_movimiento.id}")
    response= test_client.get(f"/carta_movimiento/get_cartas_jugador/{partida_set_movimiento.id}/Jugador3")
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

def test_get_cartas_len(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    response= test_client.get(f"/carta_movimiento/get/{partida_set_movimiento.id}")
    assert response.status_code == 200
    assert len(response.json()) == 49

def test_get_cartas_partida_no_iniciada(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=False)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    response= test_client.get(f"/carta_movimiento/get/{partida_set_movimiento.id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}