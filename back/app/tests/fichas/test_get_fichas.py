import pytest
from app.home.models import Partida
#chequear que se devuelvan todas las fichas
def test_get_fichas(test_client, init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    #crear fichas
    response = test_client.post(f"/game/{partida_ficha.id}/fichas/crear")
    assert response.status_code == 200, " error al crear fichas"

    #listar fichas
    response = test_client.get(f"/game/{partida_ficha.id}/fichas/listar")
    assert response.status_code == 200 , " error al listar fichas"

    response_json = response.json()
    assert len(response_json) == 36 , "las fichas creadas no son 36"

    #contadores para ver las cartas de cada color
    rojo=0
    azul=0
    verde=0
    amarillo=0

    #conjunto para guardar los id de las fichas
    ids = set()
    for ficha in response_json:
        ids.add(ficha['id_ficha'])
        if ficha['color'] == 'rojo':
            rojo +=1
        elif ficha['color'] == 'azul':
            azul +=1
        elif ficha['color'] == 'verde':
            verde +=1
        elif ficha['color'] == 'amarillo':
            amarillo +=1
    #verificar que esten todos los id
    assert len(ids) == 36, "hay ids repetidos"
    # Verificar que el set contiene el número esperado de cartas de cada color
    assert rojo == 9 , "No hay 9 fichas rojas"
    assert azul == 9 , "No hay 9 fichas azules"
    assert verde == 9 , " No hay 9 fichas verdes"
    assert amarillo == 9 , "No hay 9 fichas amarillas"


#test cuando el id de partida invalido
def test_get_fichas_partida_invalida(test_client, init_db):
    #listar fichas de partida no existente
    response = test_client.get(f"/game/9999999999/fichas/listar")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

#test cuando la partida no tiene fichas
def test_get_fichas_sin_fichas(test_client, init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    #listar fichas
    response = test_client.get(f"/game/{partida_ficha.id}/fichas/listar")
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay fichas asignadas a esta partida"}

# Test partida no iniciada
def test_get_fichas_partida_no_iniciada(test_client, init_db):
    partida_ficha = Partida(nombre="Partida Valida",iniciada=False, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida_ficha)
    db.commit()

    #listar fichas
    response = test_client.get(f"/game/{partida_ficha.id}/fichas/listar")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}
    