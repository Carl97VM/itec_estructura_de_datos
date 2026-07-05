import os

fila_normal = []
fila_tercera_edad = []
contador_ticket = 1

def sacar_ficha(tipo):
    global contador_ticket
    ticket = f"T{contador_ticket}"
    contador_ticket += 1
    if tipo == "normal":
        fila_normal.append(ticket)
    else:
        fila_tercera_edad.append(ticket)
    print(f"Se generó ficha {ticket} para {tipo}")

def ver_fichas():
    print("\n--- Fichas en espera ---")
    print("Normal:", fila_normal)
    print("Tercera Edad:", fila_tercera_edad)

def llamar_ficha():
    if fila_tercera_edad:
        ticket = fila_tercera_edad.pop(0)
        print(f"Llamando ficha {ticket} (Tercera Edad)")
        return ticket
    elif fila_normal:
        ticket = fila_normal.pop(0)
        print(f"Llamando ficha {ticket} (Normal)")
        return ticket
    else:
        print("No hay fichas en espera")
        return None

def atender_ficha(ticket):
    if ticket:
        print(f"Ficha {ticket} fue ATENDIDA")
    else:
        print("No hay ficha para atender")

def usuario_no_vino(ticket):
    if ticket:
        print(f"Ficha {ticket} marcada como NO ATENDIDA")
    else:
        print("No hay ficha para marcar")


while True:
    print("\n--- Menú Banco ---")
    print("1. Sacar ficha Normal")
    print("2. Sacar ficha Tercera Edad")
    print("3. Llamar fichas")
    print("4. Ver fichas")
    print("5. Atender fichas")
    print("6. Usuario no vino")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        sacar_ficha("normal")
    elif opcion == "2":
        sacar_ficha("tercera edad")
    elif opcion == "3":
        ticket_actual = llamar_ficha()
    elif opcion == "4":
        ver_fichas()
    elif opcion == "5":
        atender_ficha(ticket_actual if 'ticket_actual' in locals() else None)
    elif opcion == "6":
        usuario_no_vino(ticket_actual if 'ticket_actual' in locals() else None)
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")