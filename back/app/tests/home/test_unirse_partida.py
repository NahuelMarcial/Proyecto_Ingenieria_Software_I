import pytest
from app.home.models import Partida

# Configuración para la base de datos de prueba

def test_unirse_partida_id_inexistente(test_client):
    response = test_client.patch("/home/unirse/999999", json={"jugador": "Jugador1", "sid": "back" , "password": ""})
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_unirse_partida_llena(test_client, init_db):
    partida_llena = Partida(nombre="Partida Llena", owner="Jugador3", iniciada=False, cantidad_jugadores=4, max_jugadores=4 ,password="")
    db = init_db
    db.add(partida_llena)
    db.commit()

    response = test_client.patch(f"/home/unirse/{partida_llena.id}", json={"jugador": "Jugadornuevo", "sid": "back", "password": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Partida llena"}

def test_unirse_partida_iniciada(test_client, init_db):
    partida_iniciada = Partida(nombre="Partida Iniciada", owner="Jugador2", iniciada=True, cantidad_jugadores=1, max_jugadores=4, password="")
    db = init_db
    db.add(partida_iniciada)
    db.commit()

    response = test_client.patch(f"/home/unirse/{partida_iniciada.id}", json={"jugador": "Jugador3", "sid": "back", "password": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "No se puede unir a una partida iniciada"}

def test_unirse_partida_exitosa(test_client, init_db):
    partida_valida = Partida(nombre="Partida Válida", owner="Jugador1", iniciada=False, cantidad_jugadores=1, max_jugadores=4, password="")
    db = init_db
    db.add(partida_valida)
    db.commit()

    response = test_client.patch(f"/home/unirse/{partida_valida.id}", json={"jugador": "JugadorNuevo", "sid": "back", "password": ""})
    assert response.status_code == 200  ,"Error al unirse a la partida"
    partida_actualizada = response.json()

     # Verifica que el número de jugadores se haya actualizado
    assert partida_actualizada['cantidad_jugadores'] == 2 ,"La cantidad de jugadores no se ha actualizado correctamente"
    
    # Verifica que el jugador se haya agregado a la partida
    assert (partida_actualizada['jugador1'] == 'JugadorNuevo' or
    partida_actualizada['jugador2'] == 'JugadorNuevo' or
    partida_actualizada['jugador3'] == 'JugadorNuevo' or
    partida_actualizada['jugador4'] == 'JugadorNuevo')   ,"El jugador no se ha unido a la partida correctamente"


def test_unirse_partida_pass (test_client, init_db):
    sid = "back"
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid,"password": "1234", "dificil": True}
    partida_valida = test_client.post("/home/crear/", json=partida)
    assert partida_valida.status_code == 200 ,"Error al crear la partida"

    partida_valida = partida_valida.json()
    partida_valida_id = partida_valida["id"]
    response = test_client.patch(f"/home/unirse/{partida_valida_id}", json={"jugador": "JugadorNuevo", "sid": "back", "password": "1234", "dificil": True})
    assert response.status_code == 200  ,"Error al unirse a la partida"
    partida_actualizada = response.json()

     # Verifica que el número de jugadores se haya actualizado
    assert partida_actualizada['cantidad_jugadores'] == 2 ,"La cantidad de jugadores no se ha actualizado correctamente"
    
    # Verifica que el jugador se haya agregado a la partida
    assert (partida_actualizada['jugador1'] == 'JugadorNuevo' or
    partida_actualizada['jugador2'] == 'JugadorNuevo' or
    partida_actualizada['jugador3'] == 'JugadorNuevo' or
    partida_actualizada['jugador4'] == 'JugadorNuevo')   ,"El jugador no se ha unido a la partida correctamente"

def test_unirse_partida_pass_incorrecta(test_client, init_db):
    sid = "back"
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid,"password": "1234", "dificil": True}
    partida_valida = test_client.post("/home/crear/", json=partida)
    assert partida_valida.status_code == 200 ,"Error al crear la partida"

    partida_valida = partida_valida.json()
    partida_valida_id = partida_valida["id"]

    #Contraseña incorrecta
    response = test_client.patch(f"/home/unirse/{partida_valida_id}", json={"jugador": "JugadorNuevo ", "sid": "back", "password": "1235"})
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña incorrecta"}
    #Contraseña incorrecta mas de 4 caracteres
    response = test_client.patch(f"/home/unirse/{partida_valida_id}", json={"jugador": "JugadorNuevo ", "sid": "back", "password": "123545"})
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña incorrecta"}
    #Contraseña incorrecta menos de 4 caracteres
    response = test_client.patch(f"/home/unirse/{partida_valida_id}", json={"jugador": "JugadorNuevo ", "sid": "back", "password": "123"})
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña incorrecta"}
    #Contraseña incorrecta vacia
    response = test_client.patch(f"/home/unirse/{partida_valida_id}", json={"jugador": "JugadorNuevo ", "sid": "back", "password": ""})
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña incorrecta"}
    #Contraseña incorrecta con caracteres especiales
    response = test_client.patch(f"/home/unirse/{partida_valida_id}", json={"jugador": "JugadorNuevo ", "sid": "back", "password": "123@"})
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña incorrecta"}