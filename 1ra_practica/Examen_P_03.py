print("Python Módulo I - Parte práctica ")

# Ejercicio 3
"""3. Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante, 
el porcentaje de propina que desea dejar el cliente y el número de personas que 
dividirán la cuenta. El programa debe mostrar: 
El monto total con propina. 
El monto que debe pagar cada persona (con 2 decimales). 
Un mensaje será personalizado, indicará si el monto individual supera los 100 
soles, mostrando un mensaje de advertencia si es el caso. 
Entrada esperada (por input): 
Total de la cuenta: float 
Porcentaje de propina: float 
Número de personas: int 
Salida ejemplo (output): 
Monto total con propina: S/. 230.00 
Cada persona debe pagar: S/. 115.00 
¡Advertencia! El monto por persona supera los S/. 100
"""

numero_personas = 4
cuenta_sin_propina = 124.50
total_cuenta = numero_personas * cuenta_sin_propina
porcentaje_propina = 0.1
total_mas_propina = total_cuenta + (total_cuenta*porcentaje_propina)
cuenta_personal = total_mas_propina/numero_personas
print(f"Monto total con propina: S/. {total_mas_propina:.2f}")
print(f"Cada persona debe pagar: S/. {cuenta_personal}")
if cuenta_personal > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
else:
    print("Trate de no superar los S/. 100")

