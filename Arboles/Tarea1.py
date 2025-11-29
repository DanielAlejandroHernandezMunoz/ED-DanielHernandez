"""
### **Actividad 1: Construcción**

Crea una clase Node con atributos data y children.
Construye un árbol que represente el sistema de carpetas:

```
Root
 ├── Documentos
 │    ├── Escuela
 │    └── Trabajo
 └── Imágenes
      ├── Vacaciones
      └── Familia
```

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def addChildren(self,children):
        self.children.append(children)
        
    def imprimirArbol(self, level=0):
        print(' ' * level * 4 + self.data)
        for child in self.children:
            child.imprimirArbol(level + 1)
            
# Construcción del árbol
root = Node("Root")

documentos = Node("Documentos")
imagenes = Node("Imágenes")

escuela = Node("Escuela")
trabajo = Node("Trabajo")
vacaciones = Node("Vacaciones")
familia = Node("Familia")

# Armando la jerarquía
root.addChildren(documentos)
root.addChildren(imagenes)

documentos.addChildren(escuela)
documentos.addChildren(trabajo)

imagenes.addChildren(vacaciones)
imagenes.addChildren(familia)

# Imprimir el árbol
root.imprimirArbol()