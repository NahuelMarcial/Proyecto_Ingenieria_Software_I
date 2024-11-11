import pytest
from app.home.models import Partida
# Test para reponer cartas de un jugador exitosamente
def test_reponer_cartas_jugador_exitoso(test_client, init_db):
    # Crear una partida
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    
    # Añadir cartas de figura para el jugador
    response = test_client.post(f"/game/{partida.id}/carta_figura/set")
    assert response.status_code == 200,f"Error en añadir cartas de figura: {response.json()}"
    
    # Realizar la petición para reponer cartas
    response = test_client.patch(f"/game/{partida.id}/carta_figura/reponer_cartas_jugador", json={"id_player": "Jugador1"})
    
    assert response.status_code == 200 , "Error en reponer cartas de jugador por segunda vez"
    
    response_json = response.json()
    
    # Verificar que el jugador tenga 3 cartas "mostradas"
    assert len(response_json) == 3,"El jugador no tiene 3 cartas mostradas"
    for carta in response_json:
        assert carta["id_partida"] == partida.id, f"La carta no pertenece a la partida correspondiente"
        assert carta["id_player"] == "Jugador1" , f"La carta no pertenece al jugador esperado"
        assert carta["mostrar"] == True , f"La carta no está mostrada"
        assert carta["descartada"] == False , f"La carta está descartada"

    # Verificar que no se asignen de nuevo si ya hay 3 cartas mostradas
    response2 = test_client.patch(f"/game/{partida.id}/carta_figura/reponer_cartas_jugador", json={"id_player": "Jugador1"})
    assert response2.status_code == 200
    response_json2 = response.json()
    assert response_json == response_json2 , "La asignasion de cartas cambio cuando no deberia"

# Test para partida no encontrada
def test_reponer_cartas_jugador_partida_no_encontrada(test_client):
    # Realizar la petición para una partida inexistente
    response = test_client.patch("/game/99999999/carta_figura/reponer_cartas_jugador", json={"id_player": "Jugador1"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Test para partida no iniciada
def test_reponer_cartas_jugador_partida_no_iniciada(test_client, init_db):
    # Crear una partida que no ha iniciado
    partida = Partida(nombre="Partida Test No Iniciada", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=False)
    db = init_db
    db.add(partida)
    db.commit()
    
    # Realizar la petición para reponer cartas
    response = test_client.patch(f"/game/{partida.id}/carta_figura/reponer_cartas_jugador", json={"id_player": "Jugador1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

# Test para jugador sin cartas por reponer
def test_reponer_cartas_jugador_sin_cartas(test_client, init_db):
    # Crear una partida iniciada
    partida = Partida(nombre="Partida Test Sin Cartas", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    
    # Realizar la petición para reponer cartas cuando el jugador no tiene cartas no descartadas
    response = test_client.patch(f"/game/{partida.id}/carta_figura/reponer_cartas_jugador", json={"id_player": "Jugador1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no tiene cartas para reponer"}