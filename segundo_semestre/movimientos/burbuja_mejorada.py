def burbuja_mejorada(arreglo):
    # Calculamos la longitud a la antigua, contando los elementos
    n = 0
    for _ in arreglo:
        n += 1

    print(f"Estado inicial: {arreglo}\n")

    for i in range(n):
        intercambiado = False
        
        # En cada pasada, el elemento más grande "burbujea" al final, 
        # por lo que no necesitamos revisar los últimos 'i' elementos.
        for j in range(0, n - i - 1):
            
            print(f"  Comparando posiciones [{j}]={arreglo[j]} y [{j+1}]={arreglo[j+1]}")
            
            if arreglo[j] > arreglo[j + 1]:
                # Intercambio manual usando una variable temporal
                temp = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = temp
                
                intercambiado = True
                print(f"  -> ¡Intercambio! El {arreglo[j]} pasa a la pos [{j}] y el {arreglo[j+1]} a la pos [{j+1}]")
                print(f"  Estado actual: {arreglo}")
        
        print("-" * 40)
        
        # Si no hubo intercambios en esta pasada, el arreglo ya está ordenado
        if not intercambiado:
            print(f"Proceso detenido en la vuelta {i+1}. Ya está ordenado.")
            break

# Prueba del algoritmo
datos = [45, 20, 70, 30, 50]
burbuja_mejorada(datos)