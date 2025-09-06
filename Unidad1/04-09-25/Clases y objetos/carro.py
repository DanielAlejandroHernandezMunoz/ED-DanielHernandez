# DANIEL ALEJANDRO HERNANDEZ MUÑOZ #24100507
# Estructuras de datos 04/09/25
# Crear una clase Coche con atributos (marca, modelo, velocidad)
# y métodos (acelerar, frenar).

class Carro:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def Acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Velocidad actual: {self.velocidad}")

    def Frenar(self):
        self.velocidad = 0
        print(f"Velocidad actual: {self.velocidad}")


miCarro = Carro("Toyota", "Corolla")
miCarro.Acelerar(10) 
miCarro.Acelerar(20)
miCarro.Frenar()
print("Fin del programa")