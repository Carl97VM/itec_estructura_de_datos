# Desafío: "El detector de duplicados".
# Implementa dos métodos para encontrar si una lista tiene elementos duplicados.
# - Método A (Fuerza Bruta): Compara cada elemento con todos los demás $O(n^2)$.
# - Método B (Optimizado): Usa un conjunto (set) para verificar existencia en $O(n)$.

def tiene_duplicados_lento(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]: return True
    return False

def tiene_duplicados_rapido(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos: return True
        vistos.add(elemento)
    return False