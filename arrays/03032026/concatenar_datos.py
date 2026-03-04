from time import asctime, localtime, strftime
from datetime import datetime

class Estudiante:
    def __init__(self, nombre, fecha=None):
        self.nombre = nombre
        fecha_guardar = ""
        if(fecha == None):
            ahora = localtime()
            fecha_guardar = strftime("%Y-%m-%d %H:%M", ahora)
            # fecha_guardar = asctime()

        # (fecha == None) ? fecha_guardar = asctime() : fecha
        self.fecha = fecha_guardar

    def __str__(self):
        return f"Nombre: {self.nombre}, fecha: {self.fecha}"

    def __repr__(self):
        return f"estudiante({self.nombre}, {self.fecha})"
    
class ExamenesEstudiante:
    def __init__(self):
        self.examenesestudaintes = []

    def agregar_fecha(self, estudiante):
        self.examenesestudaintes.append(estudiante)
        print(f"Estudiante: {estudiante.nombre} agregado")

    def mostrar_estudiantes(self):
        if not self.examenesestudaintes:
            print("No hay estudiantes registrados")
        else:
            print("\nLista de estudiantes:")
            for estudiante in self.examenesestudaintes:
                print(estudiante)

if __name__ == "__main__":
    fecha_computadora = datetime(2026, 3, 3, 21,37)
    algo = ExamenesEstudiante()
    algo.agregar_fecha(Estudiante("Fibbi", fecha_computadora))
    algo.agregar_fecha(Estudiante("Rolando"))
    algo.agregar_fecha(Estudiante("Andres"))

    algo.mostrar_estudiantes()