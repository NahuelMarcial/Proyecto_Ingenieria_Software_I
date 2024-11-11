import pytest 
from app.home.models import Partida
from app.game.carta_movimiento.models import Carta_Movimiento
from app.game.fichas.models import Ficha
#Casos existosos movimientos posibles cruce en linea contiguo

def test_get_movimientos_posibles_cruce_contiguo_4(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=0, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=4, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=2, pos_x=3, pos_y=2, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=3, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=4, pos_x=4, pos_y=3, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea contiguo "
    expected_response = [
        {'id_ficha': 4, 'pos_x': 4, 'pos_y': 3, 'color': 'amarillo'},
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 3, 'color': 'verde'},
        {'id_ficha': 1, 'pos_x': 3, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 2, 'pos_x': 3, 'pos_y': 2, 'color': 'rojo'}
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"


def test_get_movimientos_posibles_cruce_contiguo_3(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=1, pos_y=4, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=1, pos_y=2, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=2, pos_y=3, color="verde")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea contiguo "
    expected_response = [
        {'id_ficha': 4, 'pos_x': 2, 'pos_y': 3, 'color': 'verde'},
        {'id_ficha': 2, 'pos_x': 1, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 1, 'pos_y': 2, 'color': 'rojo'},
        
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_contiguo_2(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=1, pos_y=2, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=1, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea contiguo "
    expected_response = [
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 1, 'color': 'rojo'},
        {'id_ficha': 2, 'pos_x': 1, 'pos_y': 2, 'color': 'azul'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_linea_espacio_4(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=5, pos_y=3, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=1, pos_y=3, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=3, pos_y=5, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=5, pos_x=3, pos_y=1, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea con espacio "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 5, 'pos_y': 3, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 1, 'pos_y': 3, 'color': 'rojo'},
        {'id_ficha': 4, 'pos_x': 3, 'pos_y': 5, 'color': 'verde'},
        {'id_ficha': 5, 'pos_x': 3, 'pos_y': 1, 'color': 'amarillo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_linea_espacio_3(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=2, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=5, pos_y=2, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=1, pos_y=2, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=3, pos_y=4, color="verde")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea con espacio "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 5, 'pos_y': 2, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 1, 'pos_y': 2, 'color': 'rojo'},
        {'id_ficha': 4, 'pos_x': 3, 'pos_y': 4, 'color': 'verde'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_linea_espacio_2(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=2, pos_y=2, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=4, pos_y=2, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=4, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea con espacio "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 4, 'pos_y': 2, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 4, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

#caso exitoso cruce diagonal contiguo

def test_get_movimientos_posibles_cruce_diagonal_contiguo_4(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=4, pos_y=4, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=2, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=4, pos_y=2, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=5, pos_x=2, pos_y=4, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce diagonal contiguo "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 4, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 5, 'pos_x': 2, 'pos_y': 4, 'color': 'amarillo'},
        {'id_ficha': 4, 'pos_x': 4, 'pos_y': 2, 'color': 'verde'},
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 2, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

#No existe caso de cruce diagonal contiguo con 3 fichas

def test_get_movimientos_posibles_cruce_diagonal_contiguo_2(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=2, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=2, pos_y=3, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=1, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce diagonal contiguo "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 2, 'pos_y': 3, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 1, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_diagonal_contiguo_1(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=2, pos_y=2, color="azul")
    db.add_all([ficha,f_vecina1])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce diagonal contiguo "
    expected_response = [{'id_ficha': 2, 'pos_x': 2, 'pos_y': 2, 'color': 'azul'}]
    print (response.json())
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

#caso exitoso cruce diagonal con espacio

def test_get_movimientos_posibles_cruce_diagonal_espacio_4(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=5, pos_y=5, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=1, pos_y=1, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=5, pos_y=1, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=5, pos_x=1, pos_y=5, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce diagonal con espacio "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 5, 'pos_y': 5, 'color': 'azul'},
        {'id_ficha': 5, 'pos_x': 1, 'pos_y': 5, 'color': 'amarillo'},
        {'id_ficha': 4, 'pos_x': 5, 'pos_y': 1, 'color': 'verde'},
        {'id_ficha': 3, 'pos_x': 1, 'pos_y': 1, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

#No existe caso de cruce diagonal con espacio con 3 fichas

def test_get_movimientos_posibles_cruce_diagonal_espacio_2(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=3, pos_y=5, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=3, pos_y=1, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce diagonal con espacio "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 3, 'pos_y': 5, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 3, 'pos_y': 1, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_diagonal_espacio_1(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=3, pos_y=3, color="azul")
    db.add_all([ficha,f_vecina1])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce diagonal con espacio "
    expected_response = [{'id_ficha': 2, 'pos_x': 3, 'pos_y': 3, 'color': 'azul'}]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

#caso exitoso cruce en L derecha
def test_get_movimientos_posibles_cruce_L_derecha_4(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=5, pos_y=4, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=5, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=4, pos_y=1, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=5, pos_x=1, pos_y=2, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 4, 'pos_x': 4, 'pos_y': 1, 'color': 'verde'},
        {'id_ficha': 2, 'pos_x': 5, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 5, 'color': 'rojo'},
        {'id_ficha': 5, 'pos_x': 1, 'pos_y': 2, 'color': 'amarillo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimients_posibles_cruce_L_derecha_3(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=2, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=4, pos_y=4, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=1, pos_y=5, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=3, pos_y=1, color="verde")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 4, 'pos_x': 3, 'pos_y': 1, 'color': 'verde'},
        {'id_ficha': 2, 'pos_x': 4, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 1, 'pos_y': 5, 'color': 'rojo'},
    ]
    print(response.json())
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_L_derecha_2(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=2, pos_y=2, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=4, pos_y=3, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=1, pos_y=4, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 4, 'pos_y': 3, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 1, 'pos_y': 4, 'color': 'rojo'},
    ]
    
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruce_L_derecha_1(test_client,init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=3, pos_y=2, color="azul")
    db.add_all([ficha,f_vecina1])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 3, 'pos_y': 2, 'color': 'azul'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"


#caso exitoso cruce en L izquierda

def test_get_movimientos_posibles_cruces_L_izquierda_4(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=5, pos_y=2, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=4, pos_y=5, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=1, pos_y=4, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=5, pos_x=2, pos_y=1, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 5, 'pos_x': 2, 'pos_y': 1, 'color': 'amarillo'},
        {'id_ficha': 2, 'pos_x': 5, 'pos_y': 2, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 4, 'pos_y': 5, 'color': 'rojo'},
        {'id_ficha': 4, 'pos_x': 1, 'pos_y': 4, 'color': 'verde'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruces_L_izquierda_3(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=2, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=4, pos_y=2, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=3, pos_y=5, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=1, pos_y=1, color="verde")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 4, 'pos_x': 1, 'pos_y': 1, 'color': 'verde'},
        {'id_ficha': 2, 'pos_x': 4, 'pos_y': 2, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 3, 'pos_y': 5, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruces_L_izquierda_2(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=2, pos_y=2, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=4, pos_y=1, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=3, pos_y=4, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 4, 'pos_y': 1, 'color': 'azul'},
        {'id_ficha': 3, 'pos_x': 3, 'pos_y': 4, 'color': 'rojo'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

def test_get_movimientos_posibles_cruces_L_izquierda_1(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=2, pos_y=3, color="azul")
    db.add_all([ficha,f_vecina1])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en L derecha "
    expected_response = [
        {'id_ficha': 2, 'pos_x': 2, 'pos_y': 3, 'color': 'azul'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"

#caso exitoso cruce en linea lateral 

def test_get_movimientos_posibles_cruce_linea_lateral_4(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=3, pos_y=6, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=3, pos_y=1, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=4, pos_x=6, pos_y=3, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=5, pos_x=1, pos_y=3, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea lateral "
    expected_response = [
        {'id_ficha': 3, 'pos_x': 3, 'pos_y': 1, 'color': 'rojo'},
        {'id_ficha': 2, 'pos_x': 3, 'pos_y': 6, 'color': 'azul'},
        {'id_ficha': 5, 'pos_x': 1, 'pos_y': 3, 'color': 'amarillo'},
        {'id_ficha': 4, 'pos_x': 6, 'pos_y': 3, 'color': 'verde'},
    ]
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"


def test_get_movimientos_posibles_cruce_linea_lateral_esquina(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=1, pos_y=6, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=6, pos_y=1, color="rojo")
    f_vecina3 = Ficha(id_partida = partida.id, id_ficha=4, pos_x=1, pos_y=2, color="verde")
    f_vecina4 = Ficha(id_partida = partida.id, id_ficha=5, pos_x=1, pos_y=3, color="amarillo")
    f_vecina5 = Ficha(id_partida = partida.id, id_ficha=6, pos_x=1, pos_y=4, color="azul")
    f_vecina6 = Ficha(id_partida = partida.id, id_ficha=7, pos_x=1, pos_y=5, color="rojo")
    f_vecina7 = Ficha(id_partida = partida.id, id_ficha=8, pos_x=1, pos_y=6, color="verde")
    f_vecina8 = Ficha(id_partida = partida.id, id_ficha=9, pos_x=2, pos_y=1, color="amarillo")
    f_vecina9 = Ficha(id_partida = partida.id, id_ficha=10, pos_x=3, pos_y=1, color="azul")
    f_vecina10 = Ficha(id_partida = partida.id, id_ficha=11, pos_x=4, pos_y=1, color="rojo")
    f_vecina11 = Ficha(id_partida = partida.id, id_ficha=12, pos_x=5, pos_y=1, color="verde")
    f_vecina12 = Ficha(id_partida = partida.id, id_ficha=13, pos_x=6, pos_y=1, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4,f_vecina5,f_vecina6,f_vecina7,f_vecina8,f_vecina9,f_vecina10,f_vecina11,f_vecina12])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200, "No se ha podido obtener los movimientos posibles en cruce en linea lateral "
    expected_response = [
        {'id_ficha': 9, 'pos_x': 2, 'pos_y': 1, 'color': 'amarillo'},
        {'id_ficha': 10, 'pos_x': 3, 'pos_y': 1, 'color': 'azul'},
        {'id_ficha': 11, 'pos_x': 4, 'pos_y': 1, 'color': 'rojo'},
        {'id_ficha': 12, 'pos_x': 5, 'pos_y': 1, 'color': 'verde'},
        {'id_ficha': 3, 'pos_x': 6, 'pos_y': 1, 'color': 'rojo'},
        {'id_ficha': 4, 'pos_x': 1, 'pos_y': 2, 'color': 'verde'},
        {'id_ficha': 5, 'pos_x': 1, 'pos_y': 3, 'color': 'amarillo'},
        {'id_ficha': 6, 'pos_x': 1, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 7, 'pos_x': 1, 'pos_y': 5, 'color': 'rojo'},
        {'id_ficha': 2, 'pos_x': 1, 'pos_y': 6, 'color': 'azul'},
    ]
    print(response.json())
    assert response.json() == expected_response, "Los movimientos posibles no son los esperados"


#Casos no exitoso partida no iniciada 
def test_get_movimientos_posibles_partida_no_iniciada(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=2,iniciada=False)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=1, pos_y=6, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=6, pos_y=1, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 400, "Se esperaba codigo 400 porque la partida no ha iniciado"

#caso no exitoso ficha no existe 

def test_get_movimientos_posibles_ficha_no_existe(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=2,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()
    
    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)
    
    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=1, pos_y=6, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=6, pos_y=1, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()
    
    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/9999999999")
    assert response.status_code == 404, "Se esperaba codigo 404 porque la ficha no existe"

#caso no exitoso carta no existe

def test_get_movimientos_posibles_carta_no_existe(test_client, init_db):
    partida = Partida(nombre="Partida Valida", owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador 2', max_jugadores=2,iniciada=True)
    db= init_db
    db.add(partida)
    db.commit()

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1", gastada=False)
    db.add(carta)
    db.commit()

    ficha = Ficha(id_partida = partida.id, id_ficha=1, pos_x=1, pos_y=1, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=2, pos_x=1, pos_y=6, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=3, pos_x=6, pos_y=1, color="rojo")
    db.add_all([ficha,f_vecina1,f_vecina2])
    db.commit()

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/9999999999/{ficha.id_ficha}")
    assert response.status_code == 404, "Se esperaba codigo 404 porque la carta no existe"

#caso no exitoso Partida no existe

def test_get_movimientos_posibles_partida_no_existe(test_client, init_db):
    response = test_client.get(f"game/999999999/carta_movimiento/get_movimientos_posibles/1/1")
    assert response.status_code == 404, "Se esperaba codigo 404 porque la partida no existe"

