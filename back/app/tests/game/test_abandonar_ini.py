import pytest
from app.home.models import Partida
# Test para verificar que un jugador abandona la partida correctamente
def test_abandonar_partida_ini_exitoso(test_client, init_db):
    # Crear una partida válida con 2 jugadores
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=2,
        turno=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    test_client.post(f"/game/{partida.id}/carta_movimiento/set")
    test_client.post(f"/game/{partida.id}/carta_figura/set")


    # Realizar la petición al endpoint para que Jugador2 abandone la partida
    response = test_client.patch(f"/game/{partida.id}/abandonar_partida_ini", json={"id_player": "Jugador2", "sid": "back"})
    partida_data = response.json()
    # Verificar que la respuesta es exitosa
    assert response.status_code == 200,"Error al abandonar partida iniciada"
    partida_data = response.json()

    # Verificar que la cantidad de jugadores se reduce y que Jugador2 fue eliminado
    assert partida_data["cantidad_jugadores"] == 1 , "La cantidad de jugadores no se redujo"
    assert partida_data["jugador2"] == "" ,"El jugador 2 no fue eliminado"
    assert partida_data["turno"] == 1 ,"El turno no se actualizo"

# Test fallo: el jugador no pertenece a la partida
def test_abandonar_partida_ini_jugador_no_pertenece(test_client, init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=1
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Intentar que un jugador no registrado abandone la partida
    data = {"id_player": "Jugador2", "sid": "back"}
    response = test_client.patch(f"/game/{partida.id}/abandonar_partida_ini", json=data)

    # Verificar que se devuelve un error
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

# Test fallo: la partida no está iniciada
def test_abandonar_partida_ini_partida_no_iniciada(test_client, init_db):
    # Crear una partida válida con 1 jugador que no ha sido iniciada
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        max_jugadores=2,
        iniciada=False,
        cantidad_jugadores=1
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Intentar que el jugador abandone la partida
    data = {"id_player": "Jugador1", "sid": "back"}
    response = test_client.patch(f"/game/{partida.id}/abandonar_partida_ini", json=data)

    # Verificar que se devuelve un error
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

# Test fallo: la partida no existe
def test_abandonar_partida_ini_partida_no_existente(test_client):
    # Intentar que un jugador abandone una partida que no existe
    data = {"id_player": "Jugador1", "sid": "back"}
    response = test_client.patch(f"/game/999999999/abandonar_partida_ini", json=data)

    # Verificar que se devuelve un error 404
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}
