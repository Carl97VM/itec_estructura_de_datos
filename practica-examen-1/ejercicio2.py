import os
from collections import deque

class ColaAtencion:
    def __init__(self):
        self._cola = deque()
        self._contador = 1
        
    def dar_turno(self):
        cliente = f"Cliente #{self._contador}"
        self._cola.append(cliente)
        self._contador += 1
        return f"Ficha dada a: {cliente}"
    
    def llamar_cliente(self):
        if not self.esta_vacia():
            cliente = self._cola.popleft() # Elimina el cliente de la cola y lo devuelve Complejidad 0(1)
            return f"Llamando a la ventanilla a: {cliente}"
        return "No hay clientes en la cola."
    
    def esta_vacia(self):
        return len(self._cola) == 0
    
    def cantidad_clientes(self):
        return len(self._cola)
    
def menu():
    sistema = ColaAtencion()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Limpia la consola
        print("\n--- Sistema de Atención al Cliente ---")
        print(f"Personas esperando: {sistema.cantidad_clientes()}")
        print("--------------------------------------")
        print("1. Dar turno")
        print("2. Llamar cliente")
        print("3. Ver cantidad de clientes en la cola")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print(sistema.dar_turno())
            input("Presione Enter para continuar...")
        elif opcion == '2':
            print(sistema.llamar_cliente())
            input("Presione Enter para continuar...")
        elif opcion == '3':
            print(f"\nCantidad de clientes en la cola: {sistema.cantidad_clientes()}")
            input("Presione Enter para continuar...")
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
            
if __name__ == "__main__":
    menu()