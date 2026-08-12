"""
Ejercicio 1: Lista enlazada con nodos

Objetivo:
- Practicar el uso de nodos en una estructura de datos lineal.
- Implementar operaciones típicas sobre listas enlazadas simples.

Requisitos:
1. Crear la clase Nodo con los atributos: valor y siguiente.
2. Crear la clase ListaEnlazada con:
   - agregar(valor): agrega al final.
   - insertar_inicio(valor): inserta al inicio.
   - eliminar(valor): elimina la primera aparición.
   - buscar(valor): devuelve True si existe.
   - mostrar(): imprime los elementos en orden.
   - longitud(): devuelve la cantidad de elementos.
3. Probar el comportamiento con un menú interactivo.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.valor == valor:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, valor):
        actual = self.cabeza
        while actual is not None:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        print("Lista enlazada:", " -> ".join(elementos))

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador


def menu():
    lista = ListaEnlazada()
    while True:
        print("\n=== Ejercicio de Nodos / Lista Enlazada ===")
        print("1. Agregar al final")
        print("2. Insertar al inicio")
        print("3. Eliminar un valor")
        print("4. Buscar un valor")
        print("5. Mostrar lista")
        print("6. Longitud de la lista")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            valor = input("Ingrese el valor a agregar: ")
            lista.agregar(valor)
            print("Valor agregado al final.")
        elif opcion == "2":
            valor = input("Ingrese el valor a insertar al inicio: ")
            lista.insertar_inicio(valor)
            print("Valor insertado al inicio.")
        elif opcion == "3":
            valor = input("Ingrese el valor a eliminar: ")
            eliminado = lista.eliminar(valor)
            print("Valor eliminado." if eliminado else "No se encontró el valor.")
        elif opcion == "4":
            valor = input("Ingrese el valor a buscar: ")
            existe = lista.buscar(valor)
            print("Valor encontrado." if existe else "Valor no encontrado.")
        elif opcion == "5":
            lista.mostrar()
        elif opcion == "6":
            print(f"Longitud de la lista: {lista.longitud()}")
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    menu()
