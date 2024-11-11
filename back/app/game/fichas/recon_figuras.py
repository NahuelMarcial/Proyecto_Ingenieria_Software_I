def get_pivote(conjunto):
    # Encuentra el pivote con menor y, y si hay empate, el menor x
    return min(conjunto, key=lambda ficha: (ficha[1], ficha[0]))
  # Cambia los accesos de diccionario a índices de tupla


def normalizar_conjunto(conjunto, pivote):
    # Normaliza el conjunto restando las coordenadas del pivote
    return {(ficha[0] - pivote[0], ficha[1] - pivote[1]) for ficha in conjunto}  # Usa índices de tupla

def check_figura(candidato, figura):
    # Encuentra el pivote del candidato
    pivote_candidato = get_pivote(candidato)
    
    # Normaliza el conjunto candidato usando su pivote
    candidato_normalizado = normalizar_conjunto(candidato, pivote_candidato)

    # Convertir figura a un conjunto de tuplas
    figura_set = {(ficha['pos_x'], ficha['pos_y']) for ficha in figura}

    # Comparar
    return candidato_normalizado == figura_set
    
def check_figura_4(candidato):
    checkfige = check_fige1(candidato)
    if checkfige:
        return checkfige
    checkfige = check_fige2(candidato)
    if checkfige:
        return checkfige
    checkfige = check_fige3(candidato)
    if checkfige:
        return checkfige
    checkfige = check_fige4(candidato)
    if checkfige:
        return checkfige
    checkfige = check_fige5(candidato)
    if checkfige:
        return checkfige
    checkfige = check_fige6(candidato)
    if checkfige:
        return checkfige
    checkfige = check_fige7(candidato)
    if checkfige:
        return checkfige
    else:
        return ""
    
fige1_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]


fige1_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2}
]

    
def check_fige1(candidato):

    figuras = [fige1_n, fige1_e]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fige1"
    
    return ""

fige2 = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1}
]

def check_fige2(candidato):

    if check_figura(candidato, fige2):
        return "fige2"
    else:
        return ""
    
fige3_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1}
]


fige3_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2}
]


def check_fige3(candidato):

    figuras = [fige3_n, fige3_e]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fige3"
    
    return ""

fige4_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1}
]

fige4_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1}
]

fige4_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 1}
]

fige4_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 1}
]

def check_fige4(candidato):

    figuras = [fige4_n, fige4_s, fige4_e, fige4_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fige4"
        
    return ""

fige5_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -2, "pos_y": 1}
]

fige5_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0}
]

fige5_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2}
]

fige5_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2}
]

def check_fige5(candidato):

    figuras = [fige5_n, fige5_s, fige5_e, fige5_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fige5"
    
    return ""

fige6_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 3, "pos_y": 0}
]


fige6_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3}
]


def check_fige6(candidato):

    figuras = [fige6_n, fige6_e]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fige6"
    
    return ""

fige7_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 2, "pos_y": 1}
]

fige7_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fige7_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 0}
]

fige7_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2}
]

def check_fige7(candidato):

    figuras = [fige7_n, fige7_s, fige7_e, fige7_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fige7"
    
    return ""

def check_figura_5(candidato):
    checkfig = check_fig1(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig2(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig3(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig4(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig5(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig6(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig7(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig8(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig9(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig10(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig11(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig12(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig13(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig14(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig15(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig16(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig17(candidato)
    if checkfig:
        return checkfig
    checkfig = check_fig18(candidato)
    if checkfig:
        return checkfig
    else:
        return ""
    
fig1_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fig1_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -2, "pos_y": 1}
]

fig1_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2}
]

fig1_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2}
]

def check_fig1(candidato):

    figuras = [fig1_n, fig1_s, fig1_e, fig1_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig1"
    
    return ""

fig2_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0}
]

fig2_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -2, "pos_y": 1},
    {"pos_x": 1, "pos_y": 0}
]

fig2_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 1, "pos_y": 3}
]

fig2_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 1, "pos_y": 3}
]

def check_fig2(candidato):

    figuras = [fig2_n, fig2_s, fig2_e, fig2_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig2"
    
    return ""

fig3_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 3, "pos_y": 1}
]

fig3_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 3, "pos_y": 1}
]

fig3_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2},
    {"pos_x": -1, "pos_y": 3}
]

fig3_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2},
    {"pos_x": -1, "pos_y": 3}
]

def check_fig3(candidato):

    figuras = [fig3_n, fig3_s, fig3_e, fig3_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig3"
    
    return ""

fig4_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2}
]

fig4_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2},
    {"pos_x": -2, "pos_y": 2}
]

fig4_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 2, "pos_y": 2}
]

fig4_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 2, "pos_y": 2}
]

def check_fig4(candidato):

    figuras = [fig4_n, fig4_s, fig4_e, fig4_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig4"
    
    return ""

fig5_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 3, "pos_y": 0},
    {"pos_x": 4, "pos_y": 0}
]


fig5_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3},
    {"pos_x": 0, "pos_y": 4}
]


def check_fig5(candidato):

    figuras = [fig5_n, fig5_e]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig5"
    
    return ""

fig6_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0}
]

fig6_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2},
    {"pos_x": -2, "pos_y": 2}
]

fig6_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 2, "pos_y": 2}
]

fig6_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 2, "pos_y": 2}
]

def check_fig6(candidato):

    figuras = [fig6_n, fig6_s, fig6_e, fig6_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig6"
    
    return ""

fig7_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": -3, "pos_y": 1},
    {"pos_x": -2, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1}
]

fig7_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 3, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1}
]

fig7_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 1, "pos_y": 3},
    {"pos_x": 1, "pos_y": 0}
]

fig7_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3},
    {"pos_x": 1, "pos_y": 3}
]

def check_fig7(candidato):

    figuras = [fig7_n, fig7_s, fig7_e, fig7_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig7"
    
    return ""

fig8_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 3, "pos_y": 0},
    {"pos_x": 3, "pos_y": 1}
]

fig8_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 3, "pos_y": 1}
]

fig8_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3}
]

fig8_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3},
    {"pos_x": -1, "pos_y": 3}
]

def check_fig8(candidato):

    figuras = [fig8_n, fig8_s, fig8_e, fig8_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig8"
    
    return ""

fig9_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2}
]

fig9_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 2, "pos_y": 1}
]

fig9_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 1}
]

fig9_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2}
]

def check_fig9(candidato):

    figuras = [fig9_n, fig9_s, fig9_e, fig9_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig9"
    
    return ""

fig10_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 2, "pos_y": 2}
]


fig10_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2}
]


def check_fig10(candidato):

    figuras = [fig10_n, fig10_e]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig10"
    
    return ""

fig11_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2}
]

fig11_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -2, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2}
]

fig11_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2}
]

fig11_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2}
]

def check_fig11(candidato):

    figuras = [fig11_n, fig11_s, fig11_e, fig11_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig11"
    
    return ""

fig12_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": -2, "pos_y": 1},
    {"pos_x": -2, "pos_y": 2}
]

fig12_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 2, "pos_y": 2}
]


def check_fig12(candidato):

    figuras = [fig12_n, fig12_e]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig12"
    
    return ""

fig13_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": -2, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1}
]

fig13_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 3, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1}
]

fig13_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3}
]

fig13_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3}
]

def check_fig13(candidato):

    figuras = [fig13_n, fig13_s, fig13_e, fig13_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig13"
    
    return ""

fig14_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 3, "pos_y": 0},
    {"pos_x": 2, "pos_y": 1}
]

fig14_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fig14_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3}
]

fig14_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": -1, "pos_y": 2},
    {"pos_x": 0, "pos_y": 3}
]

def check_fig14(candidato):

    figuras = [fig14_n, fig14_s, fig14_e, fig14_o] 

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig14"
    
    return ""

fig15_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fig15_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fig15_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2}
]

fig15_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": -1, "pos_y": 2},
    {"pos_x": 0, "pos_y": 2}
]

def check_fig15(candidato):

    figuras = [fig15_n, fig15_s, fig15_e, fig15_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig15"
    
    return ""

fig16_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fig16_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 2, "pos_y": 1}
]

fig16_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2}
]

fig16_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2}
]

def check_fig16(candidato):

    figuras = [fig16_n, fig16_s, fig16_e, fig16_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig16"
    
    return ""

fig17 = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2}
]

def check_fig17(candidato):

    ret = check_figura(candidato, fig17)
    if ret:
        return "fig17"
    
    return ""

fig18_n = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": -1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1}
]

fig18_s = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 2, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1}
]

fig18_e = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 1, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 1, "pos_y": 2}
]

fig18_o = [
    {"pos_x": 0, "pos_y": 0},
    {"pos_x": 0, "pos_y": 1},
    {"pos_x": 1, "pos_y": 1},
    {"pos_x": 0, "pos_y": 2},
    {"pos_x": 1, "pos_y": 2}
]

def check_fig18(candidato):

    figuras = [fig18_n, fig18_s, fig18_e, fig18_o]

    for figura in figuras:
        if check_figura(candidato, figura):
            return "fig18"
    
    return ""
