import time
import os
import sys
import shutil
import random

try:
    import pygame  # type: ignore[import]

    AUDIO_DISPONIBLE = True
except ImportError:
    AUDIO_DISPONIBLE = False
    print("Pygame no está instalado. La función de audio no estará disponible.")

CYAN = "\033[96m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
MAGENTA = "\033[35m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


# Dar un orden de llegada a las distintas canciones, para que se reproduzcan en el orden correcto
class Cola:
    def __init__(self):
        self.items = []

    # Encolar: Agregar un elemento al final de la cola
    def encolar(self, item):
        self.items.append(item)

    # Desencolar: Eliminar un elemento del frente de la cola
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0


coleccion_canciones = [
    {
        "titulo": "Mi Chica de Pueblo",
        "artista": "Nocheros y Migrantes",
        "archivo": "pista.mp3",
        "letras": [
            {
                "texto": "Estaba borracho y miré pa' atrás\nHabía una morocha, diosa mal\nEntre la gente, toda sonriente\nTomé su mano pa' bailar",
                "espera": 2,
                "color": AMARILLO,
            },
            {
                "texto": "Estaba con Anto y alguien más\nEran invisibles las demás\nY fijamente mira mi boca\nMientras de ella me cuenta",
                "espera": 2,
                "color": CYAN,
            },
            {
                "texto": "Que es estudiante del interior\nQue anduvo mal por un amor\nSi él no te quiere, voy a quererte, porque yo",
                "espera": 2,
                "color": VERDE,
            },
            {
                "texto": "Por un beso de amor de tu boca\nTe juro, me muero, yo me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
                "espera": 2,
                "color": MAGENTA,
            },
            {
                "texto": "Yo solo quiero darte amor\nEntregarte mi corazón\nQue me bese tu roja boca\nY emborracharnos de pasión",
                "espera": 2,
                "color": AMARILLO,
            },
            {
                "texto": "Que nos bailemos la vida\nYo quiero tus buenos días\nSeré el que toque tu alma\nY la mantenga encendida",
                "espera": 2,
                "color": MAGENTA,
            },
            {
                "texto": "Porque del cielo cayó este ángel\nEs donde quiero quedarme\nDame esta noche pa' demostrarte",
                "espera": 2,
                "color": AMARILLO,
            },
            {
                "texto": "Por un beso de amor de tu boca\nTe juro, me muero, yo me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
                "espera": 2,
                "color": CYAN,
            },
            {
                "texto": "Por tu boquita de Luna\nY recorrer tu cintura\nVoy a morir preso de ilusión\nYo te espero, aunque pensés\nQue soy un nochero\nSoy sincero esta noche",
                "espera": 2,
                "color": MAGENTA,
            },
            {
                "texto": "Por un beso de amor de tu boca\nTe juro, me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
                "espera": 2,
                "color": VERDE,
            },
        ],
    },
    {
        "titulo": "Mi Chica de Pueblo",
        "artista": "Nocheros y Migrantes",
        "archivo": "pista1.mp3",
        "letras": [
            {
                "texto": "Estaba borracho y miré pa' atrás\nHabía una morocha, diosa mal\nEntre la gente, toda sonriente\nTomé su mano pa' bailar",
                "espera": 2,
                "color": AMARILLO,
            },
            {
                "texto": "Estaba con Anto y alguien más\nEran invisibles las demás\nY fijamente mira mi boca\nMientras de ella me cuenta",
                "espera": 2,
                "color": CYAN,
            },
            {
                "texto": "Que es estudiante del interior\nQue anduvo mal por un amor\nSi él no te quiere, voy a quererte, porque yo",
                "espera": 2,
                "color": VERDE,
            },
            {
                "texto": "Por un beso de amor de tu boca\nTe juro, me muero, yo me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
                "espera": 2,
                "color": MAGENTA,
            },
            {
                "texto": "Yo solo quiero darte amor\nEntregarte mi corazón\nQue me bese tu roja boca\nY emborracharnos de pasión",
                "espera": 2,
                "color": AMARILLO,
            },
            {
                "texto": "Que nos bailemos la vida\nYo quiero tus buenos días\nSeré el que toque tu alma\nY la mantenga encendida",
                "espera": 2,
                "color": MAGENTA,
            },
            {
                "texto": "Porque del cielo cayó este ángel\nEs donde quiero quedarme\nDame esta noche pa' demostrarte",
                "espera": 2,
                "color": AMARILLO,
            },
            {
                "texto": "Por un beso de amor de tu boca\nTe juro, me muero, yo me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
                "espera": 2,
                "color": CYAN,
            },
            {
                "texto": "Por tu boquita de Luna\nY recorrer tu cintura\nVoy a morir preso de ilusión\nYo te espero, aunque pensés\nQue soy un nochero\nSoy sincero esta noche",
                "espera": 2,
                "color": MAGENTA,
            },
            {
                "texto": "Por un beso de amor de tu boca\nTe juro, me muero\nTe prometo que dejo esta vida de soltero\nQue en el suelo se quede tu ropa y toquemos el cielo\nY te cebo unos mates después de cada mañanero\nMi chica de pueblo",
                "espera": 2,
                "color": VERDE,
            },
        ],
    },
]


def efecto_escribir_centrado(texto, color, tiempo_espera=0.05):
    oracion = texto.split("\n")
    tiempo_espera_linea = (
        tiempo_espera / len(oracion) if len(oracion) > 0 else tiempo_espera
    )

    ancho_terminal = shutil.get_terminal_size().columns

    for linea in oracion:
        if len(linea) == 0:
            print()
            continue

        tiempo_por_letra = tiempo_espera_linea / len(linea)
        espacios = " " * ((ancho_terminal - len(linea)) // 2)

        sys.stdout.write(espacios + color + NEGRITA)

        for letra in linea:
            sys.stdout.write(letra)
            sys.stdout.flush()  # Fuerza a imprimir cada letra inmediatamente/instante
            time.sleep(tiempo_por_letra)

        sys.stdout.write(RESET + "\n")
    print()  # Agrega una línea en blanco al final


def reproducir_karaoke(cancion):
    os.system("cls" if os.name == "nt" else "clear")
    ancho_terminal = shutil.get_terminal_size().columns
    
    titulo = f"Reproduciendo: {cancion['titulo']} - {cancion['artista']}"
    print(f"{VERDE}{NEGRITA}{titulo.center(ancho_terminal)}{RESET}\n")
    time.sleep(2)

    if AUDIO_DISPONIBLE:
        try:
            ruta_completa = os.path.dirname(os.path.abspath(__file__))
            ruta_cancion = os.path.join(ruta_completa, cancion["archivo"]) ## MODO SILECIOSO PARA EVITAR ERRORES DE RUTA EN DISTINTOS SISTEMAS OPERATIVOS
            pygame.mixer.init()
            pygame.mixer.music.load(ruta_cancion)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error al cargar o reproducir el audio: {e}")
            print("Continuando sin audio...")
            time.sleep(2)

    for letra in cancion["letras"]:
        efecto_escribir_centrado(letra["texto"], letra["color"], letra["espera"])

    # Audio de la musica al terminar la canción
    if AUDIO_DISPONIBLE and pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(2000)  # Desvanece el audio en 2 segundos
        time.sleep(2)  # Espera a que el audio se desvanezca completamente

def iniciar_rockola():
    # Inicializar el motor de audio de Pygame una sola vez al inicio del programa
    if AUDIO_DISPONIBLE:
        pygame.mixer.init()
        
    # Mezclar la colección de canciones para que se reproduzcan en orden aleatorio
    random.shuffle(coleccion_canciones)
    
    playlist = Cola()
    for cancion in coleccion_canciones:
        playlist.encolar(cancion)
        
    # Bucle principal para reproducir las canciones en la cola
    while not playlist.esta_vacia():
        cancion_actual = playlist.desencolar()
        reproducir_karaoke(cancion_actual)
        
        # Transición suave entre canciones
        if not playlist.esta_vacia():
            os.system("cls" if os.name == "nt" else "clear")
            ancho_terminal = shutil.get_terminal_size().columns
            mensaje_transicion = "Preparando la siguiente canción..."
            print(f"{CYAN}{NEGRITA}{mensaje_transicion.center(ancho_terminal)}{RESET}\n")
            time.sleep(3)  # Espera 3 segundos antes de reproducir la siguiente
            
    os.system("cls" if os.name == "nt" else "clear")
    ancho_terminal = shutil.get_terminal_size().columns
    mensaje_final = "¡Gracias por cantar con nosotros! ¡Hasta la próxima!"
    print(f"{VERDE}{NEGRITA}{mensaje_final.center(ancho_terminal)}{RESET}\n")

if __name__ == "__main__":
    iniciar_rockola()