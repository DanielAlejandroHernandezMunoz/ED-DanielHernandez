from abc import ABC, abstractmethod

# ===================================================================================================
# Clase abstracta e interfaz
# ===================================================================================================
class GestionBiblioteca(ABC):
    @abstractmethod
    def prestarLibro(self, libro, usuario):
        pass

    @abstractmethod
    def devolverLibro(self, libro):
        pass

# ===================================================================================================
# Clase Libro
# ===================================================================================================
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__prestado = False

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    def estaPrestado(self):
        return self.__prestado

    def prestar(self):
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

# ===================================================================================================
# Clase Usuario
# ===================================================================================================
class Usuario:
    def __init__(self, nombre, idUsuario):
        self.__nombre = nombre
        self.__idUsuario = idUsuario

    def getNombre(self):
        return self.__nombre

    def getIdUsuario(self):
        return self.__idUsuario

# ===================================================================================================
# Clase Biblioteca
# ===================================================================================================
class Biblioteca(GestionBiblioteca):
    def __init__(self):
        self.__libros = []

    def VerLibros(self):
        if not self.__libros:
            print("No hay libros registrados.")
            return
        print("\n--- LISTA DE LIBROS ---")
        for libro in self.__libros:
            estado = "Prestado" if libro.estaPrestado() else "Disponible"
            print(f"{libro.getTitulo()} - {libro.getAutor()} ({libro.getIsbn()}) [{estado}]")

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def buscarLibroPorIsbn(self, isbn):
        for l in self.__libros:
            if l.getIsbn() == isbn:
                return l
        return None

    def prestarLibro(self, libro, usuario):
        if libro is None or usuario is None:
            print("Libro o usuario inválido.")
            return
        if libro.estaPrestado():
            print(f"El libro '{libro.getTitulo()}' ya está prestado.")
        else:
            libro.prestar()
            print(f"El libro '{libro.getTitulo()}' ha sido prestado a {usuario.getNombre()}.")

    def devolverLibro(self, libro):
        if libro is None:
            print("Libro no encontrado.")
            return
        if libro.estaPrestado():
            libro.devolver()
            print(f"El libro '{libro.getTitulo()}' ha sido devuelto.")
        else:
            print(f"El libro '{libro.getTitulo()}' no estaba prestado.")

# =================================================================================================
# Aplicación
# =================================================================================================
def mostrar_menu():
    print("\n===== MENÚ BIBLIOTECA =====")
    print("1. Ver libros")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")
    return input("Elige una opción: ").strip()

def buscar_usuario(usuarios, id_usuario):
    for u in usuarios:
        if u.getIdUsuario() == id_usuario:
            return u
    return None

if __name__ == "__main__":
    biblioteca = Biblioteca()
    usuarios = [
        Usuario("Juan Pérez", 1),
        Usuario("María López", 2)
    ]

    biblioteca.agregarLibro(Libro("1984", "George Orwell", "123456789"))
    biblioteca.agregarLibro(Libro("Cien años de soledad", "Gabriel García Márquez", "987654321"))

    while True:
        opcion = mostrar_menu()

        match opcion:
            case "1":
                biblioteca.VerLibros()

            case "2":
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                isbn = input("ISBN: ").strip()
                if titulo and autor and isbn:
                    if biblioteca.buscarLibroPorIsbn(isbn):
                        print("Ya existe un libro con ese ISBN.")
                    else:
                        biblioteca.agregarLibro(Libro(titulo, autor, isbn))
                        print(f"Libro '{titulo}' agregado correctamente.")
                else:
                    print("Datos incompletos.")

            case "3":
                biblioteca.VerLibros()
                isbn = input("ISBN del libro a prestar: ").strip()
                try:
                    user_id = int(input("ID del usuario (1=Juan, 2=María): ").strip())
                except ValueError:
                    print("ID inválido.")
                    continue
                libro = biblioteca.buscarLibroPorIsbn(isbn)
                usuario = buscar_usuario(usuarios, user_id)
                if libro and usuario:
                    biblioteca.prestarLibro(libro, usuario)
                else:
                    print("Libro o usuario no encontrado.")

            case "4":
                biblioteca.VerLibros()
                isbn = input("ISBN del libro a devolver: ").strip()
                libro = biblioteca.buscarLibroPorIsbn(isbn)
                if libro:
                    biblioteca.devolverLibro(libro)
                else:
                    print("Libro no encontrado.")

            case "5":
                print("Fin del Programa.")
                break

            case _:
                print("Opción no válida, intenta de nuevo.")
