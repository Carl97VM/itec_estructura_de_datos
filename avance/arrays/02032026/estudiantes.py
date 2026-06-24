class Estudiante:
    def __init__(self, nombre, edad, nota, carrera):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        self.carrera = carrera

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}, Carrera: {self.carrera}"

    def __repr__(self):
        return f"estudiante({self.nombre}, {self.edad}, {self.nota}, {self.carrera})"

class ListaEstudiantes:
    def __init__(self):
        self.estudiantes = []

    # C.R.U.D
    # Create, Read, Update, Delete
    # Crear, Leer, Actualizar, Eliminar
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado exitosamente")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")
        else:
            print("\nLista de estudiantes:")
            for estudiante in self.estudiantes:
                print(estudiante)

    def remover_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante {nombre} removido exitosamente")
                return
        print(f"Estudiante {nombre} no encontrado")

    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                print(f"Estudiante {nombre} encontrado")
                return estudiante
        print(f"Estudiante {nombre} no encontrado")
        return None

    def actualizar_estudiante(self, nombre, edad, nota, carrera):
        estudiante = self.buscar_estudiante(nombre)
        if estudiante:
            estudiante.edad = edad
            estudiante.nota = nota
            estudiante.carrera = carrera
            print(f"Estudiante {nombre} actualizado exitosamente")

if __name__ == "__main__":
    lista_estudiantes = ListaEstudiantes()
    lista_estudiantes.agregar_estudiante(Estudiante("Juan", 20, 15, "Informatica"))
    lista_estudiantes.agregar_estudiante(Estudiante("Maria", 22, 18, "Informatica"))
    lista_estudiantes.mostrar_estudiantes()
    lista_estudiantes.remover_estudiante("Juan")
    lista_estudiantes.mostrar_estudiantes()
    lista_estudiantes.buscar_estudiante("Maria")
    lista_estudiantes.actualizar_estudiante("Maria", 23, 19, "Informatica")
    lista_estudiantes.mostrar_estudiantes()