# DANIEL ALEJANDRO HERNANDEZ MUÑOZ #24100507
# Estructuras de Control 03/09/25
# Números Primos
try:
    # Ingresar los números separados por comas
    NumerosPreguntados = input("Ingrese los números separados por comas: ")

    # Convertir los numeros preguntados en un vector
    numeros = [int(x) for x in NumerosPreguntados.split(",")]

    for numero in numeros:
        if numero > 1:
            es_primo = True
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(f"{numero} es primo.")
            else:
                print(f"{numero} no es primo.")
        else:
            print(f"{numero} no es primo.")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros separados por comas")