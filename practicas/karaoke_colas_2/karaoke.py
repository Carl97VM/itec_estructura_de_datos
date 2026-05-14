import time
import os
import sys
import shutil
import random

try:
    import pygame

    AUDIO_DISPONIBLE = True
except ImportError:
    AUDIO_DISPONIBLE = False
    print("Pygame no está instalado. La función de audio no estará disponible.")
    time.sleep(2)

CYAN = "\033[96m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
MAGENTA = "\033[35m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(
                0
            )  # FIFO: El primero en entrar, es el primero en salir
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener_elementos(self):
        return self.items

    def cantidad(self):
        return len(self.items)


coleccion_canciones = [
    {
        "titulo": "Mi Chica de Pueblo",
        "artista": "Nocheros y Migrantes",
        "archivo": "pista_1.mp3",
        "letras": [
            {
                "texto": "Estaba borracho y miré pa' atrás\nHabía una morocha, diosa mal",
                "espera": 3,
                "color": AMARILLO,
            }
        ],
    },
    {
        "titulo": "Ella",
        "artista": "Ricardo Arjona",
        "archivo": "pista_2.mp3",
        "letras": [
            {
                "texto": "Empezó de cero a ser lo que querían\nLas muñecas, y dar siempre la razón",
                "espera": 3,
                "color": MAGENTA,
            }
        ],
    },
    {
        "titulo": "Lamento Boliviano",
        "artista": "Enanitos Verdes",
        "archivo": "pista_3.mp3",
        "letras": [
            {
                "texto": "Me quieren agitar\nMe incitan a gritar\nSoy como una roca...",
                "espera": 3,
                "color": VERDE,
            }
        ],
    },
    {
        "titulo": "De Música Ligera",
        "artista": "Soda Stereo",
        "archivo": "pista_4.mp3",
        "letras": [
            {
                "texto": "Ella durmió al calor de las masas\nY yo desperté queriendo soñarla",
                "espera": 3,
                "color": CYAN,
            }
        ],
    },
    {
        "titulo": "Oye Mujer",
        "artista": "Raymix",
        "archivo": "pista_5.mp3",
        "letras": [
            {
                "texto": "Oye mujer\nLo que me has hecho, te digo que no es normal",
                "espera": 3,
                "color": AMARILLO,
            }
        ],
    },
    {
        "titulo": "Tu Cárcel",
        "artista": "Marco Antonio Solís",
        "archivo": "pista_6.mp3",
        "letras": [
            {
                "texto": "Te vas amor\nSi así lo quieres, ¿qué le voy a hacer?",
                "espera": 3,
                "color": MAGENTA,
            }
        ],
    },
    {
        "titulo": "El Perdedor",
        "artista": "Aventura",
        "archivo": "pista_7.mp3",
        "letras": [
            {
                "texto": "Dime si él te conoce la mitad\nDime si él tiene la sensibilidad...",
                "espera": 3,
                "color": VERDE,
            }
        ],
    },
    {
        "titulo": "Rayando el Sol",
        "artista": "Maná",
        "archivo": "pista_8.mp3",
        "letras": [
            {
                "texto": "Rayando el sol\nDesesperación\nEs más fácil llegar al sol que a tu corazón",
                "espera": 3,
                "color": CYAN,
            }
        ],
    },
    {
        "titulo": "A Puro Dolor",
        "artista": "Son By Four",
        "archivo": "pista_9.mp3",
        "letras": [
            {
                "texto": "Perdona si te estoy llamando en este momento\nPero me hacía falta escuchar de nuevo tu voz",
                "espera": 3,
                "color": AMARILLO,
            }
        ],
    },
    {
        "titulo": "Color Esperanza",
        "artista": "Diego Torres",
        "archivo": "pista_10.mp3",
        "letras": [
            {
                "texto": "Saber que se puede, querer que se pueda\nQuitarse los miedos, sacarlos afuera",
                "espera": 3,
                "color": MAGENTA,
            }
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
            sys.stdout.flush()
            time.sleep(tiempo_por_letra)

        sys.stdout.write(RESET + "\n")
    print()


def reproducir_karaoke(cancion):
    os.system("cls" if os.name == "nt" else "clear")
    ancho_terminal = shutil.get_terminal_size().columns

    titulo = f"🎵 Reproduciendo: {cancion['titulo']} - {cancion['artista']} 🎵"
    print(f"{VERDE}{NEGRITA}{titulo.center(ancho_terminal)}{RESET}\n")
    time.sleep(2)

    if AUDIO_DISPONIBLE:
        try:
            ruta_completa = os.path.dirname(os.path.abspath(__file__))
            ruta_cancion = os.path.join(ruta_completa, cancion["archivo"])
            pygame.mixer.init()
            pygame.mixer.music.load(ruta_cancion)
            pygame.mixer.music.play()
        except Exception as e:
            print(
                f"⚠️ Aviso: No se encontró '{cancion['archivo']}'. Continuamos sin pista de audio."
            )
            time.sleep(2)

    for letra in cancion["letras"]:
        efecto_escribir_centrado(letra["texto"], letra["color"], letra["espera"])

    if AUDIO_DISPONIBLE and pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(2000)
        time.sleep(2)


def mostrar_catalogo(catalogo):
    print(f"\n{CYAN}{NEGRITA}--- CATÁLOGO DE CANCIONES (10 DISPONIBLES) ---{RESET}")
    for i, cancion in enumerate(catalogo):
        print(f"[{i + 1}] {cancion['titulo']} - {cancion['artista']}")
    print("-" * 45)


def iniciar_rockola():
    catalogo_disponible = coleccion_canciones.copy()
    playlist = Cola()
    LIMITE_CANCIONES = 5

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{AMARILLO}{NEGRITA}=== ROCKOLA VIP (MÁXIMO 5 CANCIONES) ==={RESET}")

        espacio_libre = LIMITE_CANCIONES - playlist.cantidad()
        print(f"{VERDE}Espacios disponibles en tu Playlist: {espacio_libre}/5{RESET}\n")

        print("1. Ver catálogo completo")
        print("2. Agregar canción a mi Playlist")
        print("3. Ver orden de mi Playlist actual")
        print("4. ¡COMENZAR EL KARAOKE! (Play)")
        print("0. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            mostrar_catalogo(catalogo_disponible)
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            if playlist.cantidad() >= LIMITE_CANCIONES:
                print(
                    f"\n{MAGENTA}❌ ¡LÍMITE ALCANZADO! Ya has elegido tus 5 canciones.{RESET}"
                )
                print("Debes reproducir tu lista actual antes de poder elegir más.")
                input("\nPresiona Enter para continuar...")
                continue

            mostrar_catalogo(catalogo_disponible)
            try:
                seleccion = int(
                    input("\nIngresa el número de la canción que deseas agregar: ")
                )
                if 1 <= seleccion <= len(catalogo_disponible):
                    cancion_elegida = catalogo_disponible[seleccion - 1] # 0,1,2,3,4,5,6,7,8,9 # 1,2,3,4,5,6,7,8,9,10
                    playlist.encolar(cancion_elegida)
                    print(
                        f"{VERDE}✔ '{cancion_elegida['titulo']}' ha sido agregada en la posición {playlist.cantidad()}.{RESET}"
                    )
                else:
                    print(f"{MAGENTA}Número inválido.{RESET}")
            except ValueError:
                print(f"{MAGENTA}Por favor, ingresa un número válido.{RESET}")
            input("Presiona Enter para continuar...")

        elif opcion == "3":
            elementos = playlist.obtener_elementos()
            print(f"\n{VERDE}{NEGRITA}--- ORDEN DE MI PLAYLIST ---{RESET}")
            if not elementos:
                print("Tu cola está vacía. ¡Agrega tus 5 canciones!")
            else:
                for i, cancion in enumerate(elementos):
                    print(f"Turno {i + 1}: {cancion['titulo']} - {cancion['artista']}")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            if playlist.esta_vacia():
                print(
                    f"\n{MAGENTA}⚠️ No puedes iniciar sin canciones. Agrega al menos una a tu lista. ⚠️{RESET}"
                )
                input("Presiona Enter para continuar...")
            else:
                print(
                    f"\n{AMARILLO}¡Bloqueando lista! Preparando el escenario...{RESET}"
                )
                time.sleep(2)
                break

        elif opcion == "0":
            print("\nSaliendo de la Rockola...")
            sys.exit()
        else:
            print(f"\n{MAGENTA}Opción no válida. Intenta de nuevo.{RESET}")
            time.sleep(1)

    if AUDIO_DISPONIBLE:
        pygame.mixer.init()

    while not playlist.esta_vacia():
        cancion_actual = playlist.desencolar()
        reproducir_karaoke(cancion_actual)

        if not playlist.esta_vacia():
            os.system("cls" if os.name == "nt" else "clear")
            ancho_terminal = shutil.get_terminal_size().columns
            mensaje_transicion = (
                f"Cambiando de pista... Quedan {playlist.cantidad()} canciones"
            )
            print(
                f"{CYAN}{NEGRITA}{mensaje_transicion.center(ancho_terminal)}{RESET}\n"
            )
            time.sleep(3)

    os.system("cls" if os.name == "nt" else "clear")
    ancho_terminal = shutil.get_terminal_size().columns
    mensaje_final = "¡Lista terminada! Gracias por usar la Rockola."
    print(f"{VERDE}{NEGRITA}{mensaje_final.center(ancho_terminal)}{RESET}\n")


if __name__ == "__main__":
    iniciar_rockola()
