# /*
# Este es el salto a estructuras jerárquicas y relacionales.

# Ejercicio 4: Verificación de Árbol de Búsqueda Binaria (BST)
# Problema: Dado un nodo raíz, determina si el árbol cumple la propiedad de BST (hijo izquierdo < padre < hijo derecho).
# */

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def es_bst_valido(nodo, limite_inf=float('-inf'), limite_sup=float('inf')):
    if not nodo:
        return True
    
    if not (limite_inf < nodo.valor < limite_sup):
        return False
        
    return (es_bst_valido(nodo.izq, limite_inf, nodo.valor) and 
            es_bst_valido(nodo.der, nodo.valor, limite_sup))

# Por qué: Los árboles son la base de los sistemas de archivos (carpetas) 
# y de las bases de datos indexadas.