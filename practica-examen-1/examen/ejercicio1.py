import os
from collections import deque

class CallCenter:
    def __init__(self):
        self.cola_normal = deque()
        self.cola_callback = deque()
        self.pila_prioritaria = [] # Pila para promociones recientes

    def llegada_llamada(self, id_cliente):
        self.cola_normal.append(id_cliente)
        print(f"Llamada recibida: {id_cliente}")

    def cliente_cuelga_callback(self, id_cliente):
        # Primero quitamos de la normal si está ahí
        self.cola_callback.append(id_cliente)
        print(f"Callback solicitado por: {id_cliente}")

    def promover_cliente(self, id_cliente):
        # Busca en cola normal, usa pila auxiliar para mover a pila prioritaria
        pila_aux = []
        encontrado = False
        
        # 1. Vaciar cola normal a pila auxiliar
        while self.cola_normal:
            temp = self.cola_normal.popleft()
            if temp == id_cliente:
                encontrado = True
                self.pila_prioritaria.append(temp)
            else:
                pila_aux.append(temp)
        
        # 2. Restaurar cola normal
        while pila_aux:
            self.cola_normal.appendleft(pila_aux.pop())
            
        if encontrado: print(f"Cliente {id_cliente} promovido a prioridad.")
        else: print("Cliente no encontrado en cola normal.")

    def atender(self):
        if self.pila_prioritaria:
            print(f"Atendiendo desde PRIORIDAD: {self.pila_prioritaria.pop()}")
        elif self.cola_normal:
            print(f"Atendiendo desde NORMAL: {self.cola_normal.popleft()}")
        else:
            print("No hay llamadas pendientes.")

    def procesar_callback(self):
        if self.cola_callback:
            cliente = self.cola_callback.popleft()
            # Encolar al frente de la normal usando pilas auxiliares
            pila_aux = []
            while self.cola_normal:
                pila_aux.append(self.cola_normal.popleft())
            self.cola_normal.append(cliente)
            while pila_aux:
                self.cola_normal.appendleft(pila_aux.pop())
            print(f"Callback {cliente} reinsertado al frente de la cola normal.")
        else:
            print("No hay callbacks pendientes.")

    def mostrar_estado(self):
        print(f"\n--- ESTADO ---")
        print(f"Prioridad (Pila): {self.pila_prioritaria}")
        print(f"Normal (Cola): {list(self.cola_normal)}")
        print(f"Callbacks (Cola): {list(self.cola_callback)}")

def menu():
    cc = CallCenter()
    while True:
        print("\n1. Llegada llamada \n 2. Atender \n 3. Solicitar Callback \n 4. Procesar Callback \n 5. Promover \n 6. Mostrar \n 0. Salir")
        op = input("Opción: ")
        if op == '1': cc.llegada_llamada(input("ID: "))
        elif op == '2': cc.atender()
        elif op == '3': cc.cliente_cuelga_callback(input("ID: "))
        elif op == '4': cc.procesar_callback()
        elif op == '5': cc.promover_cliente(input("ID a promover: "))
        elif op == '6': cc.mostrar_estado()
        elif op == '0': break

if __name__ == "__main__":
    menu()