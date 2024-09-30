import pytest
from app.partida.models import Partida
def test_get_owner(test_client, init_db):
    # Crear una partida de prueba
    partida = Partida(
        nombre="Partida de Prueba",
        owner="Hola soy el owner",
        max_jugadores=4,
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la solicitud GET para obtener el id del owner
    response = test_client.get(f"/lobby/owner/{partida.id}")

    # Validar que la respuesta sea 200
    assert response.status_code == 200

    # Validar que el JSON de la respuesta tiene el id del owner correcto
    data = response.json()
    assert data == {"owner": "Hola soy el owner"}

def test_get_jugadores_partida_no_existe(test_client, init_db):
    # Intentar obtener id del owner de una partida que no existe
    response = test_client.get("/lobby/jugadores/999999")  # ID que no existe
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
