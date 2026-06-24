import os

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class RegistroAsistencia:
    def __init__(self, carpeta='arrays/12032026', archivo='asistencia.txt'):
        # Construimos la ruta completa para que no dependa de la raíz
        self.ruta_completa = os.path.join(carpeta, archivo)
        self.cabeza = None
        
        # Si la carpeta no existe, la creamos para evitar errores
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.ruta_completa):
            with open(self.ruta_completa, 'r') as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    if nombre:
                        # Cargamos a la lista en memoria (sin volver a escribir al archivo)
                        self._agregar_a_memoria(nombre)
        else:
            print(f"Aviso: El archivo {self.ruta_completa} se creará al guardar datos.")

    def _agregar_a_memoria(self, nombre):
        """Método interno para armar la lista enlazada en RAM"""
        nuevo_nodo = Nodo(nombre)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def agregar_estudiante(self, nombre, guardar_en_disco=True):
        self._agregar_a_memoria(nombre)
        if guardar_en_disco:
            with open(self.ruta_completa, 'a') as archivo:
                archivo.write(nombre + '\n')

    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print("\nLa lista de asistencia está vacía.")
            return
        print("\n--- Lista de Asistencia Actual (Memoria) ---")
        while actual:
            print(f"Estudiante: {actual.nombre}")
            actual = actual.siguiente
        print("-------------------------------------------\n")

    def vaciar_registros(self):
        self.cabeza = None
        # 'w' sobreescribe el archivo dejándolo vacío
        with open(self.ruta_completa, 'w') as archivo:
            archivo.write('')
        print(">>> Registros eliminados del archivo y de la memoria.")

if __name__ == "__main__":
    # Se inicializa con la ruta correcta que viste en tu terminal
    lista = RegistroAsistencia()

    while True:
        print("Opciones: [Nombre Estudiante] | 'salir' (ver lista) | 'eliminar' (borrar todo)")
        entrada = input("Introduce una opción: ").strip()

        if entrada.lower() == 'salir':
            lista.mostrar()
            break
        
        elif entrada.lower() == 'eliminar':
            lista.vaciar_registros()
            
        elif entrada:
            # Agregamos a memoria y al bloc de notas
            lista.agregar_estudiante(entrada)
            print(f"'{entrada}' registrado.")
        
        else:
            print("Por favor, introduce un nombre válido.")