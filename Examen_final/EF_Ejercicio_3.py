# Examen Final

## Ejercicio 3
"""
Reglas: - El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario. - Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente. - La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos” - La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""

from datetime import datetime

def conteo(funcion):
    def datos_internos(*args, **kwargs):
        cantidad = len(args) + len(kwargs)
        print(f"La cantidad de parámetros usados es {cantidad}")

        if cantidad <= 1:
            print("Error: La función requiere más de un parámetro para proceder con la lógica (los códigos Dx)")
            return None

        resultado = funcion(*args, **kwargs)

        print("La función fue ejecutada correctamente.\n")
        return resultado
    return datos_internos

@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    hora_actual = datetime.now()
    hora = hora_actual.hour
    minuto = hora_actual.minute

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"El alumno {nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos.")
    print(f"Su media de notas es {media:.2f}")

    return media

print("Primer caso:")
registrar_alumno("Brayan", 24, 15, 16, 17, 18)

print("Segundo caso:")
registrar_alumno("Roly", 23, 16, 17, 18, 19)
