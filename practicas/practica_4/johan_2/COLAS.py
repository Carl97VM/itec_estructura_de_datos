import time
import os
import sys
import pygame

CYAN      = '\033[96m'
VERDE     = '\033[32m'
AMARILLO  = '\033[33m'
MAGENTA   = '\033[35m'
NEGRITA   = '\033[1m'
RESET     = '\033[0m'

# 🔹 NUEVA ESTRUCTURA: COLA (FIFO)
class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0


cancion = [
        {
        "texto": "Are we stuck where we can't go back?",
        "tiempo": 19,
        "espera": 2,
        "color": AMARILLO   
    },
    {
        "texto": "Are we stuck where we can't move on?", 
        "tiempo": 22.5,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "This regret that we bury deep inside", 
        "tiempo": 26.7,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "And now the memories are burning us in time", 
        "tiempo": 32,
        "espera": 2,
        "color": MAGENTA 
    },
    {
        "texto": "But maybe", 
        "tiempo": 38,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "In another moment", 
        "tiempo": 39.6,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "In another place and time", 
        "tiempo": 42.9,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "Would you feel the same", 
        "tiempo": 46.7,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "If I said we'd live forever", 
        "tiempo": 47,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "(Said we'd live forever) said we'd live forever", 
        "tiempo": 52.4,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "(Said we'd live forever) said we'd live forever", 
        "tiempo": 59,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "Every time that we fell off track", 
        "tiempo": 67,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "Every time that we ran so far", 
        "tiempo": 70.7,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "From the world we created side by side", 
        "tiempo": 73.8,
        "espera": 2,
        "color": MAGENTA
    },

    {
        "texto": "I see you here and I can't let go", 
        "tiempo": 80,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "I see you now and it's all I know", 
        "tiempo": 83.5,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "It is too soon to let go", 
        "tiempo": 88,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "But maybe", 
        "tiempo": 92,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "In another moment", 
        "tiempo": 94,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "In another place and time", 
        "tiempo": 97.5,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "Would you feel the same", 
        "tiempo": 101,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "If I said we'd live forever", 
        "tiempo": 102.8,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "(Said we'd live forever) said we'd live forever", 
        "tiempo": 107,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "(Said we'd live forever) said we'd live forever", 
        "tiempo": 113.5,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "It is too soon to let go", 
        "tiempo": 131.8,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "It is too soon to let go", 
        "tiempo": 142,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "But maybe", 
        "tiempo": 147,
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "In another moment", 
        "tiempo": 148,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "In another place and time", 
        "tiempo": 151.7,
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "Would you feel the same", 
        "tiempo": 155,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "If I said we'd live forever", 
        "tiempo": 156.8,
        "espera": 2,
        "color": AMARILLO
    },

    {
        "texto": "(Said we'd live forever) said we'd live forever", 
        "tiempo": 161.5,
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "(Said we'd live forever) said we'd live forever", 
        "tiempo": 167.8,
        "espera": 2,
        "color": VERDE
    },

    {
        "texto": "It is too soon to let go", 
        "tiempo": 178.7,
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "Said we'd live forever", 
        "tiempo": 185,
        "espera": 2,
        "color": AMARILLO
    }, 
] 

def reproducir_audio(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()

def efecto_escribir(texto, color, tiempo_espera=0.05):
    lineas = texto.split('\n')
    tiempo_espera_linea = tiempo_espera / len(lineas) if len(lineas) > 0 else tiempo_espera
    
    for linea in lineas:
        if len(linea) == 0:
            print()
            continue

        tiempo_por_letra = tiempo_espera_linea / len(linea)

        sys.stdout.write(color + NEGRITA)
        
        for letra in linea:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(tiempo_por_letra)
            
        sys.stdout.write(RESET + '\n')
    
    print()


def reproducir_karaoke():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{AMARILLO}{NEGRITA}PREPARANDO LISTA DE CANCION...\n")
    time.sleep(3)

    # 🔹 Crear cola
    cola_karaoke = Cola()

    # 🔹 Encolar todas las líneas en orden
    for linea in cancion:
        cola_karaoke.encolar(linea)

    inicio = time.time()

    # 🔹 Procesar en orden FIFO
    while not cola_karaoke.esta_vacia():
        linea_actual = cola_karaoke.desencolar()

        while time.time() - inicio < linea_actual["tiempo"]:
            time.sleep(0.01)

        efecto_escribir(
            linea_actual["texto"],
            linea_actual["color"],
            1.5
        )


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo_audio = os.path.join(script_dir, "04 - Another Moment.mp3")
    reproducir_audio(archivo_audio)
    reproducir_karaoke()