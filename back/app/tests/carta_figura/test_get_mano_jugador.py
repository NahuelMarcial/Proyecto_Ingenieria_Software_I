import pytest
import json
from app.home.models import Partida
from app.game.carta_figura.models import Carta_Figura
# Test para obtener las cartas figura de un jugador

# Test caso exitoso
def test_get_cartas_figura_mano_jugador(test_client, init_db):
    partida = Partida(nombre="Partida de prueba", owner="j1", jugador1="j1", jugador2= "j2", iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/game/{partida.id}/carta_figura/set")
    assert response.status_code == 200, f"Error al crear el set de cartas de figura"

    # Realizar la petición al endpoint para obtener las cartas figura de la mano
    response = test_client.get(f"/game/{partida.id}/carta_figura/mano_jugador/j1")
    assert response.status_code == 200,f"Error al obtener las cartas de figura de la mano"

    response_json = response.json()

    for carta in response_json:
        assert carta["mostrar"] == True ,"En la mano no debe haber cartas no mostradas"
        assert carta["id_player"] == "j1", f"El jugador de la carta es incorrecto. Esperado: j1, Actual: {carta['id_player']}"
    
    assert len(response_json) <= 3

# Caso exitoso: Obtener cartas figura mostradas de un jugador
def test_get_cartas_figura_mano_jugador_esp(test_client, init_db):
    # Crear una partida y asignar cartas figura
    partida = Partida(nombre="Partida Test", owner="Owner", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear y asignar cartas figura para un jugador
    carta1 = Carta_Figura(id_carta=1, nombre="Carta 1", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="Carta 2", color="blanca", id_partida=partida.id, id_player="Jugador2", mostrar=True)
    db.add_all([carta1, carta2])
    db.commit()

    # Realizar la petición al endpoint
    response = test_client.get(f"/game/{partida.id}/carta_figura/mano_jugador/Jugador1")

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200, f"Error al obtener las cartas de figura de la mano"
    cartas = response.json()
    assert len(cartas) == 1 ,f"El número de cartas es incorrecto. Esperado: 1, Actual: {len(cartas)}"
    assert cartas[0]["id_carta"] == 1 ,f"El id de la carta es incorrecto. Esperado: 1, Actual: {cartas[0]['id_carta']}"
    assert cartas[0]["nombre"] == "Carta 1",f"El nombre de la carta es incorrecto. Esperado: Carta 1, Actual: {cartas[0]['nombre']}"


# Caso de error: Partida no encontrada
def test_get_cartas_figura_jugador_partida_no_encontrada(test_client, init_db):
    # Realizar la petición al endpoint con un `partida_id` inexistente
    response = test_client.get("/game/99999999/carta_figura/mano_jugador/Jugador1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Caso de error: No hay cartas asignadas a la partida
def test_get_cartas_figura_jugador_sin_cartas(test_client, init_db):
    # Crear una partida sin cartas asignadas
    partida = Partida(nombre="Partida Sin Cartas", owner="Owner", jugador1="Jugador1", max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint
    response = test_client.get(f"/game/{partida.id}/carta_figura/mano_jugador/Jugador1")
    
    # Verificar que la respuesta indique que no hay cartas asignadas
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay cartas asignadas a la partida"}

# Caso de error: Jugador no pertenece a la partida
def test_get_cartas_figura_jugador_no_pertenece(test_client, init_db):
    # Crear una partida y asignar cartas figura
    partida = Partida(nombre="Partida Test", owner="Owner", jugador1="Jugador1", max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    test_client.post(f"/game/{partida.id}/carta_figura/set")

    # Realizar la petición al endpoint con un `jugador_id` que no pertenece a la partida
    response = test_client.get(f"/game/{partida.id}/carta_figura/mano_jugador/Jugador2")
    
    # Verificar que la respuesta indique que el jugador no pertenece a la partida
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}   