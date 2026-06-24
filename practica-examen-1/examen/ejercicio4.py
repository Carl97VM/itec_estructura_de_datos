import os
from collections import deque

class Ascensor:
    def __init__(self):
        # Configuración del edificio
        self.MAX_PISOS = 10
        self.piso_actual = 0
        
        # Estructuras de datos puras
        self.cola_normal = deque()  # Solo FIFO
        self.pila_override = []     # Solo LIFO
        
        # Métricas del sistema
        self.movimientos = 0
        self.distancia_total = 0

    def validar_piso(self, piso):
        """Asegura que el ascensor no viaje a pisos que no existen."""
        return 0 <= piso <= self.MAX_PISOS

    def solicitar_piso(self, piso):
        """Ingresa una solicitud a la cola normal (FIFO)."""
        if self.validar_piso(piso):
            self.cola_normal.append(piso)
            print(f"Solicitud normal registrada: Piso {piso}")
        else:
            print(f"Error: El piso {piso} no existe. (Límite: 0 a {self.MAX_PISOS})")

    def solicitar_override(self, piso, prioridad):
        """Ingresa una emergencia a la pila (LIFO)."""
        if self.validar_piso(piso):
            # Guardamos un diccionario para mantener el piso y la prioridad unidos
            emergencia = {'piso': piso, 'prioridad': prioridad}
            self.pila_override.append(emergencia)
            print(f"OVERRIDE ACTIVADO: Piso {piso} (Prioridad: {prioridad})")
        else:
            print(f"Error: El piso {piso} no existe.")

    def mover(self):
        """Procesa la siguiente petición respetando la prioridad absoluta."""
        if self.pila_override:
            # La pila tiene prioridad absoluta. Atendemos el último en entrar (LIFO)
            peticion = self.pila_override.pop()
            piso_destino = peticion['piso']
            print(f"\nATENDIENDO EMERGENCIA -> Prioridad: {peticion['prioridad']}")
        elif self.cola_normal:
            # Si no hay emergencias, atendemos la cola normal por orden de llegada (FIFO)
            piso_destino = self.cola_normal.popleft()
            print("\nAtendiendo solicitud normal.")
        else:
            print("\nEl ascensor está en reposo. No hay solicitudes pendientes.")
            return

        # Cálculo de métricas
        distancia_recorrida = abs(piso_destino - self.piso_actual)
        self.distancia_total += distancia_recorrida
        self.movimientos += 1
        self.piso_actual = piso_destino
        
        print(f"Elevador en movimiento... Llegó al piso {self.piso_actual}.")
        print(f"Distancia de este viaje: {distancia_recorrida} pisos.")

    def cancelar_solicitud(self, piso):
        """Busca y elimina una solicitud normal usando una pila temporal."""
        pila_auxiliar = []
        encontrado = False

        # 1. Desencolar sucesivamente hasta encontrar el objetivo
        while self.cola_normal:
            temp = self.cola_normal.popleft()
            if temp == piso and not encontrado:
                # Si es el piso buscado, lo descartamos y marcamos como encontrado
                print(f"\nSolicitud al piso {piso} cancelada con éxito.")
                encontrado = True
            else:
                # Si no es, lo guardamos en nuestro almacén temporal
                pila_auxiliar.append(temp)

        # 2. Reconstruir la cola conservando el orden original
        # Como los sacamos a una pila, al hacer pop() e insertarlos al frente (appendleft),
        # recuperan su orden exacto en la cola original.
        while pila_auxiliar:
            self.cola_normal.appendleft(pila_auxiliar.pop())

        if not encontrado:
            print(f"\nNo se encontró ninguna solicitud normal al piso {piso}.")

    def mostrar_estado(self):
        """Imprime el tablero de control del sistema."""
        print("\n--- TABLERO DEL ASCENSOR ---")
        print(f"Piso Actual: {self.piso_actual}")
        print(f"Movimientos Totales: {self.movimientos}")
        print(f"Distancia Total Recorrida: {self.distancia_total} pisos")
        print(f"Cola Normal (Pendientes): {list(self.cola_normal)}")
        print(f"Pila Override (Emergencias): {self.pila_override}")

def menu():
    ascensor = Ascensor()
    
    while True:
        print("\n=== PANEL DE CONTROL - EDIFICIO 10 PISOS ===")
        print("1. Solicitar piso (Normal)")
        print("2. Solicitar override (Emergencia)")
        print("3. Mover ascensor")
        print("4. Cancelar solicitud normal")
        print("5. Mostrar estado")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            piso = int(input("Ingresa el piso destino (0-10): "))
            ascensor.solicitar_piso(piso)
        elif opcion == '2':
            piso = int(input("Ingresa el piso destino (0-10): "))
            prioridad = input("Identificador de prioridad (ej. Bomberos, Médico): ")
            ascensor.solicitar_override(piso, prioridad)
        elif opcion == '3':
            ascensor.mover()
        elif opcion == '4':
            piso = int(input("Ingresa el piso a cancelar: "))
            ascensor.cancelar_solicitud(piso)
        elif opcion == '5':
            ascensor.mostrar_estado()
        elif opcion == '0':
            print("Apagando sistema del ascensor...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == '__main__':
    menu()