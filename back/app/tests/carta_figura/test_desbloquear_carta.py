from app.home.models import Partida
from app.game.carta_figura.models import Carta_Figura
from app.game.fichas.models import Ficha

def test_desbloquear_carta (test_client,init_db):
    partida = Partida(
        nombre="Partida",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True, bloqueada=True)
    db.add(carta2)
    db.commit()

    # Juego la carta 1 para desbloquear la carta 2
    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)

    assert response.status_code == 200, "Error al usar carta de figura"
    db.refresh(carta2)
    assert carta2.bloqueada == False, "La carta no se desbloqueo"
    assert carta2.mostrar == True, "la carta desbloqueada se dejo de mostrar"

def test_desbloquear_carta_no_bloqueada (test_client,init_db):
    partida = Partida(
        nombre="Partida",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta2)
    db.commit()

    # Juego la carta 1 para desbloquear la carta 2
    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)

    assert response.status_code == 200, "Error al usar carta de figura"
    db.refresh(carta2)
    assert carta2.bloqueada == False, "La carta2 deberia estar desbloqueada pero se bloqueo"
    assert carta2.mostrar == True, "la carta desbloqueada se dejo de mostrar"

def test_no_desbloquear (test_client,init_db):
    partida = Partida(
        nombre="Partida",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True, bloqueada=True)
    db.add(carta2)
    db.commit()

    carta3 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta3)
    db.commit()

    # Juego la carta 1 para desbloquear la carta 2
    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)

    assert response.status_code == 200, "Error al usar carta de figura"
    db.refresh(carta2)
    assert carta2.bloqueada == True, "La carta2 deberia estar bloqueada pero se desbloqueo"
    assert carta2.mostrar == True, "la carta desbloqueada se dejo de mostrar"

def test_desbloquear_despues_de_2_juegos (test_client,init_db):
    partida = Partida(
        nombre="Partida",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=1, color="azul")
    ficha6 = Ficha(id_ficha=6, id_partida=partida.id, pos_x=2, pos_y=1, color="azul")
    ficha7 = Ficha(id_ficha=7, id_partida=partida.id, pos_x=1, pos_y=2, color="azul")
    ficha8 = Ficha(id_ficha=8, id_partida=partida.id, pos_x=2, pos_y=2, color="azul")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5, ficha6, ficha7, ficha8])
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True, bloqueada=True)
    db.add(carta2)
    db.commit()

    carta3 = Carta_Figura(id_carta=3, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta3)
    db.commit()

    #primer consumo de carta
    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)

    assert response.status_code == 200, "Error al usar carta de figura"
    db.refresh(carta2)
    assert carta2.bloqueada == True, "La carta2 deberia estar bloqueada pero se desbloqueo"
    assert carta2.mostrar == True, "la carta desbloqueada se dejo de mostrar"

    #segundo consumo de carta
    data_json = {
    "id_carta": carta3.id_carta,
    "id_ficha": ficha5.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)

    assert response.status_code == 200, f"Error al usar carta de figura"
    db.refresh(carta2)
    assert carta2.bloqueada == False, "La carta no se desbloqueo"
    assert carta2.mostrar == True, "la carta desbloqueada se dejo de mostrar"