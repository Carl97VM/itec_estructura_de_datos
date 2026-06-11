import os
import time

CYAN = '\033[96m'
VERDE = '\033[92m'
AMARILLO  = '\033[33m'
MAGENTA   = '\033[35m'
ROJO     = '\033[31m'
BLANCO    = '\033[97m'
NEGRITA   = '\033[1m'
RESET     = '\033[0m'

class Pila:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        return None  # Retorna None si la pila está vacía

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        return None  # Retorna None si la pila está vacía

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
    
    def obtener_pila(self):
        return self._items
    
class ValidarSintaxis:
    def __init__(self):
        # Diccionario de pares de símbolos
        self.parejas = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def evaluar_codigo(self, codigo):
        pila = Pila()
        for char in codigo:
            if char not in "({[":
                pila.push(char)
            elif char in ")}]":
                if(pila.is_empty() or pila.peek() != self.parejas[char]):
                    return False
                pila.pop()
        return pila.is_empty()
    
    def evaluar_interactivo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{CYAN}=== Evaluar Sintaxis ==={RESET}")
        print("Ingrese el código a evaluar (puede incluir paréntesis, llaves y corchetes):")       
        
        pila_en_vivo = Pila()
        while True:
            char = input("Ingrese un símbolo (o 'salir' para terminar): ")
            if char.upper() == 'SALIR':
                break
            
            if char not in "({[":
                pila_en_vivo.push(char)
                print(f"{MAGENTA}Símbolo '{char}' agregado a la pila.{RESET}")
            elif char in ")}]":
                if(pila_en_vivo.is_empty() or pila_en_vivo.peek() != self.parejas[char]):
                    print(f"{ROJO}La sintaxis es inválida.{RESET}")
                else:
                    pila_en_vivo.pop()
                    print(f"{VERDE}Símbolo de cierre '{char}' encontrado y coincide con el último símbolo de apertura.{RESET}")
                    
        if pila_en_vivo.is_empty():
            print(f"{VERDE}La sintaxis es válida.{RESET}")
        else:            
            print(f"{AMARILLO}La sintaxis está incompleta.{RESET}")
            
def menu():
    motor = ValidarSintaxis()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Validar Sintaxis ===")
        print("1. Evaluar código")
        print("2. Observación interactiva")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            codigo = input("Ingrese el código a evaluar: ")
            print("Evaluando sintaxis...")
            time.sleep(1)  # Simula un proceso de evaluación
            print("Resultado:", "Válida" if motor.evaluar_codigo(codigo) else "Inválida")
            input("Presione Enter para continuar...")
        elif opcion == '2':
            motor.evaluar_interactivo()
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            
if __name__ == "__main__":
    menu()