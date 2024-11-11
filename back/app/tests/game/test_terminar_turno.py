import pytest 
from app.home.models import Partida
from app.game.carta_movimiento.models import Carta_Movimiento, movimientos
from app.game.fichas.models import Ficha
from app.game.carta_movimiento.carta_movimiento_repository import create_movimientos_db, get_movimientos_db


def test_pasar_turno_correctamente(test_client, init_db):
    # Creamos una partida iniciada con 2 jugadores
    partida = Partida(
        nombre="Partida Test", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="",
        jugador3="Jugador3",
        iniciada=True, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()
    test_client.post(f"/game/{partida.id}/carta_movimiento/set")
    test_client.post(f"/game/{partida.id}/carta_figura/set")
    # Terminamos el turno del jugador1
    response = test_client.patch(f"/game/{partida.id}/terminar_turno", json={"id_player": "Jugador1"})
    assert response.status_code == 200 ,"Error al terminar turno turno"
    
    # Verificamos que el turno pasó correctamente al siguiente jugador
    assert response.json() == {"id_player": "Jugador3"} ,f"El turno no pasó correctamente al siguiente jugador, se esperaba Jugador3 y se obtuvo {response.json()}"

    # Testeamos que de la vuelta completa correctamente
    response = test_client.patch(f"/game/{partida.id}/terminar_turno", json={"id_player": "Jugador3"})
    assert response.status_code == 200 , "Error al terminar turno"
    assert response.json() == {"id_player": "Jugador1"} ,f"El turno no pasó correctamente al siguiente jugador, se esperaba Jugador1 y se obtuvo {response.json()}"

def test_deshacer_mov_parciales(test_client, init_db):
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        iniciada=True,
        turno=1,
        cantidad_jugadores=2,
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
    ficha2 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=3)
    db.add(ficha1)
    db.add(ficha2)
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)

    data_json = {
    "id_carta": carta_movimiento.id_carta,
    "id_jugador": "Jugador1",
    "id_ficha1": ficha1.id_ficha,
    "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea contiguo arriba"

    db.refresh(carta_movimiento)
    movimientos1 = get_movimientos_db(db, partida.id)
    assert movimientos1[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea contiguo arriba] :No se asigno carta al movimiento"
    assert movimientos1[0].id_ficha1 == ficha1.id_ficha, "[Cruce en linea contiguo arriba]: No se asigno ficha1 al movimiento"
    assert movimientos1[0].id_ficha2 == ficha2.id_ficha, "[Cruce en linea contiguo arriba] : No se asigno ficha2 al movimiento"
    assert movimientos1[0].id_mov ==1, "[Cruce en linea contiguo arriba] :No se asigno id al movimiento"
    assert movimientos1[0].id_partida == partida.id, "[Cruce en linea contiguo arriba] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "No se marco carta como gastada"

    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 2, "Error al mover ficha1 en x"
    assert ficha1.pos_y == 3, "Error al mover ficha1 en y"
    assert ficha2.pos_x == 2, "Error al mover ficha2 en x"
    assert ficha2.pos_y == 2, "Error al mover ficha2 en y"

    response = test_client.patch(f"/game/{partida.id}/terminar_turno", json={"id_player": "Jugador1"})

    db.refresh(carta_movimiento)
    movimientos2 = db.query(movimientos).filter(movimientos.id_partida == partida.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos2)
    assert movimientos2.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    assert carta_movimiento.gastada == False, "Error al deshacer carta de movimiento cruce en linea contiguo arriba"

def test_pasar_turno_partida_no_iniciada(test_client, init_db):
    # Creamos una partida que no ha sido iniciada
    partida = Partida(
        nombre="Partida No Iniciada", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2", 
        iniciada=False, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.patch(f"/game/{partida.id}/terminar_turno", json={"id_player": "Jugador1"})
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

def test_jugador_no_pertenece_a_partida(test_client, init_db):
    # Creamos una partida iniciada con un jugador
    partida = Partida(
        nombre="Partida Test", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        iniciada=True, 
        turno=1, 
        cantidad_jugadores=1, 
        max_jugadores=1
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.patch(f"/game/{partida.id}/terminar_turno", json={"id_player": "JugadorDesconocido"})
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

def test_no_es_el_turno_del_jugador(test_client, init_db):
    # Creamos una partida con dos jugadores y el turno es del jugador 1
    partida = Partida(
        nombre="Partida Test", 
        owner="Jugador1", 
        jugador1="Jugador1", 
        jugador2="Jugador2", 
        iniciada=True, 
        turno=1, 
        cantidad_jugadores=2, 
        max_jugadores=2
    )
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.patch(f"/game/{partida.id}/terminar_turno", json={"id_player": "Jugador2"})
    assert response.status_code == 400
    assert response.json() == {"detail": "No es tu turno"}

def test_partida_no_existe(test_client, init_db):
    response = test_client.patch("/game/99999999/terminar_turno", json={"id_player": "Jugador1"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}