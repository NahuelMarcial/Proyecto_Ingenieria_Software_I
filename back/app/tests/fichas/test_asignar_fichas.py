import pytest
from app.home.models import Partida

#test chequear que todas la fichas esten "dentro del tablero" 6x6
def test_asignar_fichas_tablero (test_client,init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    #chequeo que se creo bien
    assert response.status_code == 200 ,"error al crear fichas"
    response_json = response.json()
    assert len(response_json) == 36 , "las fichas creadas no son 36"


    #chequeo que se ocuparon todas las posiciones
    for ficha in response_json:
        #chequeo que todas la fichas esten "dentro del tablero"
        assert 1<= ficha["pos_x"] <= 6 , "la ficha no esta dentro del tablero en la posicion x"
        assert 1<= ficha["pos_y"] <= 6 , "la ficha no esta dentro del tablero en la posicion y"

#test chequear que en todas las posiciones hay solo una ficha
def test_asignar_fichas_pos (test_client,init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    #chequeo que se creo bien
    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 36 ,"las fichas creadas no son 36"
    
    #creo un conjunto donde meto todas las posiciones donde ya hay una ficha
    posiciones = set()
    for ficha in response_json:
        assert 1<= ficha["pos_x"] <= 6 , "la ficha no esta dentro del tablero en la posicion x"
        assert 1<= ficha["pos_y"] <= 6 , "la ficha no esta dentro del tablero en la posicion y"
        pos=(ficha["pos_x"],ficha["pos_y"])
        assert pos not in posiciones , "hay mas de una ficha en la misma posicion"
        posiciones.add(pos) 
    #verificar que todas las posiciones esten ocupadas
    assert len(posiciones) == 36 ,"no hay 36 fichas en el tablero"






