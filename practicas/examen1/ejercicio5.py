import os
from collections import deque

class Jugada:
    # Clase para empaquetar la información de una jugada con el
    # Id de la jugada, el jugador que la realizó y la sílaba añadida.
    # Ejemplo: Jugada(1, "A", "ma")
    def __init__(self, id_jugada, jugador, silaba):
        self.id_jugada = id_jugada
        self.jugador = jugador
        self.silaba = silaba

class JuegoPalabras:
    def __init__(self):
        self.cola_frase = deque()  # Cola para almacenar las sílabas añadidas
        self.pila_jugadores = {}
        self.historial_jugadas = []  # Lista para almacenar el historial de jugadas
        self.contador_ids = 0  # Contador para asignar IDs únicos a las jugadas
        
        
    def iniciar_jugador(self, jugador):
        if jugador not in self.pila_jugadores:
            self.pila_jugadores[jugador] = []  # Pila para almacenar las sílabas añadidas por el jugador
            
    def añadir_silaba(self, jugador, silaba):
        self.iniciar_jugador(jugador)
        self.contador_ids += 1
        # Objeto unico del jugador y la silaba añadida, con un id unico
        nueva_jugada = Jugada(self.contador_ids, jugador, silaba)
        
        self.cola_frase.append(nueva_jugada)  # Añadir la sílaba a la cola de la frase
        
        self.pila_jugadores[jugador].append(nueva_jugada)  # Añadir la jugada a la pila del jugador
        print(f"Jugador {jugador} añadió la sílaba: {silaba}")
        
    def deshacer_ultima_silaba(self, jugador):
        self.iniciar_jugador(jugador)
        
        if not self.pila_jugadores[jugador]:
            print(f"No hay sílabas para deshacer para el jugador {jugador}.")
            return
        
        jugada_objetivo = self.pila_jugadores[jugador].pop()  # Obtener la última jugada del jugador
        pila_auxiliar = []
        
        while self.cola_frase:
            temp = self.cola_frase.popleft() # Sacar elementos de la cola hasta encontrar la jugada a deshacer
            if temp.id_jugada == jugada_objetivo.id_jugada:
                print(f"Jugador {jugador} deshizo la sílaba: {temp.silaba}")
            else:
                pila_auxiliar.append(temp)  # Guardar las jugadas que no se deshacen en la pila auxiliar
                
        while pila_auxiliar:
            self.cola_frase.appendleft(pila_auxiliar.pop())  # Restaurar las jugadas restantes a la cola de la frase
            
    def mostrar_frase(self):
        frase_actual = ' '.join([j.silaba for j in self.cola_frase])
        if frase_actual:
            print(f"Frase actual: {frase_actual}")
        else:
            print("La frase actual está vacía.")
            
    def finalizar_juego(self):
        if not self.cola_frase:
            print("No hay frase para finalizar.")
            return
        
        frase_final = ' '.join([j.silaba for j in self.cola_frase])
        self.historial_jugadas.append(frase_final)  # Guardar la frase final en el historial
        self.cola_frase.clear()  # Limpiar la cola de la frase
        for jugador in self.pila_jugadores:
            self.pila_jugadores[jugador].clear()  # Limpiar las pilas de los jugadores
            
        print(f"Juego finalizado. Frase final: {frase_final}")
        print(f"Historial de la partida: {self.historial_jugadas}")
        
    

def menu():
    juego = JuegoPalabras()
    
    while True:
        print("=== Juego de Palabras ===")
        print("1. Jugador Añade Silaba")
        print("2. Jugador deshace ultima silaba")
        print("3. Mostrar frase actual")
        print("4. Finalizar juego")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            jugador = input("Identificador A o B: ")
            silaba = input("Ingrese la sílaba a añadir: ")
            juego.añadir_silaba(jugador, silaba)
            print(f"Sílabas añadidas: {silaba}")
            
        elif opcion == "2":
            jugador = input("Identificador A o B: ")
            juego.deshacer_ultima_silaba(jugador)
            print("Última sílaba deshecha.")
        elif opcion == "3":
            # juego.mostrar_frase()
            juego.mostrar_frase()
        elif opcion == "4":
            # juego.finalizar_juego()
            juego.finalizar_juego()
        elif opcion == "0":
            print("Saliendo del juego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
if __name__ == "__main__":
    menu()