# Función que reciba una lista y devuelva su promedio.
# DANIEL ALEJANDRO HERNANDEZ MUÑOZ #24100507
# Estructuras de datos 04/09/25
# Definición y llamada de funciones.
# Parámetros y retorno de valores.
# Alcance de variables (globales vs. locales).

def CalcularPromedio(Calificaciones):
    Promedio = 0 
    for i in Calificaciones:
        Promedio += i 
    return Promedio / len(Calificaciones)

print("Calificaciones Alumnos")
strCalificaciones = input("Ingrese las calificaciones separadas por comas Ejemplo: 1,2,4: ")
calificaciones = [int(i) for i in strCalificaciones.split(",")]
print(f"El Promedio de las calificaciones ingresadas es: {CalcularPromedio(calificaciones)}")