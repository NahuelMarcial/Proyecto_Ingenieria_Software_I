
import pytest
from app.home.models import Partida

def test_mostrar_partida(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.get(f"/home/partida/{partidavalida.id}")
    assert response.status_code == 200,"Error al mostrar partida"
    print(response.json())
    assert response.json() == {
        "id": partidavalida.id,
        "nombre": "Partida Valida",
        "owner": "Jugador1",
        "iniciada": False,
        "cantidad_jugadores": 1,
        "color_bloqueado": "",
        "turno": 1,
        "jugador1": "Jugador1",
        "jugador2": "",
        "jugador3": "",
        "jugador4": "",
        "max_jugadores": 4,
        "password": "",
        "dificil": False
    }, "La partida no coincide con la esperada"

def test_mostrar_partida_no_visible(test_client, init_db):
    partidavalida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", iniciada=True, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partidavalida)
    db.commit()

    response = test_client.get(f"/home/partida/{partidavalida.id}")
    assert response.status_code == 200 ,"Error al mostrar partida"
    assert response.json() == {
        "id": partidavalida.id,
        "nombre": "Partida Valida",
        "owner": "Jugador1",
        "iniciada": True,
        "cantidad_jugadores": 4,
        "color_bloqueado": "",
        "turno": 1,
        "jugador1": "Jugador1",
        "jugador2": "",
        "jugador3": "",
        "jugador4": "",
        "max_jugadores": 4,
        "password": "",
        "dificil": False
    },"La partida no coincide con la esperada"

def test_mostrar_partida_id_inexistente(test_client, init_db):
    response = test_client.get("/home/partida/9999999")  # ID que no existe
    assert response.status_code == 404  # Debe devolver 404 para ID no encontrado
    assert response.json() == {"detail": "Partida no encontrada"}
