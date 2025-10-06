# Examen Final

## Ejercicio 2 , AQUÍ VAN LAS FUNCIONES (ES EL MODULO dX)
"""
Reglas: - Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones) - Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola. - Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola. - Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola. - Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)
"""

from random import randint

def crear_lista_aleatoria(x_numeros):
    try:
        if not isinstance(x_numeros, int):
            raise TypeError("El valor de x_numeros debe ser un número entero. Digira correctamente por favor")
        if x_numeros <= 0:
            raise ValueError("El número debe ser positivo. Digita correcatamente por favor")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []

    lista = []
    for i in range(x_numeros):
        numero_aleatorio = randint(1, 50)
        lista.append(numero_aleatorio)

