# Examen Final

## Ejercicio 4
"""
Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas: - Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos” - Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora - Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior. - Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados usando el decorador
implementado con un mínimo tres ejemplos.
"""

from datetime import datetime

def mostrar_hora_y_sumar(funcion):
    def datos_internos(*args, **kwards):
        ahora = datetime.now()
        hora = ahora.hour
        minuto = ahora.minute
        segundo = ahora.hour
        print(f"El decorador esta siendo ejecutado a las {hora} con {minuto} minutos y {segundo} segundos")

        suma_total = sum(args) + sum(kwards.values())
        print(f"La suma total de los valores es: {suma_total}")

        resultado = funcion(*args, **kwards)
        print(f"El resultado de la función decorada es {resultado}\n")
        return resultado
    return datos_internos

@mostrar_hora_y_sumar
def encontrar_mayor(*args, **kwards):
    todos_valores = list(args) + list(kwards.values())
    mayor = max(todos_valores)
    anote = f"El mayor valor es {mayor}"
    return anote

### USOS
print("Ejemplo 1:")
encontrar_mayor(10, 20, 30, 40, 50, 60)

print("Ejemplo 2:")
encontrar_mayor(5, 15, 25, value_7=35, value_8=45, value_9=55)

print("Ejemplo 3:")
encontrar_mayor(value_1=12, value_2=22, value_3=32, value_4=42, value_5=52, value_6=62, value_7=72)




