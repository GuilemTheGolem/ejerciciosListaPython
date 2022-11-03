import random
# Ejercicio 9 #

'''
Implementar la siguientes funciones 
        - sumaVector(<Lista>) devuelve <Entero>.
        - sumaVectorDeVector(<Lista>) devuelve <Entero>.
        
      
              
'''

# Dado una lista con números enteros devolver la suma de todos ellos por ejemplo:
              # sumaVector([1,2,3]) -->  6
              # sumaVector([3,4]) --> 7



# Dado una lista con listas de números enteros devolver la suma de todos ellos por ejemplo:
              # sumaVectorDeVector([[1,2],[3,4],[5,6,7]]) --> 28


lst = [0, 1, 3, 5]
def sumaLista(lst):
    sumaTotal = 0
    for i in lst:
        sumaTotal = sumaTotal + i
    return sumaTotal
        
    


      
              

def generarListaRandom():
    lst = []
    for i in range(0,random.randint(0,10)):
        lst.append(random.randint(0, 50))
    return lst

def generarListadeListaRandom():
    lst = []
    for i in range(0, random.randint(0,5)):
        lst.append(generarListaRandom())
    return lst


def sumaVector(lst):
 
    sumaTotal = 0
    for i in range(0, len(lst)):
    
        sumaTotal = sumaTotal + lst[i]
   
    return sumaTotal



def sumaVectorDeVector(lst):
    resultado = 0
    
    for i in lst:
        resultado = resultado + sumaVector(i)
    
    return resultado
