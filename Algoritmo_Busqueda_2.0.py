#Programadores
#Mayra Yazmin Vargas Arredondo
#Jorge Antonio Toscano Lara
#Luis Ernesto Garcia Alvarez

#En este programa el robot SÍ muere, termina su ejecución una vez que se haya quedado sin batería o haya limpiado toda la basura


from Basura_Random_1 import area, cant_Basura


#Variables base que estaremos usando para controlar el robot
bateria = [1000]
movimiento = 10
recoger = 20
posicion_Actual = [0,0]
posicion_Ultima = []
cambio_Fila = 0


def Termino():
    #Determinar cual de los parámetros de coordenada es mayor
    if posicion_Actual[0]-1 > posicion_Actual[1]-1:
        cor_Max = posicion_Actual[0]-1
    else: cor_Max = posicion_Actual[1]-1

    for i in range(cor_Max):
        if posicion_Actual[0] > 1: 
            posicion_Actual[0] -= 1
        if posicion_Actual[1] > 1: 
            posicion_Actual[1] -= 1

        bateria[0] -= movimiento
        print(f"Batería: {bateria}")
        print(f"Posición Actual: {posicion_Actual}")

        area[posicion_Actual[0]][posicion_Actual[1]] = 9
        for z in range(0, len(area[0])):
            print(area[z])
        area[posicion_Actual[0]][posicion_Actual[1]] = 0

        print()
    
    while bateria[0]>0:
        posicion_Actual[0] += 1
        bateria[0] -= movimiento
        print(f"Batería: {bateria}")
        print(f"Posición Actual: {posicion_Actual}")
        for z in range(0, len(area[0])):
            print(area[z])
        posicion_Actual[0] -= 1
        bateria[0] -= movimiento
        print(f"Batería: {bateria}")
        print(f"Posición Actual: {posicion_Actual}")
        for z in range(0, len(area[0])):
            print(area[z])

        print()

        if bateria[0] < 1:
            print("El robot a muerto, pero ha finalizado su tarea con exito.")
            break

    

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

            area[posicion_Actual[0]][posicion_Actual[1]] = 9
            for z in range(0, len(area[0])):
                print(area[z])
            area[posicion_Actual[0]][posicion_Actual[1]] = 0

            print()

            if cant_Basura == 0: break
        
            if bateria[0] < 1: break

    if bateria[0] < 1:
        print("La batería no fue suficiente para recoger toda la basura.")
        print("Lamentablemente el robot murió...")
        print(":'c")
        break

    if cant_Basura == 0: 
        print("Ta todo limpio :) ")
        Termino()
    cambio_Fila = 1


