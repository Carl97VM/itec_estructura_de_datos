import os
from collections import deque

class RoundRobinSystem:
    def __init__(self, equipos):
        # Cola de equipos para el turno
        self.cola_equipos = deque(equipos)
        # Diccionario de colas: ID_Equipo -> Cola de Tareas
        self.tareas_por_equipo = {eq: deque() for eq in equipos}
        # Pila global de penalizaciones
        self.pila_penalizaciones = [] 

    def agregar_tarea(self, equipo_id, tarea_id):
        if equipo_id in self.tareas_por_equipo:
            self.tareas_por_equipo[equipo_id].append(tarea_id)
            print(f"Tarea '{tarea_id}' agregada al equipo {equipo_id}")
        else:
            print("Error: Equipo no encontrado.")

    def procesar_tarea(self):
        if not self.cola_equipos:
            print("No hay equipos activos.")
            return

        # 1. Obtener turno
        eq_id = self.cola_equipos.popleft()
        
        # 2. Intentar procesar
        if self.tareas_por_equipo[eq_id]:
            tarea = self.tareas_por_equipo[eq_id].popleft()
            print(f"Equipo {eq_id} procesando: {tarea}")
            # El equipo vuelve a la cola para el siguiente turno
            self.cola_equipos.append(eq_id)
        else:
            print(f"Equipo {eq_id} sin tareas pendientes.")
            self.cola_equipos.append(eq_id)

    def penalizar_actual(self, eq_id):
        # Para penalizar, debemos sacar la última tarea asignada al equipo
        # Restricción: Solo podemos usar colas para equipos, así que reconstruimos
        if self.tareas_por_equipo[eq_id]:
            aux = []
            while self.tareas_por_equipo[eq_id]:
                aux.append(self.tareas_por_equipo[eq_id].popleft())
            
            tarea_penalizada = aux.pop() # La última tarea
            # Guardamos en la pila el objeto {tarea, equipo}
            self.pila_penalizaciones.append({'tarea': tarea_penalizada, 'equipo': eq_id})
            
            # Regresamos el resto a la cola
            for item in aux: self.tareas_por_equipo[eq_id].append(item)
            print(f"Tarea {tarea_penalizada} penalizada.")

    def reinsertar_penalizaciones(self):
        # LIFO: El último en penalizarse es el primero en reinsertarse (pop de pila)
        while self.pila_penalizaciones:
            info = self.pila_penalizaciones.pop()
            self.tareas_por_equipo[info['equipo']].append(info['tarea'])
            print(f"Reinsertada {info['tarea']} al equipo {info['equipo']}")

    def mostrar_estado(self):
        print("\n=== ESTADO ACTUAL ===")
        print(f"Cola de Equipos: {list(self.cola_equipos)}")
        print(f"Tareas por Equipo: { {k: list(v) for k, v in self.tareas_por_equipo.items()} }")
        print(f"Pila Penalizaciones: {self.pila_penalizaciones}")

def menu():
    equipos = ['A', 'B']
    sistema = RoundRobinSystem(equipos)
    
    while True:
        print("\n1. Agregar Tarea \n 2. Procesar \n 3. Penalizar \n 4. Reinsertar \n 5. Mostrar \n 0. Salir")
        op = input("Opción: ")
        if op == '1': sistema.agregar_tarea(input("Equipo: "), input("Tarea ID: "))
        elif op == '2': sistema.procesar_tarea()
        elif op == '3': sistema.penalizar_actual(input("Equipo a penalizar: "))
        elif op == '4': sistema.reinsertar_penalizaciones()
        elif op == '5': sistema.mostrar_estado()
        elif op == '0': break

if __name__ == "__main__":
    menu()