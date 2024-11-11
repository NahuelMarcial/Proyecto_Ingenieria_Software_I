import pytest
from app.home.models import Partida
from app.game.carta_movimiento.models import Carta_Movimiento

#caso exitoso traer cartas de movimiento de un jugador de una partida

def test_get_carta_movimiento(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    test_client.post(f"/game/{partida_set_movimiento.id}/carta_movimiento/set")
    response= test_client.get(f"/game/{partida_set_movimiento.id}/carta_movimiento/get_cartas_jugador/Jugador1")
    assert response.status_code == 200,f"Error al obtener cartas de movimiento de jugador"
    assert len(response.json()) == 3, "El largo de la lista de cartas de movimiento no es 3"
    assert response.json()[0]["id_player"] == "Jugador1" , "El jugador no tiene asignada la primer carta de movimiento"
    assert response.json()[1]["id_player"] == "Jugador1" , "El jugador no tiene asignada la segunda carta de movimiento"
    assert response.json()[2]["id_player"] == "Jugador1","El jugador no tiene asignada la tercer carta de movimiento"
#caso fallido traer cartas de movimiento de un jugador de una partida
def test_get_carta_movimiento_fallido(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    test_client.post(f"/game/{partida_set_movimiento.id}/carta_movimiento/set")
    test_client.patch(f"/game/{partida_set_movimiento.id}/carta_movimiento/asignar")
    response= test_client.get(f"/game/{partida_set_movimiento.id}/carta_movimiento/get_cartas_jugador/Jugador3")
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

def test_get_cartas_len(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    test_client.post(f"/game/{partida_set_movimiento.id}/carta_movimiento/set")
    response= test_client.get(f"/game/{partida_set_movimiento.id}/carta_movimiento/get")
    assert response.status_code == 200
    assert len(response.json()) == 49 , " Las cartas de movimiento creadas no son 49"

def test_get_cartas_partida_no_iniciada(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=False)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    response= test_client.get(f"/game/{partida_set_movimiento.id}/carta_movimiento/get")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}