import os

class pilaHistorial:
    def __init__(self):
        self.pilaHistorial = []

    def escribir(self, texto):
        # Agrega el texto a la pila de historial o equivale a hacer push o apilar
        self.pilaHistorial.append(texto)
        print("[+] Texto escrito: " + texto)
        
    def deshacer(self):
        # Elimina el último texto escrito de la pila de historial o equivale a hacer pop o desapilar
        if len(self.pilaHistorial) > 0:
            texto = self.pilaHistorial.pop()
            print("[-] Texto deshecho: " + texto)
        else:
            print("[-] No hay texto para deshacer.")
            
    def esta_vacia(self):
        # Verifica si la pila de historial está vacía
        return len(self.pilaHistorial) == 0
    
    def mostrar_historial(self):
        # Muestra el historial de textos escritos
        return ' '.join(self.pilaHistorial)
         
def menu():
    historial = pilaHistorial()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        print("====Ejercicio 1====\nMenú:")
        print(f"Texto actual: {historial.mostrar_historial()}")
        print("-"*12)
        print("1. Escribir texto")
        print("2. Deshacer último texto")
        print("3. Mostrar historial")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            texto = input("Ingrese el texto a escribir: ")
            historial.escribir(texto)
            input("Presione Enter para continuar...")
        elif opcion == "2":
            historial.deshacer()
            input("Presione Enter para continuar...")
        elif opcion == "3":
            print("Historial de textos escritos:")
            print(historial.mostrar_historial())
            input("Presione Enter para continuar...")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

# Ejemplo de uso
if __name__ == "__main__":
    menu()