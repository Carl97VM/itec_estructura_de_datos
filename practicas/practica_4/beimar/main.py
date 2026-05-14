import time
import os
import sys
import shutil

# --- CONFIGURACIÓN DE AUDIO ---
try:
    import pygame
    AUDIO_DISPONIBLE = True
except ImportError:
    AUDIO_DISPONIBLE = False

# --- COLORES ---
CYAN, VERDE, AMARILLO, MAGENTA, NEGRITA, RESET = "\033[96m", "\033[32m", "\033[33m", "\033[35m", "\033[1m", "\033[0m"

# --- ESTRUCTURA DE DATOS (PILA) ---
class Pila:
    def __init__(self):
        self.items = []
    def apilar(self, item):
        self.items.append(item)
    def desapilar(self):
        return self.items.pop()
    def esta_vacia(self):
        return len(self.items) == 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- LÓGICA VISUAL (FUENTE ESTÁNDAR) ---
def imprimir_frase_centrada(texto, color):
    lineas = texto.split('\n')
    ancho_terminal = shutil.get_terminal_size().columns
    for linea in lineas:
        if not linea:
            print(); continue
        espacio_izquierdo = " " * ((ancho_terminal - len(linea)) // 2)
        # Se imprime directamente sin efectos de "pincel" ni fondo
        print(espacio_izquierdo + color + NEGRITA + linea + RESET)

# --- BIBLIOTECA (5 CANCIONES - TIEMPOS REALES) ---
biblioteca = {
    "1": {
        "titulo": "Traicionero - La Beriso",
        "archivo": "laberiso.mp3",
        "letras": [
            {"texto": "Cuántas noches de gira", "segundo": 0, "color": MAGENTA},
            {"texto": "Días llenos de melancolía", "segundo": 6, "color": CYAN},
            {"texto": "Mi casa sin vos se ve tan vacía", "segundo": 13, "color": VERDE},
            {"texto": "Sé que tu amor fue tan sincero", "segundo": 20, "color": AMARILLO},
            {"texto": "Perdón, el mío fue tan traicionero", "segundo": 26, "color": MAGENTA},
        ]
    },
    "2": {
        "titulo": "Notenianada",
        "archivo": "notenianada.mp3",
        "letras": [
            {"texto": "Cuando no tenía nada,", "segundo": 0, "color": CYAN},
            {"texto": "nadie vino a preguntar", "segundo": 3, "color": VERDE},
            {"texto": "Si el frío me atravesaba", "segundo": 6, "color": AMARILLO},
            {"texto": "o si podía aguantar", "segundo": 9, "color": MAGENTA},
            {"texto": "Me sé fuerte en el silencio,", "segundo": 12, "color": CYAN},
            {"texto": "aprendí a sobreviviiiir", "segundo": 15, "color": VERDE},
            {"texto": "Y ahora que camino erguida,", "segundo": 17, "color": AMARILLO},
            {"texto": "les molesta verme aaaasiiiiií", "segundo": 21, "color": MAGENTA},
            {"texto": "Que hablen de miiiiiií,", "segundo": 26, "color": CYAN},
            {"texto": "inventen razonesss", "segundo": 30, "color": VERDE},
            {"texto": "No estuvieron cuando el mundo", "segundo": 33, "color": AMARILLO},
            {"texto": "me dejaba sin opcioneeeeees", "segundo": 36, "color": MAGENTA},
            {"texto": "Que hablen de miiiiií,", "segundo": 40, "color": CYAN},
            {"texto": "no me voy a escondeeer", "segundo": 42, "color": VERDE},
            {"texto": "Si disfruto de mi vidaaaaaa,", "segundo": 45, "color": AMARILLO},
            {"texto": "no me pienso deteneeeer", "segundo": 48, "color": MAGENTA},
        ]
    },
    "3": {
        "titulo": "Tiziano",
        "archivo": "tiziano.mp3",
        "letras": [
            {"texto": "Soy pesado, es antiguo, mas te amo", "segundo": 0, "color": AMARILLO},
            {"texto": "Perdona si te amo y si nos encontramos hace un mes o poco máaaaaaaaas", "segundo": 5, "color": CYAN},
            {"texto": "Perdona si no te hablo bajo, si no grito muero", "segundo": 17, "color": VERDE},
            {"texto": "Te he dicho ya que te amoooooooooo", "segundo": 23, "color": MAGENTA},
            {"texto": "Perdona si me río por mi desasosiego", "segundo": 29, "color": AMARILLO},
            {"texto": "Te miro, fijo y tiemblooo", "segundo": 35, "color": CYAN},
            {"texto": "Solo con tenerte al lado y sentirme entre tus brazos", "segundo": 41, "color": VERDE},
            {"texto": "Si estoy aquí, si te hablo emocionado, sí, si estoy alucinado", "segundo": 47, "color": MAGENTA},
        ]
    },
    "4": {
        "titulo": "PONER NOMBRE AQUÍ",
        "archivo": "cancion4.mp3",
        "letras": []
    },
    "5": {
        "titulo": "PONER NOMBRE AQUÍ",
        "archivo": "cancion5.mp3",
        "letras": []
    }
}

def ejecutar_karaoke(datos):
    # Invertimos para usar la Pila (LIFO)
    pila = Pila()
    for frase in reversed(datos["letras"]):
        pila.apilar(frase)

    if AUDIO_DISPONIBLE:
        pygame.mixer.init()
        ruta_audio = os.path.join(SCRIPT_DIR, datos["archivo"])
        if os.path.exists(ruta_audio):
            pygame.mixer.music.load(ruta_audio)
            pygame.mixer.music.play()
        else:
            print(f"\n❌ Error: No se encontró el archivo '{ruta_audio}'")
            time.sleep(2)
            return

    os.system('cls' if os.name == 'nt' else 'clear')
    inicio_tiempo = time.time()
    
    print(f"\n{AMARILLO}REPRODUCIENDO: {datos['titulo']}{RESET}\n")

    while not pila.esta_vacia():
        # Miramos el elemento superior de la pila sin sacarlo
        proxima_frase = pila.items[-1]
        tiempo_actual = time.time() - inicio_tiempo

        # Si el tiempo de la canción alcanzó el segundo marcado
        if tiempo_actual >= proxima_frase["segundo"]:
            f = pila.desapilar()
            imprimir_frase_centrada(f["texto"], f["color"])
        
        time.sleep(0.05) # Pequeña espera para no sobrecargar la CPU

    if AUDIO_DISPONIBLE:
        pygame.mixer.music.stop()
    print(f"\n{VERDE}--- FIN DE LA CANCIÓN ---{RESET}")
    time.sleep(2)

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print(" PROYECTO KARAOKE - 5 TEMAS ")
        print("========================================")
        for k, v in biblioteca.items():
            print(f"{k}. {v['titulo']}")
        print("s. Salir")
        
        op = input("\nElige una opción: ")
        if op.lower() == 's':
            break
        if op in biblioteca:
            if not biblioteca[op]["letras"]:
                print("\nOpción vacía. Falta cargar letras.")
                time.sleep(2)
            else:
                ejecutar_karaoke(biblioteca[op])
