"""
## Tarea

1. **Implementación:**
   Implementar una clase `ArbolAVL` y una clase `ArbolSplay` con inserción y recorrido inorden.

"""

class ArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class AVL():
    @staticmethod
    def altura(nodo):
        return nodo.altura if nodo else 0

    @staticmethod
    def rotacion_derecha(y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(AVL.altura(y.izq), AVL.altura(y.der))
        x.altura = 1 + max(AVL.altura(x.izq), AVL.altura(x.der))
        return x

    @staticmethod
    def rotacion_izquierda(x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(AVL.altura(x.izq), AVL.altura(x.der))
        y.altura = 1 + max(AVL.altura(y.izq), AVL.altura(y.der))
        return y

    @staticmethod
    def factor_balanceo(nodo):
        return AVL.altura(nodo.izq) - AVL.altura(nodo.der) if nodo else 0

    @staticmethod
    def insertar(raiz, valor):
        if not raiz:
            return ArbolBinario(valor)
        if valor < raiz.valor:
            raiz.izq = AVL.insertar(raiz.izq, valor)
        else:
            raiz.der = AVL.insertar(raiz.der, valor)

        raiz.altura = 1 + max(AVL.altura(raiz.izq), AVL.altura(raiz.der))
        fb = AVL.factor_balanceo(raiz)

        # Casos de rotación
        if fb > 1 and valor < raiz.izq.valor:
            return AVL.rotacion_derecha(raiz)
        if fb < -1 and valor > raiz.der.valor:
            return AVL.rotacion_izquierda(raiz)
        if fb > 1 and valor > raiz.izq.valor:
            raiz.izq = AVL.rotacion_izquierda(raiz.izq)
            return AVL.rotacion_derecha(raiz)
        if fb < -1 and valor < raiz.der.valor:
            raiz.der = AVL.rotacion_derecha(raiz.der)
            return AVL.rotacion_izquierda(raiz)

        return raiz

    @staticmethod
    def inorden(raiz):
        if raiz:
            AVL.inorden(raiz.izq)
            print(raiz.valor, end=' ')
            AVL.inorden(raiz.der)
    

class Splay(): 
    @staticmethod
    def rotacion_derecha(x):
        y = x.izq
        x.izq = y.der
        y.der = x
        return y

    @staticmethod
    def rotacion_izquierda(x):
        y = x.der
        x.der = y.izq
        y.izq = x
        return y

    @staticmethod
    def splay(raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz

        # Zig-Zig izquierda
        if valor < raiz.valor and raiz.izq:
            if valor < raiz.izq.valor:
                raiz.izq.izq = Splay.splay(raiz.izq.izq, valor)
                raiz = Splay.rotacion_derecha(raiz)
            elif valor > raiz.izq.valor:
                raiz.izq.der = Splay.splay(raiz.izq.der, valor)
                if raiz.izq.der:
                    raiz.izq = Splay.rotacion_izquierda(raiz.izq)
            return Splay.rotacion_derecha(raiz) if raiz.izq else raiz

        # Zig-Zig derecha
        if valor > raiz.valor and raiz.der:
            if valor > raiz.der.valor:
                raiz.der.der = Splay.splay(raiz.der.der, valor)
                raiz = Splay.rotacion_izquierda(raiz)
            elif valor < raiz.der.valor:
                raiz.der.izq = Splay.splay(raiz.der.izq, valor)
                if raiz.der.izq:
                    raiz.der = Splay.rotacion_derecha(raiz.der)
            return Splay.rotacion_izquierda(raiz) if raiz.der else raiz

        return raiz

# Ejemplo de uso
raiz_avl = None
valores = [10, 20, 30, 40, 50, 25]
for valor in valores:
    raiz_avl = AVL.insertar(raiz_avl, valor)
    
print("Recorrido inorden del árbol AVL:")
AVL.inorden(raiz_avl)

# Construir árbol para Splay usando inserciones y luego realizar accesos (splay)
raiz_splay = None
for valor in valores:
    raiz_splay = AVL.insertar(raiz_splay, valor)

for valor in valores:
    raiz_splay = Splay.splay(raiz_splay, valor)

print("\nÁrbol Splay después de accesos:")
AVL.inorden(raiz_splay)

