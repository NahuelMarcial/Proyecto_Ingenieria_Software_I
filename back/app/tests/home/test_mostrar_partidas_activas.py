from app.home.schemas import PartidaActiva
from app.home.models import Partida
import app.home.home_repository as home_repository

def test_partidas_activas(test_client, init_db):
    # Crear partidas de prueba
    partida1 = Partida(
        nombre="Partida 1", owner="owner", iniciada=False, jugador1="owner",
        jugador2="test_player", cantidad_jugadores=2, max_jugadores=4, password=""
    )
    partida2 = Partida(
        nombre="Partida 2", owner="owner", iniciada=False, jugador1="owner",
        jugador2="test_player", cantidad_jugadores=2, max_jugadores=4, password="123456"
    )
    partida3 = Partida(
        nombre="Partida 3", owner="owner", iniciada=False, jugador1="owner",
        jugador2="test_player", jugador3="Pedro", jugador4="Juan",
        cantidad_jugadores=4, max_jugadores=4, password=""
    )
    partida4 = Partida(
        nombre="Partida 4", owner="owner", iniciada=True, jugador1="owner",
        jugador2="test_player", cantidad_jugadores=2, max_jugadores=4, password=""
    )
    partida5 = Partida(
        nombre="Partida 5", owner="owner", iniciada=False, jugador1="owner",
        jugador2="Pedro", cantidad_jugadores=2, max_jugadores=4, password=""
    )

    db = init_db
    db.add_all([partida1, partida2, partida3, partida4, partida5])
    db.commit()

    # Llamar al endpoint con el id del jugador
    response = test_client.get(f"/home/partidas_activas/test_player")
    assert response.status_code == 200, (
        "Error al obtener las partidas activas del jugador"
    )

    # Obtener la respuesta y verificar que sea una lista de PartidaActiva
    partidas_activas = response.json()
    assert isinstance(partidas_activas, list), (
        "La respuesta no es una lista de partidas"
    )

    for partida in partidas_activas:
        # Verificar que cada partida en la lista corresponde a una instancia de PartidaActiva
        partida_activa = PartidaActiva(**partida)

        assert partida_activa.id in [partida1.id, partida2.id, partida3.id], (
            f"La partida {partida_activa.id} no es una partida válida"
        )
        
        # Verificar que el jugador esté en cada partida
        jugadores = home_repository.get_jugadores_db(init_db, partida_activa.id)
        assert "test_player" in jugadores, (
            f"El jugador test_player no está en la partida {partida_activa.id}"
        )

        # Verificar si el campo `tu_turno` es True cuando corresponde al turno del jugador
        turno_actual = jugadores[partida_activa.turno - 1]
        if turno_actual == "test_player":
            assert partida_activa.tu_turno is True, (
                f"Es el turno del jugador test_player en la partida {partida_activa.id}"
            )
        else:
            assert partida_activa.tu_turno is False, (
                f"No es el turno del jugador test_player en la partida {partida_activa.id}"
            )
