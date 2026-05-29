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
    print(f"==============================\n{RESET}")
    
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
        
def trigonometria_basica():
    print(f"\n{AMARILLO}--- ANÁLISIS TRIGONOMÉTRICO ---{RESET}")
    try:
        grados = float(input(f"{CYAN}Ingresa un ángulo (en grados):{RESET} "))
        
        # math funciona con radianes, así que primero convertimos
        radianes = math.radians(grados)
        
        seno = math.sin(radianes)
        coseno = math.cos(radianes)
        tangente = math.tan(radianes) if grados % 90 != 0 else "Indefinido"
        
        print("\n" + "="*35)
        print(f"{MAGENTA}Resultados para {grados}°:{RESET}")
        print(f"{VERDE}• Seno (sin):{RESET}   {seno:.4f}")
        print(f"{VERDE}• Coseno (cos):{RESET} {coseno:.4f}")
        
        if isinstance(tangente, float):
            print(f"{VERDE}• Tangente (tan):{RESET} {tangente:.4f}")
        else:
            print(f"{ROJO}• Tangente (tan):{RESET} {tangente}")
        print("="*35)
        
    except ValueError:
        print(f"{ROJO}❌ Error: Ingresa un valor numérico válido.{RESET}")
    
def iniciar_consola():
    
    if os.name == 'nt':
        os.system('cls')
        
    
    while True:
        dibujar_encabezado()
        print(f" {BLANCO}Seleccione un módulo matemático:{RESET}\n")
        print(f" {CYAN}[1]{RESET} Pitágoras (Geometría)")
        print(f" {CYAN}[2]{RESET} Caída Libre (Física)")
        print(f" {CYAN}[3]{RESET} Trigonometría (Ángulos)")
        print(f" {ROJO}[0]{RESET} Apagar Motor")
        print("\n" + "─"*48)
        
        opcion = input(f" {AMARILLO}>> Comando:{RESET} ")
        
        match opcion:
            case '1':
                calcular_hipotemusa()
            case '2':
                caida_libre()
            case '3':
                trigonometria_basica()
            case '0':
                efecto_maquina_escribir("\nApagando subsistemas matemáticos... ¡Hasta pronto!", 0.05, ROJO)
                sys.exit()
            case _:
                print(f"\n{ROJO}❌ Módulo no encontrado. Intente de nuevo.{RESET}")
        
        input(f"\n{NEGRITA}Presione ENTER para volver al panel principal...{RESET}")

if __name__ == "__main__":
    iniciar_consola()