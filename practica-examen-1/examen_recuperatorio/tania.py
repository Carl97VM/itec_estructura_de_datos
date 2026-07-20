from collections import deque  # Importa deque desde collections para manejar la estructura de Cola (FIFO)

# --- ESTRUCTURAS DE DATOS ---

class Equipo:  # Define la clase Equipo para almacenar los datos de cada selección
    def __init__(self, nombre):  # Método constructor que se ejecuta al crear un objeto Equipo
        self.nombre = nombre  # Asigna el nombre del equipo (ej. "Argentina") al atributo del objeto
        self.plantilla = []  # Inicializa una lista vacía que utilizaremos estrictamente como una Pila

class Partido:  # Define la clase Partido para controlar la lógica del juego y los eventos
    def __init__(self, equipo1, equipo2):  # Método constructor que vincula los dos equipos rivales
        self.equipo1 = equipo1  # Guarda el objeto del primer equipo en el atributo self.equipo1
        self.equipo2 = equipo2  # Guarda el objeto del segundo equipo en el atributo self.equipo2
        self.eventos = deque()  # Inicializa una cola vacía para registrar cronológicamente los goles y cambios

    def buscar_jugador_en_pila(self, equipo, nombre_jugador):  # Función para verificar si un jugador existe en la pila
        encontrado = False  # Variable booleana (bandera) que cambia a True si el jugador es hallado
        pila_aux = []  # Crea una lista vacía que funcionará como Pila Auxiliar temporal

        while len(equipo.plantilla) > 0:  # Ciclo que se ejecuta mientras queden elementos en la pila del equipo
            jugador = equipo.plantilla.pop()  # Extrae (pop) el jugador que está en el tope de la pila
            if jugador == nombre_jugador:  # Condición para evaluar si ese jugador es el que estamos buscando
                encontrado = True  # Si coincide, marcamos la bandera como verdadera (encontrado)
            pila_aux.append(jugador)  # Guarda al jugador extraído en la pila auxiliar para no perder el dato

        while len(pila_aux) > 0:  # Ciclo para regresar los elementos de la pila auxiliar a la original
            equipo.plantilla.append(pila_aux.pop())  # Extrae de la auxiliar y lo reinserta en la plantilla original

        return encontrado  # Retorna el resultado de la búsqueda (True si existía, False si no)

    def registrar_gol(self, minuto, nombre_jugador):  # Función para almacenar un gol en la cola de eventos
        en_equipo1 = self.buscar_jugador_en_pila(self.equipo1, nombre_jugador)  # Busca al jugador en el equipo 1
        en_equipo2 = self.buscar_jugador_en_pila(self.equipo2, nombre_jugador)  # Busca al jugador en el equipo 2

        if en_equipo1 or en_equipo2:  # Estructura condicional: si el jugador existe en cualquiera de los dos equipos
            evento = {  # Crea un diccionario para representar el nodo del evento
                "minuto": minuto,  # Asigna el minuto ingresado al diccionario
                "tipo_evento": "GOL ⚽",  # Define el tipo de evento como un gol
                "jugador_involucrado": nombre_jugador  # Asigna el nombre del anotador al diccionario
            }  # Cierre del diccionario
            self.eventos.append(evento)  # Encola (añade al final) el evento dentro de la cola FIFO de eventos
            print(f"¡Gol registrado de {nombre_jugador}!")  # Imprime un mensaje de confirmación en la consola
        else:  # Si la búsqueda en ambos equipos devolvió False
            print("Error: El jugador no está en la plantilla.")  # Muestra mensaje de error por pantalla

    def realizar_cambio(self, equipo, jugador_sale, jugador_entra):  # Función para sustituir un jugador en la pila
        pila_aux = []  # Inicializa la pila auxiliar obligatoria para la manipulación destructiva
        encontrado = False  # Bandera para saber si el jugador que va a salir realmente jugaba en el equipo

        while len(equipo.plantilla) > 0:  # Recorre la pila del equipo extrayendo elementos uno a uno
            jugador = equipo.plantilla.pop()  # Saca el elemento del tope de la pila
            if jugador == jugador_sale:  # Compara si el jugador extraído es el que debe salir
                encontrado = True  # Activa la bandera confirmando que fue localizado
                pila_aux.append(jugador_entra)  # En lugar de regresar al que sale, inserta al jugador entrante en la auxiliar
                break  # Rompe el ciclo inmediatamente porque ya se realizó la sustitución en esa posición
            else:  # Si no es el jugador buscado
                pila_aux.append(jugador)  # Lo resguarda temporalmente en la pila auxiliar

        if encontrado:  # Si la sustitución fue exitosa (el jugador a salir sí existía)
            while len(pila_aux) > 0:  # Ciclo para vaciar la pila auxiliar y restaurar el equipo
                equipo.plantilla.append(pila_aux.pop())  # Regresa los elementos en el orden correspondiente a la pila principal
           
            evento = {  # Crea un diccionario para documentar el cambio realizado
                "minuto": "N/A",  # Asigna un valor por defecto al minuto del cambio
                "tipo_evento": "CAMBIO 🔄",  # Clasifica el tipo de evento como una sustitución
                "jugador_involucrado": f"Sale: {jugador_sale} -> Entra: {jugador_entra}"  # Describe la acción del cambio
            }  # Cierre del diccionario
            self.eventos.append(evento)  # Registra (encola) la acción en la cola cronológica de eventos del partido
            print("Cambio exitoso.")  # Muestra un mensaje de éxito en la consola
        else:  # En caso de que el jugador que supuestamente sale nunca haya estado en la pila
            while len(pila_aux) > 0:  # Ciclo de emergencia para no romper la estructura original
                equipo.plantilla.append(pila_aux.pop())  # Devuelve los datos de la auxiliar dejando la pila como estaba
            print("Error: El jugador no fue encontrado.")  # Muestra una notificación de fallo por pantalla

    def mostrar_nomina(self, equipo):  # Función para listar los jugadores vigentes en las pilas
        print(f"\n--- Nómina de {equipo.nombre} ---")  # Imprime el encabezado con el nombre de la selección
        pila_aux = []  # Genera una pila auxiliar para poder leer los datos sin borrarlos definitivamente
       
        while len(equipo.plantilla) > 0:  # Bucle que se repite hasta dejar vacía la pila del equipo
            jugador = equipo.plantilla.pop()  # Extrae el elemento del tope
            print(f"- {jugador}")  # Imprime en pantalla el nombre del jugador extraído
            pila_aux.append(jugador)  # Deposita al jugador en la pila auxiliar para conservarlo
       
        while len(pila_aux) > 0:  # Bucle para regresar la estructura a su estado original
            equipo.plantilla.append(pila_aux.pop())  # Saca de la auxiliar y lo vuelve a apilar en la plantilla

    def ver_resumen_partido(self):  # Función para imprimir y vaciar la cola de eventos al concluir el partido
        print("\n=== RESUMEN FINAL ===")  # Imprime la cabecera estética del reporte final
        if not self.eventos:  # Condicional que evalúa si la cola de eventos se encuentra completamente vacía
            print("No hay eventos.")  # Indica en la terminal que no hubo incidencias registradas
            return  # Corta la ejecución de la función de manera anticipada

        while len(self.eventos) > 0:  # Bucle que opera de forma iterativa mientras existan nodos en la cola
            ev = self.eventos.popleft()  # Extrae el primer evento registrado de la cola (Comportamiento FIFO / Primero en entrar)
            print(f"[{ev['tipo_evento']}] Minuto: {ev['minuto']} | {ev['jugador_involucrado']}")  # Imprime la información formateada
        print("=====================")  # Cierre estético de la impresión del resumen


# --- MENÚ DE OPERACIONES DE USUARIO ---

def menu():  # Función principal encargada de desplegar la interfaz de menú interactivo
    eq1 = Equipo("Argentina")  # Instancia (crea) el objeto para el equipo 1 llamándolo "Argentina"
    eq2 = Equipo("Francia")  # Instancia (crea) el objeto para el equipo 2 llamándolo "Francia"
    partido = Partido(eq1, eq2)  # Vincula ambos objetos de equipo creando una instancia de la clase Partido
    equipos_cargados = False  # Bandera de control para impedir que operen el sistema si no hay jugadores registrados

    while True:  # Bucle infinito que mantiene el menú activo hasta que el usuario decida salir deliberadamente
        print("\n--- MENÚ FIFA WORLD CUP 2026 ---")  # Título principal expuesto en el menú
        print("1. Registrar Equipos (Validar 16)")  # Opción asignada al proceso de carga y conteo de jugadores
        print("2. Registrar Gol")  # Opción asignada a la inserción de goles en la cola
        print("3. Realizar Cambio")  # Opción asignada al algoritmo de intercambio en las pilas
        print("4. Mostrar Nóminas")  # Opción asignada a la lectura no destructiva de las pilas
        print("5. Ver Resumen del Partido")  # Opción asignada al vaciado y procesamiento FIFO de la cola
        print("6. Salir")  # Opción asignada al cierre definitivo del flujo de ejecución
       
        opcion = input("Seleccione una opción: ")  # Captura por teclado el número digitado por el operador

        if opcion == "1":  # Bloque lógico si el usuario presiona la opción 1
            jugadores_arg = [  # Array estático simulando la base de datos de Argentina con 16 personas reales
                "Emiliano Martinez", "Nahuel Molina", "Cristian Romero", "Nicolas Otamendi",
                "Nicolas Tagliafico", "Rodrigo De Paul", "Enzo Fernandez", "Alexis Mac Allister",
                "Lionel Messi", "Julian Alvarez", "Angel Di Maria",
                "Geronimo Rulli", "Gonzalo Montiel", "German Pezzella", "Leandro Paredes", "Lautaro Martinez"
            ]  # Cierre del array de nombres
           
            jugadores_fra = [  # Array estático simulando la base de datos de Francia con 16 personas reales
                "Hugo Lloris", "Jules Kounde", "Raphael Varane", "Dayot Upamecano",
                "Theo Hernandez", "Aurelien Tchouameni", "Adrien Rabiot", "Ousmane Dembele",
                "Antoine Griezmann", "Kylian Mbappe", "Olivier Giroud",
                "Steve Mandanda", "Benjamin Pavard", "Ibrahima Konate", "Eduardo Camavinga", "Kingsley Coman"
            ]  # Cierre del array de nombres

            for j in jugadores_arg:  # Itera cada elemento de la lista de strings de Argentina
                eq1.plantilla.append(j)  # Apila mediante append() cada string en la pila del equipo 1
               
            for j in jugadores_fra:  # Itera cada elemento de la lista de strings de Francia
                eq2.plantilla.append(j)  # Apila mediante append() cada string en la pila del equipo 2

            if len(eq1.plantilla) >= 16 and len(eq2.plantilla) >= 16:  # Validación obligatoria: Compara tamaños de las pilas
                print("\nEquipos cargados y validados.")  # Informa al usuario que las dos pilas cumplen la restricción de tamaño
                equipos_cargados = True  # Modifica la bandera de control para desbloquear el acceso al resto del menú
            else:  # Si por alguna razón alguna de las listas tuviese menos de 16 elementos
                print("\nError: Faltan jugadores.")  # Notifica que la validación falló rotundamente
                eq1.plantilla = []  # Resetea y limpia la pila del equipo 1
                eq2.plantilla = []  # Resetea y limpia la pila del equipo 2

        elif opcion == "2":  # Bloque lógico si se elige la opción 2
            if not equipos_cargados:  # Valida si la bandera de carga sigue en estado False
                print("Primero cargue los equipos.")  # Restringe el paso e instruye usar primero la opción 1
                continue  # Salta el resto del código del ciclo saltando al inicio del menú de nuevo
           
            minuto = input("Minuto: ")  # Pide y almacena en memoria la marca de tiempo del gol
            jugador = input("Jugador: ")  # Pide y almacena en memoria la identidad del futbolista
            partido.registrar_gol(minuto, jugador)  # Ejecuta el método pasándole las dos variables capturadas

        elif opcion == "3":  # Bloque lógico si se presiona la opción 3
            if not equipos_cargados:  # Comprobación de seguridad para garantizar que existan plantillas guardadas
                print("Primero cargue los equipos.")  # Impide la ejecución si las pilas están vacías
                continue  # Fuerza la redirección del flujo de control directo al menú primordial
           
            print("1. Argentina\n2. Francia")  # Despliega submenú veloz para identificar el conjunto afectado
            selec = input("Equipo: ")  # Recibe el índice de selección numérica (1 o 2)
            equipo_obj = eq1 if selec == "1" else eq2  # Operador ternario para asignar dinámicamente el objeto correspondiente
           
            sale = input("Sale: ")  # Captura del string con el nombre del futbolista que abandona la actividad
            entra = input("Entra: ")  # Captura del string con el nombre de la variante que ocupará su lugar
            partido.realizar_cambio(equipo_obj, sale, entra)  # Invoca la lógica del algoritmo de intercambio

        elif opcion == "4":  # Bloque lógico si el usuario digita la opción 4
            if not equipos_cargados:  # Validación de existencia previa de registros en memoria dinámica
                print("Primero cargue los equipos.")  # Bloqueo de visualización por falta de datos base
                continue  # Interrumpe el flujo corriente mandándolo de vuelta al menú inicial
            partido.mostrar_nomina(eq1)  # Llama al visualizador no destructivo para la pila de Argentina
            partido.mostrar_nomina(eq2)  # Llama al visualizador no destructivo para la pila de Francia

        elif opcion == "5":  # Bloque lógico si se activa la opción 5
            if not equipos_cargados:  # Filtro preventivo anti-errores por falta de inicialización previa
                print("Primero cargue los equipos.")  # Notificación de requisito previo obligatorio en consola
                continue  # Salta la ejecución y reactiva la espera de instrucciones en el menú
            partido.ver_resumen_partido()  # Llama al procedimiento que procesa, imprime y destruye la cola de eventos

        elif opcion == "6":  # Bloque lógico en caso de presionar la opción de salida 6
            print("Saliendo...")  # Imprime un breve aviso de despedida en el flujo de salida
            break  # Destruye el bucle While interrumpiendo el programa permanentemente
        else:  # Captura cualquier carácter o número fuera del rango del 1 al 6
            print("Opción inválida.")  # Imprime advertencia de selección errónea

if __name__ == "__main__":  # Valida si este script de Python es ejecutado directamente como el programa raíz
    menu()  # Dispara la ejecución del menú para dar inicio a toda la aplicación interactiva
