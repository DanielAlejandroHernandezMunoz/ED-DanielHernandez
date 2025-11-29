"""
### **Actividad 2: Árbol binario**

Estructura visual:

        A
       / \
      B   C
     / \   \
    D   E   F


1. Implementa la clase `NodoBinario`.
2. Crea el árbol del ejemplo anterior (A–F).
3. Implementa e imprime los recorridos:

   * Preorden
   * Inorden
   * Postorden
"""

"""
 Preorden (Root → Left → Right)
 Inorden (Left → Root → Right)
 Postorden (Left → Right → Root)
"""

class NodoBinario:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def PreOrden(self):
        print(self.data, "")
        if self.left:
            self.left.PreOrden()
        if self.right:
            self.right.PreOrden()
    
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.data, "")
        if self.right:
            self.right.InOrder()
    
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.data, "")
        

A = NodoBinario("A")
A.left = NodoBinario("B")
A.right = NodoBinario("C")
A.left.left = NodoBinario("D")
A.left.right = NodoBinario("E")
A.right.right = NodoBinario("F")

print("Recorrido Inorden:")
A.InOrder()
print("Recorrido Postorden:")
A.PostOrder()
print("Recorrido Preorden:")
A.PreOrden()


"""
Otra forma valida:
def preorden(nodo):
    if nodo:
        print(nodo.dato, end=' ')
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

def PreOrden(nodo):
    if nodo:
        print(nodo.data, end=' ')
        PreOrden(nodo.left)
        PreOrden(nodo.right)
def InOrder(nodo):
    if nodo:
        InOrder(nodo.left)
        print(nodo.data, end=' ')
        InOrder(nodo.right)
def PostOrder(nodo):
    if nodo:
        PostOrder(nodo.left)
        PostOrder(nodo.right)
        print(nodo.data, end=' ')
print("Recorrido Inorden:")
InOrder(A)
print("\nRecorrido Postorden:")
PostOrder(A)
print("\nRecorrido Preorden:")
PreOrden(A)
"""