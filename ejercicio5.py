import random
# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y 
posterior ordene los elementos de menor a mayor
'''
def listaAleatoria():
    lst = []
    for i in range(0,10):
        lst.append(random.randint(0,10))
    return lst
  
def ordenaLista(lst):
    lst.sort()
    return lst
  
def ejercicio5():
    lst = listaAleatoria()
    print(ordenaLista(lst))
