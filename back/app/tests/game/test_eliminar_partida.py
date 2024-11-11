import pytest
from app.home.models import Partida
import app.game.carta_figura.carta_figura_repository as carta_figura_repository

def test_eliminar_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", max_jugadores=4,iniciada=False, cantidad_jugadores=1)
    db = init_db
    db.add(partidavalida)
    db.commit()
    response = test_client.delete(f"/game/{partidavalida.id}/eliminar/back")
    assert response.status_code == 200 , "Error al eliminar partida"
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
    }, "La partida no coincide con la esperada"
    response = test_client.get(f"/home/partida/{partidavalida.id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
    response = test_client.delete(f"/game/{partidavalida.id}/eliminar/back")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_eliminar_partida_no_existente(test_client, init_db):
    response = test_client.delete(f"/game/99999999/eliminar/back")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_eliminar_db(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador",jugador2="Jugador2", max_jugadores=4,iniciada=True, cantidad_jugadores=2)

    db = init_db
    db.add(partidavalida)
    db.commit()

    # Agregamos los sets
    response = test_client.post(f"/game/{partidavalida.id}/fichas/crear")
    assert response.status_code == 200 , "Error al crear fichas"
    response = test_client.post(f"/game/{partidavalida.id}/carta_figura/set")
    assert response.status_code == 200 ,"Error al crear cartas figura"
    response = test_client.post(f"/game/{partidavalida.id}/carta_movimiento/set")
    assert response.status_code == 200 ,"Error al crear cartas movimiento"

    # Eliminamos la partida, lo que deberia eliminar los sets
    response = test_client.delete(f"/game/{partidavalida.id}/eliminar/back")
    assert response.status_code == 200,"Error al eliminar partida"

    response = test_client.get(f"/game/{partidavalida.id}/fichas/listar")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

    response = carta_figura_repository.get_cartas_figura_db(db, partidavalida.id)
    assert response == [] , "Error al eliminar cartas figura"

    response = test_client.get(f"/game/{partidavalida.id}/carta_movimiento/get")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}