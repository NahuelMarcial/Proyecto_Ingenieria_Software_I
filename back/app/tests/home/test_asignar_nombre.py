from app.home.models import Info_Jugador

# Test para asignar un nombre exitosamente a un jugador nuevo
def test_asignar_nombre_exitoso(test_client, init_db):
    db = init_db

    id_nueva = db.query(Info_Jugador).count() + 1
    data = {
        "player_id": str(id_nueva),
        "nombre": "JugadorValido",
        "sid": "sid"
    }

    response = test_client.post("/home/asignar_nombre/", json=data)

    assert response.status_code == 200, "Fallo en endpoint asignar_nombre"
    jugador = response.json()
    assert jugador["player_id"] == str(id_nueva) , "El player_id no es el esperado"
    assert jugador["nombre"] == "JugadorValido" , "El nombre no es el esperado"

# Test para actualizar el nombre de un jugador existente
def test_el_jugador_ya_tiene_nombre(test_client, init_db):
    db = init_db

    # Insertar jugador existente en la base de datos
    jugador = Info_Jugador(player_id = "player1", nombre="JugadorAnterior")
    db.add(jugador)
    db.commit()

    data = {
        "player_id": "player1",
        "nombre": "NuevoNombre",
        "sid": "sid"
    }

    response = test_client.post("/home/asignar_nombre/", json=data)

    assert response.status_code == 400, "Se esperaba un status code 400"
    assert response.json() == {"detail": "Jugador ya tiene nombre"}

# Test fallo: nombre nulo o vacío
def test_asignar_nombre_fallo_nombre_vacio(test_client):
    data = {
        "player_id": "player2",
        "nombre": "",
        "sid": "sid"
    }

    response = test_client.post("/home/asignar_nombre/", json=data)

    assert response.status_code == 422 , "Se esperaba un status code 422"
    assert response.json() == {"detail": "Nombre de jugador invalido, debe ser entre 1 y 30 caracteres"}

# Test fallo: nombre demasiado largo
def test_asignar_nombre_fallo_nombre_largo(test_client):
    data = {
        "player_id": "player3",
        "nombre": "a" * 31,  # 31 caracteres
        "sid": "sid"
    }

    response = test_client.post("/home/asignar_nombre/", json=data)

    assert response.status_code == 422 , "Se esperaba un status code 422"
    assert response.json() == {"detail": "Nombre de jugador invalido, debe ser entre 1 y 30 caracteres"}

# Test fallo: nombre con caracteres no permitidos
def test_asignar_nombre_fallo_nombre_invalido(test_client):
    data = {
        "player_id": "player4",
        "nombre": "Nombre@Invalido",
        "sid": "sid"
    }

    response = test_client.post("/home/asignar_nombre/", json=data)

    assert response.status_code == 422, "Se esperaba un status code 422"
    assert response.json() == {"detail": "Nombre de jugador contiene caracteres inválidos"}
