def burbuja_bidireccional(arreglo):
    """
    Ordenamiento de Burbuja Bidireccional (Cocktail Sort) con:
      - Modificación A: Recorrido de ida (izquierda -> derecha) y vuelta (derecha -> izquierda),
        mostrando visualmente en consola cada dirección.
      - Modificación B: Auditoría de rendimiento (pasadas, comparaciones e intercambios)
        y validación para listas vacías o de un solo elemento.
    """
    # Calculamos la longitud a la antigua, contando los elementos
    n = 0
    for _ in arreglo:
        n += 1

    # Modificación B: Validación de lista vacía o con un solo elemento
    if n <= 1:
        print(f"[ADVERTENCIA] La lista tiene {n} elemento(s): {arreglo}.")
        print("No es necesario ordenar. El programa se detiene.")
        return

    print(f"Estado inicial: {arreglo}\n")

    pasadas = 0
    comparaciones = 0
    intercambios = 0

    inicio = 0
    fin = n - 1
    intercambiado = True

    while intercambiado:
        intercambiado = False

        # ------------------------------------------------------------------
        # RECORRIDO DE IDA (Izquierda -> Derecha): empuja el mayor al final
        # ------------------------------------------------------------------
        pasadas += 1
        print(f">>> PASADA {pasadas} - [IDA: Izquierda -> Derecha] (rango [{inicio}..{fin}]) >>>")

        for j in range(inicio, fin):
            comparaciones += 1
            print(f"  [IDA] Comparando posiciones [{j}]={arreglo[j]} y [{j+1}]={arreglo[j+1]}")

            if arreglo[j] > arreglo[j + 1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = temp

                intercambios += 1
                intercambiado = True
                print(f"  -> ¡Intercambio! El {arreglo[j]} pasa a [{j}] y el {arreglo[j+1]} a [{j+1}]")
                print(f"  Estado actual: {arreglo}")

        print("-" * 50)

        # Si no hubo intercambios en la ida, la lista ya está ordenada
        if not intercambiado:
            print(f"Proceso detenido tras la ida (pasada {pasadas}). Ya está ordenado.")
            break

        # El último elemento ya quedó en su posición definitiva
        fin -= 1
        intercambiado = False

        # ------------------------------------------------------------------
        # RECORRIDO DE VUELTA (Derecha -> Izquierda): empuja el menor al inicio
        # ------------------------------------------------------------------
        pasadas += 1
        print(f"<<< PASADA {pasadas} - [VUELTA: Derecha -> Izquierda] (rango [{inicio}..{fin}]) <<<")

        for j in range(fin, inicio, -1):
            comparaciones += 1
            print(f"  [VUELTA] Comparando posiciones [{j-1}]={arreglo[j-1]} y [{j}]={arreglo[j]}")

            if arreglo[j - 1] > arreglo[j]:
                temp = arreglo[j - 1]
                arreglo[j - 1] = arreglo[j]
                arreglo[j] = temp

                intercambios += 1
                intercambiado = True
                print(f"  -> ¡Intercambio! El {arreglo[j-1]} pasa a [{j-1}] y el {arreglo[j]} a [{j}]")
                print(f"  Estado actual: {arreglo}")

        print("-" * 50)

        # El primer elemento ya quedó en su posición definitiva
        inicio += 1

        if not intercambiado:
            print(f"Proceso detenido tras la vuelta (pasada {pasadas}). Ya está ordenado.")
            break

    # Modificación B: Reporte de Auditoría al finalizar
    print("\n" + "=" * 50)
    print("              REPORTE DE AUDITORÍA")
    print("=" * 50)
    print(f" 1) Número total de pasadas realizadas     : {pasadas}")
    print(f" 2) Número total de comparaciones (if)     : {comparaciones}")
    print(f" 3) Número total de intercambios físicos   : {intercambios}")
    print(f" Arreglo final ordenado                    : {arreglo}")
    print("=" * 50)


if __name__ == "__main__":
    print("=== PRUEBA 1: Lista desordenada ===")
    datos = [45, 20, 70, 30, 50, 10]
    burbuja_bidireccional(datos)

    print("\n=== PRUEBA 2: Lista con un solo elemento ===")
    burbuja_bidireccional([42])

    print("\n=== PRUEBA 3: Lista vacía ===")
    burbuja_bidireccional([])
