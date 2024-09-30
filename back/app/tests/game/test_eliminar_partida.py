import pytest
from app.partida.models import Partida
import app.carta_figura.carta_figura_repository as carta_figura_repository

def test_mostrar_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

def test_eliminar_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", max_jugadores=4,iniciada=False, cantidad_jugadores=1)
    db = init_db
    db.add(partidavalida)
    db.commit()
    response = test_client.delete(f"/game/eliminar/{partidavalida.id}/back")
    assert response.status_code == 200
    print (response.json())
    assert response.json() == {
        "id": partidavalida.id,
        "nombre": "Partida Valida",
        "owner": "Jugador1",
        "jugador1": "Jugador1",
        "jugador2": "",
        "jugador3": "",
        "jugador4": "",
        "color_bloqueado": "",
        "max_jugadores": 4,
        "iniciada": False,
        "cantidad_jugadores": 1,
        "turno": 1
    }
    response = test_client.get(f"/partida/partidas/{partidavalida.id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
    response = test_client.delete(f"/game/eliminar/{partidavalida.id}/back")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_eliminar_partida_no_existente(test_client, init_db):
    response = test_client.delete(f"/game/eliminar/99999999/back")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_eliminar_db(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador",jugador2="Jugador2", max_jugadores=4,iniciada=True, cantidad_jugadores=2)

    db = init_db
    db.add(partidavalida)
    db.commit()

    # Agregamos los sets
    response = test_client.post(f"/fichas/crear/{partidavalida.id}")
    assert response.status_code == 200
    response = test_client.post(f"/carta_figura/set/{partidavalida.id}")
    assert response.status_code == 200
    response = test_client.post(f"/carta_movimiento/set/{partidavalida.id}")
    assert response.status_code == 200

    # Eliminamos la partida, lo que deberia eliminar los sets
    response = test_client.delete(f"/game/eliminar/{partidavalida.id}/back")
    assert response.status_code == 200

    response = test_client.get(f"/fichas/listar/{partidavalida.id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

    response = carta_figura_repository.get_cartas_figura_db(db, partidavalida.id)
    assert response == []

    response = test_client.get(f"/carta_movimiento/get/{partidavalida.id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}