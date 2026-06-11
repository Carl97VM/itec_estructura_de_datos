import os
from collections import deque

class ImpresoraSecretaria:
    def __init__(self):
        self._alta_prioridad = deque()
        self._baja_prioridad = deque()
        
    def agregar_trabajo(self, trabajo, es_docente=False):
        if es_docente:
            self._alta_prioridad.append(trabajo)
            return "Trabajo agregado a alta prioridad."
        else:
            self._baja_prioridad.append(trabajo)
            return "Trabajo agregado a baja prioridad."
        
    def imprimir_trabajo(self):
        if self._alta_prioridad:
            return f"Imprimiendo trabajo de alta prioridad: {self._alta_prioridad.popleft()}"
        elif self._baja_prioridad:
            return f"Imprimiendo trabajo de baja prioridad: {self._baja_prioridad.popleft()}"
        else:
            return "No hay trabajos para imprimir."
        
    def estado_impresora(self):
        # return {
        #     "alta_prioridad": list(self._alta_prioridad),
        #     "baja_prioridad": list(self._baja_prioridad)
        # }
        return len(self._alta_prioridad), len(self._baja_prioridad)
    
def menu():
    impresora = ImpresoraSecretaria()
    
    while True:
        print("\nMenú de la Impresora de la Secretaria:")
        print("1. Agregar trabajo (Docente)")
        print("2. Agregar trabajo (No Docente)")
        print("3. Imprimir trabajo")
        print("4. Estado de la impresora")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            trabajo = input("Ingrese el nombre del trabajo: ")
            print(impresora.agregar_trabajo(trabajo, es_docente=True))
        elif opcion == '2':
            trabajo = input("Ingrese el nombre del trabajo: ")
            print(impresora.agregar_trabajo(trabajo, es_docente=False))
        elif opcion == '3':
            print(impresora.imprimir_trabajo())
        elif opcion == '4':
            alta, baja = impresora.estado_impresora()
            print(f"Trabajos en alta prioridad: {alta}")
            print(f"Trabajos en baja prioridad: {baja}")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
            
if __name__ == "__main__":
    menu()