import pytest
from app.partida.models import Partida
from app.carta_movimiento.models import Carta_Movimiento
from app.carta_movimiento import carta_movimiento_repository
from fastapi import HTTPException

# Test para verificar que las cartas de movimiento se desasignan correctamente de un jugador
def test_desasignar_cartas_movimiento_jugador(init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear las cartas de movimiento para la partida y asignarlas al jugador
    cartas_movimiento = []
    for i in range(3):
        carta = Carta_Movimiento(id_partida=partida.id, id_carta=i, tipo_movimiento="Mover 1", descartada=False, id_player="Jugador1")
        cartas_movimiento.append(carta)
    db.add_all(cartas_movimiento)
    db.commit()

    # Llamar a la función para desasignar las cartas de movimiento
    cartas_desasignadas = carta_movimiento_repository.desasignar_cartas_movimiento(db, partida.id, "Jugador1")

    # Verificar que las cartas de movimiento se desasignaron correctamente del jugador
    assert len(cartas_desasignadas) == 3
    for carta in cartas_desasignadas:
        assert carta.id_player == ""

# Test fallo no hay cartas de movimiento asignadas al jugador
def test_desasignar_cartas_movimiento_jugador_no_asignadas(init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Llamar a la función y verificar lance error de set no asignado
    try:
        carta_movimiento_repository.desasignar_cartas_movimiento(db, partida.id, "Jugador1")
        assert False, "Debería haber lanzado una excepción ya que la partida no tiene cartas de movimiento asignadas"
    except HTTPException as e:
        assert str(e) == "400: La partida no tiene cartas asignadas"

# Test fallo partida no iniciada
def test_desasignar_cartas_movimiento_partida_no_iniciada(test_client, init_db):
    # Crear una partida válida que no ha sido iniciada
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=False)
    db = init_db
    db.add(partida)
    db.commit()

    # Llamar a la función y verificar que la partida no ha sido iniciada
    try:
        carta_movimiento_repository.desasignar_cartas_movimiento(db, partida.id, "Jugador1")
        assert False, "Debería haber lanzado una excepción ya que la partida no ha iniciado"
    except HTTPException as e:
        assert str(e) == "400: La partida no ha iniciado"

# Test fallo jugador no pertenece a la partida
def test_desasignar_cartas_movimiento_jugador_no_pertenece(test_client, init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", max_jugadores=1, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    response=test_client.post(f"/carta_movimiento/set/{partida.id}")
    # Intentar desasignar cartas de movimiento para un jugador que no pertenece a la partida
    try:
        carta_movimiento_repository.desasignar_cartas_movimiento(db, partida.id, "Jugador2")
        assert False, "Debería haber lanzado una excepción ya que el jugador no pertenece a la partida"
    except HTTPException as e:
        assert str(e) == "400: El jugador no pertenece a la partida"

# Test fallo partida no encontrada
def test_desasignar_cartas_movimiento_partida_no_encontrada(init_db):
    # Llamar a la función para desasignar cartas de una partida que no existe
    
    try:
        carta_movimiento_repository.desasignar_cartas_movimiento(init_db, 999999, "Jugador1")
        assert False, "Debería haber lanzado una excepción ya que la partida no fue encontrada"
    except HTTPException as e:
        assert str(e) == "404: Partida no encontrada"
