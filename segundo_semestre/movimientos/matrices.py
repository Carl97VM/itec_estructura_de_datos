def imprimir_matriz_resaltada(matriz, n, camino):
    """
    Dibuja la matriz. Muestra los números que forman la suma y 
    oculta los demás con un punto '.' para que resalte el camino.
    """
    print("\nMatriz con el camino encontrado:")
    print("=" * 30)
    for i in range(n):
        linea = ""
        for j in range(n):
            # Comprobación a la antigua de si la coordenada está en el camino
            es_parte_del_camino = False
            for pos in camino:
                if pos[0] == i and pos[1] == j:
                    es_parte_del_camino = True
                    break
            
            if es_parte_del_camino:
                # Formato a 3 espacios para que se vea alineado
                linea += f"[{matriz[i][j]:2d}] "
            else:
                linea += "  .  "
        print(linea)
    print("=" * 30)

def busqueda_recursiva(matriz, n, fila, col, objetivo, suma_actual, camino, visitados, usar_diagonales):
    # Sumamos la celda actual
    suma_actual += matriz[fila][col]
    camino.append((fila, col))
    visitados.append((fila, col))

    # CASO BASE 1: ¡Encontramos el objetivo exacto!
    if suma_actual == objetivo:
        return True

    # CASO BASE 2: Nos pasamos del objetivo (asumiendo números positivos)
    if suma_actual > objetivo:
        # Revertimos (Backtracking)
        camino.pop()
        visitados.pop()
        return False

    # Si aún no llegamos al objetivo, definimos hacia dónde podemos movernos
    if usar_diagonales:
        # 8 direcciones (Horizontal, Vertical y Diagonales)
        movimientos = [
            (-1, 0), (1, 0), (0, -1), (0, 1),   # Arriba, Abajo, Izquierda, Derecha
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
        ]
    else:
        # 4 direcciones (Solo Horizontal y Vertical)
        movimientos = [
            (-1, 0), (1, 0), (0, -1), (0, 1)    # Arriba, Abajo, Izquierda, Derecha
        ]

    # Exploramos cada dirección posible
    for mov_f, mov_c in movimientos:
        nueva_f = fila + mov_f
        nueva_c = col + mov_c

        # Verificamos que no nos salgamos de los bordes de la matriz (n x n)
        if 0 <= nueva_f < n and 0 <= nueva_c < n:
            
            # Verificamos que no hayamos visitado ya esta celda en el camino actual
            ya_visitado = False
            for v in visitados:
                if v[0] == nueva_f and v[1] == nueva_c:
                    ya_visitado = True
                    break
            
            if not ya_visitado:
                # Llamada recursiva (bajamos un nivel más profundo)
                encontrado = busqueda_recursiva(matriz, n, nueva_f, nueva_c, objetivo, suma_actual, camino, visitados, usar_diagonales)
                
                # Si la llamada recursiva encontró el camino, propagamos el éxito hacia arriba
                if encontrado:
                    return True

    # Si ninguna dirección sirvió, revertimos nuestro paso y volvemos (Backtracking)
    camino.pop()
    visitados.pop()
    return False

def encontrar_camino_suma(matriz, n, objetivo, usar_diagonales=False):
    print(f"\nBuscando objetivo: {objetivo}")
    print(f"Modo: {'Cualquier dirección (Incluye Diagonales)' if usar_diagonales else 'Solo Horizontal y Vertical'}")
    
    # Intentamos empezar la búsqueda desde cada celda de la matriz
    for i in range(n):
        for j in range(n):
            camino = []
            visitados = []
            
            if busqueda_recursiva(matriz, n, i, j, objetivo, 0, camino, visitados, usar_diagonales):
                print(f"\n¡Éxito! Camino encontrado empezando en la fila {i}, columna {j}")
                
                # Mostramos los pasos y las posiciones
                print("Secuencia de posiciones (fila, columna):")
                for paso, (f, c) in enumerate(camino):
                    print(f"  Paso {paso + 1}: Posición ({f}, {c}) -> Valor: {matriz[f][c]}")
                
                imprimir_matriz_resaltada(matriz, n, camino)
                return True
                
    print(f"\n[!] No se encontró ninguna secuencia que sume exactamente {objetivo}.")
    return False

# ==========================================
# PRUEBA DEL ALGORITMO
# ==========================================

# Creamos una matriz de 5x5
n = 5
matriz_prueba = [
    [1, 2, 3, 1, 5],
    [4, 1, 1, 2, 1],
    [1, 5, 2, 8, 2],
    [2, 2, 3, 1, 4],
    [6, 1, 1, 5, 1]
]

# Imprimimos la matriz original
print("MATRIZ ORIGINAL:")
for fila in matriz_prueba:
    linea = ""
    for num in fila:
        linea += f"{num:2d} "
    print(linea)

# 1. Buscar en horizontal/vertical (Ej. buscar suma = 10)
encontrar_camino_suma(matriz_prueba, n, objetivo=10, usar_diagonales=False)

# 2. Buscar en todas direcciones (Ej. buscar suma = 18)
encontrar_camino_suma(matriz_prueba, n, objetivo=18, usar_diagonales=True)