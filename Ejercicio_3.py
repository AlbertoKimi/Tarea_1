"""
Problema 3. Trabajo con conjuntos
Escribe una función que reciba dos listas de enteros y devuelva un diccionario
con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
CALCULARLOS)
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto,
pero no en ambos).

"""

def conjuntos(lista1, lista2):

    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    resultado = {
        "interseccion": interseccion(conjunto1, conjunto2),
        "union": union(conjunto1, conjunto2),
        "diferencia_simetrica": diferencia_simetrica(conjunto1, conjunto2)
    }
    return resultado


"""
Funciones auxiliares para el ejercicio de conjuntos.

"""

def interseccion(conjunto1, conjunto2):
    return conjunto1&conjunto2

def union(conjunto1, conjunto2):
    return conjunto1|conjunto2

def diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1^conjunto2

"""
Ahora vamos a probar la función anterior

"""

lista1 = [1,6,8,8,3,5,9]
lista2 = [11,22,1,4,1,9,3]

resultado = conjuntos(lista1, lista2)
print(f"Diccionario con los resultados del ejercicio:", resultado)
