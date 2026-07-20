from collections import deque  # esto es para poder usar la cola 

print("--- SISTEMA DE GESTION DE PARTIDOS FIFA WORLD CUP 2026 ---")

class Equipo:
    # esta clase representa a cada equipo con su nombre y su plantilla
    def __init__(self, nombre):
        self.nombre = nombre
        self.plantilla = []  # aqui guardamos los jugadores, esto funciona como una pila
class Partido:
    # esta clase junta a los dos equipos y guarda los eventos del partido
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.eventos = deque()  # esta es la cola, aqui se guardan los goles y cambios en orden
    def realizar_cambio(self, equipo, jugador_sale, jugador_entra):
        # esta funcion saca a un jugador y mete a otro nuevo
        # aqui se usa una pila auxiliar para ir sacando jugadores uno por uno
        # hasta encontrar al que queremos sacar, sin usar indices
        pila_auxiliar = []  # aqui vamos a ir guardando temporalmente a los jugadores que sacamos
        encontrado = False  # esto nos dice si ya encontramos al jugador que sale
        while len(equipo.plantilla) > 0:
            jugador = equipo.plantilla.pop()  # sacamos al jugador de arriba de la pila
            if jugador == jugador_sale and not encontrado:
                encontrado = True
                # a este no lo guardamos en la auxiliar porque este es el que sale
            else:
                pila_auxiliar.append(jugador)  # a los demas los guardamos aparte un ratito

        # ahora squi devolvemos todo a la plantilla otra vez, para que quede como estaba
        while len(pila_auxiliar) > 0:
            equipo.plantilla.append(pila_auxiliar.pop())

        if encontrado:
            equipo.plantilla.append(jugador_entra)  # aqui metemos al jugador nuevo
            print("Cambio realizado: sale", jugador_sale, ", entra", jugador_entra)
        else:
            print("Error: el jugador", jugador_sale, "no esta en la plantilla de", equipo.nombre)

        return encontrado  # con esto avisamos si el cambio si se pudo hacer o no
def buscar_jugador(equipo, jugador):
    # esta funcion revisa si un jugador esta en la plantilla de un equipo
    # se usa una pila auxiliar para no usar listas con indice
    pila_auxiliar = []  # aqui guardamos temporalmente a los jugadores mientras buscamos
    encontrado = False  # bandera para saber si el jugador aparecio o no
    while len(equipo.plantilla) > 0:
        jugador_actual = equipo.plantilla.pop()  # vamos sacando uno por uno de la pila
        pila_auxiliar.append(jugador_actual)  # lo guardamos para no perderlo
        if jugador_actual == jugador:
            encontrado = True  # si coincide con el que buscamos, marcamos que si esta
    # regresamos todo a la plantilla como estaba antes
    while len(pila_auxiliar) > 0:
        equipo.plantilla.append(pila_auxiliar.pop())
    return encontrado
def cargar_equipo(numero):
    # esta funcion registra un equipo pidiendo el nombre y los jugadores
    # tiene que tener minimo 16 jugadores (11 titulares + 5 suplentes)
    nombre = input("Nombre del equipo " + str(numero) + ": ")
    equipo_nuevo = Equipo(nombre)  # aqui creamos el equipo vacio primero
    print("Ingrese los jugadores de", nombre, "(escriba FIN cuando termine)")
    while True:
        jugador = input("Nombre del jugador: ")
        if jugador == "FIN" or jugador == "fin":
            break  # con esto se sale del bucle de cargar jugadores
        equipo_nuevo.plantilla.append(jugador)  # metemos al jugador en la pila del equipo

    if len(equipo_nuevo.plantilla) < 16:
        print("Error: el equipo", nombre, "no tiene los 16 jugadores minimos. Tiene:", len(equipo_nuevo.plantilla))
        return None  # si no cumple el minimo no dejamos usar este equipo
    else:
        print("Equipo", nombre, "registrado con exito con", len(equipo_nuevo.plantilla), "jugadores.")
        return equipo_nuevo
# las variables principales del programa
partido = None  # aqui todavia no hay ningun partido creado

while True:
    print("\nMENU")
    print("1. Registro de Equipos")
    print("2. Registrar Gol")
    print("3. Realizar Cambio")
    print("4. Mostrar Nomina Actual")
    print("5. Ver Resumen del Partido")
    print("6. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        # aqui se cargan los dos equipos antes de poder jugar el partido
        equipo1 = cargar_equipo(1)
        equipo2 = cargar_equipo(2)
        if equipo1 is not None and equipo2 is not None:
            partido = Partido(equipo1, equipo2)  # se crea el partido con los dos equipos ya listos
            print("Los dos equipos quedaron registrados, ya se puede empezar el partido.")
        else:
            print("No se pudo crear el partido porque algun equipo no cumplio el minimo de jugadores.")

    elif opcion == "2":
        # esta opcion es para registrar un gol y meterlo en la cola de eventos
        if partido is None:
            print("Error: primero registre los equipos.")
        else:
            minuto = input("Minuto del gol: ")
            jugador = input("Jugador que hizo el gol: ")
            if not minuto.isdigit():
                print("Error: el minuto tiene que ser un numero.")
            else:
                # aqui revisamos que el jugador si existe en alguno de los dos equipos
                esta_en_equipo1 = buscar_jugador(partido.equipo1, jugador)
                esta_en_equipo2 = buscar_jugador(partido.equipo2, jugador)
                if esta_en_equipo1 or esta_en_equipo2:
                    evento = {"minuto": minuto, "tipo_evento": "gol", "jugador_involucrado": jugador}
                    partido.eventos.append(evento)  # metemos el evento al final de la cola
                    print("Gol registrado en el minuto", minuto, "de", jugador)
                else:
                    print("Error: el jugador", jugador, "no pertenece a ningun equipo del partido.")

    elif opcion == "3":
        # esta opcion hace un cambio de jugador en algun equipo
        if partido is None:
            print("Error: primero registre los equipos.")
        else:
            numero_equipo = input("A que equipo se le hace el cambio (1 o 2): ")
            minuto = input("Minuto del cambio: ")
            jugador_sale = input("Jugador que sale: ")
            jugador_entra = input("Jugador que entra: ")

            if numero_equipo == "1":
                equipo_elegido = partido.equipo1
            elif numero_equipo == "2":
                equipo_elegido = partido.equipo2
            else:
                equipo_elegido = None
                print("Error: opcion de equipo no valida.")

            if equipo_elegido is not None:
                tamano_antes = len(equipo_elegido.plantilla)  # guardamos el tamaño antes del cambio
                exito = partido.realizar_cambio(equipo_elegido, jugador_sale, jugador_entra)
                tamano_despues = len(equipo_elegido.plantilla)  # y el tamaño despues del cambio
                if exito:
                    evento = {"minuto": minuto, "tipo_evento": "cambio",
                              "jugador_involucrado": jugador_sale + " sale, entra " + jugador_entra}
                    partido.eventos.append(evento)  # el cambio tambien se guarda como evento
                    print("Tamano de la plantilla antes:", tamano_antes, ", despues:", tamano_despues)

    elif opcion == "4":
        # esta opcion solo muestra como esta la plantilla de cada equipo en este momento
        if partido is None:
            print("Error: primero registre los equipos.")
        else:
            print("\n--- NOMINA ACTUAL ---")
            print("Equipo:", partido.equipo1.nombre)
            print(partido.equipo1.plantilla)
            print("Equipo:", partido.equipo2.nombre)
            print(partido.equipo2.plantilla)
            print("----------------------")
    elif opcion == "5":
        # esta opcion saca todos los eventos de la cola y los muestra en orden
        if partido is None:
            print("Error: primero registre los equipos.")
        else:
            print("\n--- RESUMEN DEL PARTIDO ---")
            if len(partido.eventos) == 0:
                print("No hay eventos registrados todavia.")
            else:
                while len(partido.eventos) > 0:
                    evento = partido.eventos.popleft()  # sacamos del principio de la cola 
                    print("Minuto", evento["minuto"], "-", evento["tipo_evento"], "-", evento["jugador_involucrado"])
            print("----------------------------")

    elif opcion == "6":
        print("Programa finalizado.")
        break  # con esto se sale del menu y termina el programa

    else:
        print("Opcion incorrecta.")