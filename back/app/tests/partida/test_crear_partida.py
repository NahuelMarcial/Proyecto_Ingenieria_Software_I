import pytest
import socketio

@pytest.fixture(scope="module")
def sio_client():
    sio = socketio.Client()
    sio.connect('http://localhost:8000', socketio_path='/sockets/socket_connection')
    yield sio
    sio.disconnect()

def test_largo_nombre_y_owner(test_client, sio_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Caso válido
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid}
    response = test_client.post("/partida/crear/", json=partida)
    assert response.status_code == 200

    # Caso vacío
    partida = {"nombre": "", "owner": "", "max_jugadores": 3, "sid": sid}
    response = test_client.post("/partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de jugador invalido, debe ser entre 1 y 30 caracteres"} or response.json() == {"detail": "Nombre de partida invalido, debe ser entre 1 y 30 caracteres"}

    # Caso inválido con owner demasiado largo
    partida = {"nombre": "PartidaValida", "owner": "Hola soy un nombre de owner muy muy muy largo que no deberia de pasar", "max_jugadores": 3, "sid": sid}
    response = test_client.post("/partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de jugador invalido, debe ser entre 1 y 30 caracteres"}

    # Caso inválido con nombre partida demasiado largo
    partida = {"nombre": "Nombre de partida muuuuuuuuuuy largo que no deberia pasar", "owner": "Jugador", "max_jugadores": 3, "sid": sid}
    response = test_client.post("/partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de partida invalido, debe ser entre 1 y 30 caracteres"}

def test_caracteres_invalidos(test_client, sio_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Nombre de partida contiene caracteres inválidos
    partida = {"nombre": "Partida@Invalida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid}
    response = test_client.post("partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de partida contiene caracteres inválidos"}

    # Nombre de jugador contiene caracteres inválidos
    partida = {"nombre": "PartidaValida", "owner": "Jugador_1", "max_jugadores": 3, "sid": sid}
    response = test_client.post("partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de jugador contiene caracteres inválidos"}

def test_max_jugadores(test_client, sio_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Cantidad de jugadores < 2
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 1, "sid": sid}
    response = test_client.post("partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Cantidad de jugadores invalida, debe ser entre 2 y 4"}

    # Cantidad de jugadores > 4
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 5, "sid": sid}
    response = test_client.post("partida/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Cantidad de jugadores invalida, debe ser entre 2 y 4"}

def test_inicializacion(test_client, sio_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Caso válido, testeando que el resto de atributos sean los correctos
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid}
    response = test_client.post("partida/crear/", json=partida)
    data = response.json()
    assert response.status_code == 200
    assert data["nombre"] == "PartidaValida"
    assert data["iniciada"] == False
    assert data["owner"] == "Jugador1"
    assert data["jugador1"] == data["owner"]
    assert data["jugador2"] == ""
    assert data["jugador3"] == ""
    assert data["jugador4"] == ""
    assert data["max_jugadores"] == 3
    assert data["cantidad_jugadores"] == 1