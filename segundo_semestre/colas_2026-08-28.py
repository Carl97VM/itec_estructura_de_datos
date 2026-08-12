import os
class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = nodo(valor)
        if not self.cabeza:
            print("La lista está vacía. Agregando el primer elemento.")
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None: # Analizar la info para llegar al final de la lista
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo # BRAZO
        print(f"Agregado: {valor}")

    def invertir_lista(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            print("La lista está vacía. No se puede invertir.")
            return
        
        anterior = None
        actual = self.cabeza
        while actual is not None:
            # Guardar temporalmente el siguiente nodo antes de cambiar la referencia
            sigueinte_temporal = actual.siguiente

            # invertir el puntero del nodo actual para que apunte al nodo anterior
            actual.siguiente = anterior

            # Actualizar el nodo anterior y el nodo actual para avanzar en la lista
            anterior = actual
            actual = sigueinte_temporal

        self.cabeza = anterior
        print("La lista ha sido invertida.")

    def mostrar(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        print("Elementos en la lista:", elementos)

def menu():
    lista = ListaEnlazada()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenú:")
        print("1. Agregar elemento")
        print("2. Mostrar elementos")
        print("3. Invertir lista")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            valor = input("Ingrese el valor a agregar: ")
            lista.agregar(valor)
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            lista.mostrar()
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            lista.invertir_lista()
            lista.mostrar()
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu()