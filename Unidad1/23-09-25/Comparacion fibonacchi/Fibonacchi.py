import time

# ================== DEFINICIONES ==================

def FibonacciRecursivo(N):
    if N <= 1:
        return N
    return FibonacciRecursivo(N - 1) + FibonacciRecursivo(N - 2)

def FibonacciIterativo(N):
    if N <= 1:
        return N
    ValorAnterior, ValorActual = 0, 1
    for _ in range(2, N + 1):
        ValorAnterior, ValorActual = ValorActual, ValorAnterior + ValorActual
    return ValorActual

def MedirTiempo(Funcion, *Args):
    Inicio = time.time()
    Resultado = Funcion(*Args)
    Tiempo = time.time() - Inicio
    return Resultado, Tiempo

# ================== Ejecución ==================

ValoresPrueba = [5, 10, 20, 30, 35, 40, 50, 1000]

print("=== Comparación de Fibonacci (Recursivo vs Iterativo) ===\n")

for Numero in ValoresPrueba:
    print(f"N = {Numero}")

    ResultadoIterativo, TiempoIterativo = MedirTiempo(FibonacciIterativo, Numero)

    if Numero <= 40:
        ResultadoRecursivo, TiempoRecursivo = MedirTiempo(FibonacciRecursivo, Numero)
        print(f"  Recursivo : {ResultadoRecursivo}   ({TiempoRecursivo:.6f} s)")
    else:
        ResultadoRecursivo = None
        TiempoRecursivo = None
        print("  Recursivo : demasiado lento (>40)")

    print(f"  Iterativo : {ResultadoIterativo}   ({TiempoIterativo:.6f} s)")
    print("-" * 50)
