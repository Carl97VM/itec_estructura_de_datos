class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None ## Que el puntero esperara al siguiente elemento

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

## Tarea para el 19/03/2026
## Cuando ya no haya elementos no mostrar el none (bracito para el siguiente dato)

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar_al_final(10)
    lista.agregar_al_final(20)
    lista.agregar_al_final(30)
    lista.mostrar()