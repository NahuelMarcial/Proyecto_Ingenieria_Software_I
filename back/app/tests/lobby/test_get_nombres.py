from app.home.models import Info_Jugador, Partida

# Test para obtener los nombres de los jugadores exitosamente
def test_get_nombres_exitoso(test_client, init_db):
    db = init_db

    j1 = Info_Jugador(nombre="Jugador Uno")
    j2 = Info_Jugador(nombre="Jugador Dos")
    j4 = Info_Jugador(nombre="Jugador Cuatro")
    db.add_all([j1, j2, j4])
    db.commit()
    db.refresh(j1)
    db.refresh(j2)
    db.refresh(j4)
    
    j1.player_id = str(j1.id)
    j2.player_id = str(j2.id)
    j4.player_id = str(j4.id)
    db.commit()

    # Crear una partida válida con jugadores asignados
    partida = Partida( 
        nombre="Partida Test", 
        owner=j1.player_id,
        jugador1=j1.player_id, 
        jugador2=j2.player_id, 
        jugador3="", 
        jugador4=j4.player_id,
        iniciada=False,
        max_jugadores=4,
        cantidad_jugadores=3
    )
    db.add(partida)
    db.commit()

    # Realizar la petición GET para obtener los nombres de los jugadores
    response = test_client.get(f"/lobby/{partida.id}/nombres")

    assert response.status_code == 200, "Fallo en el endpoint /nombres"
    
    data = response.json()
    assert data["jugador1"] == "Jugador Uno", "Nombre del jugador1 incorrecto"
    assert data["jugador2"] == "Jugador Dos", "Nombre del jugador2 incorrecto"
    assert data["jugador3"] == "", "Se esperaba nombre vacío para jugador3"
    assert data["jugador4"] == "Jugador Cuatro", "Nombre del jugador4 incorrecto"

# Test fallo: Partida no encontrada
def test_get_nombres_partida_no_encontrada(test_client):
    # Realizar la petición GET para una partida inexistente
    response = test_client.get("/lobby/9999999999/nombres")

    assert response.status_code == 404, "Se esperaba un status code 404"
    assert response.json() == {"detail": "Partida no encontrada"}, "El mensaje de error no coincide"
