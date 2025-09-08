# Daniel Alejandro Hernandez Muñoz
# Examen de diagnostico 2.
# 24100507 Estructuras de datos
# mi error fué utilizar __ por mera inercia, alparecer tiene un uso detras en python
#  en su sintaxis del cual desconozco
class Rectangulo:
    def __init__(self, intAncho, intAltura):
        self._intAncho = intAncho  
        self._intAltura = intAltura

    def CalcularArea(self):
        return self._intAncho * self._intAltura

    def CalcularPerimetro(self):
        return 2 * self._intAncho + 2 * self._intAltura

    def MostrarDimensiones(self):
        return f"Alto: {self._intAltura} cm, Ancho: {self._intAncho} cm"


class Cuadrado(Rectangulo):
    def __init__(self, intLado):
        super().__init__(intLado, intLado)

    def MostrarDimensiones(self):
        return f"El tamaño del lado del Cuadrado es {self._intAncho} cm"

unRectangulo = Rectangulo(4, 5)
print(f"El Área es: {unRectangulo.CalcularArea()}")
print(f"El Perímetro es: {unRectangulo.CalcularPerimetro()}")
print(f"Las dimensiones son: {unRectangulo.MostrarDimensiones()}")

unCuadrado = Cuadrado(4)
print(f"El Área es: {unCuadrado.CalcularArea()}")
print(f"El Perímetro es: {unCuadrado.CalcularPerimetro()}")
print(f"Las dimensiones son: {unCuadrado.MostrarDimensiones()}")
