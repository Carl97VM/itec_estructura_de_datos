def imprimir_torres(torres, n):
    """
    Dibuja las torres y sus discos de arriba hacia abajo.
    El tamaño del disco (1, 2, 3...) define cuántos caracteres '_' se dibujan.
    """
    print("")
    for nivel in range(n - 1, -1, -1):
        linea = ""
        for poste in ['A', 'B', 'C']:
            discos_en_poste = torres[poste]

            if nivel < len(discos_en_poste):
                disco = discos_en_poste[nivel]
                espacios = " " * (n - disco)
                asteriscos = "_" * disco
                dibujo = espacios + asteriscos + "|" + asteriscos + espacios
                linea += dibujo + "   "
            else:
                espacios = " " * n
                dibujo = espacios + "|" + espacios
                linea += dibujo + "   "
        print(linea)

    base = "-" * (n * 2 + 1)
    print(f"{base}   {base}   {base}")

    espacios_letra = " " * n
    print(f"{espacios_letra}A{espacios_letra}   {espacios_letra}B{espacios_letra}   {espacios_letra}C{espacios_letra}")
    print("\n" + "=" * 50)


def mover_disco_visual(origen, destino, torres, n, estado_modo=None):
    """
    Saca el disco superior de la torre origen y lo pone en la torre destino.
    Incluye:
      - Modificación B: Validación estricta de física antes de hacer .append().
      - Modificación A: Pausa interactiva después de cada movimiento (con opción SALTAR).
    """
    if not torres[origen]:
        raise ValueError(f"La torre de origen '{origen}' está vacía.")

    # Sacamos (desapilamos) el último disco ingresado
    disco = torres[origen].pop()

    # Modificación B: Validación estricta de peso antes de apilar en destino
    if len(torres[destino]) > 0 and disco > torres[destino][-1]:
        # Restauramos el disco al origen para no corromper el estado antes de lanzar la alarma
        torres[origen].append(disco)
        raise ValueError("¡Alarma! Intento de romper la regla de peso")

    # Lo agregamos (apilamos) en la nueva torre
    torres[destino].append(disco)

    print(f"\n[*] Moviendo el disco de tamaño {disco} desde la Torre {origen} hacia la Torre {destino}")
    imprimir_torres(torres, n)

    # Modificación A: Modo Interactivo / Paso a Paso
    if estado_modo is not None and not estado_modo.get("saltar", False):
        try:
            respuesta = input(
                "Presiona ENTER para el siguiente movimiento (o escribe SALTAR para terminar sin pausas): "
            ).strip().upper()
            if respuesta == "SALTAR":
                estado_modo["saltar"] = True
                print("[!] Modo continuo activado. Resolviendo el resto sin pausas...")
        except EOFError:
            estado_modo["saltar"] = True


def hanoi_recursivo(cantidad_discos, origen, auxiliar, destino, torres, total_discos, estado_modo):
    # Caso Base: Si solo queda 1 disco en este sub-problema, muévelo a su destino
    if cantidad_discos == 1:
        mover_disco_visual(origen, destino, torres, total_discos, estado_modo)
        return

    # Paso 1: Mover (n-1) discos al poste auxiliar
    hanoi_recursivo(cantidad_discos - 1, origen, destino, auxiliar, torres, total_discos, estado_modo)

    # Paso 2: Mover el disco grande que quedó libre al poste destino
    mover_disco_visual(origen, destino, torres, total_discos, estado_modo)

    # Paso 3: Mover los (n-1) discos del poste auxiliar al poste destino
    hanoi_recursivo(cantidad_discos - 1, auxiliar, origen, destino, torres, total_discos, estado_modo)


if __name__ == "__main__":
    total_discos = 3

    torres_estado = {
        'A': [],
        'B': [],
        'C': []
    }

    for i in range(total_discos, 0, -1):
        torres_estado['A'].append(i)

    print("ESTADO INICIAL:")
    imprimir_torres(torres_estado, total_discos)

    # Estado compartido para controlar si el usuario escribió SALTAR
    estado_interactivo = {"saltar": False}

    hanoi_recursivo(total_discos, 'A', 'B', 'C', torres_estado, total_discos, estado_interactivo)
    print("\n¡Torres de Hanói completadas correctamente!")
