"""
Problema 1. Procesamiento de una lista de enteros.
Crea una función que reciba una lista de enteros por parámetro y devuelva otra
lista, de acuerdo a las siguientes acciones:
1. Eliminar los números nega􀆟vos de la lista.
2. Eliminar los valores que están repe􀆟dos, quedándonos con uno de ellos.
3. Ordenar los números resultantes de menor a mayor.
Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4].

"""

def lista_enteros(lista):
    positivos = [e for e in lista if e >= 0]
    sin_repetidos = list(set(positivos))
    sin_repetidos.sort()
    return sin_repetidos

"""
Ahor voy a poner un ejemplo para vér si funciona correctamente la función:

"""

lista = [2, 1, 8, 0, -4, 2, -5, 1, 8, 11, -6]
resultado =lista_enteros(lista)
print(f"La lista ordenada, sin repetidos y sin negativos es:" , resultado)