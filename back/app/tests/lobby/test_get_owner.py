import pytest
from app.home.models import Partida
def test_get_owner(test_client, init_db):
    # Crear una partida de prueba
    partida = Partida(
        nombre="Partida de Prueba",
        owner="Hola soy el owner",
        jugador1= "Hola soy el owner",
        max_jugadores=4,
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la solicitud GET para obtener el id del owner
    response = test_client.get(f"/lobby/{partida.id}/owner")

    # Validar que la respuesta sea 200
    assert response.status_code == 200 , "Error al obtener el owner"

    # Validar que el JSON de la respuesta tiene el id del owner correcto
    data = response.json()
    assert data == {"owner": "Hola soy el owner"} , "El owner no coincide con el esperado"

def test_get_jugadores_partida_no_existe(test_client, init_db):
    # Intentar obtener id del owner de una partida que no existe
    response = test_client.get("/lobby/999999/jugadores")  # ID que no existe
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
