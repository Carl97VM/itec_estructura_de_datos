import os
from collections import deque

class Jugada:
    """
    Clase para empaquetar la sílaba con un ID único.
    Esto resuelve el problema lógico de si dos jugadores ingresan la misma 
    sílaba (ej. "la" y "la") y se debe borrar una específica.
    """
    def __init__(self, id_jugada, jugador, silaba):
        self.id = id_jugada
        self.jugador = jugador
        self.silaba = silaba

class JuegoPalabras:
    def __init__(self):
        self.cola_frase = deque()       # Cola global (FIFO)
        self.pilas_jugadores = {}       # Diccionario de Pilas (LIFO por jugador)
        self.historial_rondas = []      # Pila global de rondas finalizadas
        self.contador_ids = 0           # Generador de IDs únicos

    def inicializar_jugador(self, jugador):
        """Crea la pila de un jugador si es su primer turno."""
        if jugador not in self.pilas_jugadores:
            self.pilas_jugadores[jugador] = []

    def añadir_silaba(self, jugador, texto):
        self.inicializar_jugador(jugador)
        self.contador_ids += 1
        
        # 1. Crear el objeto único de la jugada
        nueva_jugada = Jugada(self.contador_ids, jugador, texto)
        
        # 2. Enqueue en la cola global
        self.cola_frase.append(nueva_jugada)
        
        # 3. Push de la referencia en la pila del jugador
        self.pilas_jugadores[jugador].append(nueva_jugada)
        
        print(f"\nJugador {jugador} añadió: '{texto}'")

    def deshacer_ultima(self, jugador):
        self.inicializar_jugador(jugador)
        
        # Validar que el jugador tenga jugadas en su pila
        if not self.pilas_jugadores[jugador]:
            print(f"\nEl jugador {jugador} no tiene jugadas para deshacer.")
            return

        # 1. POP de la pila del jugador para saber exactamente qué borrar
        jugada_objetivo = self.pilas_jugadores[jugador].pop()
        
        # 2. Reconstrucción con Pila Auxiliar (Restricción estricta)
        pila_auxiliar = []
        
        while self.cola_frase:
            temp = self.cola_frase.popleft() # Desencolamos de frente
            
            if temp.id == jugada_objetivo.id:
                # Si encontramos la jugada, la descartamos (no va a la auxiliar)
                print(f"\nJugada '{temp.silaba}' (del jugador {jugador}) deshecha.")
            else:
                # Si no es la buscada, la resguardamos en la pila temporal
                pila_auxiliar.append(temp)
                
        # 3. Restaurar la cola original
        # Al sacar de la pila auxiliar (LIFO) e insertar al inicio de la cola (appendleft),
        # se restaura el orden exacto de los elementos.
        while pila_auxiliar:
            self.cola_frase.appendleft(pila_auxiliar.pop())

    def mostrar_frase(self):
        # Extraemos solo el texto de los objetos para imprimir
        frase = "".join([j.silaba for j in self.cola_frase])
        if frase:
            print(f"\nFrase actual: {frase}")
        else:
            print("\nFrase actual: (Vacía)")

    def finalizar_ronda(self):
        if not self.cola_frase:
            print("\nLa ronda está vacía. No hay nada que guardar.")
            return

        # Construir la frase final
        frase_final = "".join([j.silaba for j in self.cola_frase])
        
        # PUSH en el historial de rondas
        self.historial_rondas.append(frase_final)
        
        # Limpiar la cola global y vaciar la pila de todos los jugadores
        self.cola_frase.clear()
        for jugador in self.pilas_jugadores:
            self.pilas_jugadores[jugador].clear()
            
        print(f"\nRonda finalizada. Frase consolidada: '{frase_final}'")
        print(f"Historial de partidas: {self.historial_rondas}")

def menu():
    juego = JuegoPalabras()
    
    while True:
        print("\n=== JUEGO DE PALABRAS POR TURNOS ===")
        print("1. Jugador añade sílaba")
        print("2. Jugador deshace última sílaba")
        print("3. Mostrar frase actual")
        print("4. Finalizar ronda")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            jugador = input("Identificador del Jugador (ej. A o B): ").upper()
            silaba = input("Ingresa la sílaba (o palabra): ")
            juego.añadir_silaba(jugador, silaba)
            
        elif opcion == '2':
            jugador = input("Identificador del Jugador que deshace (ej. A o B): ").upper()
            juego.deshacer_ultima(jugador)
            
        elif opcion == '3':
            juego.mostrar_frase()
            
        elif opcion == '4':
            juego.finalizar_ronda()
            
        elif opcion == '0':
            print("Cerrando el juego...")
            break
            
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == '__main__':
    menu()