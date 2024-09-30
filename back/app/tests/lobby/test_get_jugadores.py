import pytest
from app.partida.models import Partida


def test_get_jugadores(test_client, init_db):
    # Crear una partida de prueba con jugadores
    partida = Partida(
        nombre="Partida de Prueba",
        owner="Owner",
        iniciada=False,
        cantidad_jugadores=3,
        max_jugadores=4,
        jugador1="Owner",
        jugador2="",
        jugador3="Jugador3",
        jugador4="Jugador4"
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la solicitud GET para obtener los jugadores
    response = test_client.get(f"/lobby/jugadores/{partida.id}")

    # Validar que la respuesta sea 200
    assert response.status_code == 200

    # Validar que el JSON de la respuesta tiene los jugadores correctos
    data = response.json()
    assert data == {
        "jugador1": "Owner",
        "jugador2": "",
        "jugador3": "Jugador3",
        "jugador4": "Jugador4"
    }

def test_get_jugadores_partida_no_existe(test_client, init_db):
    # Intentar obtener los jugadores de una partida que no existe
    response = test_client.get("/lobby/jugadores/999999")  # ID que no existe
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}