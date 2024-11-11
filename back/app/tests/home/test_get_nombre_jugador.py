from app.home.models import Info_Jugador

# Test para obtener el nombre de un jugador exitosamente
def test_get_nombre_jugador_exitoso(test_client, init_db):
    db = init_db

    # Insertar un jugador en la base de datos
    jugador = Info_Jugador(nombre="JugadorValido")
    db.add(jugador)
    db.commit()
    db.refresh(jugador)
    jugador.player_id = str(jugador.id)
    db.commit()

    # Hacer la petición GET para obtener el nombre del jugador
    response = test_client.get(f"/home/nombre_jugador/{jugador.player_id}")

    assert response.status_code == 200, "Fallo en el endpoint get_nombre_jugador"
    data = response.json()
    assert data["player_id"] == str(jugador.id), "El player_id no coincide"
    assert data["nombre"] == "JugadorValido", "El nombre no coincide"

# Test fallo: Jugador no encontrado
def test_get_nombre_jugador_no_encontrado(test_client):
    # Hacer la petición GET para un jugador que no existe
    response = test_client.get("/home/nombre_jugador/holanoexisto")

    assert response.status_code == 404, "Se esperaba un status code 404"
    assert response.json() == {"detail": "Jugador no encontrado"}, "El mensaje de error no coincide"
