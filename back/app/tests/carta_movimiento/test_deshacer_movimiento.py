from app.game.carta_movimiento.models import Carta_Movimiento,movimientos 
from app.game.fichas.models import Ficha
from app.home.models import Partida
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.carta_movimiento.logic as logic

#test deshacer 1 movimiento
def test_deshacer_1_movimiento(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_1_mov = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida_1_mov)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_1_mov.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=24, id_partida=partida_1_mov.id, pos_x=1, pos_y=2, color="rojo")
    db.add_all([ficha1, ficha2])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_1_mov.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add(carta_movimiento)
    db.commit()

    carta_movimiento_repository.create_movimientos_db(db, partida_1_mov.id)
    # Realizar un movimiento
    data = {"id_carta": 1, "id_jugador": "Jugador1", "id_ficha1": ficha1.id_ficha, "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida_1_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta de movimiento"
    
    # Verificar que el movimiento se ha registrado
    
    movimiento_db = db.query(movimientos).filter(movimientos.id_partida == partida_1_mov.id, movimientos.id_carta_mov == 1).first()
    assert movimiento_db is not None, "El movimiento no se registró en la base de datos"
    assert movimiento_db.id_ficha1 == ficha1.id_ficha, "La ficha 1 no coincide en el movimiento registrado"
    assert movimiento_db.id_ficha2 == ficha2.id_ficha, "La ficha 2 no coincide en el movimiento registrado"
    assert movimiento_db.id_carta_mov == 1, "La carta no coincide en el movimiento registrado"

    # Verificar que la carta se ha descartado
    carta_movimiento_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_1_mov.id, Carta_Movimiento.id_carta == 1).first()
    assert carta_movimiento_db.gastada == True, f"Error la carta no se gasto"

    # Verificar que las posiciones de las fichas se han cambiado
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 2, f"Error al cambiar las posiciones de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al cambiar las posiciones de las fichas"

    # Deshacer el movimiento
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida_1_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la llamada al endpoint deshacer movimiento"
    
    # Verificar que las posiciones de las fichas se han revertido
    db.refresh(ficha1)
    db.refresh(ficha2)  
    assert ficha1.pos_x == 1 and ficha1.pos_y == 1, f"Error al volver las posiciones de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 2, f"Error al volver las posiciones de las fichas"

    # Verificar que la carta ya no está descartada
    db.refresh(carta_movimiento_db)
    assert carta_movimiento_db.gastada == False, "Error la carta no se deshizo"
    assert carta_movimiento_db.id_player == "Jugador1", f"La carta no pertenece al jugador"
    assert carta_movimiento_db.id_partida == partida_1_mov.id, f"La carta no pertenece a la partida"
    assert carta_movimiento_db.id_carta == 1, f"La carta no es la esperada"

    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_1_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_1_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_1_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


#test deshacer 2 movimientos
def test_deshacer_2_movimientos(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_2_mov = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida_2_mov)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_2_mov.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=24, id_partida=partida_2_mov.id, pos_x=1, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=2, id_partida=partida_2_mov.id, pos_x=2, pos_y=2, color="verde")
    db.add_all([ficha1, ficha2, ficha3])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_2_mov.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento2 = Carta_Movimiento(id_partida=partida_2_mov.id, id_carta=2, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add_all([carta_movimiento, carta_movimiento2])
    db.commit()

    carta_movimiento_repository.create_movimientos_db(db, partida_2_mov.id)
    # Realizar movimiento 1
    data = {"id_carta": 1, "id_jugador": "Jugador1", "id_ficha1": ficha1.id_ficha, "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida_2_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 1 de movimiento"
    
    # Verificar que el movimiento 1 se ha registrado
    movimiento_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_carta_mov == 1).first()
    assert movimiento_db is not None, "El movimiento 1 no se registró en la base de datos"
    assert movimiento_db.id_ficha1 == ficha1.id_ficha, "La ficha 1 no coincide en el movimiento 1 registrado"
    assert movimiento_db.id_ficha2 == ficha2.id_ficha, "La ficha 2 no coincide en el movimiento 1 registrado"

    # Verificar que la carta 1 se ha descartado
    carta_movimiento_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_2_mov.id, Carta_Movimiento.id_carta == 1).first()
    assert carta_movimiento_db.gastada == True, f"Error la carta 1 no se gasto"

    # Verificar que las posiciones 1 de las fichas se han cambiado
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 2, f"Error al cambiar las primeras posiciones de las ficha1"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al cambiar las primeras posiciones de las ficha2"

    # Realizar movimiento 2
    data = {"id_carta": 2, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha3.id_ficha}
    response = test_client.patch(f"/game/{partida_2_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 2 de movimiento"

    # Verificar que el movimiento 2 se ha registrado
    movimiento_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_carta_mov == 2).first()
    assert movimiento_db is not None, "El movimiento 2 no se registró en la base de datos"
    assert movimiento_db.id_ficha1 == ficha2.id_ficha, "La ficha 2 no coincide en el movimiento 2 registrado"
    assert movimiento_db.id_ficha2 == ficha3.id_ficha, "La ficha 3 no coincide en el movimiento 2 registrado"

    # Verificar que la carta 2 se ha descartado
    carta_movimiento2_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_2_mov.id, Carta_Movimiento.id_carta == 2).first()
    assert carta_movimiento2_db.gastada == True, f"Error la carta 2 no se gasto"

    # Verificar que las posiciones 2 de las fichas se han cambiado
    db.refresh(ficha2)
    db.refresh(ficha3)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 2, f"Error al cambiar las segundas posiciones de las ficha2"
    assert ficha3.pos_x == 1 and ficha3.pos_y == 1, f"Error al cambiar las segundas posiciones de las ficha3"

    # Deshacer el movimiento 2
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida_2_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la primera llamada al endpoint deshacer movimiento"

    # Verificar que las posiciones de las fichas se han revertido
    db.refresh(ficha2)
    db.refresh(ficha3) 
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al volver las posiciones (carta2) de las fichas" 
    assert ficha3.pos_x == 2 and ficha3.pos_y == 2, f"Error al volver las posiciones (carta2) de las fichas"

    db.refresh(carta_movimiento2_db)
    assert carta_movimiento2_db.gastada == False, "Error la carta2 no se deshizo"
    assert carta_movimiento2_db.id_player == "Jugador1", f"La carta2 no pertenece al jugador"
    assert carta_movimiento2_db.id_partida == partida_2_mov.id, f"La carta2 no pertenece a la partida"
    assert carta_movimiento2_db.id_carta == 2, f"La carta2 no es la esperada"


    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == carta_movimiento.id_carta, "Error no deberia estar vacio el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == ficha1.id_ficha, "Error no deberia estar vacio el id_ficha1 1"
    assert movimientos_db.id_ficha2 == ficha2.id_ficha, "Error no deberia estar vacio el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"

    # Deshacer el movimiento 1
    response = test_client.patch(f"/game/{partida_2_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la segunda llamada al endpoint deshacer movimiento"

    # Verificar que las posiciones de las fichas se han revertido
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 1, f"Error al volver las posiciones (carta1) de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 2, f"Error al volver las posiciones (carta1) de las fichas"

    db.refresh(carta_movimiento_db)
    assert carta_movimiento_db.gastada == False, "Error la carta1 no se deshizo"
    assert carta_movimiento_db.id_player == "Jugador1", f"La carta1 no pertenece al jugador"
    assert carta_movimiento_db.id_partida == partida_2_mov.id, f"La carta1 no pertenece a la partida"
    assert carta_movimiento_db.id_carta == 1, f"La carta1 no es la esperada"

    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_2_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


#test deshacer 3 movimientos
def test_deshacer_3_movimientos(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_3_mov = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida_3_mov)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_3_mov.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida_3_mov.id, pos_x=1, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida_3_mov.id, pos_x=2, pos_y=2, color="verde")
    ficha4 = Ficha(id_ficha=4, id_partida=partida_3_mov.id, pos_x=2, pos_y=1, color="amarillo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_3_mov.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento2 = Carta_Movimiento(id_partida=partida_3_mov.id, id_carta=2, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento3 = Carta_Movimiento(id_partida=partida_3_mov.id, id_carta=3, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add_all([carta_movimiento, carta_movimiento2, carta_movimiento3])
    db.commit()

    carta_movimiento_repository.create_movimientos_db(db, partida_3_mov.id)
    # Realizar movimiento 1
    data = {"id_carta": 1, "id_jugador": "Jugador1", "id_ficha1": ficha1.id_ficha, "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 1 de movimiento"
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 2, f"Error al cambiar las primeras posiciones de las ficha1"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al cambiar las primeras posiciones de las ficha2"
    carta_movimiento1_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_3_mov.id, Carta_Movimiento.id_carta == 1).first()
    assert carta_movimiento1_db.gastada == True, f"Error la carta 1 no se gasto"

    # Realizar movimiento 2
    data = {"id_carta": 2, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha3.id_ficha}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 2 de movimiento"
    db.refresh(ficha2)
    db.refresh(ficha3)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 2, f"Error al cambiar las segundas posiciones de las ficha2"
    assert ficha3.pos_x == 1 and ficha3.pos_y == 1, f"Error al cambiar las segundas posiciones de las ficha3"
    carta_movimiento2_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_3_mov.id, Carta_Movimiento.id_carta == 2).first()
    assert carta_movimiento2_db.gastada == True, f"Error la carta 2 no se gasto"

    # Realizar movimiento 3
    data = {"id_carta": 3, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha4.id_ficha}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 3 de movimiento"
    db.refresh(ficha2)
    db.refresh(ficha4)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 1, f"Error al cambiar las terceras posiciones de las ficha2"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 2, f"Error al cambiar las terceras posiciones de las ficha4"

    carta_movimiento3_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_3_mov.id, Carta_Movimiento.id_carta == 3).first()
    assert carta_movimiento3_db.gastada == True, f"Error la carta 3 no se gasto"

    # Deshacer el movimiento 3
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la primera llamada al endpoint deshacer movimiento"
    db.refresh(ficha2)
    db.refresh(ficha4)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 2, f"Error al volver las posiciones (carta 3) de las fichas"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 1, f"Error al volver las posiciones (carta 3) de las fichas"
    db.refresh(carta_movimiento3_db)
    assert carta_movimiento3_db.gastada == False, "Error la carta 3 no se deshizo"
    assert carta_movimiento3_db.id_player == "Jugador1", f"La carta 3 no pertenece al jugador"
    assert carta_movimiento3_db.id_partida == partida_3_mov.id, f"La carta 3 no pertenece a la partida"
    assert carta_movimiento3_db.id_carta == 3, f"La carta 3 no es la esperada"

    #verificar que se vacian los movimientos 3
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == carta_movimiento.id_carta, "Error no deberia estar vacio el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == ficha1.id_ficha, "Error no deberia estar vacio el id_ficha1 1"
    assert movimientos_db.id_ficha2 == ficha2.id_ficha, "Error no deberia estar vacio el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == carta_movimiento2.id_carta, "Error no deberia estar vacio el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == ficha2.id_ficha, "Error no deberia estar vacio el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == ficha3.id_ficha, "Error no deberia estar vacio el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


    # Deshacer el movimiento 2
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la segunda llamada al endpoint deshacer movimiento"
    db.refresh(ficha2)
    db.refresh(ficha3)
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al volver las posiciones (carta 2) de las fichas"
    assert ficha3.pos_x == 2 and ficha3.pos_y == 2, f"Error al volver las posiciones (carta 2) de las fichas"
    db.refresh(carta_movimiento2_db)
    assert carta_movimiento2_db.gastada == False, "Error la carta 2 no se deshizo"
    assert carta_movimiento2_db.id_player == "Jugador1", f"La carta 2 no pertenece al jugador"
    assert carta_movimiento2_db.id_partida == partida_3_mov.id, f"La carta 2 no pertenece a la partida"
    assert carta_movimiento2_db.id_carta == 2, f"La carta 2 no es la esperada"

    #verificar que se vacian los movimientos 2
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == carta_movimiento.id_carta, "Error no deberia estar vacio el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == ficha1.id_ficha, "Error no deberia estar vacio el id_ficha1 1"
    assert movimientos_db.id_ficha2 == ficha2.id_ficha, "Error no deberia estar vacio el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"

    # Deshacer el movimiento 1
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la tercera llamada al endpoint deshacer movimiento"
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 1, f"Error al volver las posiciones (carta 1) de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 2, f"Error al volver las posiciones (carta 1) de las fichas"
    db.refresh(carta_movimiento1_db)
    assert carta_movimiento1_db.gastada == False, "Error la carta 1 no se deshizo"
    assert carta_movimiento1_db.id_player == "Jugador1", f"La carta 1 no pertenece al jugador"
    assert carta_movimiento1_db.id_partida == partida_3_mov.id, f"La carta 1 no pertenece a la partida"
    assert carta_movimiento1_db.id_carta == 1, f"La carta 1 no es la esperada"

    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


#test deshacer mov 3 alternos
def test_deshacer_3_movimientos_alterno(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_3_mov = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida_3_mov)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_3_mov.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida_3_mov.id, pos_x=1, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida_3_mov.id, pos_x=2, pos_y=2, color="verde")
    ficha4 = Ficha(id_ficha=4, id_partida=partida_3_mov.id, pos_x=2, pos_y=1, color="amarillo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_3_mov.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento2 = Carta_Movimiento(id_partida=partida_3_mov.id, id_carta=2, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento3 = Carta_Movimiento(id_partida=partida_3_mov.id, id_carta=3, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add_all([carta_movimiento, carta_movimiento2, carta_movimiento3])
    db.commit()

    carta_movimiento_repository.create_movimientos_db(db, partida_3_mov.id)
    # Realizar movimiento 1
    data = {"id_carta": 1, "id_jugador": "Jugador1", "id_ficha1": ficha1.id_ficha, "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 1 de movimiento"
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 2, f"Error al cambiar las primeras posiciones de las ficha1"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al cambiar las primeras posiciones de las ficha2"
    carta_movimiento1_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_3_mov.id, Carta_Movimiento.id_carta == 1).first()
    assert carta_movimiento1_db.gastada == True, f"Error la carta 1 no se gasto"

    # Realizar movimiento 2
    data = {"id_carta": 2, "id_jugador": "Jugador1", "id_ficha1": ficha3.id_ficha, "id_ficha2": ficha4.id_ficha}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 2 de movimiento"
    db.refresh(ficha3)
    db.refresh(ficha4)
    assert ficha3.pos_x == 2 and ficha3.pos_y == 1, f"Error al cambiar las segundas posiciones de las ficha2"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 2, f"Error al cambiar las segundas posiciones de las ficha3"
    carta_movimiento2_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_3_mov.id, Carta_Movimiento.id_carta == 2).first()
    assert carta_movimiento2_db.gastada == True, f"Error la carta 2 no se gasto"

    # Realizar movimiento 3
    data = {"id_carta": 3, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha4.id_ficha}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 3 de movimiento"
    db.refresh(ficha2)
    db.refresh(ficha4)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 2, f"Error al cambiar las terceras posiciones de las ficha2"
    assert ficha4.pos_x == 1 and ficha4.pos_y == 1, f"Error al cambiar las terceras posiciones de las ficha4"

    carta_movimiento3_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_3_mov.id, Carta_Movimiento.id_carta == 3).first()
    assert carta_movimiento3_db.gastada == True, f"Error la carta 3 no se gasto"

    # Deshacer el movimiento 3
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la primera llamada al endpoint deshacer movimiento"
    db.refresh(ficha2)
    db.refresh(ficha4)
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al volver las posiciones (carta 3) de las fichas"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 2, f"Error al volver las posiciones (carta 3) de las fichas"
    db.refresh(carta_movimiento3_db)
    assert carta_movimiento3_db.gastada == False, "Error la carta 3 no se deshizo"
    assert carta_movimiento3_db.id_player == "Jugador1", f"La carta 3 no pertenece al jugador"
    assert carta_movimiento3_db.id_partida == partida_3_mov.id, f"La carta 3 no pertenece a la partida"
    assert carta_movimiento3_db.id_carta == 3, f"La carta 3 no es la esperada"

    #verificar que se vacian los movimientos 3
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == carta_movimiento.id_carta, "Error no deberia estar vacio el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == ficha1.id_ficha, "Error no deberia estar vacio el id_ficha1 1"
    assert movimientos_db.id_ficha2 == ficha2.id_ficha, "Error no deberia estar vacio el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == carta_movimiento2.id_carta, "Error no deberia estar vacio el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == ficha3.id_ficha, "Error no deberia estar vacio el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == ficha4.id_ficha, "Error no deberia estar vacio el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


    # Deshacer el movimiento 2
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la segunda llamada al endpoint deshacer movimiento"
    db.refresh(ficha3)
    db.refresh(ficha4)
    assert ficha3.pos_x == 2 and ficha3.pos_y == 2, f"Error al volver las posiciones (carta 2) de las fichas"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 1, f"Error al volver las posiciones (carta 2) de las fichas"
    db.refresh(carta_movimiento2_db)
    assert carta_movimiento2_db.gastada == False, "Error la carta 2 no se deshizo"
    assert carta_movimiento2_db.id_player == "Jugador1", f"La carta 2 no pertenece al jugador"
    assert carta_movimiento2_db.id_partida == partida_3_mov.id, f"La carta 2 no pertenece a la partida"
    assert carta_movimiento2_db.id_carta == 2, f"La carta 2 no es la esperada"

    #verificar que se vacian los movimientos 2
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == carta_movimiento.id_carta, "Error no deberia estar vacio el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == ficha1.id_ficha, "Error no deberia estar vacio el id_ficha1 1"
    assert movimientos_db.id_ficha2 == ficha2.id_ficha, "Error no deberia estar vacio el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


    # Deshacer el movimiento 1
    response = test_client.patch(f"/game/{partida_3_mov.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 200, f"Error en la tercera llamada al endpoint deshacer movimiento"
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 1, f"Error al volver las posiciones (carta 1) de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 2, f"Error al volver las posiciones (carta 1) de las fichas"
    db.refresh(carta_movimiento1_db)
    assert carta_movimiento1_db.gastada == False, "Error la carta 1 no se deshizo"
    assert carta_movimiento1_db.id_player == "Jugador1", f"La carta 1 no pertenece al jugador"
    assert carta_movimiento1_db.id_partida == partida_3_mov.id, f"La carta 1 no pertenece a la partida"
    assert carta_movimiento1_db.id_carta == 1, f"La carta 1 no es la esperada"

    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_3_mov.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"

#tests de validaciones de deshacer movimientos

#test partida no iniciada
def test_deshacer_movimiento_partida_no_iniciada(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_no_iniciada = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=False, turno=1)
    db.add(partida_no_iniciada)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_no_iniciada.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida_no_iniciada.id, pos_x=1, pos_y=2, color="rojo")
    db.add_all([ficha1, ficha2])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_no_iniciada.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add(carta_movimiento)
    db.commit()
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida_no_iniciada.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 400, f"Error paso la validacion en una partida no iniciada"
    assert response.json() == {"detail": "La partida no ha iniciado"}, f'Error en el mensaje de error, el mensaje esperado es "La partida no ha iniciado"'

#test jugador no pertenece a la partida
def test_deshacer_movimiento_jugador_no_pertenece(test_client, init_db):
    db = init_db

    # Crear una partida
    partida = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    db.add_all([ficha1, ficha2])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add(carta_movimiento)
    db.commit()
    jugador_id = {"id_player": "Jugador3"}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 400, f"Error paso la validacion con un jugador que no pertenece a la partida"
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}, f'Error en el mensaje de error, el mensaje esperado es "El jugador no pertenece a la partida"'

#test es el turno del jugador
def test_deshacer_movimiento_no_turno(test_client, init_db):
    db = init_db

    # Crear una partida
    partida = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=2)
    db.add(partida)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    db.add_all([ficha1, ficha2])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador2", gastada=False)
    db.add(carta_movimiento)
    db.commit()
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 400, f"Error paso la validacion con un turno que no pertenece al jugador"
    assert response.json() == {"detail": "No es el turno del jugador"}, f'Error en el mensaje de error, el mensaje esperado es "No es el turno del jugador"'

#test no hay movimientos por deshacer
def test_deshacer_movimiento_no_movimientos(test_client, init_db):
    db = init_db

    # Crear una partida
    partida = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    db.add_all([ficha1, ficha2])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador2", gastada=False)
    db.add(carta_movimiento)
    db.commit()
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 400, f"Error paso la validacion cuando no habia movimiento por deshacer"
    assert response.json() == {"detail": "No hay movimientos para deshacer"}, f'Error en el mensaje de error, el mensaje esperado es "No hay movimientos para deshacer"'

#test partida no existe
def test_deshacer_movimiento_partida_no_existe(test_client, init_db):
    db = init_db
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/999999999/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 404, f"Error paso la validacion cuando no se encontro la partida"
    assert response.json() == {"detail": "Partida no encontrada"}, f'Error en el mensaje de error, el mensaje esperado es "Partida no encontrada"'

#test cartas no asignadas
def test_deshacer_movimiento_cartas_no_asignadas(test_client, init_db):
    db = init_db

    # Crear una partida
    partida = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    db.add_all([ficha1, ficha2])
    db.commit()

    # Crear carta de movimiento
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 400, f"Error paso la validacion cuando no habia cartas asignadas a la partida"
    assert response.json() == {"detail": "La partida no tiene cartas asignadas"}, f'Error en el mensaje de error, el mensaje esperado es "La partida no tiene cartas asignadas"'

#test fichas no asignadas
def test_deshacer_movimiento_fichas_no_asignadas(test_client, init_db):
    db = init_db

    # Crear una partida
    partida = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida)
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador2", gastada=False)
    db.add(carta_movimiento)
    db.commit()
    jugador_id = {"id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/deshacer_movimiento", json=jugador_id)
    assert response.status_code == 400, f"Error paso la validacion cuando no habia fichas asignadas a la partida"
    assert response.json() == {"detail": "No hay fichas asignadas a esta partida"}, f'Error en el mensaje de error, el mensaje esperado es "No hay fichas asignadas a esta partida"'


#tests para el metodo deshacer_todos_movimientos

#test deshacer todos los movimientos 2
def test_deshacer_todos_movimientos_2(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_todos_mov2 = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida_todos_mov2)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_todos_mov2.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=24, id_partida=partida_todos_mov2.id, pos_x=1, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=2, id_partida=partida_todos_mov2.id, pos_x=2, pos_y=2, color="verde")
    db.add_all([ficha1, ficha2, ficha3])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_todos_mov2.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento2 = Carta_Movimiento(id_partida=partida_todos_mov2.id, id_carta=2, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add_all([carta_movimiento, carta_movimiento2])
    db.commit()

    carta_movimiento_repository.create_movimientos_db(db, partida_todos_mov2.id)
    # Realizar movimiento 1
    data = {"id_carta": 1, "id_jugador": "Jugador1", "id_ficha1": ficha1.id_ficha, "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida_todos_mov2.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 1 de movimiento"
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 2, f"Error al cambiar las primeras posiciones de las ficha1"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al cambiar las primeras posiciones de las ficha2"
    carta_movimiento1_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_todos_mov2.id, Carta_Movimiento.id_carta == 1).first()
    assert carta_movimiento1_db.gastada == True, f"Error la carta 1 no se gasto"

    # Realizar movimiento 2
    data = {"id_carta": 2, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha3.id_ficha}
    response = test_client.patch(f"/game/{partida_todos_mov2.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 2 de movimiento"
    db.refresh(ficha2)
    db.refresh(ficha3)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 2, f"Error al cambiar las segundas posiciones de las ficha2"
    assert ficha3.pos_x == 1 and ficha3.pos_y == 1, f"Error al cambiar las segundas posiciones de las ficha3"
    carta_movimiento2_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_todos_mov2.id, Carta_Movimiento.id_carta == 2).first()
    assert carta_movimiento2_db.gastada == True, f"Error la carta 2 no se gasto"

    # Deshacer todos los movimientos
    logic.deshacer_todos_movimientos(db, partida_todos_mov2.id)
    db.refresh(ficha1)
    db.refresh(ficha2)
    db.refresh(ficha3)
    db.refresh(carta_movimiento1_db)
    db.refresh(carta_movimiento2_db)

    # Verificar que las posiciones de las fichas se han revertido correctamente
    assert ficha1.pos_x == 1 and ficha1.pos_y == 1, f"Error al volver las posiciones (carta 1) de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 2, f"Error al volver las posiciones (carta 1) de las fichas"
    assert ficha3.pos_x == 2 and ficha3.pos_y == 2, f"Error al volver las posiciones (carta 2) de las fichas"

    # Verificar que las cartas se han deshecho correctamente
    assert carta_movimiento1_db.gastada == False, "Error la carta 1 no se deshizo"
    assert carta_movimiento2_db.gastada == False, "Error la carta 2 no se deshizo"

    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_todos_mov2.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_todos_mov2.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_todos_mov2.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"


#test deshacer todos los movimientos 3
def test_deshacer_todos_movimientos_3(test_client, init_db):
    db = init_db

    # Crear una partida
    partida_todos_mov3 = Partida(nombre="Partida Valida", owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, iniciada=True, turno=1)
    db.add(partida_todos_mov3)
    db.commit()

    # Crear las fichas
    ficha1 = Ficha(id_ficha=1, id_partida=partida_todos_mov3.id, pos_x=1, pos_y=1, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida_todos_mov3.id, pos_x=1, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida_todos_mov3.id, pos_x=2, pos_y=2, color="verde")
    ficha4 = Ficha(id_ficha=4, id_partida=partida_todos_mov3.id, pos_x=2, pos_y=1, color="amarillo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Crear carta de movimiento
    carta_movimiento = Carta_Movimiento(id_partida=partida_todos_mov3.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento2 = Carta_Movimiento(id_partida=partida_todos_mov3.id, id_carta=2, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1", gastada=False)
    carta_movimiento3 = Carta_Movimiento(id_partida=partida_todos_mov3.id, id_carta=3, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1", gastada=False)
    db.add_all([carta_movimiento, carta_movimiento2, carta_movimiento3])
    db.commit()

    carta_movimiento_repository.create_movimientos_db(db, partida_todos_mov3.id)
    # Realizar movimiento 1
    data = {"id_carta": 1, "id_jugador": "Jugador1", "id_ficha1": ficha1.id_ficha, "id_ficha2": ficha2.id_ficha}
    response = test_client.patch(f"/game/{partida_todos_mov3.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 1 de movimiento"
    db.refresh(ficha1)
    db.refresh(ficha2)
    assert ficha1.pos_x == 1 and ficha1.pos_y == 2, f"Error al cambiar las primeras posiciones de las ficha1"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 1, f"Error al cambiar las primeras posiciones de las ficha2"
    carta_movimiento1_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_todos_mov3.id, Carta_Movimiento.id_carta == 1).first()
    assert carta_movimiento1_db.gastada == True, f"Error la carta 1 no se gasto"

    # Realizar movimiento 2
    data = {"id_carta": 2, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha3.id_ficha}
    response = test_client.patch(f"/game/{partida_todos_mov3.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 2 de movimiento"
    db.refresh(ficha2)
    db.refresh(ficha3)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 2, f"Error al cambiar las segundas posiciones de las ficha2"
    assert ficha3.pos_x == 1 and ficha3.pos_y == 1, f"Error al cambiar las segundas posiciones de las ficha3"
    carta_movimiento2_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_todos_mov3.id, Carta_Movimiento.id_carta == 2).first()
    assert carta_movimiento2_db.gastada == True, f"Error la carta 2 no se gasto"

    # Realizar movimiento 3
    data = {"id_carta": 3, "id_jugador": "Jugador1", "id_ficha1": ficha2.id_ficha, "id_ficha2": ficha4.id_ficha}
    response = test_client.patch(f"/game/{partida_todos_mov3.id}/carta_movimiento/usar_carta_movimiento", json=data)
    assert response.status_code == 200, f"Error al usar carta 3 de movimiento"
    db.refresh(ficha2)
    db.refresh(ficha4)
    assert ficha2.pos_x == 2 and ficha2.pos_y == 1, f"Error al cambiar las terceras posiciones de las ficha2"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 2, f"Error al cambiar las terceras posiciones de las ficha4"
    carta_movimiento3_db = db.query(Carta_Movimiento).filter(Carta_Movimiento.id_partida == partida_todos_mov3.id, Carta_Movimiento.id_carta == 3).first()
    assert carta_movimiento3_db.gastada == True, f"Error la carta 3 no se gasto"

    # Deshacer todos los movimientos
    logic.deshacer_todos_movimientos(db, partida_todos_mov3.id)
    db.refresh(ficha1)
    db.refresh(ficha2)
    db.refresh(ficha3)
    db.refresh(ficha4)
    db.refresh(carta_movimiento1_db)
    db.refresh(carta_movimiento2_db)
    db.refresh(carta_movimiento3_db)

    # Verificar que las posiciones de las fichas se han revertido correctamente
    assert ficha1.pos_x == 1 and ficha1.pos_y == 1, f"Error al volver las posiciones (carta 1) de las fichas"
    assert ficha2.pos_x == 1 and ficha2.pos_y == 2, f"Error al volver las posiciones (carta 1) de las fichas"
    assert ficha3.pos_x == 2 and ficha3.pos_y == 2, f"Error al volver las posiciones (carta 2) de las fichas"
    assert ficha4.pos_x == 2 and ficha4.pos_y == 1, f"Error al volver las posiciones (carta 3) de las fichas"

    # Verificar que las cartas se han deshecho correctamente
    assert carta_movimiento1_db.gastada == False, "Error la carta 1 no se deshizo"
    assert carta_movimiento2_db.gastada == False, "Error la carta 2 no se deshizo"
    assert carta_movimiento3_db.gastada == False, "Error la carta 3 no se deshizo"

    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida_todos_mov3.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida_todos_mov3.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida_todos_mov3.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"
