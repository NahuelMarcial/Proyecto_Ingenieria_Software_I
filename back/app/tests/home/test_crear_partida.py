def test_largo_nombre_y_owner(test_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Caso válido
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid,"password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 200 ,"Error al crear la partida"

    # Caso vacío
    partida = {"nombre": "", "owner": "", "max_jugadores": 3, "sid": sid,"password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422 
    assert response.json() == {"detail": "Nombre de jugador invalido, debe ser entre 1 y 30 caracteres"} or response.json() == {"detail": "Nombre de partida invalido, debe ser entre 1 y 30 caracteres"}

    # Caso inválido con owner demasiado largo
    partida = {"nombre": "PartidaValida", "owner": "Hola soy un nombre de owner muy muy muy largo que no deberia de pasar", "max_jugadores": 3, "sid": sid , "password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de jugador invalido, debe ser entre 1 y 30 caracteres"}

    # Caso inválido con nombre partida demasiado largo
    partida = {"nombre": "Nombre de partida muuuuuuuuuuy largo que no deberia pasar", "owner": "Jugador", "max_jugadores": 3, "sid": sid, "password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de partida invalido, debe ser entre 1 y 30 caracteres"}

def test_caracteres_invalidos(test_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Nombre de partida contiene caracteres inválidos
    partida = {"nombre": "Partida@Invalida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid,"password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de partida contiene caracteres inválidos"}

    # Nombre de jugador contiene caracteres inválidos
    partida = {"nombre": "PartidaValida", "owner": "Jugador_1", "max_jugadores": 3, "sid": sid, "password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Nombre de jugador contiene caracteres inválidos"}

def test_max_jugadores(test_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Cantidad de jugadores < 2
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 1, "sid": sid, "password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Cantidad de jugadores invalida, debe ser entre 2 y 4"}

    # Cantidad de jugadores > 4
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 5, "sid": sid, "password": "" , "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Cantidad de jugadores invalida, debe ser entre 2 y 4"}

def test_password(test_client):
    # Conectar al servidor de Socket.IO
    sid = 'back'

    #caso valido
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid , "password": "1598", "dificil": True}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 200 ,"Error al crear la partida con password"

    #caso invalido con password caracter invalido
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid , "password": "@@@@", "dificil": True}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña de partida debe contener solo números enteros"}

    #caso invalido con password larga
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid , "password": "12345partida12345partida1234", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    assert response.status_code == 422
    assert response.json() == {"detail": "Contraseña de partida invalida, debe tener exactamente 4 caracteres numericos"}




def test_inicializacion(test_client):

    # Conectar al servidor de Socket.IO
    sid = 'back'

    # Caso válido, testeando que el resto de atributos sean los correctos
    partida = {"nombre": "PartidaValida", "owner": "Jugador1", "max_jugadores": 3, "sid": sid,"password": "", "dificil": False}
    response = test_client.post("/home/crear/", json=partida)
    data = response.json()
    assert response.status_code == 200 ,"Error al crear la partida"
    assert data["nombre"] == "PartidaValida" ,"Nombre de partida incorrecto"
    assert data["iniciada"] == False ,"La partida no debería estar iniciada"
    assert data["owner"] == "Jugador1" ,"Owner incorrecto"
    assert data["jugador1"] == data["owner"] ,"Jugador1 incorrecto"
    assert data["jugador2"] == "", "Jugador2 debería estar vacío"
    assert data["jugador3"] == "", "Jugador3 debería estar vacío"
    assert data["jugador4"] == "", "Jugador4 debería estar vacío"
    assert data["max_jugadores"] == 3 ,"Max jugadores incorrecto"
    assert data["cantidad_jugadores"] == 1 ,"Cantidad jugadores incorrecto"
    assert data["dificil"] == False ,"Dificultad incorrecta"