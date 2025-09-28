print("Python Módulo I - Parte práctica ")

# Ejercicio 2
"""2. Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15 
Cada curso tiene un peso diferente en la nota final: 
Matemáticas: 40%, Ciencia: 30%, Historia: 30% 
Realizar lo que se pide a continuación: 
Calcula la nota final ponderada del alumno. 
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal. 
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano: 
"¿Aprobado?: True" o "¿Aprobado?: Sí" 
Genera una cadena resumen que diga: 
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado" 
En caso no apruebe indicar lo contrario en los mensajes."""

nota_mate = 14
nota_ciencia = 16
nota_historia = 11
calculo_nota = (nota_mate*(40/100)) + (nota_ciencia*(30/100)) + (nota_historia*(30/100))
print(f"La nota final es {calculo_nota}")
if calculo_nota >= 13.0:
    calculo_nota_bool = True
    print(f"El estudiante obtuvo una nota final de {calculo_nota}. El estado final del estudiante es ¿aprobado?: {calculo_nota_bool}")
else:
    calculo_nota_bool = False
    print(f"El estudiante obtuvo una nota final de {calculo_nota}. El estado final del estudiante es ¿aprobado?: {calculo_nota_bool}")

