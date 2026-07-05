class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return self.elementos

    def cantidad(self):
        return len(self.elementos)


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return self.elementos

    def cantidad(self):
        return len(self.elementos)


cola_normal = Cola()
cola_tercera_edad = Cola()
pila_no_atendidos = Pila()

contador_normal = 0
contador_tercera_edad = 0
ticket_llamado = None

while True:
    print("\nSISTEMA SACAR TICKET")
    print("1. Sacar ficha normal")
    print("2. Sacar ficha tercera edad")
    print("3. Llamar fichas")
    print("4. Ver fichas")
    print("5. Atender ficha")
    print("6. Usuario no vino")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        contador_normal = contador_normal + 1
        ticket = "N-" + str(contador_normal)
        cola_normal.encolar(ticket)
        print("Ticket normal generado:", ticket)

    elif opcion == "2":
        contador_tercera_edad = contador_tercera_edad + 1
        ticket = "TE-" + str(contador_tercera_edad)
        cola_tercera_edad.encolar(ticket)
        print("Ticket tercera edad generado:", ticket)

    elif opcion == "3":
        if ticket_llamado is not None:
            print("Primero debe atender o marcar como no vino el ticket:", ticket_llamado)

        elif not cola_tercera_edad.esta_vacia():
            ticket_llamado = cola_tercera_edad.desencolar()
            print("Llamando al ticket:", ticket_llamado)

        elif not cola_normal.esta_vacia():
            ticket_llamado = cola_normal.desencolar()
            print("Llamando al ticket:", ticket_llamado)

        else:
            print("No hay tickets en espera")

    elif opcion == "4":
        print("Fichas normales:", cola_normal.mostrar())
        print("Fichas tercera edad:", cola_tercera_edad.mostrar())
        print("Ticket llamado:", ticket_llamado)
        print("Tickets no atendidos:", pila_no_atendidos.mostrar())
        print("Cantidad normal:", cola_normal.cantidad())
        print("Cantidad tercera edad:", cola_tercera_edad.cantidad())
        print("Cantidad no atendidos:", pila_no_atendidos.cantidad())

    elif opcion == "5":
        if ticket_llamado is None:
            print("No hay ticket llamado para atender")
        else:
            print("Se atendió el ticket:", ticket_llamado)
            ticket_llamado = None

    elif opcion == "6":
        if ticket_llamado is None:
            print("No hay ticket llamado")
        else:
            pila_no_atendidos.apilar(ticket_llamado)
            print("Ticket no atendido:", ticket_llamado)
            ticket_llamado = None

    elif opcion == "7":
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")