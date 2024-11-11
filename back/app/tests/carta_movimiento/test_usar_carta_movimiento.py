from app.home.models import Partida
from app.game.carta_movimiento.models import Carta_Movimiento
from app.game.fichas.models import Ficha
from app.game.carta_movimiento.carta_movimiento_repository import create_movimientos_db,get_movimientos_db



#Cruce linea contiguo


#casos exitosos
def test_usar_carta_movimiento_cruce_linea_contiguo_arriba(test_client, init_db):
   # Crear una partida válida con 1 jugador
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=3)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea contiguo arriba"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea contiguo arriba] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea contiguo arriba]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo arriba] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea contiguo arriba] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea contiguo arriba] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_contiguo_abajo(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=1)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea contiguo abajo"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea contiguo abajo] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea contiguo abajo]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo abajo] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea contiguo abajo] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea contiguo abajo] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea contiguo abajo] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_contiguo_derecha(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea contiguo derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea contiguo derehca] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea contiguo derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea contiguo derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea contiguo derecha] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea contiguo derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_contiguo_izquierda(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=1, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea contiguo izquierda"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea contiguo izquierda] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea contiguo izquierda]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo izquierda] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea contiguo izquierda] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea contiguo izquierda] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea contiguo izquierda] :No se marco carta como gastada"

#casos fallidos
def test_usar_carta_movimiento_cruce_linea_contiguo_diag(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=3)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 400 , "No se puede usar carta de movimiento cruce en linea contiguo diagonal"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_ficha1 == 0, "[Cruce en linea contiguo caso fallido]: se asigno ficha1 al movimiento cuando no deberia"
   assert movimientos[0].id_ficha2 == 0, "[Cruce en linea contiguo fallido] : se asigno ficha2 al movimiento cuando no deberia"
   


#Cruce linea con espacio

def test_usar_carta_movimiento_cruce_linea_con_espacio_arriba(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=4)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea con un espacio arriba"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio arriba] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio arriba]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio arriba] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio arriba] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio arriba] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio arriba] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_con_espacio_abajo(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=0)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea con un espacio abajo"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio abajo] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio abajo]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio abajo] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio abajo] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio abajo] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio abajo] :No se marco carta como gastada"


def test_usar_carta_movimiento_cruce_linea_con_espacio_derecha(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=4, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea con un espacio derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio derecha] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio derecha] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_con_espacio_izquierda(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=0, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea con un espacio izquierda"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio izquierda] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio izquierda]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio izquierda] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio izquierda] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio izquierda] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio izquierda] :No se marco carta como gastada"

#casos fallidos
def test_usar_carta_movimiento_cruce_linea_con_espacio_diag(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=3)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 400 , "No se puede usar carta de movimiento cruce en linea con un espacio diagonal"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_ficha1 == 0, "[Cruce en linea con espacio diagonal caso fallido]: se asigno ficha1 al movimiento y no deberia"
   assert movimientos[0].id_ficha2 == 0, "[Cruce en linea con espacio diagonal] : No se asigno ficha2 al movimiento"



#Cruce diagonal contiguo


def test_usar_carta_movimiento_cruce_diagonal_contiguo_arriba_der(test_client, init_db):
   # Crear una partida válida con 1 jugador
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=3)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal contiguo arriba derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce diagonal contiguo arriba derecha] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce diagonal contiguo arriba derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce diagonal contiguo arriba derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce diagonal contiguo arriba derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce diagonal contiguo arriba derecha] :No se asigno id de partida al movimiento"
def test_usar_carta_movimiento_cruce_diagonal_contiguo_arriba_izq(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=1, pos_y=3)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal contiguo arriba izquierda"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce diagonal contiguo arriba izquierda] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce diagonal contiguo arriba izquierda]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce diagonal contiguo arriba izquierda] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce diagonal contiguo arriba izquierda] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce diagonal contiguo arriba izquierda] :No se asigno id de partida al movimiento"

def test_usar_carta_movimiento_cruce_diagonal_contiguo_abajo_der(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=1)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal contiguo abajo derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce diagonal contiguo abajo derecha] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce diagonal contiguo abajo derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce diagonal contiguo abajo derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce diagonal contiguo abajo derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce diagonal contiguo abajo derecha] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce diagonal contiguo abajo derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_diagonal_contiguo_abajo_izq(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=1, pos_y=1)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal contiguo abajo izquierda"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce diagonal contiguo abajo izquierda] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce diagonal contiguo abajo izquierda]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce diagonal contiguo abajo izquierda] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce diagonal contiguo abajo izquierda] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce diagonal contiguo abajo izquierda] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)

#casos fallidos
def test_usar_carta_movimiento_cruce_diagonal_contiguo_diag(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 400 , "Se intenta cruce contiguo en diagonal"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_ficha1 == 0, "[Cruce diagonal contiguo caso fallido]: se asigno ficha1 al movimiento y no deberia"
   assert movimientos[0].id_ficha2 == 0, "[Cruce diagonal contiguo fallido] : se asigno ficha2 al movimiento y no deberia"


def test_usar_carta_movimiento_cruce_diagonal_contiguo_espacio(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=4, pos_y=4)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal contiguo", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 400 , "Se intenta crucecon espacio en cruce"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_ficha1 == 0, "[Cruce diagonal contiguo caso fallido]: se asigno ficha1 al movimiento y no deberia"
   assert movimientos[0].id_ficha2 == 0, "[Cruce diagonal contiguo fallido] : se asigno ficha2 al movimiento y no deberia"


#Cruce diagonal con espacio

def test_usar_carta_movimiento_cruce_diagonal_con_espacio_arriba_der(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=4, pos_y=4)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal con un espacio arriba derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio arriba derecha] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio arriba derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio arriba derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio arriba derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio arriba derecha] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio arriba derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_diagonal_con_espacio_arriba_izq(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=0, pos_y=4)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal con un espacio arriba izquierda"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio arriba izquierda] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio arriba izquierda]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio arriba izquierda] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio arriba izquierda] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio arriba izquierda] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio arriba izquierda] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_diagonal_con_espacio_abajo_der(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=4, pos_y=0)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal con un espacio abajo derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio abajo derecha] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio abajo derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio abajo derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio abajo derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio abajo derecha] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio abajo derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_diagonal_con_espacio_abajo_izq(test_client, init_db):
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=0, pos_y=0)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)

   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce diagonal con un espacio abajo izquierda"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea con espacio abajo izquierda] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea con espacio abajo izquierda]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea contiguo con espacio abajo izquierda] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea con espacio abajo izquierda] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea con espacio abajo izquierda] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea con espacio abajo izquierda] :No se marco carta como gastada"
#casos fallidos
def test_usar_carta_movimiento_cruce_diagonal_con_espacio_diag(test_client, init_db):
   # Crear una partida válida con 1 jugador
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=2, pos_y=2)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce diagonal con un espacio", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)
   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 400 , "Se intenta cruce diagonal con espacio en diagonal"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_ficha1 == 0, "[Cruce diagonal con espacio diagonal caso fallido]: se asigno ficha1 al movimiento y no deberia"
   assert movimientos[0].id_ficha2 == 0, "[Cruce diagonal con espacio diagonal caso faillodo] : se asigno ficha2 al movimiento y no deberia"

#Cruce en L derecha
#casos exitotosos
def test_usar_carta_movimiento_cruce_en_L_derecha_abajoL_derC(test_client, init_db):
   #arriba L hace referencia a arriba largo 
   #derC hace referencia a derecha corto
   #la idea es hacer un cruce en L hacia la derecha con la ficha de arriba largo 2 fichas de distntiancia y la de la derecha corto 1 ficha de distantica
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
   #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=4, pos_y=1)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)
   #endpoint con primera ficha arriba
   data_json = {
       "id_carta": carta_movimiento.id_carta,
       "id_jugador": "Jugador1",
       "id_ficha1": ficha_piv.id_ficha,
       "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L derecha arriba derecha"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L derecha arriba derecha] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L derecha arriba derecha]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L derecha arriba derecha] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en L derecha arriba derecha] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en L derecha arriba derecha] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en L derecha arriba derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_en_L_derecha_arribaC_derL(test_client, init_db):
    #arriba C hace referencia a arriba corto 
    #derL hace referencia a derecha largo
    #la idea es hacer un cruce en L hacia la derecha con la ficha de arriba corto 1 ficha de distntiancia y la de la derecha largo 2 fichas de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=5, pos_y=4)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L derecha arriba derecha"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L derecha arriba derecha] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L derecha arriba derecha]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L derecha arriba derecha] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L derecha arriba derecha] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L derecha arriba derecha] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L derecha arriba derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_en_L_derecha_arribaL_izqC(test_client, init_db):
    #arriba L hace referencia a arriba largo 
    #izqC hace referencia a izquierda corto
    #la idea es hacer un cruce en L hacia la derecha con la ficha de arriba largo 2 fichas de distntiancia y la de la izquierda corto 1 ficha de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=5)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L derecha arriba derecha"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L derecha arriba derecha] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L derecha arriba derecha]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L derecha arriba derecha] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L derecha arriba derecha] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L derecha arriba derecha] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L derecha arriba derecha] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_en_L_derecha_abajoC_izqL(test_client,init_db):
    #abajo C hace referencia a abajo corto 
    #izqL hace referencia a izquierda largo
    #la idea es hacer un cruce en L hacia la derecha con la ficha de abajo corto 1 ficha de distntiancia y la de la izquierda largo 2 fichas de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=1, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L derecha arriba derecha"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L derecha arriba derecha] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L derecha arriba derecha]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L derecha arriba derecha] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L derecha arriba derecha] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L derecha arriba derecha] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L derecha arriba derecha] :No se marco carta como gastada"

#casos fallidos
def test_usar_carta_movimiento_cruce_en_L_derecha_caso_no_valido(test_client,init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L derecha", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400 , "Se intenta cruce en L derecha con fichas en linea"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_ficha1 == 0, "[Cruce en L derecha caso fallido]: se asigno ficha1 al movimiento y no deberia"
    assert movimientos[0].id_ficha2 == 0, "[Cruce en L derecha caso faillodo] : se asigno ficha2 al movimiento y no deberia"

#Cruce en L izquierda
#casos exitotosos
def test_usar_carta_movimiento_cruce_en_L_izquierda_abajoL_izqC(test_client,init_db):
    #abajo L hace referencia a abajo largo 
    #izqC hace referencia a izquierda corto
    #la idea es hacer un cruce en L hacia la izquierda con la ficha de abajo largo 2 fichas de distntiancia y la de la izquierda corto 1 ficha de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=2, pos_y=1)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L izquierda abajo largo izquierda corto"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L izquierda abajo largo izquierda corto] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L izquierda abajo largo izquierda corto]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L izquierda abajo largo izquierda corto] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L izquierda abajo largo izquierda corto] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L izquierda abajo largo izquierda corto] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L izquierda abajo largo izquierda corto] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_en_L_izquierda_abajoC_derL(test_client,init_db):
    #abajo C hace referencia a abajo corto 
    #derL hace referencia a derecha largo
    #la idea es hacer un cruce en L hacia la izquierda con la ficha de abajo corto 1 ficha de distntiancia y la de la derecha largo 2 fichas de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=5, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L izquierda abajo corto derecha largo"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L izquierda abajo corto derecha largo] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L izquierda abajo corto derecha largo]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L izquierda abajo corto derecha largo] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L izquierda abajo corto derecha largo] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L izquierda abajo corto derecha largo] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L izquierda abajo corto derecha largo] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_en_L_izquierda_arribaL_derC(test_client,init_db):
    #arriba L hace referencia a arriba largo 
    #derC hace referencia a derecha corto
    #la idea es hacer un cruce en L hacia la izquierda con la ficha de arriba largo 2 fichas de distntiancia y la de la derecha corto 1 ficha de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=4, pos_y=5)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L izquierda arriba largo derecha corto"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L izquierda arriba largo derecha corto] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L izquierda arriba largo derecha corto]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L izquierda arriba largo derecha corto] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L izquierda arriba largo derecha corto] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L izquierda arriba largo derecha corto] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L izquierda arriba largo derecha corto] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_en_L_izquierda_arribaC_izqL(test_client,init_db):
    #arriba C hace referencia a arriba corto 
    #izqL hace referencia a izquierda largo
    #la idea es hacer un cruce en L hacia la izquierda con la ficha de arriba corto 1 ficha de distntiancia y la de la izquierda largo 2 fichas de distantica
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=1, pos_y=4)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en L izquierda arriba corto izquierda largo"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en L izquierda arriba corto izquierda largo] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en L izquierda arriba corto izquierda largo]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en L izquierda arriba corto izquierda largo] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en L izquierda arriba corto izquierda largo] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en L izquierda arriba corto izquierda largo] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en L izquierda arriba corto izquierda largo] :No se marco carta como gastada"

#caso fallido
def test_usar_carta_movimiento_cruce_en_L_izquierda_caso_no_valido(test_client,init_db):
    # Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en L izquierda", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    #endpoint con primera ficha arriba
    data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400 , "Se intenta cruce en L izquierda con fichas en linea"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_ficha1 == 0, "[Cruce en L izquierda caso fallido]: se asigno ficha1 al movimiento y no deberia"
    assert movimientos[0].id_ficha2 == 0, "[Cruce en L izquierda caso faillodo] : se asigno ficha2 al movimiento y no deberia"

#Cruce en linea lateral
#casos exitotosos
def test_usar_carta_movimiento_cruce_liena_lateral_x6(test_client, init_db): 
   partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
   db = init_db
   db.add(partida)
   db.commit()
    #Crear fichas
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=6, pos_y=3)
   db.add_all([ficha1,ficha_piv])
   db.commit()
    #Crear carta de movimiento a testear
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1") 
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)
     #endpoint con primera ficha arriba
   data_json = {
         "id_carta": carta_movimiento.id_carta,
         "id_jugador": "Jugador1",
         "id_ficha1": ficha_piv.id_ficha,
         "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea lateral x6"
   movimientos = get_movimientos_db(db, partida.id)
   assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea lateral x6] :No se asigno carta al movimiento"
   assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea lateral x6]: No se asigno ficha1 al movimiento"
   assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea lateral x6] : No se asigno ficha2 al movimiento"
   assert movimientos[0].id_mov ==1, "[Cruce en linea lateral x6] :No se asigno id al movimiento"
   assert movimientos[0].id_partida == partida.id, "[Cruce en linea lateral x6] :No se asigno id de partida al movimiento"
   db.refresh(carta_movimiento)
   assert carta_movimiento.gastada == True, "[Cruce en linea lateral x6] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_liena_lateral_y6(test_client, init_db):
    #Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
     #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=6)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea lateral y6"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea lateral y6] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea lateral y6]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea lateral y6] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en linea lateral y6] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en linea lateral y6] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en linea lateral y6] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_lateral_x1(test_client, init_db):
    #Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
     #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=1, pos_y=3)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea lateral x1"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea lateral x1] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea lateral x1]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea lateral x1] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1 , "[Cruce en linea lateral x1] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en linea lateral x1] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en linea lateral x1] :No se marco carta como gastada"

def test_usar_carta_movimiento_cruce_linea_lateral_y1(test_client, init_db):
    #Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
     #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=1)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 200 , "Error al usar carta de movimiento cruce en linea lateral y1"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_carta_mov == carta_movimiento.id_carta, "[Cruce en linea lateral y1] :No se asigno carta al movimiento"
    assert movimientos[0].id_ficha1 == ficha_piv.id_ficha, "[Cruce en linea lateral y1]: No se asigno ficha1 al movimiento"
    assert movimientos[0].id_ficha2 == ficha1.id_ficha, "[Cruce en linea lateral y1] : No se asigno ficha2 al movimiento"
    assert movimientos[0].id_mov ==1, "[Cruce en linea lateral y1] :No se asigno id al movimiento"
    assert movimientos[0].id_partida == partida.id, "[Cruce en linea lateral y1] :No se asigno id de partida al movimiento"
    db.refresh(carta_movimiento)
    assert carta_movimiento.gastada == True, "[Cruce en linea lateral y1] :No se marco carta como gastada"

#caso fallido

def test_usar_carta_movimiento_cruce_linea_lateral_caso_fallido(test_client, init_db): 
    #Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
     #Crear fichas
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400 , "Se intento cruce en linea lateral con fichas contiguas"
    movimientos = get_movimientos_db(db, partida.id)
    assert movimientos[0].id_ficha1 == 0, "[Cruce en linea lateral caso fallido]: se asigno ficha1 al movimiento y no deberia"
    assert movimientos[0].id_ficha2 == 0, "[Cruce en linea lateral caso faillodo] : se asigno ficha2 al movimiento y no deberia"

#partida no existe 
def test_usar_carta_movimiento_partida_no_existe(test_client, init_db): 
    #Crear una partida válida con 1 jugador
    #endpoint con primera ficha arriba
    data_json = {
            "id_carta": 1,
            "id_jugador": "Jugador1",
            "id_ficha1": 1,
            "id_ficha2": 1}
    response = test_client.patch(f"/game/999999999999/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"} 

#Partida no iniciada
def test_usar_carta_movimiento_partida_noini(test_client,init_db): 
    #Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=False)
    db = init_db
    db.add(partida)
    db.commit()
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

#Jugador no esta en la partida
def test_usar_carta_movimiento_jugador_no_esta_en_partida(test_client, init_db):
    #Crear una partida válida con 1 jugador
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True)
    db = init_db
    db.add(partida)
    db.commit()
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador3",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador no pertenece a la partida"}

#No es el turno del jugador 
def test_usar_carta_movimiento_no_es_turno(test_client,init_db):
    #Crear una partida válida con 2 jugadores
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno=2)
    db = init_db
    db.add(partida)
    db.commit()
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     #Crear carta de movimiento a testear
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1") 
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": carta_movimiento.id_carta,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail": "No es el turno del jugador"}

#No existe set cartas movimiento
def test_usar_carta_movimiento_no_existe_set_cartas_movimiento(test_client, init_db):
    #Crear una partida válida con 2 jugadores
    partida = Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno=1)
    db = init_db
    db.add(partida)
    db.commit()
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
    create_movimientos_db(db, partida.id)
      #endpoint con primera ficha arriba
    data_json = {
            "id_carta": 1,
            "id_jugador": "Jugador1",
            "id_ficha1": ficha_piv.id_ficha,
            "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400 
    assert response.json() == {"detail": "La partida no tiene cartas asignadas"}

#No existe set movimientos


#Carta ya usada
def test_usar_carta_movimiento_carta_usada(test_client, init_db):
   partida= Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno="Jugador1")
   db = init_db
   db.add(partida)
   db.commit()
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=True, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)
   data_json = {
                "id_carta": carta_movimiento.id_carta,
                "id_jugador": "Jugador1",
                "id_ficha1": ficha_piv.id_ficha,
                "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 400 
   assert response.json() == {"detail":"La carta fue descartada"}

#Carta no existe
def test_usar_carta_movimiento_carta_no_existe(test_client, init_db):
   partida= Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno="Jugador1")
   db = init_db
   db.add(partida)
   db.commit()
   ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
   ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
   db.add_all([ficha1,ficha_piv])
   db.commit()
    # Asignar cartas de movimiento a la partida
   carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea lateral", descartada=False, id_player="Jugador1")
   db.add(carta_movimiento)
   db.commit()
   create_movimientos_db(db, partida.id)
   data_json = {
                "id_carta": 99,
                "id_jugador": "Jugador1",
                "id_ficha1": ficha_piv.id_ficha,
                "id_ficha2": ficha1.id_ficha}
   response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
   assert response.status_code == 404
   assert response.json() == {"detail":"Carta de movimiento no encontrada"}

#Carta no pertenece al jugador 

def test_usar_carta_movimiento_carta_no_pertenece_jugador(test_client, init_db):
    partida= Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno="Jugador1")
    db = init_db
    db.add(partida)
    db.commit()
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     # Asignar cartas de movimiento a la partida
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador2")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    data_json = {
                 "id_carta": carta_movimiento.id_carta,
                 "id_jugador": "Jugador1",
                 "id_ficha1": ficha_piv.id_ficha,
                 "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail":"La carta no pertenece al jugador"}

#carta descartada
def test_usar_carta_movimiento_carta_descartada(test_client, init_db):
    partida= Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno="Jugador1")
    db = init_db
    db.add(partida)
    db.commit()
    ficha_piv = Ficha(id_partida=partida.id, id_ficha=1, pos_x=3, pos_y=3)
    ficha1 = Ficha(id_partida=partida.id, id_ficha=2, pos_x=3, pos_y=2)
    db.add_all([ficha1,ficha_piv])
    db.commit()
     # Asignar cartas de movimiento a la partida
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=True, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    data_json = {
                 "id_carta": carta_movimiento.id_carta,
                 "id_jugador": "Jugador1",
                 "id_ficha1": ficha_piv.id_ficha,
                 "id_ficha2": ficha1.id_ficha}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail":"La carta fue descartada"}

#las fichas no existen en la partida
def test_usar_carta_movimiento_fichas_no_existen(test_client, init_db):
    partida= Partida(nombre="Partida Test", owner="Jugador1", jugador1="Jugador1", jugador2= "Jugador2",max_jugadores=3, iniciada=True, turno="Jugador1")
    db = init_db
    db.add(partida)
    db.commit()
    # Asignar cartas de movimiento a la partida
    carta_movimiento = Carta_Movimiento(id_partida=partida.id, id_carta=1, tipo_movimiento="cruce en linea contiguo", descartada=False, id_player="Jugador1")
    db.add(carta_movimiento)
    db.commit()
    create_movimientos_db(db, partida.id)
    data_json = {
                 "id_carta": carta_movimiento.id_carta,
                 "id_jugador": "Jugador1",
                 "id_ficha1": 1,
                 "id_ficha2": 2}
    response = test_client.patch(f"/game/{partida.id}/carta_movimiento/usar_carta_movimiento", json=data_json)
    assert response.status_code == 400
    assert response.json() == {"detail":"Ficha 1 no encontrada"}