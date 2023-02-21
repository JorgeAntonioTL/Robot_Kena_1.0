#Programadores
#Mayra Yazmin Vargas Arredondo
#Jorge Antonio Toscano Lara
#Luis Ernesto Garcia Alvarez

import random

def basura():
    #Define la cantidad de basura que abrá en el área. Entre 10 y 15 elementos.
    cant_Basura = random.randint(10, 15)
    print(f"Cantidad de basura: {cant_Basura}")

    #Define las posiciones de los elementos (basura)
    for i in range(cant_Basura):
        pos = cord_Random()

    for i in range(0, len(area[0])):
        print(area[i])


    return(cant_Basura)
            
def cord_Random():
    cord_X = random.randint(0,6)
    cord_Y = random.randint(0,6)
    if cord_X == 0 and cord_Y == 0:
        cord_Random()
    else: 
        if area[cord_X][cord_Y] != 1:
            area[cord_X][cord_Y] = 1
        else: cord_Random()


area = [[2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

cant_Basura = basura()

