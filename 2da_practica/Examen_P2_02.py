# Examen Práctico 02

## Ejercicio 2
"""
- Crear una función normalizar_nombres(nombres) - El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera - Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""

def normalizar_nombres(nombres):
    nombres_limpios = []

    for entrada in nombres:
        entrada = entrada.strip()
        partes = entrada.split()

        for nombre in partes:
            nombre_titulo = nombre.title()  # o podrías ser capitalize, pero como puede haber más de 1 nombre mejor ese.
            nombres_limpios.append(nombre_titulo)

    # Eliminar duplicados
    return list(set(nombres_limpios))

lista = ["  juan  ", "maria", "Carlos", "maria jose", "JUAN", "ana sofia"]
print(normalizar_nombres(lista))

# El orden no pude mantenerlo, pero lo demás si cumple

