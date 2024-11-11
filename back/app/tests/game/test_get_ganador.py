import pytest
from app.home.models import Partida, Info_Jugador
from app.game.carta_figura.models import Carta_Figura

# Test para verificar que se obtiene correctamente el ganador de la partida
def test_ganador_exitoso(test_client, init_db):
    # Crear una partida válida con 1 jugador restante
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        max_jugadores=4,
        iniciada=True,
        cantidad_jugadores=1,
        ganador="Jugador1"
    )
    db = init_db
    db.add(partida)
    db.commit()

    jugador = Info_Jugador(
        player_id="Jugador1",
        nombre="Jugador1"
    )
    db.add(jugador)
    db.commit()


        # Crear cartas de figura para el jugador
    carta1 = Carta_Figura(id_carta = 1, nombre = "fige1", color = "blanca", id_partida = partida.id, id_player = "Jugador1", mostrar = True, descartada = False, bloqueada = False, reponer = False)
    carta2 = Carta_Figura(id_carta = 2, nombre = "fige2", color = "blanca", id_partida = partida.id, id_player = "Jugador1", mostrar = False, descartada = True, bloqueada = False, reponer = False)

    db.add_all([carta1, carta2])
    db.commit()

    # Realizar la petición al endpoint para obtener el ganador
    response = test_client.get(f"/game/{partida.id}/ganador")

    # Verificar que la respuesta es exitosa
    assert response.status_code == 200 ,"Error al obtener ganador"
    ganador_data = response.json()

    # Verificar que el ganador es "Jugador1"
    assert ganador_data["id_player"] == "Jugador1" ,"El ganador no es el jugador correspendiente, se esperaba Jugador1"

# Test fallo: La partida no existe
def test_ganador_partida_no_existente(test_client):
    # Realizar la petición al endpoint para una partida que no existe
    response = test_client.get(f"/game/99999999/ganador")

    # Verificar que se devuelve un error 404
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}


# Test ganador por cartas de figura caso exitoso no vacio
def test_ganador_cartas_figura_exitoso(test_client, init_db):
    # Crear una partida válida con 1 jugador restante
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=4,
        iniciada=True,
        cantidad_jugadores=2,
        ganador="Jugador2"
    )
    db = init_db
    db.add(partida)
    db.commit()

    jugador = Info_Jugador(
        player_id="Jugador2",
        nombre="Jugador2",
    )
    db.add(jugador)
    db.commit()

    # Crear cartas de figura para el jugador
    carta1 = Carta_Figura(id_carta = 1, nombre = "fige1", color = "blanca", id_partida = partida.id, id_player = "Jugador1", mostrar = True, descartada = False, bloqueada = False, reponer = False)
    carta2 = Carta_Figura(id_carta = 2, nombre = "fige2", color = "blanca", id_partida = partida.id, id_player = "Jugador2", mostrar = False, descartada = True, bloqueada = False, reponer = False)

    db.add_all([carta1, carta2])
    db.commit()

    # Realizar la petición al endpoint para obtener el ganador
    response = test_client.get(f"/game/{partida.id}/ganador")

    # Verificar que la respuesta es exitosa
    assert response.status_code == 200 ,"Error al obtener ganador"
    ganador_data = response.json()

    # Verificar que el ganador es "Jugador2"
    assert ganador_data["id_player"] == "Jugador2" ,"El ganador no es el jugador correspendiente, se esperaba Jugador2"

# Test ganador por cartas de figura caso exitoso vacio
def test_ganador_cartas_figura_sin_ganador(test_client, init_db):
    # Crear una partida válida con 1 jugador restante
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=4,
        iniciada=True,
        cantidad_jugadores=2,
        ganador=""
    )
    db = init_db
    db.add(partida)
    db.commit()

    jugador = Info_Jugador(
        player_id="Jugador1",
        nombre="Jugador1",
    )
    db.add(jugador)
    db.commit()

    # Crear cartas de figura para el jugador
    carta1 = Carta_Figura(id_carta = 1, nombre = "fige1", color = "blanca", id_partida = partida.id, id_player = "Jugador1", mostrar = True, descartada = False, bloqueada = False, reponer = False)
    carta2 = Carta_Figura(id_carta = 2, nombre = "fige2", color = "blanca", id_partida = partida.id, id_player = "Jugador2", mostrar = False, descartada = False, bloqueada = False, reponer = False)

    db.add_all([carta1, carta2])
    db.commit()

    # Realizar la petición al endpoint para obtener el ganador
    response = test_client.get(f"/game/{partida.id}/ganador")

    # Verificar que la respuesta es exitosa
    assert response.status_code == 200 ,"Error al obtener ganador"
    ganador_data = response.json()

    # Verificar que el ganador es "Jugador1"
    assert ganador_data["id_player"] == "" ,"Se detecto un ganador cuando no deberia haberlo"
