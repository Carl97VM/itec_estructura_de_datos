from collections import deque

# -------------------------------
# Clase Equipo (gestión con pilas)
# -------------------------------
class Equipo:
    def __init__(self, nombre):
        # Cada equipo tiene un nombre y una pila (lista usada como stack) para su plantilla
        self.nombre = nombre
        self.plantilla = []  # Pila principal de jugadores

    def cargar_plantilla(self, jugadores):
        """
        Carga la nómina de jugadores en la pila.
        Restricción: Debe haber al menos 16 jugadores (11 titulares + 5 suplentes).
        """
        if len(jugadores) < 16:
            print(f" El equipo {self.nombre} no cumple con el mínimo de 16 jugadores.")
            return False
        for jugador in jugadores:
            self.plantilla.append(jugador)  # Apilar jugadores (push)
        print(f" Plantilla del equipo {self.nombre} cargada con {len(self.plantilla)} jugadores.")
        return True

    def mostrar_nomina(self):
        """
        Muestra la nómina actual del equipo.
        Se imprime la pila desde la cima hacia abajo (último en entrar, primero en mostrar).
        """
        print(f"\n Nómina actual del equipo {self.nombre}:")
        for jugador in reversed(self.plantilla):  # reversed simula recorrer la pila desde arriba
            print(f"- {jugador}")

    def existe_jugador(self, jugador):
        """
        Verifica si un jugador está en la pila del equipo.
        """
        return jugador in self.plantilla


# -------------------------------
# Clase Partido (gestión con cola)
# -------------------------------
class Partido:
    def __init__(self, equipo1, equipo2):
        # El partido se compone de dos equipos y una cola para los eventos
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.eventos = deque()  # Cola FIFO para almacenar eventos cronológicos

    def registrar_gol(self, minuto, jugador):
        """
        Registra un gol en la cola de eventos.
        Valida que el jugador esté en alguno de los equipos antes de encolar.
        """
        if self.equipo1.existe_jugador(jugador) or self.equipo2.existe_jugador(jugador):
            self.eventos.append({"minuto": minuto, "tipo": "Gol", "jugador": jugador})
            print(f" Gol registrado en el minuto {minuto} por {jugador}.")
        else:
            print(f" El jugador {jugador} no está en cancha.")

    def realizar_cambio(self, equipo, jugador_sale, jugador_entra):
        """
        Realiza un cambio en la plantilla del equipo usando una pila auxiliar.
        - Se desapila hasta encontrar al jugador que sale.
        - Se reemplaza por el jugador que entra.
        - Se reconstruye la pila original.
        """
        pila_aux = []  # Pila auxiliar para manipulación
        encontrado = False

        # Vaciar hasta encontrar al jugador que sale
        while equipo.plantilla:
            top = equipo.plantilla.pop()
            if top == jugador_sale and not encontrado:
                encontrado = True
                print(f" Cambio: sale {jugador_sale}, entra {jugador_entra}.")
                equipo.plantilla.append(jugador_entra)  # Insertar nuevo jugador en la pila
                # Registrar evento en la cola
                self.eventos.append({"minuto": "Cambio", "tipo": "Cambio", "jugador": f"{jugador_sale} → {jugador_entra}"})
                break
            else:
                pila_aux.append(top)

        # Reconstruir la pila original devolviendo los jugadores
        while pila_aux:
            equipo.plantilla.append(pila_aux.pop())

        if not encontrado:
            print(f" El jugador {jugador_sale} no fue encontrado en el equipo {equipo.nombre}.")

    def resumen_partido(self):
        """
        Procesa la cola de eventos y muestra el resumen final del partido.
        Se desencolan los eventos en orden cronológico.
        """
        print("\n Resumen del partido:")
        while self.eventos:
            evento = self.eventos.popleft()  # FIFO
            print(f"- Minuto {evento['minuto']}: {evento['tipo']} de {evento['jugador']}")


# -------------------------------
# Menú interactivo
# -------------------------------
def menu():
    """
    Menú principal para interactuar con el sistema.
    Permite:
    1. Registrar equipos
    2. Registrar gol
    3. Realizar cambio
    4. Mostrar nómina actual
    5. Ver resumen del partido
    0. Salir
    """
    # Crear equipos
    equipo1 = Equipo("Equipo A")
    equipo2 = Equipo("Equipo B")

    partido = None  # Se inicializa el partido después de cargar equipos

    while True:
        print("\n--- Menú ---")
        print("1. Registrar equipos")
        print("2. Registrar gol")
        print("3. Realizar cambio")
        print("4. Mostrar nómina actual")
        print("5. Ver resumen del partido")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            # Cargar nóminas de ambos equipos
            jugadoresA = input("Ingrese jugadores del Equipo A separados por coma: ").split(",")
            jugadoresB = input("Ingrese jugadores del Equipo B separados por coma: ").split(",")
            if equipo1.cargar_plantilla([j.strip() for j in jugadoresA]) and equipo2.cargar_plantilla([j.strip() for j in jugadoresB]):
                partido = Partido(equipo1, equipo2)
                print(" Partido listo para iniciar.")

        elif opcion == "2":
            # Registrar gol
            if partido:
                minuto = input("Minuto del gol: ")
                jugador = input("Jugador que anotó: ")
                partido.registrar_gol(minuto, jugador)
            else:
                print(" Debe registrar equipos primero.")

        elif opcion == "3":
            # Realizar cambio
            if partido:
                equipo_nombre = input("¿Equipo A o Equipo B?: ")
                jugador_sale = input("Jugador que sale: ")
                jugador_entra = input("Jugador que entra: ")
                equipo = equipo1 if equipo_nombre == "Equipo A" else equipo2
                partido.realizar_cambio(equipo, jugador_sale, jugador_entra)
            else:
                print(" Debe registrar equipos primero.")

        elif opcion == "4":
            # Mostrar nóminas actuales
            equipo1.mostrar_nomina()
            equipo2.mostrar_nomina()

        elif opcion == "5":
            # Mostrar resumen del partido
            if partido:
                partido.resumen_partido()
            else:
                print(" No hay partido registrado.")

        elif opcion == "0":
            print(" Saliendo...")
            break

        else:
            print(" Opción inválida.")


# -------------------------------
# Ejecutar
# -------------------------------
if __name__ == "__main__":
    menu()