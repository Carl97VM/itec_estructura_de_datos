import os

class NavegadorWeb:
    def __init__(self, pagina_inicial="www.google.com"):
        self.pila_atras = []
        self.pila_adelante = []
        self.pila = pagina_inicial
        
    def visitar_pagina(self, url):
        self.pila_atras.append(self.pila)  # Agrega la página actual a la pila de atrás
        self.pila = url  # Cambia a la nueva página
        self.pila_adelante.clear()  # Limpia la pila de adelante
        print(f"Visitando a: {url}")
        
    def ir_atras(self):
        if self.pila_atras:
            self.pila_adelante.append(self.pila)  # Agrega la página actual a la pila de adelante
            self.pila = self.pila_atras.pop()  # Cambia a la página anterior
            print(f"Volviendo a: {self.pila}")
        else:
            print("No hay páginas anteriores.")
            
    def ir_adelante(self):
        if self.pila_adelante:
            self.pila_atras.append(self.pila)  # Agrega la página actual a la pila de atrás
            self.pila = self.pila_adelante.pop()  # Cambia a la página siguiente
            print(f"Avanzando a: {self.pila}")
        else:
            print("No hay páginas siguientes.")
            
def menu():
    navegador = NavegadorWeb()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        print("====Ejercicio 3====\nMenú:")
        print(f"Página actual: {navegador.pila}")
        print("-"*12)
        print("1. Visitar nueva página")
        print("2. Ir atrás")
        print("3. Ir adelante")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            url = input("Ingrese la URL de la página a visitar: ")
            navegador.visitar_pagina(url)
            input("Presione Enter para continuar...")
        elif opcion == "2":
            navegador.ir_atras()
            input("Presione Enter para continuar...")
        elif opcion == "3":
            navegador.ir_adelante()
            input("Presione Enter para continuar...")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            
if __name__ == "__main__":
    menu()