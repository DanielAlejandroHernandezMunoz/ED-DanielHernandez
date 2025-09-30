import random

"""
EXAMEN DANIEL ALEJANDRO HERNANDEZ MUÑOZ
EJERCICIO 1. LISTAS (15 PUNTOS)
Crea un programa que:
Reciba nombre de alumnos hasta que se escriba "FIN"
Guarde esos nombres en una lista.
Muestre la lista completa y cuantos alumnos se registraron.
"""

strAlumnos = input("Ingrese los nombres de los alumnos: ")
alumnos = [i for i in strAlumnos.split(",")]
totalAlumnos = 0
for j in alumnos:
    totalAlumnos = totalAlumnos + 1
    print(j)

print("Total Alumnos: " + str(totalAlumnos))

"""
Ejercicio 2 - Pila (15 Puntos)
Simula una pila de navegacion en un navegador web:
Inserta tres paginas web: "google.com", "wikipedia.org", "Openai.com"
2. El USuario presiona "volver" una vez
3. Muestra la página actual (la del tope de la pila).
"""

print("Ejercicio 2 - Ejemplo pila")
busquedas = ["google.com", "wikipedia.org", "Openai.com"]
print("Pagina actual: " + str(busquedas.pop()))

print("Accion volver x1: " + str(busquedas.pop()))

print("Accion volver x2: " + str(busquedas.pop()))


"""Ejercicio 3- Cola (15)Puntos
Simula una cola de impresion los documentos llegan en este orden "doc1.pdf"; "tarea.docx",
"presentacion.pptx"

atiende o elemina el primer documento en la cola
llega un nuevo documento informe .pdf
muestra la impresion final
"""

from collections import deque
cola = deque()
cola.append("doc1.pdf")
cola.append("tarea.docx")
cola.append("presentacion.pptx")

print("Ejercicio 3 - Cola(15 Puntos)")
print("Elementos en la cola:")

for elem in cola:
    print(str(elem))
print("Atender el primero:" + str(cola.popleft()))

print("Agregamos uno nuevo")
cola.append("informe.pdf")

print("Nuevos elementos en la cola: ")
for elem in cola:
    print(str(elem))




# ================================= PREGUNTAS TEORICAS ======================================
"""
EJERCICIO 4. Usaria busqueda binaria porque divide el campo de busqueda en la mitad varias veces y
eso haria que no tuviera que recorrer los 10000 numeros para encontrarla
"""

"""
Ejercicio 5:
 Porque ON es secuencial y O a la N duplica el mismo tiempo de busqueda 
que tiene ON²

ON se maneja con un ciclo, como una busqueda lineal
ON² Maneja 2 ciclos, como un ordenamiento burbuja
"""

"""
EJERCICIOS 6: Una lista de 100 numeros usaria bubble sort, ya que no son muchos numeros
y no requiere un algoritmo tan complejo como lo es mergesort, por el contexto no afectaria
en gran medida el tiempo en milisegundos que se tardaria.
"""

"""
Ejercicio 7: Hasta qué valor podrias calcular phibonacchi antes de que sea demasiado lento
y con la version iterativa?
"""

# =========================================================================================

"""Ejercicio 8. Deiseña un sistema que use diferentes estructuras de datos y algoritmos
para optimizar estas operaciones
busqueda de Usuarios por ID(100,000,000) usuarios
ordenamiento de productos por precio(100,000)
calculo de estadisticas en tiempo
"""

# DEFINICIONES:
def busqueda_binaria(lista, objetivo):
    """
    Busqueda binaria O(log n)
    """
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado, i, j = [], 0, 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i]); i += 1
        else:
            resultado.append(derecha[j]); j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# ============ ID USUARIOS:
IDlist = sorted(random.sample(range(1, 1000001),1000000))
objetivo = (500)

print("objetivo a buscar: 500")
print(str(busqueda_binaria(IDlist,objetivo+1)))


nuevalista = merge_sort(IDlist)
for element in nuevalista:
    print(str(element))

