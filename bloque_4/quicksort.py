# Desafío: "Quicksort (El estándar de la industria)".
# Implementa Quicksort usando el esquema de partición de Hoare (pivote).

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    return quicksort(izq) + medio + quicksort(der)