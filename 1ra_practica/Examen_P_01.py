print("Python Módulo I - Parte práctica ")

# Ejercicio 1
"""Reglas: - Asignar en variables los datos de tu nombre, salario, edad y compañía para un 
usuario e identificar sus tipos de variables - Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una 
conversión de datos - Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted 
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted 
tiene un bono del 5% en el mes diciembre” - Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su 
salario, según corresponda. """

nombre = "Brayan de la Cruz" # no escribí mi nombre completo
salario = 1400
edad = "24"
compania = "Covicho Lab"
bono_final = pow(salario, 2) + ((5/100)*salario)
if int(edad) > 30:
    print(f"Usted, {nombre}, tiene un bono del 10% en el mes de diciembre")
else:
    print(f"Usted, {nombre}, tiene un bono del 5% en el mes diciembre")
print(f"El bono final que recibe es {bono_final}")



