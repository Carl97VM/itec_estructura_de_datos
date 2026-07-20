from collections import deque # Importamos deque para implementar la cola de eventos del partido

class Equipo: # Clase que representa un equipo de fútbol utilizando una pila para gestionar la plantilla de jugadores
   
    def __init__(self, nombre): # Constructor de la clase Equipo que inicializa el nombre del equipo y la pila de jugadores.      
        self.nombre = nombre
        self.plantilla = []  # Pila para gestionar jugadores (el último elemento es el tope)
   
    def agregar_jugador(self, jugador): # Agrega un jugador a la plantilla del equipo. El jugador se coloca en el tope de la pila.      
        self.plantilla.append(jugador)
   
    def obtener_tamanio(self): # Devuelve el número de jugadores en la plantilla del equipo.
        return len(self.plantilla)
   
    def mostrar_plantilla(self): # Muestra la plantilla de jugadores del equipo desde el tope hasta el fondo de la pila.
        print(f"Plantilla de {self.nombre} (tope -> fondo):")
        if not self.plantilla:
            print("  La plantilla está vacía")
        else:
            # Mostrar desde el tope (último elemento) hasta el fondo (primer elemento)
            for i in range(len(self.plantilla) - 1, -1, -1):
                print(f"  {self.plantilla[i]}")
        print(f"Total de jugadores: {len(self.plantilla)}\n")
   
    def buscar_y_remover_jugador(self, jugador_buscar): # Busca y remueve un jugador específico de la pila usando una pila auxiliar.        
        pila_auxiliar = []  # Pila auxiliar para almacenar jugadores temporalmente
        encontrado = False
        jugador_removido = None
       
       
        while self.plantilla and not encontrado:  # Desapilar todos los elementos hasta encontrar el jugador buscado
            jugador_actual = self.plantilla.pop()  # Desapilar el tope
           
            if jugador_actual == jugador_buscar:
                # Encontramos el jugador
                encontrado = True
                jugador_removido = jugador_actual
            else:
                # Si no es el jugador buscado, lo guardamos en la pila auxiliar
                pila_auxiliar.append(jugador_actual)
       
        # Reinsertar los elementos de la pila auxiliar a la pila original
        # Esto mantiene el orden original (sin el jugador removido)
        while pila_auxiliar:
            self.plantilla.append(pila_auxiliar.pop())
       
        return encontrado, jugador_removido
   
    def verificar_jugador_en_plantilla(self, jugador_buscar): # Verifica si un jugador específico está presente en la plantilla del equipo.      
        pila_auxiliar = []  # Pila auxiliar para preservar la estructura
        existe = False
       
        # Recorremos la pila completa para buscar el jugador
        while self.plantilla:
            jugador_actual = self.plantilla.pop()
            pila_auxiliar.append(jugador_actual)
           
            if jugador_actual == jugador_buscar:
                existe = True
       
        # Restauramos la pila original
        while pila_auxiliar:
            self.plantilla.append(pila_auxiliar.pop())
       
        return existe
   
    def obtener_jugadores_en_cancha(self): # Devuelve una lista de los jugadores que están actualmente en la cancha (los primeros 11 jugadores de la pila).
                                           # Como la pila tiene el tope al final, los titulares estarían al principio, pero necesitamos obtenerlos sin modificar la pila
        pila_auxiliar = []
        titulares = []
       
        # Desapilamos todos los elementos para obtener los que están en el fondo
        while self.plantilla:
            jugador = self.plantilla.pop()
            pila_auxiliar.append(jugador)
       
        # Los primeros 11 en ser desapilados son los que estaban en el fondo (titulares)
        # Pero como los desapilamos en orden inverso, necesitamos revertir
        jugadores = []
        while pila_auxiliar:
            jugador = pila_auxiliar.pop()
            jugadores.append(jugador)
            self.plantilla.append(jugador)  # Restauramos la pila
       
        # Los primeros 11 son los titulares
        titulares = jugadores[:11] if len(jugadores) >= 11 else jugadores
        return titulares


class Partido: # Clase que representa un partido de fútbol entre dos equipos, gestionando eventos como goles y cambios de jugadores mediante una cola de eventos.
   
    def __init__(self, equipo1, equipo2): # Constructor de la clase Partido que inicializa los equipos, la cola de eventos y las estadísticas del partido.        
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.eventos = deque()  # Cola para el resumen de eventos
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.minuto_actual = 0
   
    def validar_equipos(self): # Valida que ambos equipos tengan al menos 16 jugadores en su plantilla.
       
        return (self.equipo1.obtener_tamanio() >= 16 and # Validación de que ambos equipos tengan al menos 16 jugadores
                self.equipo2.obtener_tamanio() >= 16)
   
    def registrar_gol(self, minuto, equipo_nombre, jugador): # Registra un gol en el partido, validando el minuto, el equipo y el jugador involucrado. Utiliza una cola para almacenar los eventos del partido.
       
        # Validar que el minuto sea válido
        if minuto < 0 or minuto > 120:
            print("Error: El minuto debe estar entre 0 y 120")
            return False
       
        # Determinar qué equipo es
        if equipo_nombre.lower() == self.equipo1.nombre.lower():
            equipo = self.equipo1
            # Validar que el jugador esté en la plantilla
            if not equipo.verificar_jugador_en_plantilla(jugador):
                print(f"Error: El jugador {jugador} no está en la plantilla de {equipo_nombre}")
                return False
            self.goles_equipo1 += 1
        elif equipo_nombre.lower() == self.equipo2.nombre.lower():
            equipo = self.equipo2
            if not equipo.verificar_jugador_en_plantilla(jugador):
                print(f"Error: El jugador {jugador} no está en la plantilla de {equipo_nombre}")
                return False
            self.goles_equipo2 += 1
        else:
            print(f"Error: Equipo '{equipo_nombre}' no encontrado")
            return False
       
        # Crear el evento y encolarlo
        evento = {
            'minuto': minuto,
            'tipo_evento': 'GOL',
            'jugador_involucrado': jugador,
            'equipo': equipo_nombre
        }
        self.eventos.append(evento)
        self.minuto_actual = max(self.minuto_actual, minuto)
        print(f"¡GOL! {jugador} marca para {equipo_nombre} en el minuto {minuto}")
        return True
   
    def realizar_cambio(self, equipo_nombre, jugador_sale, jugador_entra, minuto):
        """
        Realiza un cambio de jugador en un equipo.
        Utiliza una pila auxiliar para buscar y reemplazar al jugador.
       
        Args:
            equipo_nombre (str): Nombre del equipo donde se hará el cambio
            jugador_sale (str): Nombre del jugador que sale
            jugador_entra (str): Nombre del jugador que entra
            minuto (int): Minuto en que se realiza el cambio
           
        Returns:
            bool: True si el cambio se realizó exitosamente
        """
        # Validar el minuto
        if minuto < 0 or minuto > 120:
            print("Error: El minuto debe estar entre 0 y 120")
            return False
       
        # Validar que el minuto sea mayor al último registrado
        if minuto < self.minuto_actual:
            print(f"Error: El minuto {minuto} es anterior al último evento registrado ({self.minuto_actual})")
            return False
       
        # Determinar qué equipo es
        if equipo_nombre.lower() == self.equipo1.nombre.lower():
            equipo = self.equipo1
        elif equipo_nombre.lower() == self.equipo2.nombre.lower():
            equipo = self.equipo2
        else:
            print(f"Error: Equipo '{equipo_nombre}' no encontrado")
            return False
       
        # Verificar que el jugador que sale esté en la plantilla
        if not equipo.verificar_jugador_en_plantilla(jugador_sale):
            print(f"Error: El jugador {jugador_sale} no está en la plantilla de {equipo_nombre}")
            return False
       
        # Verificar que el jugador que entra no esté ya en la plantilla
        if equipo.verificar_jugador_en_plantilla(jugador_entra):
            print(f"Error: El jugador {jugador_entra} ya está en la plantilla de {equipo_nombre}")
            return False
       
        # Realizar el cambio usando pila auxiliar
        encontrado, jugador_removido = equipo.buscar_y_remover_jugador(jugador_sale)
       
        if not encontrado:
            print(f"Error: No se pudo encontrar a {jugador_sale} en {equipo_nombre}")
            return False
       
        # Agregar el nuevo jugador a la plantilla
        equipo.agregar_jugador(jugador_entra)
       
        # Registrar el evento en la cola
        evento = {
            'minuto': minuto,
            'tipo_evento': 'CAMBIO',
            'jugador_involucrado': f"{jugador_sale} -> {jugador_entra}",
            'equipo': equipo_nombre
        }
        self.eventos.append(evento)
        self.minuto_actual = max(self.minuto_actual, minuto)
       
        print(f"Cambio en {equipo_nombre}: Sale {jugador_sale}, entra {jugador_entra} en el minuto {minuto}")
        return True
   
    def mostrar_resumen(self): # Muestra un resumen completo del partido, incluyendo la cronología de eventos y el resultado final. Utiliza la cola de eventos para mostrar los goles y cambios en orden.
       
        print("\n" + "="*60)
        print(f"RESUMEN DEL PARTIDO: {self.equipo1.nombre} vs {self.equipo2.nombre}")
        print("="*60)
       
        if not self.eventos:
            print("No se registraron eventos en el partido.")
            return
       
        print("\nCRONOLOGÍA DE EVENTOS:")
        print("-"*60)
        print(f"{'Minuto':<10} {'Tipo':<15} {'Detalle':<35}")
        print("-"*60)
       
        # Desencolar y mostrar todos los eventos
        contador_eventos = 0
        while self.eventos:
            evento = self.eventos.popleft()  # Desencolar (FIFO)
            contador_eventos += 1
           
            minuto = evento['minuto']
            tipo = evento['tipo_evento']
            detalle = f"{evento['equipo']}: {evento['jugador_involucrado']}"
           
            print(f"{minuto:<10} {tipo:<15} {detalle:<35}")
       
        print("-"*60)
        print(f"Total de eventos registrados: {contador_eventos}")
        print(f"Resultado final: {self.equipo1.nombre} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2.nombre}")
        print("="*60)


def menu_principal(): # Función que implementa el menú principal del sistema de gestión de partidos, permitiendo registrar equipos, goles, cambios y mostrar resúmenes.
   
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE PARTIDOS - FIFA WORLD CUP 2026")
    print("="*60)
   
    # Inicializar variables
    equipo1 = None
    equipo2 = None
    partido = None
   
    while True:
        print("\nMENÚ PRINCIPAL:")
        print("1. Registrar Equipos")
        print("2. Registrar Gol")
        print("3. Realizar Cambio")
        print("4. Mostrar Nómina Actual")
        print("5. Ver Resumen del Partido")
        print("6. Salir")
        print("-"*60)
       
        try:
            opcion = input("Seleccione una opción (1-6): ").strip()
           
            if opcion == '1':
                # Registrar Equipos
                print("\n--- REGISTRO DE EQUIPOS ---")
               
                # Crear equipo 1
                nombre1 = input("Ingresar el nombre del Equipo 1: ").strip()
                equipo1 = Equipo(nombre1)
                print(f"Cargando plantilla de {nombre1} (mínimo 16 jugadores)...")
               
                while equipo1.obtener_tamanio() < 16:
                    jugador = input(f"Ingrese jugador {equipo1.obtener_tamanio() + 1} (o 'fin' para terminar): ").strip()
                    if jugador.lower() == 'fin':
                        if equipo1.obtener_tamanio() < 16:
                            print(f"Error: Necesita 16 jugadores. Actualmente tiene {equipo1.obtener_tamanio()}")
                        continue
                    equipo1.agregar_jugador(jugador)
                    print(f"Jugador {jugador} agregado a {nombre1}")
               
                # Crear equipo 2
                nombre2 = input("Ingrese el nombre del Equipo 2: ").strip()
                equipo2 = Equipo(nombre2)
                print(f"Cargando plantilla de {nombre2} (mínimo 16 jugadores)...")
               
                while equipo2.obtener_tamanio() < 16:
                    jugador = input(f"Ingrese jugador {equipo2.obtener_tamanio() + 1} (o 'fin' para terminar): ").strip()
                    if jugador.lower() == 'fin':
                        if equipo2.obtener_tamanio() < 16:
                            print(f"Error: Necesita 16 jugadores. Actualmente tiene {equipo2.obtener_tamanio()}")
                        continue
                    equipo2.agregar_jugador(jugador)
                    print(f"Jugador {jugador} agregado a {nombre2}")
               
                # Crear el partido
                partido = Partido(equipo1, equipo2)
               
                # Validar equipos
                if partido.validar_equipos():
                    print(f"\n¡Equipos registrados exitosamente!")
                    print(f"{equipo1.nombre}: {equipo1.obtener_tamanio()} jugadores")
                    print(f"{equipo2.nombre}: {equipo2.obtener_tamanio()} jugadores")
                    print("¡El partido está listo para comenzar!")
                else:
                    print("\nError: Ambos equipos deben tener al menos 16 jugadores.")
                    partido = None
               
            elif opcion == '2':
                # Registrar Gol
                if not partido or not partido.validar_equipos():
                    print("Error: Primero debe registrar ambos equipos (opción 1)")
                    continue
               
                print("\n--- REGISTRAR GOL ---")
                minuto = int(input("Ingrese el minuto del gol: "))
                equipo_nombre = input("Ingrese el nombre del equipo que marcó: ").strip()
                jugador = input("Ingrese el nombre del jugador que marcó: ").strip()
               
                partido.registrar_gol(minuto, equipo_nombre, jugador)
               
            elif opcion == '3':
                # Realizar Cambio
                if not partido or not partido.validar_equipos():
                    print("Error: Primero debe registrar ambos equipos (opción 1)")
                    continue
               
                print("\n--- REALIZAR CAMBIO ---")
                equipo_nombre = input("Ingrese el nombre del equipo: ").strip()
                jugador_sale = input("Ingrese el nombre del jugador que sale: ").strip()
                jugador_entra = input("Ingrese el nombre del jugador que entra: ").strip()
                minuto = int(input("Ingrese el minuto del cambio: "))
               
                partido.realizar_cambio(equipo_nombre, jugador_sale, jugador_entra, minuto)
               
            elif opcion == '4':
                # Mostrar Nómina Actual
                if not partido or not partido.validar_equipos():
                    print("Error: Primero debe registrar ambos equipos (opción 1)")
                    continue
               
                print("\n--- NÓMINA ACTUAL ---")
                partido.equipo1.mostrar_plantilla()
                partido.equipo2.mostrar_plantilla()
               
            elif opcion == '5':
                # Ver Resumen del Partido
                if not partido or not partido.validar_equipos():
                    print("Error: Primero debe registrar ambos equipos (opción 1)")
                    continue
               
                partido.mostrar_resumen()
               
            elif opcion == '6':
                # Salir
                print("\n¡Gracias por usar el sistema de gestión de partidos!")
                print("¡Hasta luego!")
                break
               
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 6.")
               
        except ValueError as e:
            print(f"Error: Ingrese un valor numérico válido. {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()