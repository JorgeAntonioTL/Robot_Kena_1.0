import random

def basura():
    #Define la cantidad de basura que abrá en el área. Entre 10 y 15 elementos.
    cant_Basura = random.randint(10, 15)

    #Define las posiciones de los elementos (basura)
    for i in range(cant_Basura):
        pos = cord_Random()
        if area[pos[0]][pos[1]] != 1:
            area[pos[0]][pos[1]] = 1
            print(area[pos[0]][pos[1]])
    


def cord_Random():
    cord_X = random.randint(0,6)
    cord_Y = random.randint(0,6)
    if cord_X == 0 and cord_Y == 0:
        cord_Random()
    else: 
        cords = [cord_X,cord_Y]
        return cords


area = [[2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

basura()
print(area)
