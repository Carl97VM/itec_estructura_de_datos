import time
import os
import sys
import shutil


try:
    import pygame
    AUDIO_DISPONIBLE = True
except ImportError:
    AUDIO_DISPONIBLE = False
    print("Pygame no está instalado. La función de audio no estará disponible.")

CYAN      = '\033[96m'
VERDE     = '\033[32m'
AMARILLO  = '\033[33m'
MAGENTA   = '\033[35m'
NEGRITA   = '\033[1m'
RESET     = '\033[0m'

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

cancion = [
    {
        "texto": "Estaba borracho y miré pa' atrás\nHabía una morocha, diosa mal\nEntre la gente, toda sonriente\nTomé su mano pa' bailar",
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "Estaba con Anto y alguien más\nEran invisibles las demás\nY fijamente mira mi boca\nMientras de ella me cuenta",
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "Que es estudiante del interior\nQue anduvo mal por un amor\nSi él no te quiere, voy a quererte, porque yo",
        "espera": 2,
        "color": VERDE
    },
    {
        "texto": "Por un beso de amor de tu boca\nTe juro, me muero, yo me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "Yo solo quiero darte amor\nEntregarte mi corazón\nQue me bese tu roja boca\nY emborracharnos de pasión",
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "Que nos bailemos la vida\nYo quiero tus buenos días\nSeré el que toque tu alma\nY la mantenga encendida",
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "Porque del cielo cayó este ángel\nEs donde quiero quedarme\nDame esta noche pa' demostrarte",
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "Por un beso de amor de tu boca\nTe juro, me muero, yo me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
        "espera": 2,
        "color": CYAN
    },
    {
        "texto": "Por tu boquita de Luna\nY recorrer tu cintura\nVoy a morir preso de ilusión\nYo te espero, aunque pensés\nQue soy un nochero\nSoy sincero esta noche",
        "espera": 2,
        "color": MAGENTA
    },
    {
        "texto": "Por un beso de amor de tu boca\nTe juro, me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
        "espera": 2,
        "color": VERDE
    }
]

def efecto_escribir(texto, color, tiempo_espera=0.05):
    lineas = texto.split('\n')
    tiempo_espera_linea = tiempo_espera / len(lineas) if len(lineas) > 0 else tiempo_espera
    
    ancho_terminal = shutil.get_terminal_size().columns

    for linea in lineas:
        if len(linea) == 0:
            print()
            continue

        tiempo_por_letra = tiempo_espera_linea / len(linea)
        espacios = ' ' * ((ancho_terminal - len(linea)) // 2)

        sys.stdout.write(espacios + color + NEGRITA)
        
        for letra in linea:
            sys.stdout.write(letra)
            sys.stdout.flush() # Fuerza a imprimir cada letra inmediatamente/instante
            time.sleep(tiempo_por_letra)
            
        sys.stdout.write(RESET + '\n')
    print()  # Agrega una línea en blanco al final

def reproducir_karaoke():
    pila_karaoke = Pila()

    for linea in reversed(cancion):
        pila_karaoke.apilar(linea)

    os.system('cls' if os.name == 'nt' else 'clear')

    ancho_terminal = shutil.get_terminal_size().columns
    titulo = "PREPARANDO LISTA DE CANCION: Mi CHICA DE PUEBLO BY NOCHEROS AND MIGRANTES"
    print(f"{AMARILLO}{NEGRITA}{titulo.center(ancho_terminal)}\n")
    time.sleep(2)

    if AUDIO_DISPONIBLE:
        try:
            ruta_completa = os.path.dirname(os.path.abspath(__file__))
            print(ruta_completa)
            ruta_cancion = os.path.join(ruta_completa, 'pista.mp3')
            print(ruta_cancion)
            pygame.mixer.init()
            pygame.mixer.music.load(ruta_cancion)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error al cargar o reproducir el audio: {e}")
            print("Continuando sin audio...")
            time.sleep(2)
    
    while not pila_karaoke.esta_vacia():
        linea_actual = pila_karaoke.desapilar()

        texto = linea_actual["texto"]
        espera = linea_actual["espera"]
        color = linea_actual["color"]

        efecto_escribir(texto, color, espera)

if __name__ == "__main__":
    reproducir_karaoke()