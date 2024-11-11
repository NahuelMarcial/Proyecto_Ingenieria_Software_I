import pytest
from app.home.models import Partida

# Caso exitoso: Crear el set de cartas de figura
def test_create_fichas(test_client, init_db):
    
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    assert response.status_code == 200, "Error al crear el set de cartas de figura"

    # Convertir el contenido de la respuesta a JSON
    response_json = response.json()
    # Verificar que el set contiene el número esperado de cartas (por ejemplo, 50)
    assert len(response_json) == 36, "El set de fichas no contiene 36 fichas"

# Caso fallido: Crear las fichas en un id de partida invalido
def test_create_fichas_id_partido_invalido(test_client, init_db):
    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"game/999999999/fichas/crear")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

# Caso fallido: Crear las fichas en un id de partida que no ha iniciado
def test_create_fichas_partida_no_iniciada(test_client, init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=False, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    # Realizar la petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

# Caso fallido: Crear las fichas en un id de partida que ya tiene fichas
def test_create_fichas_partida_con_fichas(test_client, init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    # Realizar la 1° petición al endpoint para crear el set de cartas de figura
    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    #realizar la 2° petición al endpoint para crear el set de cartas de figura (falla)
    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")

    assert response.status_code == 400
    assert response.json() == {"detail": "Ya se asignaron las fichas a esta partida"}

#test se crearon 9 de cada color
def test_create_todas_9por_color(test_client,init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()
    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    response_json = response.json()
    # Verificar que el set contiene el número esperado de cartas (por ejemplo, 50)
    assert len(response_json) == 36
    rojo=0
    azul=0
    verde=0
    amarillo=0
    for ficha in response_json:
        if ficha['color'] == 'rojo':
            rojo +=1
        elif ficha['color'] == 'azul':
            azul +=1
        elif ficha['color'] == 'verde':
            verde +=1
        elif ficha['color'] == 'amarillo':
            amarillo +=1
    # Verificar que el set contiene el número esperado de cartas de cada color
    assert rojo == 9, "No hay 9 fichas rojas"
    assert azul == 9 , "No hay 9 fichas azules"
    assert verde == 9 , " No hay 9 fichas verdes"
    assert amarillo == 9,"No hay 9 fichas amarillas"


