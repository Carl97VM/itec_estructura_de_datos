# import math

# resultado = math.sqrt(16)
# print(f"El resultado de la raíz cuadrada de 16 es: {resultado}")


# from math import pi, pow 

import os
import time
import time
import math
import sys

CYAN = '\033[96m'
VERDE = '\033[92m'
AMARILLO  = '\033[33m'
MAGENTA   = '\033[35m'
ROJO     = '\033[31m'
BLANCO    = '\033[97m'
NEGRITA   = '\033[1m'
RESET     = '\033[0m'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def efecto_maquina_escribir(texto, velocidad=0.05, color=BLANCO):
    sys.stdout.write(color + NEGRITA)  # Establecer el color del texto
    for caracter in texto:
        sys.stdout.write(f"{color}{caracter}{RESET}")
        sys.stdout.flush()
        time.sleep(velocidad)
    sys.stdout.write(RESET)  # Restablecer el color al finalizar
    
def dibujar_encabezado():
    print(f"{CYAN}{NEGRITA}==============================")
    print("=== Bienvenido a la Consola ===")
    print("==============================\n{RESET}")
    
def calcular_hipotemusa():
    print(f"{AMARILLO}Calculadora de Hipotenusa{RESET}")
    try:
        cateto1 = float(input(f"{VERDE}Ingrese el primer cateto: {RESET}"))
        cateto2 = float(input(f"{VERDE}Ingrese el segundo cateto: {RESET}"))
        print(f"{AMARILLO}Calculando la hipotenusa...{RESET}")
        time.sleep(2)
        hipotenusa = math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))
        print(f"{VERDE}La hipotenusa es: {hipotenusa}{RESET}")
    except ValueError:
        print(f"{ROJO}Entrada no válida. Por favor, ingrese números válidos.{RESET}")
        
def caida_libre():
    print(f"{AMARILLO}Calculadora de Caída Libre{RESET}")
    try:
        altura = float(input(f"{VERDE}Ingrese la altura (en metros): {RESET}"))
        print(f"{AMARILLO}Calculando el tiempo de caída...{RESET}")
        time.sleep(2)
        gravedad = 9.81  # Aceleración debido a la gravedad en m/s^2
        tiempo = math.sqrt((2 * altura) / gravedad)
        print(f"{VERDE}El tiempo de caída libre es: {tiempo:.2f} segundos{RESET}")
    except ValueError:
        print(f"{ROJO}Entrada no válida. Por favor, ingrese un número válido.{RESET}")
    
def iniciar
