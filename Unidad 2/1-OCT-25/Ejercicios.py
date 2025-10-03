import os
"""
Ejercicio 1  Diccionario básico

Crea un diccionario llamado `alumno` con las claves: `nombre`, `edad`, `carrera`.
Imprime cada clave y valor en formato:
`nombre: Ana`
"""
def Ejercicio1():
    print()
    alumno = {}
    alumno["Nombre"] = "Ana"
    alumno["Edad"] = 20 
    alumno["Carrera"] = "ing en sistemas"
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")



"""
Ejercicio 2 Conteo de palabras

Escribe un programa que reciba una cadena y cuente la frecuencia de cada palabra usando un diccionario.
"""
def Ejercicio2():
    texto = "hola mundo hola python mundo"

    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    print(frecuencia)

"""
Ejercicio 3 Agenda telefónica

Crea un programa que permita:
1. Agregar un contacto (`nombre` → `número`).
2. Buscar un contacto por nombre.
3. Eliminar un contacto.
"""
def Ejercicio3():
    print("Ejercicio 3. Agenda telefonica")
    contactos = {} 

    def ImprimirContactos():
        for clave, valor in contactos.items():
            print(clave, valor)



    while True:
        opcion = input("¿Desea agregar un nuevo contacto? (Y/N): ")
        match opcion:
            case "Y" | "y":
                nombre = input("Ingrese el nombre del contacto a agregar: ")
                numero = input("Ingrese el número de la persona: ")
                contactos[nombre] = numero
                print(f"Contacto agregado: {nombre} → {numero}")
            case "N" | "n":
                break
            case _:
                print("Ingrese unicamente Y o N")

    while True:
        opcion = input("¿Desea buscar un número de telefono por nombre? (Y/N): ")
        match opcion:
            case "Y" | "y":
                nombre = input("Ingrese el nombre de la persona a buscar: ")
                if nombre in contactos:
                    print(f"{nombre}: {contactos[nombre]}")
                else:
                    print("Ese contacto no existe.")
            case "N" | "n":
                break
            case _:
                print("Ingrese unicamente Y o N")
    while True:
        opcion = str(input("Desea eleminar un contacto (Y/N): "))
        match opcion:
            case "Y" | "y":
                nombre = input("Ingrese el nombre de la persona a eleminar:")
                if(nombre in contactos):
                    del contactos[nombre]
                    print("Contacto eleminado correctamente")
                    ImprimirContactos()
                else:
                    print("El contacto no existe")
            case "N"| "n": break
    while True:
        opcion = str(input("Desea ver los contactos(Y/N): "))
        match opcion:
            case "Y" | "y": ImprimirContactos()
            case "N" | "n": break
    
"""Ejercicio 4 -  Diccionario con listas

Crea un diccionario que guarde materias y las calificaciones del alumno:
Calcula el promedio por materia. """

def Ejercicio4(): 
    print("Ejercicio 4 - Diccionario con listas")

    calificaciones = {    
        "Matemáticas": [90, 85, 88],
        "Programación": [100, 95, 97],
    }

    for materia, notas in calificaciones.items():
        promedio = sum(notas) / len(notas)
        print(f"Promedio {materia}: {promedio}")


"""### Ejercicio 5  Uso de `collections.Counter`"""

def Ejercicio5():
    from collections import Counter

    texto = "python java python c c c java"
    frecuencia = Counter(texto.split())
    print(frecuencia)



"""
Crea un programa que permita:

* Registrar productos con su nombre como clave y cantidad como valor.
* Vender un producto (disminuir la cantidad).
* Mostrar inventario actualizado.
* Evitar vender productos inexistentes.

Ejemplo de uso:

```
Inventario inicial: {"manzanas": 10, "peras": 5}
Vender("manzanas", 3) → {"manzanas": 7, "peras": 5}
Vender("naranjas", 2) → "Producto no encontrado"
```
"""
def Ejercicio6():
    def registrarProducto(diccionario):
        producto = input("Ingrese el nombre del producto: ")
        if producto not in diccionario:
            cantidad = int(input("Ingrese la cantidad a agregar del producto: "))
            diccionario[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")
        else:
            print("Ese producto ya existe en el inventario.")

    def venderProducto(diccionario):
        producto = input("Ingrese el producto a vender: ")
        if producto in diccionario:
            cantidad_actual = diccionario[producto]
            cantidad_vender = int(input("Ingrese la cantidad del producto: "))
            if cantidad_vender <= cantidad_actual:
                diccionario[producto] -= cantidad_vender
                print(f"Se vendieron {cantidad_vender} unidades de {producto}.")
            else:
                print(f"No hay suficiente cantidad de {producto}.")
                print(f"Cantidad actual: {cantidad_actual}")
                print(f"Cantidad a vender: {cantidad_vender}")
        else:
            print("El producto no se encuentra en el inventario.")


    Inventario = {}
    print("EJERCICIO 7")
    while True:
        print("Teclee [1] para registrar un producto")
        print("Teclee [2] para vender un producto")
        print("Teclee [3] Para ver el inventario")
        print("Teclee [4] para salir del programa")
        opcion = input()
        match int(opcion):
            case 1:
                registrarProducto(Inventario)
            case 2:
                venderProducto(Inventario)
            case 3: 
                for clave, valor in Inventario.items():
                    print("producto: "clave + " cantidad: " + str(valor))
            case 4: break

# ===========================================================================================

while True:
    print("teclee del [1],[2]...[6] para seleccionar un ejercicio")
    print("teclee [9] para salir del programa")
    opcion = int(input())
    print()
    match opcion:
        case 1: Ejercicio1()
        case 2: Ejercicio2()
        case 3: Ejercicio3()
        case 4: Ejercicio4()
        case 5: Ejercicio5()
        case 6: Ejercicio6()
        case 9: break
    input("Ingrese cualquier tecla para continuar")
    os.system("clear")
