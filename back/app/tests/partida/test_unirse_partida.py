import pytest
from app.partida.models import Partida

# Configuración para la base de datos de prueba

def test_unirse_partida_id_inexistente(test_client):
    response = test_client.patch("/partida/unirse/999999", json={"jugador": "Jugador1", "sid": "back"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_unirse_partida_llena(test_client, init_db):
    partida_llena = Partida(nombre="Partida Llena", owner="Jugador3", iniciada=False, cantidad_jugadores=4, max_jugadores=4)
    db = init_db
    db.add(partida_llena)
    db.commit()

    response = test_client.patch(f"/partida/unirse/{partida_llena.id}", json={"jugador": "Jugadornuevo", "sid": "back"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Partida llena"}

def test_unirse_partida_iniciada(test_client, init_db):
    partida_iniciada = Partida(nombre="Partida Iniciada", owner="Jugador2", iniciada=True, cantidad_jugadores=1, max_jugadores=4)
    db = init_db
    db.add(partida_iniciada)
    db.commit()

    response = test_client.patch(f"/partida/unirse/{partida_iniciada.id}", json={"jugador": "Jugador3", "sid": "back"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No se puede unir a una partida iniciada"}

def test_unirse_partida_exitosa(test_client, init_db):
    partida_valida = Partida(nombre="Partida Válida", owner="Jugador1", iniciada=False, cantidad_jugadores=1, max_jugadores=4)
    db = init_db
    db.add(partida_valida)
    db.commit()

    response = test_client.patch(f"/partida/unirse/{partida_valida.id}", json={"jugador": "JugadorNuevo", "sid": "back"})
    assert response.status_code == 200  # Debería ser un éxito
    partida_actualizada = response.json()

     # Verifica que el número de jugadores se haya actualizado
    assert partida_actualizada['cantidad_jugadores'] == 2 
    
    # Verifica que el jugador se haya agregado a la partida
    assert (partida_actualizada['jugador1'] == 'JugadorNuevo' or
    partida_actualizada['jugador2'] == 'JugadorNuevo' or
    partida_actualizada['jugador3'] == 'JugadorNuevo' or
    partida_actualizada['jugador4'] == 'JugadorNuevo')  