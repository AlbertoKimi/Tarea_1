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