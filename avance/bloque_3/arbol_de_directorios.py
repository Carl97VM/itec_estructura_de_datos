# Desafío: "El Árbol de Directorios (Recursión)".
# Crea una estructura de árbol para representar carpetas y archivos, y calcula el tamaño total.

class NodoArchivo:
    def __init__(self, nombre, tamaño=0):
        self.nombre = nombre
        self.tamaño = tamaño
        self.hijos = [] # Lista de otros NodoArchivo (carpetas)

def calcular_tamaño_total(nodo):
    total = nodo.tamaño
    for hijo in nodo.hijos:
        total += calcular_tamaño_total(hijo)
    return total