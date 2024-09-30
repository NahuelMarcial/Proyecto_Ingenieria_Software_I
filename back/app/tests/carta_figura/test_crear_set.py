import pytest
from app.partida.models import Partida
import json
# Caso exitoso: Crear el set de cartas de figura
def test_create_set_carta_figuras(test_client, init_db):
    
    partida_set_figura = Partida(nombre="Partida Valida", iniciada= True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_set_figura)
    db.commit()

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/carta_figura/set/{partida_set_figura.id}")
    assert response.status_code == 200

    # Convertir el contenido de la respuesta a JSON
    response_json = response.json()

    # Verificar que el set contiene el número esperado de cartas (por ejemplo, 50)
    assert len(response_json) == 50

    # Verificar que los atributos de las cartas son los correctos
    with open("app/carta_figura/cartas_figura.json") as json_file:
        cartas_json = json.load(json_file)
        for i, carta in enumerate(response_json):
            assert carta["id_partida"] == partida_set_figura.id
            assert carta["id_carta"] == cartas_json[i]["id_carta"]
            assert carta["nombre"] == cartas_json[i]["nombre"]
            assert carta["color"] == cartas_json[i]["color"]
            assert carta["descartada"] == False
            assert carta["bloqueada"] == False
            assert carta["reponer"] == False

# Partida no encontrada
def test_create_set_carta_figuras_partida_no_encontrada(test_client, init_db):
    
    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post("/carta_figura/set/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Cartas de figura ya asignadas a la partida
def test_create_set_carta_figuras_cartas_ya_asignadas(test_client, init_db):
    
    partida_set_figura = Partida(nombre="Partida Valida",iniciada= True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_set_figura)
    db.commit()

    # Crear el set de cartas de figura
    test_client.post(f"/carta_figura/set/{partida_set_figura.id}")

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/carta_figura/set/{partida_set_figura.id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "Ya se asignaron las cartas figura a esta partida"}