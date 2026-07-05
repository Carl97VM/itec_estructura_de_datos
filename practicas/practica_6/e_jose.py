"""
Sistema de Simulación de Atención al Cliente (Pilas y Colas)
Basado en los diagramas de flujo y especificaciones provistas.
"""

class Ticket:
    def __init__(self, identificador, tipo):
        self.identificador = identificador  # Puede ser número (1, 2..) o letra (a, b..)
        self.tipo = tipo                    # "Normal" o "Tercera Edad"
        self.estado = "Pendiente"           # Estados: Pendiente, Atendido, No Atendido

    def __str__(self):
        return f"[{self.tipo}] Ticket {self.identificador} - Estado: {self.estado}"


class SistemaAtencion:
    def __init__(self):
       
        self.pila_atencion_normal = []
        self.pila_atencion_tercera_edad = []
        self.cola_de_control = []
       
       
        self.contador_normal = 1
        self.contador_te = ord('a')  

    def sacar_ficha_normal(self):
        """Opción 1: Crea un ticket normal y lo añade a su Pila"""
        nuevo_ticket = Ticket(self.contador_normal, "Normal")
        self.pila_atencion_normal.append(nuevo_ticket)
        print(f"\n[✓] Ticket Normal generado con éxito: {nuevo_ticket.identificador}")
        self.contador_normal += 1

    def sacar_ficha_tercera_edad(self):
        """Opción 2: Crea un ticket de Tercera Edad y lo añade a su Pila"""
        letra = chr(self.contador_te)
        nuevo_ticket = Ticket(letra, "Tercera Edad")
        self.pila_atencion_tercera_edad.append(nuevo_ticket)
        print(f"\n[✓] Ticket Tercera Edad generado con éxito: {nuevo_ticket.identificador}")
       
       
        self.contador_te += 1

    def llamar_fichas(self):
        """
        Opción 3: Pasa los elementos de las Pilas a la Cola de Control.
        De acuerdo con el diagrama, los de Tercera Edad tienen prioridad y se consolidan en la Cola.
        Al ser Pilas (LIFO), al desapilarlos se van insertando en la Cola de Control.
        """
        if not self.pila_atencion_normal and not self.pila_atencion_tercera_edad:
            print("\n[!] No hay tickets en las pilas para llamar.")
            return

        elementos_trasladados = 0

       
        while self.pila_atencion_tercera_edad:
            ticket = self.pila_atencion_tercera_edad.pop()  
            self.cola_de_control.append(ticket)            
            elementos_trasladados += 1

       
        while self.pila_atencion_normal:
            ticket = self.pila_atencion_normal.pop()        
            self.cola_de_control.append(ticket)            
            elementos_trasladados += 1

        print(f"\n[✓] Se han llamado las fichas. {elementos_trasladados} ticket(s) movidos a la Cola de Control.")

    def ver_fichas(self):
        """Opción 4: Muestra el estado actual de la Cola de Control"""
        if not self.cola_de_control:
            print("\n[i] La Cola de Control está vacía en este momento.")
            return
       
        print("\n--- ESTADO DE LA COLA DE CONTROL (Primero en atender al inicio) ---")
        for idx, ticket in enumerate(self.cola_de_control, 1):
            print(f"{idx}. {ticket}")
        print("------------------------------------------------------------------")

    def atender_ficha(self):
        """Opción 5: Atiende al primer ticket de la Cola (FIFO) y cambia su estado"""
        if not self.cola_de_control:
            print("\n[!] No hay tickets en la Cola de Control para atender.")
            return
       
       
        ticket_atendido = self.cola_de_control.pop(0)
        ticket_atendido.estado = "Atendido"
        print(f"\n[➔] ATENDIENDO: {ticket_atendido}")

    def usuario_no_vino(self):
        """Opción 6: Remueve al primer ticket de la Cola y cambia su estado a No Atendido"""
        if not self.cola_de_control:
            print("\n[!] No hay tickets en la Cola de Control para procesar.")
            return
       
        ticket_ausente = self.cola_de_control.pop(0)
        ticket_ausente.estado = "No Atendido"
        print(f"\n[×] REGISTRADO: {ticket_ausente} (El usuario no se presentó)")


def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE CONTROL DE TICKETS     ")
    print("========================================")
    print("1. Sacar Ficha Normal")
    print("2. Sacar Ficha Tercera Edad")
    print("3. Llamar Fichas (Mover a la Cola)")
    print("4. Ver Fichas (Cola de Control)")
    print("5. Atender Fichas")
    print("6. Usuario No Vino")
    print("7. Salir")
    print("========================================")


def ejecutar_sistema():
    sistema = SistemaAtencion()
   
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-7): "))
        except ValueError:
            print("\n[!] Error: Por favor, ingrese un número válido.")
            continue
           
        if opcion == 1:
            sistema.sacar_ficha_normal()
        elif opcion == 2:
            sistema.sacar_ficha_tercera_edad()
        elif opcion == 3:
            sistema.llamar_fichas()
        elif opcion == 4:
            sistema.ver_fichas()
        elif opcion == 5:
            sistema.atender_ficha()
        elif opcion == 6:
            sistema.usuario_no_vino()
        elif opcion == 7:
            print("\nSaliendo del sistema... ¡Muchas gracias!")
            break
        else:
            print("\n[!] Opción inválida. Intente con un número del 1 al 7.")

if __name__ == '__main__':
    # Este bloque inicia la simulación interactiva en consola
    ejecutar_sistema()