# #region Pila_Pro
class Pila:
    """Implementación de una Pila usando el principio LIFO."""
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not self.items

    def push(self, item):
        # O(1) Amortizado
        self.items.append(item)

    def pop(self):
        # O(1)
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        """Ver el elemento superior sin sacarlo."""
        return self.items[-1]

# Uso del algoritmo: Invertir una palabra
def invertir_texto(texto):
    pila = Pila()
    for char in texto:
        pila.push(char)
    
    resultado = ""
    while not pila.esta_vacia():
        resultado += pila.pop()
    return resultado

print(invertir_texto("Estructura")) # arutcurtsE
# #endregion