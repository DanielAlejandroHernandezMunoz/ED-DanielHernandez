# DANIEL ALEJANDRO HERNANDEZ MUÑOZ #24100507
# Estructuras de Control 03/09/25

# Algoritmo:
# 1. Generar un numero aleatorio 
# 2. Iniciar un bucle # 3. Dentro del bucle preguntar al usuario un numero 
# 4. Mostrar un porcentaje de que tan cerca este del numero seguido de la palabra Frio o caliente según lo cerca que este 
# 5. Sí el usuario acierta reiniciar el juego.


import random
import os

NumeroTotalCasos = 100
NumeroAleatorio = random.randint(1, NumeroTotalCasos)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        entrada = input(
            "Adivina el número del 1 al 100 (o escribe 'SALIR' para terminar): "
        )

        # Caso especial para salir
        if entrada.strip().upper() == "SALIR":
            print("Saliendo del juego...")
            break

        NumeroPreguntado = int(entrada)
        diferencia = abs(NumeroAleatorio - NumeroPreguntado)
        porcentaje = 100 - int((diferencia / NumeroTotalCasos) * 100)

        if diferencia == 0:
            print("¡Correcto!...\n")
            NumeroAleatorio = random.randint(1, NumeroTotalCasos)
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        else:
            # Clasificación usando porcentaje
            if porcentaje >= 90:
                estado = " Muy caliente"
            elif porcentaje >= 70:
                estado = " Caliente"
            elif porcentaje >= 40:
                estado = " Tibio"
            elif porcentaje >= 10:
                estado = " Frío"
            else:
                estado = " Muy frío"

            print(f"Cercanía: {porcentaje}% → {estado}\n")

    except ValueError:
        print("Error: Por favor, ingresa solo números enteros.\n")
