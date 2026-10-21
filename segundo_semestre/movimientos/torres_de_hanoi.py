def imprimir_torres(torres, n):
    """
    Dibuja las torres y sus discos de arriba hacia abajo.
    El tamaño del disco (1, 2, 3...) define cuántos caracteres '_' se dibujan.
    """
    print("")
    # Recorremos los niveles de arriba hacia abajo (desde n-1 hasta 0)
    for nivel in range(n - 1, -1, -1):
        linea = ""
        for poste in ['A', 'B', 'C']:
            discos_en_poste = torres[poste]
            
            # Si hay un disco en este nivel del poste, lo dibujamos
            if nivel < len(discos_en_poste):
                disco = discos_en_poste[nivel]
                espacios = " " * (n - disco)
                asteriscos = "_" * disco
                # Dibujamos el disco: ej. __|__
                dibujo = espacios + asteriscos + "|" + asteriscos + espacios
                linea += dibujo + "   "
            else:
                # Si no hay disco, dibujamos solo el poste vacío
                espacios = " " * n
                dibujo = espacios + "|" + espacios
                linea += dibujo + "   "
        print(linea)
    
    # Dibujamos la base de las 3 torres
    base = "-" * (n * 2 + 1)
    print(f"{base}   {base}   {base}")
    
    # Etiquetamos las torres
    espacios_letra = " " * n
    print(f"{espacios_letra}A{espacios_letra}   {espacios_letra}B{espacios_letra}   {espacios_letra}C{espacios_letra}")
    print("\n" + "="*50)

def mover_disco_visual(origen, destino, torres, n):
    """
    Saca el disco superior de la torre origen y lo pone en la torre destino.
    """
    # Sacamos (desapilamos) el último disco ingresado
    disco = torres[origen].pop()
    # Lo agregamos (apilamos) en la nueva torre
    torres[destino].append(disco)
    
    print(f"\n[*] Moviendo el disco de tamaño {disco} desde la Torre {origen} hacia la Torre {destino}")
    imprimir_torres(torres, n)

def hanoi_recursivo(cantidad_discos, origen, auxiliar, destino, torres, total_discos):
    # Caso Base: Si solo queda 1 disco en este sub-problema, muévelo a su destino
    if cantidad_discos == 1:
        mover_disco_visual(origen, destino, torres, total_discos)
        return

    # Paso 1: Mover (n-1) discos al poste auxiliar
    hanoi_recursivo(cantidad_discos - 1, origen, destino, auxiliar, torres, total_discos)
    
    # Paso 2: Mover el disco grande que quedó libre al poste destino
    mover_disco_visual(origen, destino, torres, total_discos)
    
    # Paso 3: Mover los (n-1) discos del poste auxiliar al poste destino
    hanoi_recursivo(cantidad_discos - 1, auxiliar, origen, destino, torres, total_discos)

# ==========================================
# CONFIGURACIÓN INICIAL Y EJECUCIÓN
# ==========================================
total_discos = 3

# Inicializamos el diccionario que guarda el estado de cada torre.
# La Torre A empezará con los discos [3, 2, 1] (el 3 está en la base, el 1 en la cima).
torres_estado = {
    'A': [],
    'B': [],
    'C': []
}

# Llenamos la Torre A a la antigua (del más grande al más pequeño)
for i in range(total_discos, 0, -1):
    torres_estado['A'].append(i)

print("ESTADO INICIAL:")
imprimir_torres(torres_estado, total_discos)

# Iniciamos el algoritmo
hanoi_recursivo(total_discos, 'A', 'B', 'C', torres_estado, total_discos)