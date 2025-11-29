"""
### **Actividad 3**

Agrega un método a `NodoBinario` que calcule la **altura** del árbol:

```python
def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))

"""

class NodoBinario:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
        
A = NodoBinario("A")
A.left = NodoBinario("B")
A.right = NodoBinario("C")
A.left.left = NodoBinario("D")
A.left.right = NodoBinario("E")
A.right.right = NodoBinario("F")
def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.left), altura(nodo.right))

print("Altura del árbol:", altura(A))

