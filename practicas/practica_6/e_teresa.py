from collections import deque

# Pilas y colas
pila_atencion_normal = []          # pila para tickets normales
pila_atencion_tercera_edad = []    # pila para tickets tercera edad
cola_control = deque()             # cola de control

# Estados
PENDIENTE = "Pendiente"
ATENDIDO = "Atendido"
NO_ATENDIDO = "No Atendido"

ticket_id = 1

def crear_ticket(tipo):
    global ticket_id
    ticket = {"id": ticket_id, "tipo": tipo, "estado": PENDIENTE}
    ticket_id += 1
    if tipo == "Normal":
        pila_atencion_normal.append(ticket)
    else:
        pila_atencion_tercera_edad.append(ticket)
    print(f"Ticket creado: {ticket}")

def llamar_fichas():
    # prioridad tercera edad
    if pila_atencion_tercera_edad:
        ticket = pila_atencion_tercera_edad.pop()
    elif pila_atencion_normal:
        ticket = pila_atencion_normal.pop()
    else:
        print("No hay tickets en las pilas.")
        return
    cola_control.append(ticket)
    print(f"Ticket llamado: {ticket}")

def ver_estado():
    print("\n--- Estado actual ---")
    print("Pila Normal:", pila_atencion_normal)
    print("Pila Tercera Edad:", pila_atencion_tercera_edad)
    print("Cola de Control:", list(cola_control))

def atender_ticket():
    if cola_control:
        ticket = cola_control.popleft()
        ticket["estado"] = ATENDIDO
        print(f"Ticket atendido: {ticket}")
    else:
        print("Cola de control vacía.")

def usuario_no_vino():
    if cola_control:
        ticket = cola_control.popleft()
        ticket["estado"] = NO_ATENDIDO
        # vuelve a su pila original
        if ticket["tipo"] == "Normal":
            pila_atencion_normal.append(ticket)
        else:
            pila_atencion_tercera_edad.append(ticket)
        print(f"Usuario no vino, ticket devuelto: {ticket}")
    else:
        print("Cola de control vacía.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Sacar ficha Normal")
        print("2. Sacar ficha Tercera Edad")
        print("3. Llamar fichas")
        print("4. Ver estado")
        print("5. Atender fichas")
        print("6. Usuario no vino")
        print("7. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            crear_ticket("Normal")
        elif opcion == "2":
            crear_ticket("Tercera Edad")
        elif opcion == "3":
            llamar_fichas()
        elif opcion == "4":
            ver_estado()
        elif opcion == "5":
            atender_ticket()
        elif opcion == "6":
            usuario_no_vino()
        elif opcion == "7":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()