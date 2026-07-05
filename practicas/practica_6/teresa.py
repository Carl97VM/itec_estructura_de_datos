# ejercicio 1
from collections import deque

# Estructuras principales
cola_normal = deque()
cola_callbacks = deque()
pila_prioridad = []
pila_aux = []

def llegada_llamada(id_llamada, tipo):
    cola_normal.append((id_llamada, tipo))

def atender_siguiente():
    if pila_prioridad:
        cliente = pila_prioridad.pop()
        print(f"Atendiendo desde prioridad: {cliente}")
    elif cola_normal:
        cliente = cola_normal.popleft()
        print(f"Atendiendo desde cola normal: {cliente}")
    else:
        print("No hay llamadas para atender.")

def cliente_cuelga_callback():
    if cola_normal:
        cliente = cola_normal.popleft()
        cola_callbacks.append(cliente)
        print(f"Cliente {cliente} pidió callback.")
    else:
        print("No hay clientes en cola normal.")

def procesar_callback():
    if cola_callbacks:
        cliente = cola_callbacks.popleft()
        # Para poner al frente de la cola normal
        while cola_normal:
            pila_aux.append(cola_normal.popleft())
        cola_normal.append(cliente)
        while pila_aux:
            cola_normal.appendleft(pila_aux.pop())
        print(f"Callback procesado: {cliente} volvió a cola normal.")
    else:
        print("No hay callbacks pendientes.")

def promover_cliente(id_llamada):
    encontrado = False
    while cola_normal:
        cliente = cola_normal.popleft()
        if cliente[0] == id_llamada:
            pila_prioridad.append(cliente)
            encontrado = True
            print(f"Cliente {cliente} promovido a prioridad.")
            break
        else:
            pila_aux.append(cliente)
    # Restaurar los demás en la cola normal
    while pila_aux:
        cola_normal.appendleft(pila_aux.pop())
    if not encontrado:
        print(f"Cliente {id_llamada} no encontrado en cola normal.")

def atender_prioridad():
    if pila_prioridad:
        cliente = pila_prioridad.pop()
        print(f"Atendiendo desde prioridad: {cliente}")
    else:
        print("No hay clientes en prioridad.")

def mostrar_estado():
    print("Cola normal:", list(cola_normal))
    print("Cola callbacks:", list(cola_callbacks))
    print("Pila prioridad:", pila_prioridad)

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Llegada llamada (ID, tipo)")
        print("2. Atender siguiente")
        print("3. Cliente cuelga y solicita callback")
        print("4. Procesar siguiente callback")
        print("5. Promover cliente por tiempo de espera")
        print("6. Atender desde prioridad")
        print("7. Mostrar estado")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            id_llamada = input("Ingrese ID: ")
            tipo = input("Ingrese tipo: ")
            llegada_llamada(id_llamada, tipo)
        elif opcion == "2":
            atender_siguiente()
        elif opcion == "3":
            cliente_cuelga_callback()
        elif opcion == "4":
            procesar_callback()
        elif opcion == "5":
            id_llamada = input("Ingrese ID a promover: ")
            promover_cliente(id_llamada)
        elif opcion == "6":
            atender_prioridad()
        elif opcion == "7":
            mostrar_estado()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar menú
if __name__ == "__main__":
    menu()

# ejercicio 2

from collections import deque

# Estructuras
pila_commits = []       # historial de commits
pila_redo = []          # commits revertidos (para rehacer)
cola_stash = deque()    # cola de stashes (FIFO)
CAPACIDAD_STASH = 5     # capacidad máxima de la cola de stashes

# Operaciones
def commit(mensaje):
    commit_id = len(pila_commits) + len(pila_redo) + len(cola_stash) + 1
    nuevo_commit = {"id": commit_id, "mensaje": mensaje}
    pila_commits.append(nuevo_commit)
    pila_redo.clear()  # limpiar pila redo
    print(f"Commit realizado: {nuevo_commit}")

def revert():
    if pila_commits:
        ultimo = pila_commits.pop()
        pila_redo.append(ultimo)
        print(f"Revert: {ultimo}")
    else:
        print("No hay commits para revertir.")

def redo():
    if pila_redo:
        commit_rehecho = pila_redo.pop()
        pila_commits.append(commit_rehecho)
        print(f"Redo: {commit_rehecho}")
    else:
        print("No hay commits para rehacer.")

def stash():
    # Guardar copia del estado actual (último commit)
    if pila_commits:
        estado = pila_commits[-1].copy()
        if len(cola_stash) >= CAPACIDAD_STASH:
            descartado = cola_stash.popleft()
            print(f"Stash lleno, descartado: {descartado}")
        cola_stash.append(estado)
        print(f"Stash guardado: {estado}")
    else:
        print("No hay commits para guardar en stash.")

def apply_stash():
    if cola_stash:
        estado = cola_stash.popleft()
        pila_commits.append(estado)
        print(f"Stash aplicado como commit: {estado}")
    else:
        print("No hay stashes para aplicar.")

def mostrar_historial():
    print("\n--- Estado actual ---")
    print("Commits:", pila_commits)
    print("Redo:", pila_redo)
    print("Stashes:", list(cola_stash))

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Commit (mensaje)")
        print("2. Revert")
        print("3. Redo")
        print("4. Stash")
        print("5. Apply stash")
        print("6. Mostrar historial")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            mensaje = input("Ingrese mensaje del commit: ")
            commit(mensaje)
        elif opcion == "2":
            revert()
        elif opcion == "3":
            redo()
        elif opcion == "4":
            stash()
        elif opcion == "5":
            apply_stash()
        elif opcion == "6":
            mostrar_historial()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()

# EJERCICIO 3

from collections import deque

# Estructuras
cola_equipos = deque()       # cola de equipos en rotación
tareas_por_equipo = {}       # diccionario: equipoID -> cola de tareas
pila_penalizaciones = []     # pila global de penalizaciones

# Operaciones
def agregar_tarea(equipoID, tareaID):
    if equipoID not in tareas_por_equipo:
        tareas_por_equipo[equipoID] = deque()
        cola_equipos.append(equipoID)
    tareas_por_equipo[equipoID].append(tareaID)
    print(f"Tarea {tareaID} agregada al equipo {equipoID}")

def procesar_siguiente():
    if not cola_equipos:
        print("No hay equipos en rotación.")
        return
    equipo = cola_equipos.popleft()
    if tareas_por_equipo[equipo]:
        tarea = tareas_por_equipo[equipo].popleft()
        print(f"Procesando tarea {tarea} del equipo {equipo}")
        # Si aún quedan tareas, el equipo vuelve a la cola
        if tareas_por_equipo[equipo]:
            cola_equipos.append(equipo)
    else:
        print(f"Equipo {equipo} no tiene tareas.")

def penalizar_tarea_actual(equipoID, tareaID):
    pila_penalizaciones.append((equipoID, tareaID))
    print(f"Tarea {tareaID} del equipo {equipoID} penalizada.")

def reinsertar_penalizaciones():
    while pila_penalizaciones:
        equipoID, tareaID = pila_penalizaciones.pop()
        if equipoID not in tareas_por_equipo:
            tareas_por_equipo[equipoID] = deque()
            cola_equipos.append(equipoID)
        tareas_por_equipo[equipoID].append(tareaID)
        print(f"Tarea {tareaID} reinsertada al final del equipo {equipoID}")

def mostrar_estado():
    print("\n--- Estado actual ---")
    for equipo, cola in tareas_por_equipo.items():
        print(f"Equipo {equipo}: {list(cola)}")
    print("Cola de equipos:", list(cola_equipos))
    print("Pila penalizaciones:", pila_penalizaciones)

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea a equipo (equipoID, tareaID)")
        print("2. Procesar siguiente tarea")
        print("3. Penalizar tarea actual")
        print("4. Reinsertar penalizaciones")
        print("5. Mostrar estado")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            equipoID = input("Ingrese ID del equipo: ")
            tareaID = input("Ingrese ID de la tarea: ")
            agregar_tarea(equipoID, tareaID)
        elif opcion == "2":
            procesar_siguiente()
        elif opcion == "3":
            equipoID = input("Ingrese ID del equipo: ")
            tareaID = input("Ingrese ID de la tarea: ")
            penalizar_tarea_actual(equipoID, tareaID)
        elif opcion == "4":
            reinsertar_penalizaciones()
        elif opcion == "5":
            mostrar_estado()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()

# EJERCICIO 4

from collections import deque

# Estructuras
cola_solicitudes = deque()   # solicitudes normales
pila_overrides = []          # overrides/emergencias
pila_aux = []                # auxiliar para cancelar solicitudes
piso_actual = 0              # piso actual del ascensor
distancia_total = 0          # distancia recorrida
movimientos = 0              # cantidad de movimientos

# Operaciones
def solicitar_piso(piso):
    cola_solicitudes.append(piso)
    print(f"Solicitud normal registrada: piso {piso}")

def solicitar_override(piso, prioridad):
    pila_overrides.append((piso, prioridad))
    print(f"Override registrado: piso {piso} con prioridad {prioridad}")

def mover_ascensor():
    global piso_actual, distancia_total, movimientos
    if pila_overrides:
        piso, prioridad = pila_overrides.pop()
        print(f"Atendiendo OVERRIDE: piso {piso} (prioridad {prioridad})")
    elif cola_solicitudes:
        piso = cola_solicitudes.popleft()
        print(f"Atendiendo solicitud normal: piso {piso}")
    else:
        print("No hay solicitudes pendientes.")
        return
    distancia = abs(piso - piso_actual)
    distancia_total += distancia
    movimientos += 1
    print(f"Ascensor se movió de {piso_actual} a {piso} (distancia {distancia})")
    piso_actual = piso

def cancelar_solicitud(piso):
    encontrado = False
    while cola_solicitudes:
        solicitud = cola_solicitudes.popleft()
        if solicitud == piso and not encontrado:
            print(f"Solicitud de piso {piso} cancelada.")
            encontrado = True
        else:
            pila_aux.append(solicitud)
    while pila_aux:
        cola_solicitudes.appendleft(pila_aux.pop())
    if not encontrado:
        print(f"No se encontró la solicitud de piso {piso} en la cola.")

def mostrar_estado():
    print("\n--- Estado actual ---")
    print("Cola de solicitudes:", list(cola_solicitudes))
    print("Pila de overrides:", pila_overrides)
    print(f"Piso actual: {piso_actual}")
    print(f"Movimientos: {movimientos}, Distancia total: {distancia_total}")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Solicitar piso (número de piso)")
        print("2. Solicitar override (número de piso, prioridad)")
        print("3. Mover ascensor")
        print("4. Cancelar solicitud")
        print("5. Mostrar cola y pila")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            piso = int(input("Ingrese número de piso: "))
            solicitar_piso(piso)
        elif opcion == "2":
            piso = int(input("Ingrese número de piso: "))
            prioridad = input("Ingrese prioridad: ")
            solicitar_override(piso, prioridad)
        elif opcion == "3":
            mover_ascensor()
        elif opcion == "4":
            piso = int(input("Ingrese número de piso a cancelar: "))
            cancelar_solicitud(piso)
        elif opcion == "5":
            mostrar_estado()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()

# EJERCICIO 5

from collections import deque

# Estructuras
cola_frase = deque()             # cola global de sílabas
pilas_jugadores = {}             # diccionario: jugador -> pila de sus jugadas
pila_aux = []                    # auxiliar para deshacer
historial_rondas = []            # pila de rondas completadas

# Operaciones
def jugador_añade(jugador, silaba):
    if jugador not in pilas_jugadores:
        pilas_jugadores[jugador] = []
    cola_frase.append((jugador, silaba))
    pilas_jugadores[jugador].append(silaba)
    print(f"Jugador {jugador} añadió sílaba: {silaba}")

def jugador_deshace(jugador):
    if jugador not in pilas_jugadores or not pilas_jugadores[jugador]:
        print(f"Jugador {jugador} no tiene jugadas para deshacer.")
        return
    ultima = pilas_jugadores[jugador].pop()
    encontrado = False
    # Buscar y eliminar de la cola
    while cola_frase:
        jug, sil = cola_frase.popleft()
        if jug == jugador and sil == ultima and not encontrado:
            print(f"Jugador {jugador} deshizo su sílaba: {sil}")
            encontrado = True
        else:
            pila_aux.append((jug, sil))
    # Reconstruir la cola
    while pila_aux:
        cola_frase.appendleft(pila_aux.pop())
    if not encontrado:
        print("No se encontró la sílaba en la cola.")

def mostrar_frase():
    frase = " ".join([sil for _, sil in cola_frase])
    print(f"Frase actual: {frase}")

def finalizar_ronda():
    ronda = " ".join([sil for _, sil in cola_frase])
    historial_rondas.append(ronda)
    cola_frase.clear()
    print(f"Ronda finalizada. Frase: '{ronda}' guardada en historial.")

def mostrar_estado():
    print("\n--- Estado actual ---")
    mostrar_frase()
    print("Historial de rondas:", historial_rondas)
    for jugador, pila in pilas_jugadores.items():
        print(f"Jugador {jugador} pila: {pila}")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Jugador X añade sílaba")
        print("2. Jugador X deshace última sílaba")
        print("3. Mostrar frase actual")
        print("4. Finalizar ronda")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            jugador = input("Ingrese ID del jugador: ")
            silaba = input("Ingrese sílaba: ")
            jugador_añade(jugador, silaba)
        elif opcion == "2":
            jugador = input("Ingrese ID del jugador: ")
            jugador_deshace(jugador)
        elif opcion == "3":
            mostrar_frase()
        elif opcion == "4":
            finalizar_ronda()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()