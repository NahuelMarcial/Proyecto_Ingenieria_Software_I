import pytest
from app.partida.models import Partida
import json
#caso exitoso asignar cartas de movimento
def test_asignar_cartas_movimiento_2(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    response=test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    assert response.status_code == 200
    cartas_asignadas = response.json()
    with open("app/carta_movimiento/cartas_movimiento.json") as file:
        cartas_movimiento = json.load(file)
        for i , carta in enumerate(cartas_asignadas):
            assert carta["id_carta"] == cartas_movimiento[i]["id_carta"]
            assert carta["tipo_movimiento"] == cartas_movimiento[i]["tipo_movimiento"]
            assert carta["descartada"] == False
            assert carta["id_partida"] == partida_set_movimiento.id
    #contar las cartas asignadas
    cartas_jugador= {"Jugador1": 0, "Jugador2": 0}
    for carta in cartas_asignadas: 
        if carta["id_player"] in cartas_jugador:
            cartas_jugador[carta["id_player"]] += 1
    assert cartas_jugador["Jugador1"] == 3
    assert cartas_jugador["Jugador2"] == 3

#caso fallido asignar cartas de movimento Partida no iniciada
def test_asignar_cartas_movimiento_noini(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=False)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()

    response=test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

#caso fallido asignar cartas de movimento Partida no encontrada
def test_asignar_cartas_movimiento_noenc(test_client,init_db):
    response=test_client.post(f"/carta_movimiento/set/999999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

#caso fallido ya se asignaron cartas de movimiento 
def test_asignar_cartas_movimiento_asig(test_client,init_db):
    partida_set_movimiento = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida_set_movimiento)
    db.commit()
    response=test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    assert response.status_code == 200
    response=test_client.post(f"/carta_movimiento/set/{partida_set_movimiento.id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "Ya se asignaron las cartas movimiento a esta partida"}