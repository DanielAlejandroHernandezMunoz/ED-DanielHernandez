"""
Actividad 1: Construcción

Crea una clase Node con atributos data y children. Construye un árbol que represente el sistema de carpetas:

Root
 ├── Documentos
 │    ├── Escuela
 │    └── Trabajo
 └── Imágenes
      ├── Vacaciones
      └── Familia

Implementa un método print_tree() para mostrarlo jerárquicamente.
"""

class Nodo:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        print("  " * level + self.data)
        for child in self.children:
            child.print_tree(level + 1)
                
                
                            
        



root = Nodo("Root")
documentos = Nodo("Documentos")
escuela = Nodo("Escuela")
trabajo = Nodo("Trabajo")
imagenes = Nodo("Imágenes")
vacaciones = Nodo("Vacaciones")
familia = Nodo("Familia")

root.add_child(documentos)
documentos.add_child(escuela)
documentos.add_child(trabajo)
root.add_child(imagenes)
imagenes.add_child(vacaciones)
imagenes.add_child(familia)
root.print_tree()

"""
ACTIVIDAD 2:
    Implementa la clase NodoBinario.
    Crea el árbol del ejemplo anterior (A–F).
    Implementa e imprime los recorridos:
        Preorden
        Inorden
        Postorden
 """
class NodoBinario:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Preorden: raíz → izquierda → derecha
    def preorder(self):
        if self:
            print(self.data, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    # Inorden: izquierda → raíz → derecha
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right:
                self.right.inorder()

    # Postorden: izquierda → derecha → raíz
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data, end=' ')

    # Altura del árbol
    def altura(self):
        izquierda = self.left.altura() if self.left else 0
        derecha = self.right.altura() if self.right else 0
        return 1 + max(izquierda, derecha)


# -----------------------------
# Construir árbol A–F
A = NodoBinario("A")
B = NodoBinario("B")
C = NodoBinario("C")
D = NodoBinario("D")
E = NodoBinario("E")
F = NodoBinario("F")

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

# -----------------------------
# Demostración de recorridos e altura
print("Preorden:")
A.preorder()  # Salida: A B D E C F

print("\nInorden:")
A.inorder()   # Salida: D B E A C F

print("\nPostorden:")
A.postorder() # Salida: D E B F C A

"""ACTIVIDAD 3 ALTURA DEL ARBOL. """
print("\nAltura del árbol:", A.altura())  # Salida: 3
