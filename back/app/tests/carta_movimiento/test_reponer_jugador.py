import pytest
from app.partida.models import Partida
from app.carta_movimiento.models import Carta_Movimiento
# Test para verificar que las cartas de movimiento se asignan correctamente a un jugador
def test_asignar_cartas_movimiento_jugador(test_client, init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear las cartas de movimiento para la partida
    cartas_movimiento = []
    for i in range(5):
        carta = Carta_Movimiento(id_partida=partida.id, id_carta=i, tipo_movimiento="Mover 1", descartada=False, id_player="")
        cartas_movimiento.append(carta)
    db.add_all(cartas_movimiento)
    db.commit()


    # Realizar la petición al endpoint que asigna las cartas de movimiento
    data = {"id_player": "Jugador1"}
    response = test_client.patch(f"/carta_movimiento/reponer_jugador/{partida.id}", json=data)
    assert response.status_code == 200

    # Obtener las cartas asignadas de la respuesta
    cartas_asignadas = response.json()

    # Verificar que se asignaron correctamente las cartas de movimiento al jugador
    num_cartas_movimiento = 3  # Asumimos que el jugador debe tener 5 cartas de movimiento

    # Verificar que el jugador tiene la cantidad correcta de cartas de movimiento
    assert len(cartas_asignadas) == num_cartas_movimiento
    for carta in cartas_asignadas:
        assert carta["id_player"] == "Jugador1"

# Test fallo no hay cartas asignadas de la partida
def test_asignar_cartas_movimiento_jugador_no_cartas(test_client, init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint que asigna las cartas de movimiento
    data = {"id_player": "Jugador1"}
    response = test_client.patch(f"/carta_movimiento/reponer_jugador/{partida.id}", json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no tiene cartas asignadas"}

# Test fallo partida no iniciada
def test_asignar_cartas_movimiento_jugador_partida_no_iniciada(test_client, init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=False)
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint que asigna las cartas de movimiento
    data = {"id_player": "Jugador1"}
    response = test_client.patch(f"/carta_movimiento/reponer_jugador/{partida.id}", json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

# Test fallo jugador no pertenece a la partida
def test_asignar_cartas_movimiento_jugador_no_pertenece(test_client, init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    test_client.post(f"/carta_movimiento/set/{partida.id}")

    # Realizar la petición al endpoint que asigna las cartas de movimiento
    data = {"id_player": "Jugador2"}
    response = test_client.patch(f"/carta_movimiento/reponer_jugador/{partida.id}", json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

# Test fallo partida no encontrada
def test_asignar_cartas_movimiento_jugador_partida_no_encontrada(test_client, init_db):
    # Realizar la petición al endpoint que asigna las cartas de movimiento
    data = {"id_player": "Jugador1"}
    response = test_client.patch(f"/carta_movimiento/reponer_jugador/999999", json=data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}