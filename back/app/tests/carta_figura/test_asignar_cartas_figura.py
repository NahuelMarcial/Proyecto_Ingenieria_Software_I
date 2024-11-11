import pytest
from app.home.models import Partida




# Test para verificar que las cartas de figura se asignan correctamente a 4 jugadores
def test_asignar_cartas_figura_4(test_client, init_db):
   # Crear una partida válida con 4 jugadores
   partida = Partida(nombre="Partida Test", owner="Jugador1", iniciada= True, jugador1="Jugador1", jugador2="Jugador2", jugador3="Jugador3", jugador4="Jugador4", max_jugadores=4)
   db = init_db
   db.add(partida)
   db.commit()


   # Realizar la petición al endpoint que asigna las cartas de figura
   response = test_client.post(f"/game/{partida.id}/carta_figura/set")
   assert response.status_code == 200 ,f"Error al asignar cartas de figura"


   # Obtener las cartas asignadas de la respuesta
   cartas_asignadas = response.json()


   # Verificar que el número de cartas asignadas coincide con el total esperado
   num_cartas_azul = 14 // 4  # 4 jugadores, debe haber 3 cartas azules por jugador
   num_cartas_blanca = 36 // 4  # 4 jugadores, debe haber 9 cartas blancas por jugador


   # Contar las cartas asignadas a cada jugador
   cartas_por_jugador = {"Jugador1": {"azul": 0, "blanca": 0},
                         "Jugador2": {"azul": 0, "blanca": 0},
                         "Jugador3": {"azul": 0, "blanca": 0},
                         "Jugador4": {"azul": 0, "blanca": 0}}


   for carta in cartas_asignadas:
       if carta["id_player"] in cartas_por_jugador:
           cartas_por_jugador[carta["id_player"]][carta["color"]] += 1


   # Verificar que cada jugador tiene la cantidad correcta de cartas de figura
   for jugador, cartas in cartas_por_jugador.items():
       assert cartas["azul"] == num_cartas_azul, f"El jugador {jugador} no tiene la cantidad correcta de cartas azules. Esperado: {num_cartas_azul}, Actual: {cartas['azul']}"
       assert cartas["blanca"] == num_cartas_blanca, f"El jugador {jugador} no tiene la cantidad correcta de cartas blancas. Esperado: {num_cartas_blanca}, Actual: {cartas['blanca']}"


   # Verificar que el total de cartas es correcto
   assert sum([cartas["azul"] for cartas in cartas_por_jugador.values()]) == num_cartas_azul*4 ,f"El total de cartas azules es incorrecto. Esperado: {num_cartas_azul*4}, Actual: {sum([cartas['azul'] for cartas in cartas_por_jugador.values()])}"
   assert sum([cartas["blanca"] for cartas in cartas_por_jugador.values()]) == num_cartas_blanca*4 , f"El total de cartas blancas es incorrecto. Esperado: {num_cartas_blanca*4}, Actual: {sum([cartas['blanca'] for cartas in cartas_por_jugador.values()])}"


# Test para verificar que las cartas de figura se asignan correctamente a 3 jugadores
def test_asignar_cartas_figura_3(test_client, init_db):
   # Crear una partida válida con 3 jugadores
   partida = Partida(nombre="Partida Test", owner="Jugador1", iniciada= True, jugador1="Jugador1", jugador2="Jugador2", jugador3="Jugador3", max_jugadores=4)
   db = init_db
   db.add(partida)
   db.commit()


   # Realizar la petición al endpoint que asigna las cartas de figura
   response = test_client.post(f"/game/{partida.id}/carta_figura/set")
   assert response.status_code == 200 ,f"Error al asignar cartas de figura"


   # Obtener las cartas asignadas de la respuesta
   cartas_asignadas = response.json()


   # Verificar que el número de cartas asignadas coincide con el total esperado
   num_cartas_azul = 14 // 3  # 3 jugadores, debe haber 4 cartas azules por jugador
   num_cartas_blanca = 36 // 3  # 3 jugadores, debe haber 12 cartas blancas por jugador


   # Contar las cartas asignadas a cada jugador
   cartas_por_jugador = {"Jugador1": {"azul": 0, "blanca": 0},
                         "Jugador2": {"azul": 0, "blanca": 0},
                         "Jugador3": {"azul": 0, "blanca": 0}}


   for carta in cartas_asignadas:
       if carta["id_player"] in cartas_por_jugador:
           cartas_por_jugador[carta["id_player"]][carta["color"]] += 1


   # Verificar que cada jugador tiene la cantidad correcta de cartas de figura
   for jugador, cartas in cartas_por_jugador.items():
       assert cartas["azul"] == num_cartas_azul,f"El jugador {jugador} no tiene la cantidad correcta de cartas azules. Esperado: {num_cartas_azul}, Actual: {cartas['azul']}"
       assert cartas["blanca"] == num_cartas_blanca,f"El jugador {jugador} no tiene la cantidad correcta de cartas blancas. Esperado: {num_cartas_blanca}, Actual: {cartas['blanca']}"


   # Verificar que el total de cartas es correcto
   assert sum([cartas["azul"] for cartas in cartas_por_jugador.values()]) == num_cartas_azul*3,f"El total de cartas azules es incorrecto. Esperado: {num_cartas_azul*3}, Actual: {sum([cartas['azul'] for cartas in cartas_por_jugador.values()])}"
   assert sum([cartas["blanca"] for cartas in cartas_por_jugador.values()]) == num_cartas_blanca*3,f"El total de cartas blancas es incorrecto. Esperado: {num_cartas_blanca*3}, Actual: {sum([cartas['blanca'] for cartas in cartas_por_jugador.values()])}"


# Test para verificar que las cartas de figura se asignan correctamente a 2 jugadores
def test_asignar_cartas_figura_2(test_client, init_db):
   # Crear una partida válida con 2 jugadores
   partida = Partida(nombre="Partida Test", owner="Jugador1", iniciada= True, jugador1="Jugador1", jugador2="Jugador2", max_jugadores=4)
   db = init_db
   db.add(partida)
   db.commit()


   # Realizar la petición al endpoint que asigna las cartas de figura
   response = test_client.post(f"/game/{partida.id}/carta_figura/set")
   assert response.status_code == 200,f"Error al asignar cartas de figura"


   # Obtener las cartas asignadas de la respuesta
   cartas_asignadas = response.json()


   # Verificar que el número de cartas asignadas coincide con el total esperado
   num_cartas_azul = 14 // 2  # 2 jugadores, debe haber 7 cartas azules por jugador
   num_cartas_blanca = 36 // 2  # 2 jugadores, debe haber 18 cartas blancas por jugador


   # Contar las cartas asignadas a cada jugador
   cartas_por_jugador = {"Jugador1": {"azul": 0, "blanca": 0},
                         "Jugador2": {"azul": 0, "blanca": 0}}


   for carta in cartas_asignadas:
       if carta["id_player"] in cartas_por_jugador:
           cartas_por_jugador[carta["id_player"]][carta["color"]] += 1


   # Verificar que cada jugador tiene la cantidad correcta de cartas de figura
   for jugador, cartas in cartas_por_jugador.items():
       assert cartas["azul"] == num_cartas_azul,f"El jugador {jugador} no tiene la cantidad correcta de cartas azules. Esperado: {num_cartas_azul}, Actual: {cartas['azul']}"
       assert cartas["blanca"] == num_cartas_blanca,f"El jugador {jugador} no tiene la cantidad correcta de cartas blancas. Esperado: {num_cartas_blanca}, Actual: {cartas['blanca']}"


   # Verificar que el total de cartas es correcto
   assert sum([cartas["azul"] for cartas in cartas_por_jugador.values()]) == num_cartas_azul*2 ,f"El total de cartas azules es incorrecto. Esperado: {num_cartas_azul*2}, Actual: {sum([cartas['azul'] for cartas in cartas_por_jugador.values()])}"
   assert sum([cartas["blanca"] for cartas in cartas_por_jugador.values()]) == num_cartas_blanca*2,f"El total de cartas blancas es incorrecto. Esperado: {num_cartas_blanca*2}, Actual: {sum([cartas['blanca'] for cartas in cartas_por_jugador.values()])}"


# Test cantidad de jugadores invalida
def test_asignar_cartas_figura_invalido(test_client, init_db):
   # Crear una partida válida con 5 jugadores
   partida = Partida(nombre="Partida Test", owner="Jugador1", iniciada= True, jugador1="Jugador1", max_jugadores=4)
   db = init_db
   db.add(partida)
   db.commit()


   # Realizar la petición al endpoint que asigna las cartas de figura
   response = test_client.post(f"/game/{partida.id}/carta_figura/set")
   assert response.status_code == 400
   assert response.json() == {"detail": "El número de jugadores debe ser entre 2 y 4"}

def test_partida_no_existe(test_client, init_db):
   # Realizar la petición al endpoint que asigna las cartas de figura
   response = test_client.post(f"/game/9999999999/carta_figura/set")
   assert response.status_code == 404
   assert response.json() == {"detail": "Partida no encontrada"}
