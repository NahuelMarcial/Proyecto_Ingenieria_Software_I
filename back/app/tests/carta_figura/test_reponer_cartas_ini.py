import pytest
from app.partida.models import Partida
# Test para reponer cartas de inicio para todos los jugadores de una partida
def test_reponer_cartas_ini(test_client, init_db):
    # Crear una partida con 4 jugadores
    partida = Partida(nombre="Partida de prueba", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", jugador3="Jugador3", jugador4="Jugador4", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear un set de cartas de figura para la partida
    test_client.post(f"/carta_figura/set/{partida.id}")

    # Realizar la petición al endpoint para reponer cartas de inicio para todos los jugadores
    response = test_client.patch(f"/carta_figura/reponer_cartas_ini/{partida.id}")
    assert response.status_code == 200

    # Verificar que cada jugador tiene 3 cartas mostradas
    cartas_mostradas = response.json()
    jugadores = [partida.jugador1, partida.jugador2, partida.jugador3, partida.jugador4]
    
    # Contar la cantidad de cartas mostradas por jugador
    cartas_por_jugador = {jugador: 0 for jugador in jugadores if jugador != ""}
    for carta in cartas_mostradas:
        cartas_por_jugador[carta["id_player"]] += 1

    # Asegurarse de que cada jugador tiene exactamente 3 cartas mostradas
    for jugador, cantidad in cartas_por_jugador.items():
        assert cantidad == 3

# Caso cuando la partida no existe
def test_reponer_cartas_ini_partida_no_existe(test_client):
    # Intentar reponer cartas de inicio en una partida inexistente
    response = test_client.patch("/carta_figura/reponer_cartas_ini/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Caso cuando la partida no ha iniciado
def test_reponer_cartas_ini_partida_no_iniciada(test_client, init_db):
    # Crear una partida que no ha iniciado
    partida = Partida(nombre="Partida no iniciada", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=False)
    db = init_db
    db.add(partida)
    db.commit()

    # Intentar reponer cartas de inicio
    response = test_client.patch(f"/carta_figura/reponer_cartas_ini/{partida.id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

# Caso cuando las cartas de figura ya han sido asignadas a un jugador
def test_reponer_cartas_ini_ya_asignadas1(test_client, init_db):
    # Crear una partida con 4 jugadores
    partida = Partida(nombre="Partida de prueba", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", jugador3="Jugador3", jugador4="Jugador4", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear un set de cartas de figura para la partida
    test_client.post(f"/carta_figura/set/{partida.id}")

    response1 = test_client.patch(f"/carta_figura/reponer_cartas_jugador/{partida.id}", json={"id_player": "Jugador1"})
    assert response1.status_code == 200
    response1_json = response1.json()

    # 
    response = test_client.patch(f"/carta_figura/reponer_cartas_ini/{partida.id}")
    assert response.status_code == 200
    response_json = response.json()
    # Verificar que cada carta en response1_json esté en response_json
    for carta in response1_json:
        assert carta in response_json
    assert len(response_json) == 12

# Caso cuando las cartas de figura ya han sido asignadas a todos los jugadores
def test_reponer_cartas_ini_ya_asignadas(test_client, init_db):
    # Crear una partida con 4 jugadores
    partida = Partida(nombre="Partida de prueba", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", jugador3="Jugador3", jugador4="Jugador4", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear un set de cartas de figura para la partida
    test_client.post(f"/carta_figura/set/{partida.id}")

    response1 = test_client.patch(f"/carta_figura/reponer_cartas_ini/{partida.id}")
    assert response1.status_code == 200
    response1_json = response1.json()

    # 
    response = test_client.patch(f"/carta_figura/reponer_cartas_ini/{partida.id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response1_json == response_json