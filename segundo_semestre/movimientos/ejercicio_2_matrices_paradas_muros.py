# Contador global de retrocesos (Backtracking)
contador_backtracking = 0


def imprimir_matriz_resaltada(matriz, n, camino, parada_obligatoria=None):
    """
    Dibuja la matriz. Muestra los números que forman la suma,
    marca los muros (-1) con '#' y la parada obligatoria con '*'.
    """
    print("\nMatriz con el camino encontrado:")
    print("=" * 38)
    for i in range(n):
        linea = ""
        for j in range(n):
            es_parte_del_camino = False
            for pos in camino:
                if pos[0] == i and pos[1] == j:
                    es_parte_del_camino = True
                    break

            if es_parte_del_camino:
                marca = "*" if parada_obligatoria == (i, j) else " "
                linea += f"[{matriz[i][j]:2d}{marca}] "
            elif matriz[i][j] == -1:
                linea += "  #   "
            else:
                linea += "  .   "
        print(linea)
    print("=" * 38)
    print("Leyenda: [n ] = Camino | [n*] = Parada obligatoria | # = Muro (-1)")


def busqueda_recursiva(
    matriz,
    n,
    fila,
    col,
    objetivo,
    suma_actual,
    camino,
    visitados,
    usar_diagonales,
    parada_obligatoria
):
    global contador_backtracking

    # Modificación B: Nunca pisar un muro/pozo (-1)
    if matriz[fila][col] == -1:
        return False

    # Sumamos la celda actual
    suma_actual += matriz[fila][col]
    camino.append((fila, col))
    visitados.append((fila, col))

    # CASO BASE 1: Llegamos a la suma objetivo
    if suma_actual == objetivo:
        # Modificación A: Verificar si se pisó la coordenada obligatoria
        if parada_obligatoria is None or parada_obligatoria in camino:
            return True
        else:
            # Rechazamos este camino porque no pasó por la parada obligatoria
            contador_backtracking += 1
            camino.pop()
            visitados.pop()
            return False

    # CASO BASE 2: Nos pasamos del objetivo (asumiendo números >= 0)
    if suma_actual > objetivo:
        contador_backtracking += 1
        camino.pop()
        visitados.pop()
        return False

    # Definimos hacia dónde podemos movernos
    if usar_diagonales:
        movimientos = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
    else:
        movimientos = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

    # Exploramos cada dirección posible
    for mov_f, mov_c in movimientos:
        nueva_f = fila + mov_f
        nueva_c = col + mov_c

        if 0 <= nueva_f < n and 0 <= nueva_c < n:
            # Modificación B: No avanzar hacia un muro (-1)
            if matriz[nueva_f][nueva_c] == -1:
                continue

            ya_visitado = False
            for v in visitados:
                if v[0] == nueva_f and v[1] == nueva_c:
                    ya_visitado = True
                    break

            if not ya_visitado:
                encontrado = busqueda_recursiva(
                    matriz,
                    n,
                    nueva_f,
                    nueva_c,
                    objetivo,
                    suma_actual,
                    camino,
                    visitados,
                    usar_diagonales,
                    parada_obligatoria
                )
                if encontrado:
                    return True

    # Si ninguna dirección sirvió, hacemos Backtracking
    contador_backtracking += 1
    camino.pop()
    visitados.pop()
    return False


def encontrar_camino_suma(matriz, n, objetivo, parada_obligatoria, usar_diagonales=False):
    global contador_backtracking
    contador_backtracking = 0

    print(f"\nBuscando objetivo: {objetivo}")
    print(f"Parada obligatoria: {parada_obligatoria}")
    print(f"Modo: {'8 direcciones (Incluye Diagonales)' if usar_diagonales else 'Solo Horizontal y Vertical'}")

    # Validamos que la parada obligatoria esté dentro de la matriz y no sea un muro
    pf, pc = parada_obligatoria
    if not (0 <= pf < n and 0 <= pc < n):
        print(f"[!] La coordenada obligatoria {parada_obligatoria} está fuera de la matriz.")
        return False
    if matriz[pf][pc] == -1:
        print(f"[!] La coordenada obligatoria {parada_obligatoria} es un muro (-1). Camino imposible.")
        return False

    for i in range(n):
        for j in range(n):
            if matriz[i][j] == -1:
                continue

            camino = []
            visitados = []

            if busqueda_recursiva(
                matriz,
                n,
                i,
                j,
                objetivo,
                0,
                camino,
                visitados,
                usar_diagonales,
                parada_obligatoria
            ):
                print(f"\n¡Éxito! Camino encontrado empezando en la fila {i}, columna {j}")
                print("Secuencia de posiciones (fila, columna):")
                for paso, (f, c) in enumerate(camino):
                    etiqueta = " <-- PARADA OBLIGATORIA" if (f, c) == parada_obligatoria else ""
                    print(f"  Paso {paso + 1}: Posición ({f}, {c}) -> Valor: {matriz[f][c]}{etiqueta}")

                imprimir_matriz_resaltada(matriz, n, camino, parada_obligatoria)
                print(f"[Auditoría] Total de retrocesos (Backtracking): {contador_backtracking}")
                return True

    print(f"\n[!] No se encontró ningún camino que sume {objetivo} pasando por {parada_obligatoria}.")
    print(f"[Auditoría] Total de retrocesos (Backtracking): {contador_backtracking}")
    return False


if __name__ == "__main__":
    n = 5
    # Matriz con muros (-1) representados como terreno intransitable
    matriz_prueba = [
        [ 1,  2, -1,  1,  5],
        [ 4,  1,  1, -1,  1],
        [ 1, -1,  2,  3,  2],
        [ 2,  2,  3,  1, -1],
        [ 6,  1, -1,  5,  1]
    ]

    print("MATRIZ ORIGINAL (-1 = muro/pozo):")
    for fila in matriz_prueba:
        print(" ".join(f"{num:3d}" for num in fila))

    try:
        entrada_f = input("\nIngresa la fila obligatoria (0-4, Enter para 2): ").strip()
        entrada_c = input("Ingresa la columna obligatoria (0-4, Enter para 2): ").strip()
        fila_obl = int(entrada_f) if entrada_f != "" else 2
        col_obl = int(entrada_c) if entrada_c != "" else 2
    except (ValueError, EOFError):
        fila_obl, col_obl = 2, 2

    encontrar_camino_suma(
        matriz_prueba,
        n,
        objetivo=10,
        parada_obligatoria=(fila_obl, col_obl),
        usar_diagonales=False
    )
