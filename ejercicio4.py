# Ejercicio 4 #
'''
Programa que declare una lista y la vaya llenando de núemros hasta que introducimos un número negativo.
Entonces se debe imprmir el vector (sólo los elementos introducidos)
'''
def listanumeronegativo():
    lst = []
    try:
        while(True):
            cadena = input("Dime una cadena de números:")
            print(cadena)
            num = int(cadena)
            if(num< 0):
                return lst
            else:
                lst.append(num)
    except:
        print("Tiene que ser un número")
