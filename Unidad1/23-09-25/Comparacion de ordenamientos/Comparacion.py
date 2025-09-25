import random, time

# ================== Algoritmos ==================

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

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

# ================== Utilidad ==================

def medir_tiempo(func, datos):
    copia = datos[:]
    inicio = time.time()
    resultado = func(copia)
    if resultado is not None:
        copia = resultado
    tiempo = time.time() - inicio
    return tiempo

# ================== Ejecución ==================

dimensiones = [100, 500, 1000]

print("=== Comparación Bubble vs Merge ===\n")
for n in dimensiones:
    datos = random.sample(range(n*10), n)
    t_bubble = medir_tiempo(bubble_sort, datos)
    t_merge  = medir_tiempo(merge_sort,  datos)
    print(f"Dimensión: {n}")
    print(f"  Bubble Sort : {t_bubble:.4f} s")
    print(f"  Merge Sort  : {t_merge:.4f} s")
    if t_merge > 0:
        print(f"  Relación    : {t_bubble/t_merge:.1f}x")
    print("-"*30)

# Escenarios específicos n=1000
print("\n=== Escenarios especiales (n=1000) ===\n")
escenarios = {
    "Ordenado"     : list(range(1000)),
    "Inverso"      : list(range(1000, 0, -1)),
    "Casi ordenado": [x if x % 100 != 0 else x + 500 for x in range(1000)],
}

for nombre, datos in escenarios.items():
    t_bubble = medir_tiempo(bubble_sort, datos)
    t_merge  = medir_tiempo(merge_sort,  datos)
    print(f"Escenario: {nombre}")
    print(f"  Bubble Sort : {t_bubble:.4f} s")
    print(f"  Merge Sort  : {t_merge:.4f} s")
    if t_merge > 0:
        print(f"  Relacion    : {t_bubble/t_merge:.1f}x")
    print("-"*30)
