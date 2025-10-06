# Examen Final

## Ejercicio 1
"""
Reglas:
• Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(anio_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.
• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos
o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido.
"""

### Clase de Persona
class Persona:
    def __init__(self, nombre, edad, nacionalidad = "peruana", saldo =0.0):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def actualizar_nombre(self, nombre):
        self.nombre = nombre
        print(f"Ahora el nombre es {nombre}")

    def actualizar_edad(self, edad):
        self.edad = edad
        if edad > 0:
            print(f"La edad actualizada es {edad}")
        else:
            print("Este número no tiene sentido a nivel biológico")

    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido años. La edad actual es {self.edad}")

    def mostrar_saldo(self):
        print(f"El saldo que tiene actualmente es S/ {self.saldo:.2f}")

    def transferir(self, destino, monto=0):
        if monto <= 0:
            print("El monto no puede ser negativo, digita correctamente por favor.")
        elif self.saldo < monto:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto
            destino.saldo += monto
            print(f"Transferencia realizada: S/ {monto:.2f} de {self.nombre} a {destino.nombre}")

### Clase de Empleado, considerando la Herencia

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, nacionalidad = "peruana", saldo =0.0):
        super().__init__(nombre, edad, nacionalidad, saldo)
        self.sueldo = sueldo

    def aumento_sueldo(self, porcentaje = 0.30):
        incrementar = self.sueldo * porcentaje
        self.sueldo += incrementar
        print(f"El sueldo actualizado (por el aumento de {porcentaje*100}%) de {self.nombre} es de S/ {self.sueldo:.2f}")

    def prediccion(self, anio_objetivo, edad_param = None):
        anio_actual = 2025
        diferencia_anios = anio_objetivo - anio_actual

        if edad_param is not None and edad_param < self. edad:
            print("No es posible realizar la operación")
            return

        if edad_param is not None:
            edad_futura = edad_param
        else:
            edad_futura = self.edad + diferencia_anios
        print(f"En el año {anio_objetivo} tendrá {edad_futura} años")

### Respecto a las pruebas

empleado1 = Empleado("Brayan", 25, 2500, "peruana",saldo=500)
empleado2 = Empleado("Rosa", 30, 3500, "peruana",saldo=200)

empleado1.aumento_sueldo(0.10)
empleado1.aumento_sueldo()
print(f"Sueldo final de {empleado1.nombre}: S/ {empleado1.sueldo:.2f}\n")

empleado1.mostrar_saldo()
empleado2.mostrar_saldo()

empleado1.transferir(empleado2, 300)  ### para transferir
empleado2.transferir(empleado1, 1000)

empleado1.prediccion(2030)             # sin edad_param
empleado1.prediccion(2030, edad_param=20)  # con edad_param inválido

