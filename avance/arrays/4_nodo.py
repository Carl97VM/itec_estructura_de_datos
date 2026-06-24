# #region Listas_Enlazadas_Python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None # El puntero al vecino

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None # El inicio de la lista

    def insertar_al_inicio(self, dato):
        # O(1)
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        # O(n)
        actual = self.cabeza
        while actual:
            print(f"[{actual.dato}] -> ", end="")
            actual = actual.siguiente
        print("None")

# Uso
lista = ListaEnlazada()
lista.insertar_al_inicio("Nodo C")
lista.insertar_al_inicio("Nodo B")
lista.insertar_al_inicio("Nodo A")
lista.recorrer() # [Nodo A] -> [Nodo B] -> [Nodo C] -> None
# #endregion