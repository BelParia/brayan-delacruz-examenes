# Examen Práctico 02

## Ejercicio 1
"""
Reglas: -  Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas. - Calcular el promedio de cada estudiante. - Devolver un nuevo diccionario donde
la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor - Mostrar en pantalla el estudiante con mayor
promedio
"""


def procesar_notas(estudiantes):
    keys = list(estudiantes.keys())
    valores = list(estudiantes.values())

    pasa = "aprobado"
    no_pasa = "desaprobado"
    nuevo_diccionario = {}
    mayor_promedio = 0
    ganador = ""

    for i in range(len(keys)):
        notas = valores[i]
        resultado = sum(notas)
        promedio = resultado / len(notas)

        if promedio > 11:
            estado = pasa
        else:
            estado = no_pasa

        nuevo_diccionario[keys[i]] = {"promedio": promedio, "estado": estado}

        if promedio > mayor_promedio:
            mayor_promedio = promedio
            ganador = keys[i]

    print(f"El estudiante de mayor promedio es {ganador.capitalize()}, con una nota de {mayor_promedio}")
    print(f"\nEl nuevo diccionario es:\n{nuevo_diccionario}")

diccionario_prueba = {"brayan": [10, 11, 12], "carlos": [13, 14, 15], "mirian": [16, 17, 18]}

procesar_notas(diccionario_prueba)
