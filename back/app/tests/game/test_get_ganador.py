import pytest
from app.partida.models import Partida

# Test para verificar que se obtiene correctamente el ganador de la partida
def test_ganador_exitoso(test_client, init_db):
    # Crear una partida válida con 1 jugador restante
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        max_jugadores=4,
        iniciada=True,
        cantidad_jugadores=1
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint para obtener el ganador
    response = test_client.get(f"/game/ganador/{partida.id}")

    # Verificar que la respuesta es exitosa
    assert response.status_code == 200
    ganador_data = response.json()

    # Verificar que el ganador es "Jugador1"
    assert ganador_data["id_player"] == "Jugador1"

# Test fallo: No hay un único jugador restante
def test_ganador_no_hay_unico_jugador(test_client, init_db):
    # Crear una partida con múltiples jugadores aún en la partida
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=4,
        iniciada=True,
        cantidad_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint para obtener el ganador
    response = test_client.get(f"/game/ganador/{partida.id}")

    # Verificar que la respuesta es exitosa pero no hay un ganador definido
    assert response.status_code == 200
    ganador_data = response.json()
    
    # Verificar que no se determina un ganador
    assert ganador_data["id_player"] == ""

# Test fallo: La partida no existe
def test_ganador_partida_no_existente(test_client):
    # Realizar la petición al endpoint para una partida que no existe
    response = test_client.get(f"/game/ganador/999999")

    # Verificar que se devuelve un error 404
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
