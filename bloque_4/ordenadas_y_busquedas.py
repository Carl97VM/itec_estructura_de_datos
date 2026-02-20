# /*
# El cierre donde aplicamos "Divide y Vencerás".

# Ejercicio 5: Mergesort (Ordenamiento por Mezcla)
# Problema: Implementa Mergesort para ordenar una lista de desordenada.
# */

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izq = mergesort(lista[:medio])
    der = mergesort(lista[medio:])
    
    return mezclar(izq, der)

def mezclar(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Por qué: Mergesort es un algoritmo estable O(n log n). 
# Es el concepto base de Timsort, el algoritmo real que usa Python en .sort()