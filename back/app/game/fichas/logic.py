from fastapi import HTTPException

import app.home.home_repository as home_repository
import app.game.fichas.fichas_repository as fichas_repository
import app.game.carta_movimiento.carta_movimiento_repository as carta_movimiento_repository
import app.game.carta_figura.carta_figura_repository as carta_figura_repository
from app.game.fichas.recon_figuras import check_figura_4, check_figura_5
from app.game.fichas.models import Ficha
from app.game.fichas.schemas import FigFormada, SugerenciaData
import app.game.fichas.endpoints as fichas_endpoints
import app.game.carta_movimiento.movimientos_logic as mov_logic

def validar_partida(partida_id, db):
    error = False
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if not partida.iniciada :
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    fichas = fichas_repository.get_fichas_db(db, partida_id)
    if fichas:
        raise HTTPException(status_code=400, detail="Ya se asignaron las fichas a esta partida")
    return error

def validar_partida_exist(partida_id, db):
    error = False
    partida = home_repository.get_partida_db(db, partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if not partida.iniciada :
        raise HTTPException(status_code=400, detail="La partida no ha iniciado")
    fichas = fichas_repository.get_fichas_db(db, partida_id)
    if not fichas:
        raise HTTPException(status_code=400, detail="No hay fichas asignadas a esta partida")
    return error   

def validar_fichas(db, partida_id, id_ficha1, id_ficha2):
    error = False
    ficha1 = fichas_repository.get_ficha_partida_db(db, id_ficha1, partida_id)
    ficha2 = fichas_repository.get_ficha_partida_db(db, id_ficha2, partida_id)
    if not ficha1 or not ficha2:
        error = True
        raise HTTPException(status_code=404, detail="No se encontraron las fichas")
    return error

def validar_ficha(db, partida_id, id_ficha):
    error = False
    ficha = fichas_repository.get_ficha_partida_db(db, id_ficha, partida_id)
    if not ficha:
        error = True
        raise HTTPException(status_code=404, detail="No se encontro la ficha")
    return error

def swap_fichas(ficha1:Ficha,ficha2:Ficha):
    temp_pos_x = ficha1.pos_x
    temp_pos_y = ficha1.pos_y
    ficha1.pos_x = ficha2.pos_x
    ficha1.pos_y = ficha2.pos_y
    ficha2.pos_x = temp_pos_x
    ficha2.pos_y = temp_pos_y
    return ficha1,ficha2

def get_figuras_formadas_db(db, partida_id):
    fichas = get_fichas_formateadas(db, partida_id)
    partida = home_repository.get_partida_db(db, partida_id)
    candidatos = []

    if partida.color_bloqueado != "rojo":
        fichas_rojo = [f for f in fichas if f["color"].value == "rojo"]
        candidatos = candidatos_color(candidatos, fichas_rojo)

    if partida.color_bloqueado != "azul":
        candidatos_azul = [f for f in fichas if f["color"].value == "azul"]
        candidatos = candidatos_color(candidatos, candidatos_azul)

    if partida.color_bloqueado != "verde":
        candidatos_verde = [f for f in fichas if f["color"].value == "verde"]
        candidatos = candidatos_color(candidatos, candidatos_verde)

    if partida.color_bloqueado != "amarillo":
        candidatos_amarillo = [f for f in fichas if f["color"].value == "amarillo"]
        candidatos = candidatos_color(candidatos, candidatos_amarillo)

    figuras_formadas = []

    for conjunto in candidatos:
        figura = []
        if len(conjunto) < 4:
            continue
        if len(conjunto) > 5:
            continue
        if len(conjunto) == 4:
            fig = check_figura_4(conjunto)
            if fig:
                figura = FigFormada(figura=fig, fichas=[conjunto]) 
                figuras_formadas.append(figura) 

        if len(conjunto) == 5:
            fig = check_figura_5(conjunto)
            if fig:
                figura = FigFormada(figura=fig, fichas=[conjunto])  
                figuras_formadas.append(figura)


    return figuras_formadas

def agrupar_fichas(ficha_inicial, fichas, visitadas):
    # Implementamos una búsqueda por profundidad (DFS)
    grupo = set()
    stack = [ficha_inicial]
    
    while stack:
        ficha = stack.pop()
        pos_x = ficha["pos_x"]
        pos_y = ficha["pos_y"]
        posicion_ficha = (pos_x, pos_y)
        
        if posicion_ficha not in visitadas:
            visitadas.add(posicion_ficha)
            grupo.add(posicion_ficha)
            
            adyacentes = [
                (pos_x, pos_y + 1),  
                (pos_x, pos_y - 1),  
                (pos_x + 1, pos_y),  
                (pos_x - 1, pos_y)   
            ]
            

            for otra_ficha in fichas:
                if (otra_ficha["pos_x"], otra_ficha["pos_y"]) in adyacentes:
                    otra_posicion = (otra_ficha["pos_x"], otra_ficha["pos_y"])
                    if otra_posicion not in visitadas:
                        stack.append(otra_ficha)
    
    return grupo
    
def candidatos_color(candidatos, fichas):
    visitadas = set()  # Para llevar un control de las fichas que ya hemos procesado

    # Para cada ficha, intentamos agruparla con sus adyacentes
    for ficha in fichas:
        posicion_ficha = (ficha["pos_x"], ficha["pos_y"])
        if posicion_ficha not in visitadas:
            nuevo_grupo = agrupar_fichas(ficha, fichas, visitadas)
            if nuevo_grupo:
                candidatos.append(nuevo_grupo)
    
    return candidatos

def get_fichas_formateadas(db, partida_id):
    # Obtener fichas desde la base de datos
    fichas = fichas_repository.get_fichas_db(db, partida_id)
    
    # Lista para almacenar las fichas en el formato deseado
    fichas_formateadas = []

    # Convertir cada objeto Ficha a un diccionario
    for ficha in fichas:
        ficha_dict = {
            "id_ficha": ficha.id,       # Atributo 'id' de la ficha
            "pos_x": ficha.pos_x,       # Atributo 'pos_x' de la ficha
            "pos_y": ficha.pos_y,       # Atributo 'pos_y' de la ficha
            "color": ficha.color        # Atributo 'color' de la ficha
        }
        fichas_formateadas.append(ficha_dict)

    # Devolver las fichas formateadas (si es necesario)
    return fichas_formateadas

def get_sugerencia(partida_id: int, player_id: str, db):
    from app.game.app import get_turno_jugador
    turno = get_turno_jugador(partida_id, db)
    if turno["id_player"] != player_id:
        rta = SugerenciaData(id_ficha1=-1, id_ficha2=-1, id_carta=-1)  
        return rta
    
    fichas = get_fichas_formateadas(db, partida_id)
    partida = home_repository.get_partida_db(db, partida_id)
    candidatos = []

    if partida.color_bloqueado != "rojo":
        fichas_rojo = [f for f in fichas if f["color"].value == "rojo"]
        candidatos = candidatos_color(candidatos, fichas_rojo)

    if partida.color_bloqueado != "azul":
        candidatos_azul = [f for f in fichas if f["color"].value == "azul"]
        candidatos = candidatos_color(candidatos, candidatos_azul)

    if partida.color_bloqueado != "verde":
        candidatos_verde = [f for f in fichas if f["color"].value == "verde"]
        candidatos = candidatos_color(candidatos, candidatos_verde)

    if partida.color_bloqueado != "amarillo":
        candidatos_amarillo = [f for f in fichas if f["color"].value == "amarillo"]
        candidatos = candidatos_color(candidatos, candidatos_amarillo)

    cartas_movi = carta_movimiento_repository.get_mano_cartas_movimiento_db(db, partida_id, player_id)
    figuras = fichas_endpoints.get_figuras_formadas(partida_id, db)
    find = False
    ficha_find_A = None
    ficha_find_B = None

    mano = carta_figura_repository.get_cartas_jugador_mostradas_no_bloqu_db(db, partida_id, player_id)
    
    # Obtener los nombres de las figuras en `figuras`
    nombres_figuras = {figura.figura for figura in figuras}
    
    # Filtrar `mano` para eliminar las cartas cuyo nombre esté en `nombres_figuras`
    mano_filtrada = [carta for carta in mano if carta.nombre not in nombres_figuras]
    
    # Obtener los nombres de las cartas en `mano_filtrada`
    nombres_mano_filtrada = {carta.nombre for carta in mano_filtrada}

    for conjunto in candidatos:
        if find:
            break
        for carta in cartas_movi:
            if find:
                break
            for ficha in conjunto:
                ficha_temp = fichas_repository.get_ficha_pos_db(db, partida_id, ficha[0], ficha[1])
                if ficha_temp:  # Verificar que ficha_temp no sea None
                    find = probar_carta(figuras, carta.id_carta, ficha_temp.id_ficha, partida_id, nombres_mano_filtrada, db)
                    if find:
                        carta_find = carta.id_carta
                        ficha_find_A = ficha
                        ficha_find_B = find
                        break

    if find and ficha_find_A:
        ficha_A = fichas_repository.get_ficha_pos_db(db, partida_id, ficha_find_A[0], ficha_find_A[1])
        if ficha_A:  # Verificar que ficha_A no sea None
            rta = SugerenciaData(id_ficha1=ficha_A.id_ficha, id_ficha2=ficha_find_B, id_carta=carta_find)
        else:
            rta = SugerenciaData(id_ficha1=-1, id_ficha2=-1, id_carta=-1)
    else:
        rta = SugerenciaData(id_ficha1=-1, id_ficha2=-1, id_carta=-1)  # Devolver un objeto válido con valores por defecto

    return rta

def probar_carta(figuras, carta_id: int, ficha_id: int, partida_id: int, nombres_mano_filtrada, db):
    ficha = fichas_repository.get_ficha_partida_db(db, ficha_id, partida_id)
    if not ficha:
        raise HTTPException(status_code=400, detail="Ficha no encontrada")
    
    carta = carta_movimiento_repository.get_carta_movimiento_id_db(db, partida_id, carta_id)
    if not carta:
        raise HTTPException(status_code=400, detail="Carta de movimiento no encontrada")
    
    movimientos = []
    
    movimientos = mov_logic.movimientos_posibles(db, partida_id, carta_id, ficha_id)

    for mov in movimientos:
        if mov:
            ficha2_id = mov.id_ficha
            ficha2 = fichas_repository.get_ficha_partida_db(db, ficha2_id, partida_id)
            if not ficha2:
                continue
            
            # Intercambiar las posiciones de las fichas
            ficha1, ficha2 = swap_fichas(ficha, ficha2)
            db.add(ficha1)
            db.add(ficha2)
                
            # Verificar nuevas figuras formadas
            nuevas_figuras = fichas_endpoints.get_figuras_formadas(partida_id, db)

            # Intercambiar las posiciones de las fichas
            ficha1, ficha2 = swap_fichas(ficha, ficha2)
            db.add(ficha1)
            db.add(ficha2)
            # Verificar si alguna figura en `nuevas_figuras` tiene un nombre que coincida con los nombres de las cartas en `mano_filtrada`
            for figura in nuevas_figuras:
                if figura.figura in nombres_mano_filtrada:
                    return ficha2_id
                
    
    return None