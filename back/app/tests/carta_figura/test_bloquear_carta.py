from app.game.carta_figura.models import Carta_Figura
from app.game.fichas.models import Ficha
from app.home.models import Partida

# Test exitoso para bloquear una carta
def test_bloquear_carta_exitoso(test_client, init_db):
    db = init_db

    # Crear partida y jugadores necesarios
    partida = Partida(nombre="Partida Test", iniciada=True, turno=1, owner= "bloqueador", jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    # Agregar carta y ficha en la base de datos
    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()


    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Datos del request
    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    # Hacer petición para bloquear la carta
    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    print(response.json())
    
    assert response.status_code == 200, "Fallo al bloquear la carta"
    db.refresh(carta)
    assert carta.bloqueada == True, "La carta no se bloqueó"
    assert carta.reponer == False, "La carta sigue reponiendo"
    assert carta.mostrar == True, "La carta no se muestra"
    
# Test fallo: La partida no existe
def test_bloquear_carta_fallo_partida_no_existe(test_client, init_db):
    db = init_db

    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    response = test_client.patch("/game/99999999/carta_figura/bloquear_carta", json=data)
    assert response.status_code == 404, "Se esperaba un status code 404"
    assert response.json() == {"detail": "Partida no encontrada"}

# Test fallo: Partida no iniciada
def test_bloquear_carta_fallo_partida_no_iniciada(test_client, init_db):
    db = init_db

    # Crear partida que no está iniciada
    partida = Partida(nombre="Partida No Iniciada", owner="bloqueador", iniciada=False, turno=1, jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()

    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    assert response.status_code == 400, "Se esperaba un status code 400"
    assert response.json() == {"detail": "La partida no ha iniciado"}

# Test fallo: No es el turno del jugador
def test_bloquear_carta_fallo_no_es_turno(test_client, init_db):
    db = init_db

    # Crear partida con turno para otro jugador
    partida = Partida(nombre="Partida Turno", owner="bloqueador", iniciada=True, turno=2, jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()

    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    assert response.status_code == 400, "Se esperaba un status code 400"
    assert response.json() == {"detail": "No es el turno del jugador"}

# Test fallo: Carta no pertenece al jugador bloqueado
def test_bloquear_carta_fallo_carta_no_pertenece_jugador(test_client, init_db):
    db = init_db

    # Crear partida e insertar carta de otro jugador
    partida = Partida(nombre="Partida Test",owner="bloqueador", iniciada=True, turno=1, jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()
    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueador", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueador", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()

    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    assert response.status_code == 400, "Se esperaba un status code 400"
    assert response.json() == {"detail": "No se puede bloquear a uno mismo"}

# Test fallo: No se puede bloquear la última carta
def test_bloquear_carta_fallo_ultima_carta(test_client, init_db):
    db = init_db

    # Crear partida e insertar una única carta del jugador a bloquear
    partida = Partida(nombre="Partida Test", owner="bloqueador", iniciada=True, turno=1, jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add(carta)
    db.commit()

    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    assert response.status_code == 400, "Se esperaba un status code 400"
    assert response.json() == {"detail": "No se puede bloquear la última carta"}

# Test fallo: No hay cartas en la partida
def test_bloquear_carta_fallo_no_hay_cartas(test_client, init_db):
    db = init_db

    # Crear partida sin cartas
    partida = Partida(nombre="Partida Test", owner="bloqueador", iniciada=True, turno=1, jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    assert response.status_code == 400, "Se esperaba un status code 400"
    assert response.json() == {"detail": "No hay cartas asignadas a la partida"}

# Test fallo: La carta no pertenece a la figura
    db = init_db

    # Crear partida y jugadores necesarios
    partida = Partida(nombre="Partida Test", iniciada=True, turno=1, owner= "bloqueador", jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    # Agregar carta y ficha en la base de datos
    carta = Carta_Figura(id_carta=1, nombre="fige3", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()


    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Datos del request
    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    # Hacer petición para bloquear la carta
    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    print(response.json())
    
    assert response.status_code == 400, "Se esperaba codigo 400"
    assert response.json() == {"detail": "La ficha no pertenece a la figura de la carta"}


# Test fallo: La carta ya está bloqueada
def test_bloquear_carta_fallo_carta_ya_bloqueada(test_client, init_db):
    db = init_db

    # Crear partida y jugadores necesarios
    partida = Partida(nombre="Partida Test", iniciada=True, turno=1, owner= "bloqueador", jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    # Agregar carta y ficha en la base de datos
    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True, bloqueada=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()


    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Datos del request
    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 1,
        "id_ficha": 1
    }

    # Hacer petición para bloquear la carta
    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    print(response.json())
    
    assert response.status_code == 400, "Se esperaba codigo 400"
    assert response.json() == {"detail": "La carta ya está bloqueada"}

# Test fallo: El jugador ya tiene una carta bloqueada
def test_bloquear_fallo_ya_tiene_carta_bloqueada(test_client, init_db):
    db = init_db

    # Crear partida y jugadores necesarios
    partida = Partida(nombre="Partida Test", iniciada=True, turno=1, owner= "bloqueador", jugador1="bloqueador", jugador2="bloqueado")
    db.add(partida)
    db.commit()

    # Agregar carta y ficha en la base de datos
    carta = Carta_Figura(id_carta=1, nombre="fige1", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True, bloqueada=True)
    carta2 = Carta_Figura(id_carta=2, nombre="fige2", color="azul", id_partida=partida.id, id_player="bloqueado", mostrar=True)
    db.add_all([carta, carta2])
    db.commit()


    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    # Datos del request
    data = {
        "id_bloqueador": "bloqueador",
        "id_carta": 2,
        "id_ficha": 1
    }

    # Hacer petición para bloquear la carta
    response = test_client.patch(f"/game/{partida.id}/carta_figura/bloquear_carta", json=data)
    print(response.json())
    
    assert response.status_code == 400, "Se esperaba codigo 400"
    assert response.json() == {"detail": "El jugador ya tiene una carta bloqueada"}