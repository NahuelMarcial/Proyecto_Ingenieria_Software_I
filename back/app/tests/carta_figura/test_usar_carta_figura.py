from app.home.models import Partida
from app.game.fichas.models import Ficha
from app.game.carta_figura.models import Carta_Figura
from app.game.carta_movimiento.models import movimientos, Carta_Movimiento
from app.game.carta_movimiento.carta_movimiento_repository import create_movimientos_db


def check_movimientos_vacios(db, partida_id):
    partida = db.query(Partida).filter(Partida.id == partida_id).first()
    #verificar que se vacian los movimientos
    movimientos_db = db.query(movimientos).filter(movimientos.id_partida == partida.id, movimientos.id_mov == 1).first()
    db.refresh(movimientos_db)
    assert movimientos_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 1"
    assert movimientos_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 1"
    assert movimientos_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 1"
    movimientos2_db = db.query(movimientos).filter(movimientos.id_partida == partida.id, movimientos.id_mov == 2).first()
    db.refresh(movimientos2_db)
    assert movimientos2_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 2"
    assert movimientos2_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 2"
    assert movimientos2_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 2"
    movimientos3_db = db.query(movimientos).filter(movimientos.id_partida == partida.id, movimientos.id_mov == 3).first()
    db.refresh(movimientos3_db)
    assert movimientos3_db.id_carta_mov == 0, "Error al vaciar el id_carta_mov 3"
    assert movimientos3_db.id_ficha1 == 0, "Error al vaciar el id_ficha1 3"
    assert movimientos3_db.id_ficha2 == 0, "Error al vaciar el id_ficha2 3"

def test_usar_carta_fige1_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    # Norte
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fige2(test_client, init_db):
    partida = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=1, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fige3_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=6, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=7, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=8, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=3, nombre="fige3", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"
    
def test_usar_carta_fige4_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=4, nombre="fige4", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fige5_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=0, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=5, nombre="fige5", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fige6_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=6, nombre="fige6", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fige7_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    carta = Carta_Figura(id_carta=7, nombre="fige7", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig1_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    # Definir las fichas en la posición que forman la figura fig1_n
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig2_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=0, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=2, nombre="fig2", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig3_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=3, nombre="fig3", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig4_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=4, nombre="fig4", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig5_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=6, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=5, nombre="fig5", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig6_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=6, nombre="fig6", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig7_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=7, nombre="fig7", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig8_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=8, nombre="fig8", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig9_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=9, nombre="fig9", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig10_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=10, nombre="fig10", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig11_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=11, nombre="fig11", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig12_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=12, nombre="fig12", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig13_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=6, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=13, nombre="fig13", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig14_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=14, nombre="fig14", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig15_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=15, nombre="fig15", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig16_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=16, nombre="fig16", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig17(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=17, nombre="fig17", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_fig18_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta = Carta_Figura(id_carta=18, nombre="fig18", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "rojo", "El color bloqueado no se actualizo"

    db.refresh(carta)
    assert carta.descartada == True, "La carta no se descarto"
    assert carta.mostrar == False, "La carta no se oculto"

def test_usar_carta_no_fig(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")

    db.add(ficha1)
    db.commit()

    carta = Carta_Figura(id_carta=19, nombre="fig19", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha1.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400, "Error al usar carta de figura"

    response_json = response.json()
    assert response_json == {"detail": "La ficha no pertenece a la figura de la carta"}

def test_formar_fig_con_mov_valido(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    # fige4
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=5, pos_y=5, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=6, pos_y=6, color="azul")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=5, pos_y=6, color="azul")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=6, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=6, color="azul")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    carta_fig = Carta_Figura(id_carta=5, nombre="fige4", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta_fig)
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)

    data_json = {
    "id_carta": carta_movimiento.id_carta,
    "id_jugador": "Jugador1",
    "id_ficha1": ficha4.id_ficha,
    "id_ficha2": ficha5.id_ficha}

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al buscar figuras formadas"
    response_json = response.json()
    assert response_json == [], "Se encontro figura formada (no deberia)" 

    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200, "Error al usar carta de movimiento"

    db.refresh(ficha4)
    assert ficha4.pos_x == 3, "La ficha no se movio"
    assert ficha4.pos_y == 6, "La ficha no se movio"

    db.refresh(ficha5)
    assert ficha5.pos_x == 4, "La ficha no se movio"
    assert ficha5.pos_y == 6, "La ficha no se movio"

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al buscar figuras formadas"
    response_json = response.json()
    assert response_json != [], "No se encontro figura formada"

    data_json = {
    "id_carta": carta_fig.id_carta,
    "id_ficha": ficha5.id_ficha,
    "id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "azul", "El color bloqueado no se actualizo"

    db.refresh(carta_fig)
    assert carta_fig.descartada == True, "La carta no se descarto"
    assert carta_fig.mostrar == False, "La carta no se oculto"

    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == False, "No se revertio el gastada de la carta de movimiento"
    assert carta_movimiento.id_player == "", "No se borro el id_player de la carta de movimiento"

    db.refresh(ficha4)
    assert ficha4.pos_x == 3, "La ficha se movio, y debia quedarse"
    assert ficha4.pos_y == 6, "La ficha se movio, y debia quedarse"

    db.refresh(ficha5)
    assert ficha5.pos_x == 4, "La ficha se movio, y debia quedarse"
    assert ficha5.pos_y == 6, "La ficha se movio, y debia quedarse"

    check_movimientos_vacios(db, partida.id)

def test_formar_fig_con_mov_invalido(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    # fige4
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=5, pos_y=5, color="azul")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=6, pos_y=6, color="azul")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=5, pos_y=6, color="azul")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=6, color="azul")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    ficha6 = Ficha(id_ficha=6, id_partida=partida.id, pos_x=1, pos_y=2, color="verde")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5, ficha6])
    db.commit()

    carta_fig = Carta_Figura(id_carta=5, nombre="fige4", color="azul", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta_fig)
    db.commit()

    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)

    data_json = {
    "id_carta": carta_movimiento.id_carta,
    "id_jugador": "Jugador1",
    "id_ficha1": ficha5.id_ficha,
    "id_ficha2": ficha6.id_ficha}

    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200, "Error al usar carta de movimiento"

    db.refresh(ficha5)
    assert ficha5.pos_x == 1, "La ficha no se movio"
    assert ficha5.pos_y == 2, "La ficha no se movio"

    db.refresh(ficha6)
    assert ficha6.pos_x == 1, "La ficha no se movio"
    assert ficha6.pos_y == 1, "La ficha no se movio"

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al buscar figuras formadas"
    response_json = response.json()
    assert response_json != [], "No se encontro figura formada"

    data_json = {
    "id_carta": carta_fig.id_carta,
    "id_ficha": ficha4.id_ficha,
    "id_player": "Jugador1"}
    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 200, "Error al usar carta de figura"

    db.refresh(partida)
    assert partida.color_bloqueado == "azul", "El color bloqueado no se actualizo"

    db.refresh(carta_fig)
    assert carta_fig.descartada == True, "La carta no se descarto"
    assert carta_fig.mostrar == False, "La carta no se oculto"

    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == False, "No se revertio el gastada de la carta de movimiento"
    assert carta_movimiento.id_player == "Jugador1", "No se mantuvo el id_player de la carta de movimiento"

    db.refresh(ficha5)
    assert ficha5.pos_x == 1, "La ficha se mantuvo y debia volver"
    assert ficha5.pos_y == 1, "La ficha se mantuvo y debia volver"

    db.refresh(ficha6)
    assert ficha6.pos_x == 1, "La ficha se mantuvo y debia volver"
    assert ficha6.pos_y == 2, "La ficha se mantuvo y debia volver"

    check_movimientos_vacios(db, partida.id)

def test_usar_carta_figuras_no_iniciada(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=False, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

def test_usar_carta_figuras_no_existe_partida(test_client, init_db):
    response = test_client.get(f"/game/999999999/fichas/buscar_figuras_formadas")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_usar_carta_figuras_no_fichas(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": 1,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay fichas asignadas a esta partida"}

def test_usar_carta_no_cartas_figuras(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()

    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    data_json = {
    "id_carta": 1,
    "id_ficha": 1,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay cartas asignadas a la partida"}
    
def test_jugador_no_pertenece(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador2", jugador2='Jugador1', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha.id_ficha,
    "id_player": "Jugador4"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

def test_jugador_sin_cartas(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador2", jugador2='Jugador1', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha.id_ficha,
    "id_player": "Jugador2"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no tiene cartas para jugar"}

def test_carta_no_pertenece(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador2", jugador2='Jugador1', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fig2", color="blanca", id_partida=partida.id, id_player="Jugador2", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha.id_ficha,
    "id_player": "Jugador2"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "La carta no pertenece al jugador"}

def test_no_turno(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador2", jugador2='Jugador1', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fig2", color="blanca", id_partida=partida.id, id_player="Jugador2", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha.id_ficha,
    "id_player": "Jugador1"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "No es el turno del jugador"}

def test_jugador_sin_cartas(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador2", jugador2='Jugador1', max_jugadores=4, turno = 1)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    db.add(ficha)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fig1", color="blanca", id_partida=partida.id, id_player="Jugador2", mostrar=True, descartada=True)
    db.add(carta)
    db.commit()

    data_json = {
    "id_carta": carta.id_carta,
    "id_ficha": ficha.id_ficha,
    "id_player": "Jugador2"}

    response = test_client.patch(f"/game/{partida.id}/carta_figura/jugar_carta", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "La carta ya fue jugada"}