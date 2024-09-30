import pytest
from app.partida.models import Partida

#test chequear que todas la fichas esten "dentro del tablero" 6x6
def test_asignar_fichas_tablero (test_client,init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    response = test_client.post(f"/fichas/crear/{partida_ficha.id}")
    #chequeo que se creo bien
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 36


    #chequeo que se ocuparon todas las posiciones
    for ficha in response_json:
        #chequeo que todas la fichas esten "dentro del tablero"
        assert 1<= ficha["pos_x"] <= 6
        assert 1<= ficha["pos_y"] <= 6

#test chequear que en todas las posiciones hay solo una ficha
def test_asignar_fichas_pos (test_client,init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    response = test_client.post(f"/fichas/crear/{partida_ficha.id}")
    #chequeo que se creo bien
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 36
    
    #creo un conjunto donde meto todas las posiciones donde ya hay una ficha
    posiciones = set()
    for ficha in response_json:
        assert 1<= ficha["pos_x"] <= 6
        assert 1<= ficha["pos_y"] <= 6
        pos=(ficha["pos_x"],ficha["pos_y"])
        assert pos not in posiciones
        posiciones.add(pos)
    #verificar que todas las posiciones esten ocupadas
    assert len(posiciones) == 36






