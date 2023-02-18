from Basura_Random_1 import area, cant_Basura


#Variables base que estaremos usando para controlar el robot
bateria = [1000]
movimiento = 10
recoger = 20
posicion_Actual = [0,0]
posicion_Ultima = []
cambio_Fila = 0

def bateria_Baja():
    #Determinar cual de los parámetros de coordenada es mayor
    if posicion_Actual[0] > posicion_Actual[1]:
        cor_Max = posicion_Actual[0]
    else: cor_Max = posicion_Actual[1]

    for i in range(cor_Max):
        if posicion_Actual[0] > 0: 
            posicion_Actual[0] -= 1
        if posicion_Actual[1] > 0: 
            posicion_Actual[1] -= 1
        print(posicion_Actual)
        bateria[0] -= movimiento
        print(bateria[0])
        

    bateria[0] = 1000
    volver_Ultima()

def volver_Ultima():

    #Determinar cual de los parámetros de coordenada es mayor
    if posicion_Ultima[0] > posicion_Ultima[1]:
        cor_Max = posicion_Ultima[0]
    else: cor_Max = posicion_Ultima[1]

    for i in range(cor_Max):
        if posicion_Actual[0] < posicion_Ultima[0]:
            posicion_Actual[0]+= 1
        if posicion_Actual[1] < posicion_Ultima[1]:
            posicion_Actual[1]+= 1
        print(posicion_Actual)
        bateria[0] -= movimiento
        print(bateria[0])

for i in range(7):
    posicion_Actual[0] = i
    for j in range(7):
        if i is not 0 or j is not 0:
            bateria[0] -= movimiento
            if cambio_Fila is 0:
                if i % 2 == 0: 
                    posicion_Actual[1] += 1
                else: posicion_Actual[1] -= 1
            cambio_Fila = 0

            #Comprobación de basura (Recoger)
            if area[posicion_Actual[0]][posicion_Actual[1]] is 1:
                area[posicion_Actual[0]][posicion_Actual[1]] = 0
                bateria[0] -= recoger
                cant_Basura -= 1

            print(f"Batería: {bateria}")
            print(f"Basura: {cant_Basura}")

            for z in range(0, len(area[0])):
                print(area[z])

            print()

            if cant_Basura == 0: 
                print("Ta todo limpio :) ")
        
            if bateria[0] <= 350:
                posicion_Ultima = posicion_Actual.copy()
                print("Batería Baja")
                bateria_Baja()

    cambio_Fila = 1


