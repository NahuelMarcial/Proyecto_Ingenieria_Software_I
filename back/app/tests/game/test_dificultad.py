import pytest
from app.home.models import Partida
from app.game.carta_movimiento.models import Carta_Movimiento
from app.game.fichas.models import Ficha
from app.game.carta_figura.models import Carta_Figura
#caso valido : 
# se crea una partida con dificultad dificil 
# Los jugadores se unen 
# Se incia la partida
# Se arma el tablero y se reparten las cartas 
# Se corrobora que no existan ayudas al jugador 

def test_dificultad(test_client, init_db) : 
    partida = Partida(nombre="partida1", iniciada=True, owner="jugador1", jugador1= "jugador1", jugador2="jugdaor2", max_jugadores=4, password="", dificil=True)
    db = init_db 
    db.add(partida)
    db.commit()
    db.refresh(partida)

    carta = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False) 
    db.add(carta)
    db.commit()
    db.refresh(carta)

    #fichas de prueba en carta de movimiento
    ficha = Ficha(id_partida = partida.id, id_ficha=0, pos_x=3, pos_y=3, color="azul")
    f_vecina1= Ficha(id_partida = partida.id, id_ficha=1, pos_x=3, pos_y=4, color="azul")
    f_vecina2= Ficha(id_partida = partida.id, id_ficha=2, pos_x=3, pos_y=2, color="rojo")
    f_vecina3= Ficha(id_partida = partida.id, id_ficha=3, pos_x=2, pos_y=3, color="verde")
    f_vecina4= Ficha(id_partida = partida.id, id_ficha=4, pos_x=4, pos_y=3, color="amarillo")
    db.add_all([ficha,f_vecina1,f_vecina2,f_vecina3,f_vecina4])
    db.commit()

    #fichas de prueba en buscar figura formada 
    ficha_form1= Ficha(id_partida = partida.id, id_ficha=5, pos_x=1, pos_y=1, color="azul")
    ficha_form2= Ficha(id_partida = partida.id, id_ficha=6, pos_x=2, pos_y=1, color="azul")
    ficha_form3= Ficha(id_partida = partida.id, id_ficha=7, pos_x=3, pos_y=1, color="azul")
    ficha_form4= Ficha(id_partida = partida.id, id_ficha=8, pos_x=4, pos_y=1, color="azul")
    db.add_all([ficha_form1,ficha_form2,ficha_form3,ficha_form4])
    db.commit()

    #asignar 3 cartas de figura al jugador 2 
    cartas = [
        Carta_Figura(id_carta=1, nombre="fig6", color="blanca", id_partida=partida.id, id_player="jugador1", mostrar=True),
        Carta_Figura(id_carta=2, nombre="fig5", color="blanca", id_partida=partida.id, id_player="jugador1", mostrar=True),
        Carta_Figura(id_carta=3, nombre="fig6", color="blanca", id_partida=partida.id, id_player="jugador1", mostrar=True)
    ]
    db.add_all(cartas)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200 , " Error al buscar figuras formadas"
    assert response.json() == [] , "Se obtuvo ayuda de figura formada en partida dificil"

    response = test_client.get(f"game/{partida.id}/carta_movimiento/get_movimientos_posibles/{carta.id_carta}/{ficha.id_ficha}")
    assert response.status_code == 200 , "Error al obtener movimientos posibles"
    expected_movimientos_posibles_response= [
        {'id_ficha': 0, 'pos_x': 3, 'pos_y': 3, 'color': 'azul'}, 
        {'id_ficha': 1, 'pos_x': 3, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 2, 'pos_x': 3, 'pos_y': 2, 'color': 'rojo'}, 
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 3, 'color': 'verde'}, 
        {'id_ficha': 4, 'pos_x': 4, 'pos_y': 3, 'color': 'amarillo'}, 
        {'id_ficha': 5, 'pos_x': 1, 'pos_y': 1, 'color': 'azul'}, 
        {'id_ficha': 6, 'pos_x': 2, 'pos_y': 1, 'color': 'azul'}, 
        {'id_ficha': 7, 'pos_x': 3, 'pos_y': 1, 'color': 'azul'}, 
        {'id_ficha': 8, 'pos_x': 4, 'pos_y': 1, 'color': 'azul'}]
    helped_movimientos_poisibles_response = [
        {'id_ficha': 4, 'pos_x': 4, 'pos_y': 3, 'color': 'amarillo'},
        {'id_ficha': 3, 'pos_x': 2, 'pos_y': 3, 'color': 'verde'},
        {'id_ficha': 1, 'pos_x': 3, 'pos_y': 4, 'color': 'azul'},
        {'id_ficha': 2, 'pos_x': 3, 'pos_y': 2, 'color': 'rojo'}
    ]
    
    assert response.json() == expected_movimientos_posibles_response , "La respuesta en movimientos posibles no es la esperada" 
    assert response.json() != helped_movimientos_poisibles_response , "Se obtuvo ayuda en movimientos posibles en partida dificil"

    response = test_client.get(f"/game/{partida.id}/carta_figura/cartas_restantes")
    assert response.status_code == 200 , "Error al obtener cartas restantes"
    assert response.json() == [{'cantidad': 0, 'jugador': 'jugador1'}, {'cantidad': 0, 'jugador': 'jugdaor2'}] , "Se obtuvo ayuda en cartas restantes en partida dificil"