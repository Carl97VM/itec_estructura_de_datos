# ================================================

# CONVERSIÓN DE PILAS A COLAS CON RUTAS DINÁMICAS

# Estructura de Datos - Python

# Pista 1: Me Pones en Tensión - Zion & Lennox ft. The Noise (2019)

# Pista 2: Quizás - Tony Dize ft. Ken-Y & Wisin (2008)

# Pista 3: Gata Fiera - Trébol Clan ft. Héctor "El Father" & Joan (2004)

# ================================================



import os
import time

from collections import deque

try:
    import pygame
    AUDIO_DISPONIBLE = True
except ImportError:
    AUDIO_DISPONIBLE = False



# ============================================

# CONFIGURACIÓN DE RUTAS PARA SERVIDORES

# ============================================

# Esto detecta automáticamente la carpeta donde está corriendo este script.

# Así no importa si lo corres en Windows, Linux, un servidor web o en la nube.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Si decides guardar tus audios en una carpeta llamada "audios", descomenta la siguiente línea:

# AUDIO_DIR = os.path.join(BASE_DIR, "audios")

AUDIO_DIR = BASE_DIR # Por ahora asume que los .mp3 están junto a este código

def buscar_archivo_audio(nombre_archivo):
    if not nombre_archivo:
        return None
    ruta = os.path.join(AUDIO_DIR, nombre_archivo)
    if os.path.exists(ruta):
        return ruta
    nombre_base = os.path.splitext(nombre_archivo)[0].lower()
    for nombre in os.listdir(AUDIO_DIR):
        if nombre.lower().startswith(nombre_base) and nombre.lower().endswith(".mp3"):
            return os.path.join(AUDIO_DIR, nombre)
    return None


def reproducir_audio(ruta_audio):
    if not AUDIO_DISPONIBLE:
        print("⚠️ pygame no está instalado. No se puede reproducir audio.")
        return
    if not ruta_audio:
        print("⚠️ No se proporcionó ruta de audio.")
        return
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"⚠️ No se pudo reproducir el audio: {e}")



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



    def __str__(self):

        return f"{self.nombre} ({self.duracion_formateada()})"



    def mostrar_detalle(self):

        print(f"\n 🎵 {self.nombre} — {self.duracion_formateada()}")

        print(" " + "─" * 50)

        for linea in self.letra.strip().split("\n"):

            print(f" {linea}")

        print(" " + "─" * 50)





# ============================================

# CLASE PILA (STACK - LIFO)

# ============================================

class Pila:

    def __init__(self, nombre="", archivo_audio=None):

        self.elementos = []

        self.nombre = nombre

        self.archivo_audio_nombre = archivo_audio

        self.archivo_audio = buscar_archivo_audio(archivo_audio) if archivo_audio else None



    def push(self, elemento):

        self.elementos.append(elemento)



    def pop(self):

        if self.esta_vacia():

            print(" ¡ERROR! La pila está vacía.")

            return None

        return self.elementos.pop()



    def tope(self):

        if self.esta_vacia():

            return None

        return self.elementos[-1]



    def esta_vacia(self):

        return len(self.elementos) == 0



    def tamanio(self):

        return len(self.elementos)



    def mostrar(self):

        if self.esta_vacia():

            print(f" Pila '{self.nombre}' está vacía.")

            return

        print(f"\n 📦 PILA '{self.nombre}' (LIFO) — tope ↑")

        if self.archivo_audio:

            print(f" 📁 Audio encontrado: {self.archivo_audio}")

        elif self.archivo_audio_nombre:

            print(f" ⚠️ No se encontró el archivo: {self.archivo_audio_nombre}")

        print(" " + "─" * 50)

        for sec in reversed(self.elementos):

            print(f" | {str(sec):<46} |")

        print(" " + "─" * 50)





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

            print(" ¡ERROR! La cola está vacía.")

            return None

        return self.elementos.popleft()



    def frente(self):

        if self.esta_vacia():

            return None

        return self.elementos[0]



    def esta_vacia(self):

        return len(self.elementos) == 0



    def tamanio(self):

        return len(self.elementos)



    def mostrar(self):

        if self.esta_vacia():

            print(f" Cola '{self.nombre}' está vacía.")

            return

        print(f"\n 🎶 COLA '{self.nombre}' (FIFO) — orden de reproducción")

        if self.archivo_audio:

            print(f" 📁 Archivo listo para reproducir en servidor.")

        print(" " + "─" * 50)

        for i, sec in enumerate(self.elementos):

            prefijo = "▶ NEXT" if i == 0 else f" [{i+1}] "

            print(f" {prefijo} {str(sec)}")

        print(" " + "─" * 50)



    def mostrar_letras(self):

        print(f"\n 📖 Letras — Cola '{self.nombre}'")

        cola_temp = Cola("Temp")

        cola_temp.elementos = self.elementos.copy()

        while not cola_temp.esta_vacia():

            sec = cola_temp.dequeue()

            sec.mostrar_detalle()





# ============================================

# FUNCIÓN: CONVERTIR PILA → COLA

# ============================================

def convertir_pila_a_cola(pila: Pila, nombre_cola="") -> Cola:

    print(f"\n 🔄 Convirtiendo PILA '{pila.nombre}' → COLA '{nombre_cola}'...")

    pila_aux = Pila("Auxiliar")

    

    # Heredamos la ruta del audio a la Cola final

    cola_resultado = Cola(nombre_cola, archivo_audio=pila.archivo_audio)



    temp = Pila("Temp")

    temp.elementos = pila.elementos.copy()



    while not temp.esta_vacia():

        pila_aux.push(temp.pop())



    while not pila_aux.esta_vacia():

        cola_resultado.enqueue(pila_aux.pop())



    print(f" ✅ Conversión exitosa — {cola_resultado.tamanio()} secciones en cola.\n")

    return cola_resultado





def separador(titulo):

    print("\n" + "=" * 54)

    print(f" 🎶 {titulo}")

    print("=" * 54)





# ============================================================

# PISTA 1: "Me Pones en Tensión" - Zion & Lennox ft. The Noise

# ============================================================

separador("PISTA 1: Me Pones en Tensión — Zion & Lennox ft. The Noise")



# AQUÍ ENLAZAMOS EL ARCHIVO DE AUDIO FÍSICO

pila1 = Pila("Tensión", archivo_audio="Me Pones en Tension(MP3_160K).mp3")



pila1.push(SeccionAudio("Intro", 18,

    "Yeah, yeah, yeah\n"

    "Looney Tunes\n"

    "Zion y Lennox en la biografía\n"

    "motivando a la gyal"))



pila1.push(SeccionAudio("Verso 1 — Zion", 32,

    "Cuando bailas así no me cabe duda\n"

    "de que tú, estás bien dura..."))



# ... (resto de las secciones de Pista 1) ...



pila1.mostrar()

cola1 = convertir_pila_a_cola(pila1, "Cola Tensión")

cola1.mostrar()





# ============================================================

# PISTA 2: "Quizás" - Tony Dize ft. Ken-Y & Wisin

# ============================================================

separador("PISTA 2: Quizás — Tony Dize ft. Ken-Y & Wisin")



# AQUÍ ENLAZAS EL ARCHIVO CUANDO LO TENGAS

pila2 = Pila("Quizás", archivo_audio="Quizas_TonyDize.mp3")



pila2.push(SeccionAudio("Intro", 14,

    "Buscando donde no hay nada,\n"

    "ya no quiero discutir para qué seguir..."))



# ... (resto de las secciones de Pista 2) ...



pila2.mostrar()

cola2 = convertir_pila_a_cola(pila2, "Cola Quizás")

cola2.mostrar()





# ============================================================

# PISTA 3: "Gata Fiera" - Trébol Clan ft. Héctor "El Father" & Joan

# ============================================================

separador("PISTA 3: Gata Fiera — Trébol Clan ft. Héctor 'El Father' & Joan")



# AQUÍ ENLAZAMOS EL ARCHIVO DE AUDIO FÍSICO

pila3 = Pila("Fiera", archivo_audio="Gata Fiera(MP3_320K).mp3")



pila3.push(SeccionAudio("Intro con Dembow", 14,

    "¡Héctor el bambino! ¡Tú sabes!\n"

    "¡Con los bacatranes, Trébol Clan!"))



# ... (resto de las secciones de Pista 3) ...



pila3.mostrar()

cola3 = convertir_pila_a_cola(pila3, "Cola Fiera")

cola3.mostrar()
if cola3.archivo_audio:
    reproducir_audio(cola3.archivo_audio)



# ============================================

# RESUMEN FINAL

# ============================================

separador("RESUMEN FINAL DE LAS 3 PISTAS")



colas_finales = [cola1, cola2, cola3]



print(f"\n {'#':<4} {'Nombre Cola':<20} {'Estado del Archivo'}")

print(" " + "─" * 68)

for i, cola in enumerate(colas_finales, 1):
    estado = "LISTO" if cola.archivo_audio else "SIN AUDIO"
    print(f" {i:<4} {cola.nombre:<20} {estado}")

print(" " + "─" * 68)

print("=" * 54)