import pytest
from app.partida.models import Partida

def test_iniciar_partida(test_client, init_db):
    # Agregar partida de prueba con jugadores
    partida = Partida(
        nombre="Partida de Prueba", 
        owner="Owner", 
        iniciada=False, 
        cantidad_jugadores=2, 
        max_jugadores=4,
        jugador1="Owner", 
        jugador2="Jugador2"
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la solicitud PATCH para iniciar la partida
    response = test_client.patch(f"/lobby/iniciar/{partida.id}", json={"jugador": "Owner"})
    
    # Validar respuesta 200
    assert response.status_code == 200

    # Validar que el JSON de la respuesta tiene el atributo iniciada en True
    data = response.json()
    assert data["id"] == partida.id
    assert data["iniciada"] is True

    # Validar que el owner no cambió y que el total de jugadores sigue siendo el mismo
    assert data["owner"] == "Owner"
    jugadores = [data["jugador1"], data["jugador2"], data["jugador3"], data["jugador4"]]
    cont = 0
    owner_find = False
    j2_find = False
    for jugador in jugadores:
        if (jugador == ""):
            cont +=1
        if (jugador == "Owner"):
            owner_find = True
        if (jugador == "Jugador2"):
            j2_find = True
    assert cont == 2
    assert owner_find
    assert j2_find

    
def test_iniciar_partida_no_existe(test_client, init_db):
    # Intentar iniciar una partida que no existe
    response = test_client.patch("/lobby/iniciar/999999", json={"jugador": "Owner"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_iniciar_partida_menos_jugadores(test_client, init_db):
    # Agregar una partida con solo un jugador
    db = init_db
    partida = Partida(
        nombre="Partida Faltan Jugadores", 
        owner="Owner", 
        iniciada=False, 
        cantidad_jugadores=1, 
        max_jugadores=4,
        jugador1="Owner"
    )
    db.add(partida)
    db.commit()

    # Intentar iniciar la partida
    response = test_client.patch(f"/lobby/iniciar/{partida.id}", json={"jugador": "Owner"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay suficientes jugadores para iniciar la partida"}

def test_iniciar_partida_no_owner(test_client, init_db):
    # Agregar una partida
    db = init_db
    partida = Partida(
        nombre="Partida No Owner", 
        owner="Owner", 
        iniciada=False, 
        cantidad_jugadores=2, 
        max_jugadores=4,
        jugador1="Owner", 
        jugador2="Jugador2"
    )
    db.add(partida)
    db.commit()

    # Intentar iniciar la partida con un jugador que no es el owner
    response = test_client.patch(f"/lobby/iniciar/{partida.id}", json={"jugador": "Jugador2"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Solo el owner puede iniciar la partida"}

def test_iniciar_partida_ya_iniciada(test_client, init_db):
    # Agregar una partida que ya está iniciada
    db = init_db
    partida = Partida(
        nombre="Partida Ya Iniciada", 
        owner="Owner", 
        iniciada=True, 
        cantidad_jugadores=2, 
        max_jugadores=4,
        jugador1="Owner", 
        jugador2="Jugador2"
    )
    db.add(partida)
    db.commit()

    # Intentar iniciar la partida nuevamente
    response = test_client.patch(f"/lobby/iniciar/{partida.id}", json={"jugador": "Owner"})
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida ya ha sido iniciada"}

def test_arreglar_turno_db(test_client, init_db):
    # Configurar la base de datos de prueba
    db = init_db

    # Crear una partida con jugadores
    partida = Partida(
        nombre="Partida de Prueba", 
        owner="Owner", 
        iniciada=False, 
        cantidad_jugadores=4, 
        max_jugadores=4,
        jugador1="Owner", 
        jugador2="Jugador2", 
        jugador3="", 
        jugador4=""
    )
    db.add(partida)
    db.commit()

    response = test_client.patch(f"/lobby/iniciar/{partida.id}", json={"jugador": "Owner"})
    assert response.status_code == 200
    response_json = response.json()
    jugadores= [
        response_json["jugador1"],
        response_json["jugador2"],
        response_json["jugador3"],
        response_json["jugador4"]
    ]
    
    turno = response_json["turno"]
    assert jugadores [turno-1] != ""

    