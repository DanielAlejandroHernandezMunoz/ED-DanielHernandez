import time
import random

# =========================================
# Definiciones
# =========================================

def busqueda_lineal(lista, objetivo):
    """
    Busqueda lineal O(n)
    Retorna la posición del elemento o -1 si no existe
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

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

def EjecutarAmbas(lista, objetivo):
    """
    Ejecuta ambos y mide los tiempos de ejecución
    """
    inicio_lineal = time.time()
    busqueda_lineal(lista, objetivo)
    tiempo_lineal = time.time() - inicio_lineal

    inicio_binaria = time.time()
    busqueda_binaria(lista, objetivo)
    tiempo_binaria = time.time() - inicio_binaria

    print(f"Lista de {len(lista):,} elementos")
    print(f"Objetivo: {objetivo}")
    print(f"Búsqueda lineal : {tiempo_lineal:.6f} s")
    print(f"Búsqueda binaria: {tiempo_binaria:.6f} s")
    if tiempo_binaria > 0:
        print(f"La binaria es ~{tiempo_lineal/tiempo_binaria:.0f} veces más rápida\n")
    else:
        print()

# ==================================================================================
# EJECUCION
# ==================================================================================

Rangos = [1000, 10000, 50000, 100000]

for rango in Rangos:
    lista = list(range(rango))  
    objetivos_dentro = random.sample(lista, 5)           
    objetivos_fuera = random.sample(range(rango, rango*2), 5)  

    print(f"\n==== RANGO {rango} ====")
    print(f"Objetivos dentro: {objetivos_dentro}")
    print(f"Objetivos fuera : {objetivos_fuera}\n")

    for objetivo in objetivos_dentro + objetivos_fuera:
        EjecutarAmbas(lista, objetivo)
