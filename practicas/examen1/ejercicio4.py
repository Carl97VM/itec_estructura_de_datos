import os
from collections import deque

class Ascensor:
    def __init__(self):
        # Configuración del ascensor
        self.MAX_PISOS = 10
        self.piso_actual = 0
        
        # Estructura de datos
        self.cola_normal = deque()  # Cola para almacenar las solicitudes de piso normales
        self.pila_prioritaria = []
        
        # Metricas del sistema
        self.movimientos = 0
        self.distancia_total = 0
        
    def validar_piso(self, piso):
        # if 0 <= piso < self.MAX_PISOS:
        #     return True
        # else:
        #     print(f"Piso {piso} inválido. Debe estar entre 0 y {self.MAX_PISOS - 1}.")
        #     return False
        return 0 <= piso < self.MAX_PISOS
    
    def solicitar_piso(self, piso):
        if self.validar_piso(piso):
            self.cola_normal.append(piso)
            print(f"Solicitud de piso {piso} añadida a la cola normal.")
        else:
            print(f"Piso {piso} inválido. Debe estar entre 0 y {self.MAX_PISOS}.")
        
    def solicitar_piso_prioritario(self, piso, prioridad):
        if self.validar_piso(piso):
            emergencia = {'prioridad': prioridad, 'piso': piso}
            self.pila_prioritaria.append(emergencia)
            print(f"Solicitud de piso {piso} añadida a la cola prioritaria.")
        else:
            print(f"Piso {piso} inválido. Debe estar entre 0 y {self.MAX_PISOS}.")
            
    def mover_ascensor(self):
        if self.pila_prioritaria:
            # Atender solicitudes prioritarias primero
            solicitud = self.pila_prioritaria.pop(0)
            piso_destino = solicitud['piso']
            print(f"Atendiendo solicitud prioritaria para el piso {piso_destino}.")
        elif self.cola_normal:
            # Atender solicitudes normales si no hay prioritarias
            piso_destino = self.cola_normal.popleft()
            print(f"Atendiendo solicitud normal para el piso {piso_destino}.")
        else:
            print("No hay solicitudes pendientes.")
            return
        
        # Calcular la distancia y actualizar métricas
        distancia = abs(self.piso_destino - self.piso_actual)
        self.distancia_total += distancia
        self.movimientos += 1
        print(f"Moviendo ascensor del piso {self.piso_actual} al piso {piso_destino}. Distancia recorrida: {distancia}")
        
        # Actualizar el piso actual del ascensor
        self.piso_actual = piso_destino
        
    def cancelar_solicitud(self, piso):
        pila_auxiliar = []
        encontrado = False
        while self.cola_normal:
            temp = self.cola_normal.popleft()
            if temp == piso and not encontrado:
                print(f"Solicitud al piso {piso} cancelado con exito")
                encontrado = True
            else:
                pila_auxiliar.append(temp)
                
        while pila_auxiliar:
            self.cola_normal.appendleft(pila_auxiliar.pop())
            
    def mostrar_estado(self):
        print("\n Tablero de Ascensor")
        print(f"Piso Actual: {self.piso_actual}")
        print(f"Movimiento Total: {self.movimientos}")
        print(f"Distancia Recorrida: {self.distancia_total} pisos")
        print(f"Cola Normal (Pendientes): {list(self.cola_normal)}")
        print(f"Pila Override (Emergencias): {self.pila_prioritaria}")
        
def menu():
    ascesor = Ascensor()
    
    while True:
        print("=== Juego del Ascensor ===")
        print("1. Solicitar Piso")
        print("2. Solicitar Override")
        print("3. Mover Ascensor")
        print("4. Cancelar solicitud")
        print("5. Muestra de estados")
        print("0. Salir")
        
        
        option = input("Agregue una opcion")
        
        if option == '1':
            piso = int(input("Ingrese el numero de piso"))
            ascesor.solicitar_piso(piso)
            
        elif option == '2':
            piso = int(input("Ingrese el piso destino"))
            prioridad = input("Agregar la Prioridad")
            ascesor.solicitar_piso_prioritario()
            
if __name__ == '__main__':
    menu()