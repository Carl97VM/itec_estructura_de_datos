# ============================================================

# CONVERSIÓN DE PILAS A COLAS CON RUTAS DINÁMICAS Y MENÚ INTERACTIVO

# ============================================================


import os

import time

import sys

from collections import deque

import pygame  # NUEVO: Librería para reproducir el audio

# Inicializar el mezclador de audio de pygame

pygame.mixer.init()


# ============================================

# CONFIGURACIÓN DE COLORES ANSI Y TERMINAL

# ============================================

CYAN = "\033[96m"

VERDE = "\033[92m"

AMARILLO = "\033[33m"

MAGENTA = "\033[35m"

ROJO = "\033[31m"

BLANCO = "\033[97m"

NEGRITA = "\033[1m"

RESET = "\033[0m"


def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")


def efecto_maquina_escribir(texto, velocidad=0.03, color=BLANCO):

    sys.stdout.write(color + NEGRITA)

    for caracter in texto:

        sys.stdout.write(caracter)

        sys.stdout.flush()

        time.sleep(velocidad)

    print(RESET)


def separador(titulo, color=CYAN):

    print(f"\n{color}{NEGRITA}" + "=" * 54)

    print(f" {titulo}")

    print("=" * 54 + f"{RESET}")


# ============================================

# CONFIGURACIÓN DE RUTAS PARA SERVIDORES

# ============================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIO_DIR = BASE_DIR


# ============================================

# CLASE SECCIÓN DE CANCIÓN (con letra)

# ============================================


class SeccionAudio:

    def __init__(self, nombre, duracion_seg, letra=""):

        self.nombre = nombre

        self.duracion_seg = duracion_seg

        self.letra = letra

    def duracion_formateada(self):

        m = self.duracion_seg // 60

        s = self.duracion_seg % 60

        return f"{m}:{s:02d}"

    def mostrar_detalle_animado(self):

        print(
            f"\n{AMARILLO} SECCION: {self.nombre} — {self.duracion_formateada()}{RESET}"
        )

        print(f"{CYAN}" + "─" * 50 + f"{RESET}")

        for linea in self.letra.strip().split("\n"):

            efecto_maquina_escribir(f"  {linea}", velocidad=0.05, color=BLANCO)

            time.sleep(0.5)

        print(f"{CYAN}" + "─" * 50 + f"{RESET}")


# ============================================

# CLASE PILA (STACK - LIFO)

# ============================================


class Pila:

    def __init__(self, nombre="", archivo_audio=None):

        self.elementos = []

        self.nombre = nombre

        self.archivo_audio = (
            os.path.join(AUDIO_DIR, archivo_audio) if archivo_audio else None
        )

    def push(self, elemento):

        self.elementos.append(elemento)

    def pop(self):

        if self.esta_vacia():

            return None

        return self.elementos.pop()

    def esta_vacia(self):

        return len(self.elementos) == 0


# ============================================

# CLASE COLA (QUEUE - FIFO)

# ============================================


class Cola:

    def __init__(self, nombre="", archivo_audio=None):

        self.elementos = deque()

        self.nombre = nombre

        self.archivo_audio = archivo_audio

    def enqueue(self, elemento):

        self.elementos.append(elemento)

    def dequeue(self):

        if self.esta_vacia():

            return None

        return self.elementos.popleft()

    def esta_vacia(self):

        return len(self.elementos) == 0


# ============================================

# FUNCIÓN: CONVERTIR PILA → COLA

# ============================================


def convertir_pila_a_cola(pila: Pila, nombre_cola="") -> Cola:

    pila_aux = Pila("Auxiliar")

    cola_resultado = Cola(nombre_cola, archivo_audio=pila.archivo_audio)

    temp = Pila("Temp")

    temp.elementos = pila.elementos.copy()

    while not temp.esta_vacia():

        pila_aux.push(temp.pop())

    while not pila_aux.esta_vacia():

        cola_resultado.enqueue(pila_aux.pop())

    return cola_resultado


# ============================================================

# INICIALIZACIÓN Y CARGA DE PISTAS

# ============================================================

pila1 = Pila("Tension", archivo_audio="Tension.mp3")

pila1.push(
    SeccionAudio(
        "Intro", 18, "Yeah, yeah, yeah\nLooney Tunes\nZion y Lennox en la biografia"
    )
)

pila1.push(
    SeccionAudio(
        "Verso 1",
        32,
        "Cuando bailas asi no me cabe duda\nde que tu, estas bien dura...",
    )
)

cola1 = convertir_pila_a_cola(pila1, "Cola Tension")


pila2 = Pila("Quizas", archivo_audio="Quizas.mp3")

pila2.push(
    SeccionAudio(
        "Intro",
        14,
        "Buscando donde no hay nada,\nya no quiero discutir para que seguir...",
    )
)

cola2 = convertir_pila_a_cola(pila2, "Cola Quizas")


pila3 = Pila("Fiera", archivo_audio="Fiera.mp3")

pila3.push(
    SeccionAudio(
        "Intro", 14, "Hector el bambino! Tu sabes!\nCon los bacatranes, Trebol Clan!"
    )
)

cola3 = convertir_pila_a_cola(pila3, "Cola Fiera")


reproductores = {"1": cola1, "2": cola2, "3": cola3}


# ============================================================

# MENÚ INTERACTIVO EN CONSOLA

# ============================================================


def menu_karaoke():

    while True:

        limpiar_pantalla()

        print(f"{CYAN}{NEGRITA}" + "═" * 45)

        print("      REPRODUCTOR KARAOKE INTERACTIVO      ")

        print("═" * 45 + f"{RESET}")

        print(f"{VERDE} 1. Reproducir: Me Pones en Tension{RESET}")

        print(f"{VERDE} 2. Reproducir: Quizas{RESET}")

        print(f"{VERDE} 3. Reproducir: Gata Fiera{RESET}")

        print(f"{AMARILLO} 4. Ver Resumen de Todas las Pistas{RESET}")

        print(f"{ROJO} 0. Salir del Programa{RESET}")

        print(f"{CYAN}" + "═" * 45 + f"{RESET}")

        opcion = input(f"{NEGRITA}Seleccione una opcion (0-4): {RESET}").strip()

        if opcion in reproductores:

            cola_seleccionada = reproductores[opcion]

            limpiar_pantalla()

            efecto_maquina_escribir(
                f"CARGANDO PISTA: {cola_seleccionada.nombre}...",
                velocidad=0.08,
                color=MAGENTA,
            )

            time.sleep(1)

            cola_clon = Cola(cola_seleccionada.nombre)

            cola_clon.elementos = cola_seleccionada.elementos.copy()

            if cola_clon.esta_vacia():

                print(f"{ROJO}Error: No hay secciones musicales.{RESET}")

            else:

                # REPRODUCCIÓN DE AUDIO (NUEVO)

                if cola_seleccionada.archivo_audio and os.path.exists(
                    cola_seleccionada.archivo_audio
                ):

                    pygame.mixer.music.load(cola_seleccionada.archivo_audio)

                    pygame.mixer.music.play()

                else:

                    print(
                        f"\n{ROJO}Advertencia: No se encontró el archivo '{os.path.basename(cola_seleccionada.archivo_audio)}' en tu carpeta. Mostrando solo la letra...{RESET}"
                    )

                while not cola_clon.esta_vacia():

                    seccion = cola_clon.dequeue()

                    seccion.mostrar_detalle_animado()

                    time.sleep(2)

                pygame.mixer.music.stop()  # Detiene la música al terminar la letra

                print(f"\n{VERDE}{NEGRITA}Fin de la cancion.{RESET}")

                input(f"\n{AMARILLO}Presione Enter para continuar...{RESET}")

        elif opcion == "4":

            limpiar_pantalla()

            separador("RESUMEN FINAL DE LAS 3 PISTAS", color=CYAN)

            colas_finales = [cola1, cola2, cola3]

            print(
                f"\n {NEGRITA}{'#':<4} {'Nombre Cola':<20} {'Estado del Archivo'}{RESET}"
            )

            print(" " + "─" * 50)

            for i, cola in enumerate(colas_finales, 1):

                archivo_status = "Enlazado" if cola.archivo_audio else "No enlazado"

                print(f" [{i}]  {cola.nombre:<20} {archivo_status}")

            print(" " + "─" * 50)

            input(f"\n{AMARILLO}Presione Enter para continuar...{RESET}")

        elif opcion == "0":

            limpiar_pantalla()

            efecto_maquina_escribir(
                "Saliendo del sistema de Karaoke. Hasta luego!", color=CYAN
            )

            break

        else:

            print(f"{ROJO}Opcion no valida. Intente de nuevo.{RESET}")

            time.sleep(1.5)


if __name__ == "__main__":

    menu_karaoke()
