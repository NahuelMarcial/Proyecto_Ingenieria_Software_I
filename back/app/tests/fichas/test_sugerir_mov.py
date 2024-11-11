import pytest
from app.home.models import Partida
from app.game.fichas.models import Ficha
from app.game.carta_movimiento.models import Carta_Movimiento
from app.game.carta_figura.models import Carta_Figura
from app.game.fichas.schemas import SugerenciaData

def test_get_sugerencias_exitoso(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True,turno=1)
    db = init_db
    db.add(partida)
    db.commit()

    carta_figura = Carta_Figura(id_partida=partida.id, id_carta=1, nombre="fige6", color="azul", id_player="Jugador1", mostrar=True)
    db.add(carta_figura)
    db.commit()

    ficha0 = Ficha(id_partida=partida.id, id_ficha=1, pos_x=1, pos_y=2, color="rojo")
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_partida=partida.id, id_ficha=3, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_partida=partida.id, id_ficha=4, pos_x=4, pos_y=2, color="azul")
    ficha4 = Ficha(id_partida=partida.id, id_ficha=5, pos_x=5, pos_y=2, color="rojo")
    db.add_all([ficha0, ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 200, "No se pudo obtener la sugerencia"
    sugerencia = SugerenciaData(**response.json())
    print(sugerencia)
    print ("ficha 4 id " , ficha4.id_ficha) 
    print ("ficha 3 id " , ficha3.id_ficha)
    print ("carta id " , carta_movimiento.id_carta)
    assert sugerencia.id_ficha1 == ficha4.id_ficha, "La sugerencia no es la esperada"
    assert sugerencia.id_ficha2 == ficha3.id_ficha, "La sugerencia no es la esperada"
    assert sugerencia.id_carta == carta_movimiento.id_carta, "La sugerencia no es la esperada"

def test_get_sugerencias_bloqueada(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    carta_figura = Carta_Figura(id_partida=partida.id, id_carta=1, nombre="fige6", color="azul", id_player="Jugador1", mostrar=True, bloqueada=True)
    db.add(carta_figura)
    db.commit()

    ficha0 = Ficha(id_partida=partida.id, id_ficha=1, pos_x=1, pos_y=2, color="rojo")
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_partida=partida.id, id_ficha=3, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_partida=partida.id, id_ficha=4, pos_x=4, pos_y=2, color="azul")
    ficha4 = Ficha(id_partida=partida.id, id_ficha=5, pos_x=5, pos_y=2, color="rojo")
    db.add_all([ficha0, ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 200, "No se pudo obtener la sugerencia"
    sugerencia = SugerenciaData(**response.json())
    assert sugerencia.id_ficha1 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_ficha2 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_carta == -1, "La sugerencia no es la esperada"

def test_get_sugerencias_ya_formada(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    carta_figura = Carta_Figura(id_partida=partida.id, id_carta=1, nombre="fige6", color="azul", id_player="Jugador1", mostrar=True)
    db.add(carta_figura)
    db.commit()

    ficha0 = Ficha(id_partida=partida.id, id_ficha=1, pos_x=1, pos_y=2, color="rojo")
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_partida=partida.id, id_ficha=3, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_partida=partida.id, id_ficha=4, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_partida=partida.id, id_ficha=5, pos_x=5, pos_y=2, color="azul")
    db.add_all([ficha0, ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 200, "No se pudo obtener la sugerencia"
    sugerencia = SugerenciaData(**response.json())
    assert sugerencia.id_ficha1 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_ficha2 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_carta == -1, "La sugerencia no es la esperada"

def test_get_sugerencias_vacio(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    carta_figura = Carta_Figura(id_partida=partida.id, id_carta=1, nombre="fige5", color="azul", id_player="Jugador1", mostrar=True)
    db.add(carta_figura)
    db.commit()

    ficha0 = Ficha(id_partida=partida.id, id_ficha=1, pos_x=1, pos_y=2, color="rojo")
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_partida=partida.id, id_ficha=3, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_partida=partida.id, id_ficha=4, pos_x=4, pos_y=2, color="azul")
    ficha4 = Ficha(id_partida=partida.id, id_ficha=5, pos_x=5, pos_y=2, color="rojo")
    db.add_all([ficha0, ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 200, "No se pudo obtener la sugerencia"
    sugerencia = SugerenciaData(**response.json())
    assert sugerencia.id_ficha1 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_ficha2 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_carta == -1, "La sugerencia no es la esperada"

def test_get_sugerencias_dificil(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True, dificil=True)
    db = init_db
    db.add(partida)
    db.commit()

    carta_figura = Carta_Figura(id_partida=partida.id, id_carta=1, nombre="fige6", color="azul", id_player="Jugador1", mostrar=True)
    db.add(carta_figura)
    db.commit()

    ficha0 = Ficha(id_partida=partida.id, id_ficha=1, pos_x=1, pos_y=2, color="rojo")
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_partida=partida.id, id_ficha=3, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_partida=partida.id, id_ficha=4, pos_x=4, pos_y=2, color="azul")
    ficha4 = Ficha(id_partida=partida.id, id_ficha=5, pos_x=5, pos_y=2, color="rojo")
    db.add_all([ficha0, ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 200, "No se pudo obtener la sugerencia"
    sugerencia = SugerenciaData(**response.json())
    assert sugerencia.id_ficha1 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_ficha2 == -1, "La sugerencia no es la esperada"
    assert sugerencia.id_carta == -1, "La sugerencia no es la esperada"

def test_get_sugerencias_partida_no_iniciada(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=False)
    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 400, "Se esperaba un error porque la partida no ha iniciado"
    assert response.json()["detail"] == "La partida no ha iniciado"

def test_get_sugerencias_partida_no_existe(test_client, init_db):
    response = test_client.get(f"/game/-1/fichas/get_sugerencias/Jugador1")
    assert response.status_code == 404, "Se esperaba un error porque la partida no existe"
    assert response.json()["detail"] == "Partida no encontrada"

def test_get_sugerencias_jugador_no_existe(test_client, init_db):
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()

    ficha = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2, color="rojo")
    db.add(ficha)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/get_sugerencias/JugadorInexistente")
    print(response.json())
    assert response.status_code == 400, "Se esperaba un error porque el jugador no existe"
    assert response.json()["detail"] == "El jugador no pertenece a la partida"
