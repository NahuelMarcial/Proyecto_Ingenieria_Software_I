import pytest
from app.home.models import Partida
from app.game.carta_figura.models import Carta_Figura

# Caso: Descartar cartas correctamente para un jugador en una partida válida
def test_cheat_descartar_cartas_ok(test_client, init_db):
    # Crear una partida con 2 jugadores
    partida = Partida(
        nombre="Partida con cheat",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Asignar 3 cartas a Jugador1
    cartas = [
        Carta_Figura(id_carta=1, nombre="fig6", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True),
        Carta_Figura(id_carta=2, nombre="fig5", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True),
        Carta_Figura(id_carta=3, nombre="fig6", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    ]
    db.add_all(cartas)
    db.commit()

    # Realizar la petición para descartar cartas de Jugador1
    response = test_client.patch(f"/game/{partida.id}/carta_figura/cheat_descartar",json={"id_player": "Jugador1"})

    assert response.status_code == 200, "No se pudo descartar correctamente"
    
    # Verificar que solo queda una carta mostrada
    cartas_restantes = response.json()
    assert len(cartas_restantes) == 1, "No quedó exactamente una carta después del descarte"
    assert cartas_restantes[0]["id_player"] == "Jugador1", "La carta no pertenece al jugador esperado"

# Caso: Partida no encontrada
def test_cheat_descartar_partida_no_existe(test_client):
    response = test_client.patch("/game/999999999/carta_figura/cheat_descartar", json={"id_player": "Jugador1"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Caso: Jugador no pertenece a la partida
def test_cheat_descartar_jugador_no_existe(test_client, init_db):
    # Crear una partida con un solo jugador
    partida = Partida(nombre="Partida limitada", owner="Jugador1", jugador1="Jugador1", max_jugadores=2, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    carta = Carta_Figura(id_carta=6, nombre="fig6", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    # Intentar descartar cartas para un jugador inexistente
    response = test_client.patch(f"/game/{partida.id}/carta_figura/cheat_descartar", json={"id_player": "JugadorInexistente"})
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

# Caso: No hay cartas asignadas a la partida
def test_cheat_descartar_sin_cartas(test_client, init_db):
    # Crear una partida sin cartas asignadas
    partida = Partida(nombre="Partida sin cartas", owner="Jugador1", jugador1="Jugador1", max_jugadores=2, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Intentar descartar cartas
    response = test_client.patch(f"/game/{partida.id}/carta_figura/cheat_descartar", json={"id_player": "Jugador1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay cartas asignadas a la partida"}
