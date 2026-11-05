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


"""
Problema 2. Frecuencia de palabras en un texto.
Escribe una función que reciba por parámetro una lista de palabras y la ruta a
un fichero de texto y devuelva un diccionario que muestre cuantas veces
aparecen las dis􀆟ntas palabras de la lista en el fichero de texto. Haz un pequeño
programa que la ponga a prueba.
Requisitos:
1. Eliminar signos de puntuación y conver􀆟r todo a minúsculas.
2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.

"""

import string


def frecuencia_palabra(lista, ruta):
    conteo = {}

    with open(ruta, "r", newline='', encoding="utf-8") as f:
        for linea in f:
            linea = linea.lower()

            for signo in string.punctuation + "¿¡":
                linea = linea.replace(signo, "")

            palabras_linea = linea.split()

            for palabra in sorted(lista):
                palabra = palabra.lower()

                if palabra in palabras_linea:
                    if palabra in conteo:
                        conteo[palabra] += 1
                    else:
                        conteo[palabra] = 1
                else:
                    if palabra not in conteo:
                        conteo[palabra] = 0

    return conteo


"""
Ahora vamos a probar la función realizada con un ejemplo de texto que tenemos en esta 
carpeta llamado "texto.txt"

"""

lista_palabras = ["python", "estructura", "hola", "lenguaje", "programación"]
print(f"Diccionario con las palabras de la lista y cuantas veces aparecen en el texto:" , frecuencia_palabra(lista_palabras, "texto.txt"))

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
