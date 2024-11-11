import pytest
from app.home.models import Partida
import json
# Caso exitoso: Crear el set de cartas de figura
def test_create_set_carta_figuras(test_client, init_db):
    
    partida_set_figura = Partida(nombre="Partida Valida", iniciada= True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_set_figura)
    db.commit()

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/game/{partida_set_figura.id}/carta_figura/set")
    assert response.status_code == 200 ,f"Error al crear el set de cartas de figura"

    # Convertir el contenido de la respuesta a JSON
    response_json = response.json()

    # Verificar que el set contiene el número esperado de cartas (por ejemplo, 50)
    assert len(response_json) == 50 ,f"El número de cartas es incorrecto. Esperado: 50, Actual: {len(response_json)}"

    # Verificar que los atributos de las cartas son los correctos
    with open("app/game/carta_figura/cartas_figura.json") as json_file:
        cartas_json = json.load(json_file)
        for i, carta in enumerate(response_json):
            assert carta["id_partida"] == partida_set_figura.id ,f"El id de la partida es incorrecto. Esperado: {partida_set_figura.id}, Actual: {carta['id_partida']}"
            assert carta["id_carta"] == cartas_json[i]["id_carta"],f"El id de la carta es incorrecto. Esperado: {cartas_json[i]['id_carta']}, Actual: {carta['id_carta']}"
            assert carta["nombre"] == cartas_json[i]["nombre"],f"El nombre de la carta es incorrecto. Esperado: {cartas_json[i]['nombre']}, Actual: {carta['nombre']}"
            assert carta["color"] == cartas_json[i]["color"],f"El color de la carta es incorrecto. Esperado: {cartas_json[i]['color']}, Actual: {carta['color']}"
            assert carta["descartada"] == False,"La carta no debería estar descartada"
            assert carta["bloqueada"] == False, "La carta no debería estar bloqueada"
            assert carta["reponer"] == True, "La carta no debería estar para reponer"

# Partida no encontrada
def test_create_set_carta_figuras_partida_no_encontrada(test_client, init_db):
    
    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post("/game/99999999/carta_figura/set")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Cartas de figura ya asignadas a la partida
def test_create_set_carta_figuras_cartas_ya_asignadas(test_client, init_db):
    
    partida_set_figura = Partida(nombre="Partida Valida",iniciada= True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_set_figura)
    db.commit()

    # Crear el set de cartas de figura
    test_client.post(f"/game/{partida_set_figura.id}/carta_figura/set")

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/game/{partida_set_figura.id}/carta_figura/set")
    assert response.status_code == 400
    assert response.json() == {"detail": "Ya se asignaron las cartas figura a esta partida"}