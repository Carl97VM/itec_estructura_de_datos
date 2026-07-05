# SISTEMA DE ATENCION AL CLIENTE - TICKETERA CON PILAS Y COLA DE CONTROL
from collections import deque
class SistemaFichas:
    def __init__(self):
        self.fila_normal = []          
        self.fila_tercera_edad = []   
        self.cola_control = deque()    
        self._contador_normal = 0
        self._contador_tercera_edad = 0
    def sacar_ficha_normal(self):
        self._contador_normal += 1
        ticket = {
            "id": self._contador_normal,
            "tipo": "normal",
            "estado": "pendiente",
        }
        self.fila_normal.append(ticket)  # apilar
        print(f"Ticket normal #{ticket['id']} generado.")
    def sacar_ficha_tercera_edad(self):
        self._contador_tercera_edad += 1
        letra = chr(ord("A") + self._contador_tercera_edad - 1)
        ticket = {
            "id": letra,
            "tipo": "tercera_edad",
            "estado": "pendiente",
        }
        self.fila_tercera_edad.append(ticket)  # apilar
        print(f"Ticket tercera edad #{ticket['id']} generado.")
    def llamar_fichas(self):
        hay_tickets = bool(self.fila_normal) or bool(self.fila_tercera_edad)
        if not hay_tickets:
            print("No hay tickets para llamar (pilas vacias).")
            return
        for ticket in self.fila_tercera_edad:
            self.cola_control.append(ticket)
        self.fila_tercera_edad.clear()
        for ticket in self.fila_normal:
            self.cola_control.append(ticket)
        self.fila_normal.clear()
        print("Tickets agregados a la cola de control (con prioridad).")
    def ver_fichas(self):
        if not self.cola_control:
            print("La cola de control esta vacia.")
            return
        print("Cola de control actual:")
        for ticket in self.cola_control:
            print(f"  - {ticket['id']} ({ticket['tipo']}) -> {ticket['estado']}")
    def atender_ficha(self):
        if not self.cola_control:
            print("La cola de control esta vacia. No hay nada que atender.")
            return
        ticket = self.cola_control.popleft()  # desencolar (FIFO)
        ticket["estado"] = "atendido"
        print(f"Atendiendo ticket {ticket['id']} ({ticket['tipo']}). Estado: {ticket['estado']}")
    def usuario_no_vino(self):
        if not self.cola_control:
            print("La cola de control esta vacia. No hay nada que marcar.")
            return
        ticket = self.cola_control.popleft()  # desencolar (FIFO)
        ticket["estado"] = "no_atendido"
        if ticket["tipo"] == "normal":
            self.fila_normal.append(ticket)
        else:
            self.fila_tercera_edad.append(ticket)
        print(f"Ticket {ticket['id']} no atendido. Vuelve a su fila de origen.")
def mostrar_menu():
    print("\n######## SISTEMA DE FICHAS ########")
    print("1. Sacar ficha normal")
    print("2. Sacar ficha tercera edad")
    print("3. Llamar fichas")
    print("4. Ver fichas")
    print("5. Atender ficha")
    print("6. Usuario no vino")
    print("7. Salir")
def main():
    sistema = SistemaFichas()
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()
        if opcion == "1":
            sistema.sacar_ficha_normal()
        elif opcion == "2":
            sistema.sacar_ficha_tercera_edad()
        elif opcion == "3":
            sistema.llamar_fichas()
        elif opcion == "4":
            sistema.ver_fichas()
        elif opcion == "5":
            sistema.atender_ficha()
        elif opcion == "6":
            sistema.usuario_no_vino()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")
if __name__ == "__main__":
    main()