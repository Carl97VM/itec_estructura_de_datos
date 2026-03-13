# import os

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None ## Que el puntero esperara al siguiente elemento

class RegistroAsistencia:
    def __init__(self, archivo='asistencia.txt'):
        self.archivo = archivo
        self.cabeza = None
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivo, 'r') as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    if nombre:
                        self.agregar_estudiante(nombre)
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe.")

    def agregar_estudiante(self, nombre):
        nuevo_nodo = Nodo(nombre)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        with open(self.archivo, 'a') as archivo:
            archivo.write(nombre + '\n')

    def mostrar(self):
        actual = self.cabeza
        print("\nLista de asistencia en memoria:")
        while actual:
            print(f"Estudiante:{actual.nombre}")
            actual = actual.siguiente

    def vaciar_registros(self):
        self.cabeza = None
        with open(self.archivo, 'w') as archivo:
            archivo.write('')

## Tarea para el 19/03/2026
## Agregar a la lista sin guardar
## Agregar el metodo vaciar registros 
## Agregar el introducir datos por consola 

if __name__ == "__main__":
    lista = RegistroAsistencia()
    # lista.agregar_estudiante("Johan")
    # lista.agregar_estudiante("Jose")
    # lista.agregar_estudiante("Marvin")
    # lista.agregar_estudiante("Tania")
    # lista.agregar_estudiante("Teresa")
    nombre = input("Ingrese el nombre del estudiante o (salir)")
    if nombre != "salir":
        lista.agregar_estudiante(nombre)
    else:
        lista.vaciar_registros()
    lista.mostrar()