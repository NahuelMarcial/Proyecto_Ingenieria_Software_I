import pytest
import json
from app.partida.models import Partida
from app.carta_figura.models import Carta_Figura
# Test caso exitoso
def test_get_cartas_figura_mano(test_client, init_db):
    partida = Partida(nombre="Partida de prueba", owner="j1", jugador1="j1", jugador2= "j2", iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/carta_figura/set/{partida.id}")
    assert response.status_code == 200

    # Realizar la petición al endpoint para obtener las cartas figura de la mano
    response = test_client.get(f"/carta_figura/mano/{partida.id}")
    assert response.status_code == 200

    response_json = response.json()

    for carta in response_json:
        assert carta["mostrar"] == True
        assert (carta["id_player"] == "j1" or carta["id_player"] == "j2")
    
    assert len(response_json) <= 6



# Test para obtener las cartas figura de la mano de una partida. Caso especifico
def test_get_cartas_figura_mano_esp(test_client, init_db):
    # Crear una partida y agregar cartas a la base de datos
    partida = Partida(nombre="Partida de prueba", owner="Jugador1", jugador1="Jugador1", iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Crear algunas cartas mostradas para la partida
    carta1 = Carta_Figura(id_carta=1, nombre="Carta 1", color="Rojo", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="Carta 2", color="Azul", id_partida=partida.id, id_player="Jugador2", mostrar=True)
    db.add(carta1)
    db.add(carta2)
    db.commit()

    # Realizar la petición al endpoint para obtener las cartas figura de la mano
    response = test_client.get(f"/carta_figura/mano/{partida.id}")
    assert response.status_code == 200

    # Verificar que las cartas obtenidas sean las correctas
    cartas_mano = response.json()
    assert len(cartas_mano) == 2
    assert cartas_mano[0]["nombre"] == "Carta 1"
    assert cartas_mano[1]["nombre"] == "Carta 2"

# Test cuando la partida no existe
def test_get_cartas_figura_partida_no_existe(test_client):
    # Intentar obtener cartas de una partida inexistente
    response = test_client.get("/carta_figura/mano/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Test cuando no hay cartas asignadas a la partida
def test_get_cartas_figura_sin_cartas(test_client, init_db):
    # Crear una partida sin cartas
    partida = Partida(nombre="Partida sin cartas", owner="Jugador1", jugador1="Jugador1", iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    # Intentar obtener cartas de la partida sin cartas
    response = test_client.get(f"/carta_figura/mano/{partida.id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay cartas asignadas a la partida"}