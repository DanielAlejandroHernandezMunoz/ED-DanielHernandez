# DANIEL ALEJANDRO HERNANDEZ MUÑOZ #24100507
# Estructuras de datos 04/09/25
# Crear una clase Coche con atributos (marca, modelo, velocidad)
# y métodos (acelerar, frenar).
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def MostrarInformacion(self):
        print(f"Libro registrado => Título: {self.titulo}, Autor: {self.autor}")


strTitulo = input("Ingrese el nombre del libro: ")
strAutor = input("Ingrese el nombre del Autor: ")

unLibro = Libro(strTitulo, strAutor)
unLibro.MostrarInformacion()
print("Fin del programa")