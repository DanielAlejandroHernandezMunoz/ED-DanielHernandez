
# DANIEL ALEJANDRO HERNANDEZ MUÑOZ #24100507
# Estructuras de datos 04/09/25
# Definición y llamada de funciones.
# Parámetros y retorno de valores.
# Alcance de variables (globales vs. locales).

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

operaciones = {
    "Sumar": sumar,
    "Restar": restar,
    "Multiplicar": multiplicar,
    "Dividir": dividir
}

print("Calculadora de suma de 2 Numeros")
str_operacion = input("Escriba la instrucción a realizar [Sumar].[Restar],[Multiplicar],[Dividir]: ")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if str_operacion in operaciones:
    resultado = operaciones[str_operacion](a, b)
    print(f"El resultado de {str_operacion} es: {resultado}")
else:
    print("Operación no válida.")