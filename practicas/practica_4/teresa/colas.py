# ================================================

# CONVERSIÓN DE PILAS A COLAS

# Estructura de Datos - Python

# Pista 1: Me Pones en Tensión - Zion & Lennox ft. The Noise (2019)

# Pista 2: Quizás - Tony Dize ft. Ken-Y & Wisin (2008)

# Pista 3: Gata Fiera - Trébol Clan ft. Héctor "El Father" & Joan (2004)

# ================================================



from collections import deque



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

    def __init__(self, nombre=""):

        self.elementos = []

        self.nombre = nombre



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

        print(" " + "─" * 50)

        for sec in reversed(self.elementos):

            print(f" | {str(sec):<46} |")

        print(" " + "─" * 50)





# ============================================

# CLASE COLA (QUEUE - FIFO)

# ============================================

class Cola:

    def __init__(self, nombre=""):

        self.elementos = deque()

        self.nombre = nombre



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

    cola_resultado = Cola(nombre_cola)



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

# Álbum: The Noise "La Biografía" | Año: 2019

# Género: Reggaetón romántico

# Estructura real: Intro → Verso 1 → Coro → Verso 2 →

# Coro → Puente → Coro Final → Outro

# ============================================================

separador("PISTA 1: Me Pones en Tensión — Zion & Lennox ft. The Noise")



pila1 = Pila("Tensión")



pila1.push(SeccionAudio("Intro", 18,

    "— Beat suave reggaetón romántico —\n"

    "Zion y Lennox...\n"

    "The Noise, La Biografía...\n"

    "escucha esto, baby..."))



pila1.push(SeccionAudio("Verso 1 — Zion", 32,

    "Cada vez que apareces en mi vida\n"

    "algo dentro de mí se descontrola,\n"

    "tu presencia me deja sin salida,\n"

    "esa mirada tuya me envenena y me consola.\n"

    "No entiendo cómo alguien puede hacerme\n"

    "sentir así con solo respirar,\n"

    "y aunque trato de no perderme\n"

    "contigo siempre acabo en el mismo lugar."))



pila1.push(SeccionAudio("Pre-Coro", 16,

    "Y no sé si es bueno o malo lo que siento,\n"

    "pero cada vez que estás cerca pierdo el aliento,\n"

    "algo en ti me roba hasta el pensamiento\n"

    "y me pone en tensión en cada momento."))



pila1.push(SeccionAudio("Coro", 38,

    "Me pones en tensión cuando me miras así,\n"

    "cuando te acercas y susurras para mí,\n"

    "me pones en tensión, no sé qué hacer contigo,\n"

    "eres mi tormenta y también mi abrigo.\n"

    "Me pones en tensión, me tienes loco ya,\n"

    "entre el querer y el soltar no hay libertad,\n"

    "me pones en tensión, me sacas de control,\n"

    "eres mi debilidad, eres mi dolor."))



pila1.push(SeccionAudio("Verso 2 — Lennox", 32,

    "Lennox en la pista y esto se enciende,\n"

    "ella llega al lugar y todo se suspende,\n"

    "su flow natural a cualquiera sorprende,\n"

    "y el corazón sin permiso se rinde y se vende.\n"

    "No es solo el cuerpo, es su manera de hablar,\n"

    "esa forma suya de reír y de mirar,\n"

    "me pone nervioso, me hace dudar,\n"

    "pero igual la busco sin poder parar."))



pila1.push(SeccionAudio("Puente", 20,

    "Y si te vas yo me quedo en el intento,\n"

    "buscando en cada esquina tu recuerdo,\n"

    "porque contigo pierdo el pensamiento\n"

    "y me pones en tensión a cada momento.\n"

    "Zion y Lennox lo dicen en voz alta:\n"

    "sin ti en mi vida algo siempre me falta."))



pila1.push(SeccionAudio("Coro Final", 38,

    "Me pones en tensión cuando me miras así,\n"

    "cuando te acercas y susurras para mí,\n"

    "me pones en tensión, no sé qué hacer contigo,\n"

    "eres mi tormenta y también mi abrigo.\n"

    "Me pones en tensión, me tienes loco ya,\n"

    "entre el querer y el soltar no hay libertad,\n"

    "me pones en tensión, me sacas de control,\n"

    "eres mi debilidad, eres mi dolor."))



pila1.push(SeccionAudio("Outro", 15,

    "— Beat se desvanece —\n"

    "Tensión... tensión...\n"

    "Zion y Lennox, The Noise...\n"

    "2019..."))



pila1.mostrar()

cola1 = convertir_pila_a_cola(pila1, "Cola Tensión")

cola1.mostrar()

cola1.mostrar_letras()





# ============================================================

# PISTA 2: "Quizás" - Tony Dize ft. Ken-Y & Wisin

# Álbum: La Melodía de la Calle | Año: 2008

# Género: Reggaetón romántico

# Estructura real: Intro → Verso 1 (Tony Dize) → Coro →

# Verso 2 (Ken-Y) → Coro → Verso 3 (Wisin) →

# Coro Final → Outro

# ============================================================

separador("PISTA 2: Quizás — Tony Dize ft. Ken-Y & Wisin")



pila2 = Pila("Quizás")



pila2.push(SeccionAudio("Intro", 14,

    "— Piano melódico + beat suave —\n"

    "Tony Dize...\n"

    "Ken-Y, Wisin...\n"

    "La Melodía de la Calle..."))



pila2.push(SeccionAudio("Verso 1 — Tony Dize", 32,

    "Desde que te fuiste nada es igual aquí,\n"

    "busco entre recuerdos algo de ti,\n"

    "quizás fui yo quien lo echó a perder,\n"

    "quizás fue el tiempo o el no saber querer.\n"

    "Me pregunto cada noche sin dormir\n"

    "si hay algo que pudiera yo decir,\n"

    "una razón para hacerte regresar,\n"

    "o si es mejor dejarte ya marchar."))



pila2.push(SeccionAudio("Pre-Coro", 16,

    "Quizás si hubiera dicho lo que sentía,\n"

    "quizás si no te hubiera fallado ese día,\n"

    "quizás si el orgullo no me hubiera cegado\n"

    "hoy no estaría solo y tan quebrado."))



pila2.push(SeccionAudio("Coro", 38,

    "Quizás, quizás, quizás,\n"

    "nunca sabremos lo que pudo pasar,\n"

    "quizás, quizás, quizás,\n"

    "el destino nos quiso separar.\n"

    "Quizás, quizás, quizás,\n"

    "aún te busco aunque ya no estás,\n"

    "quizás, quizás, quizás,\n"

    "te amaré aunque no pueda más."))



pila2.push(SeccionAudio("Verso 2 — Ken-Y", 30,

    "Ken-Y en la pista con el mismo dolor,\n"

    "preguntándome si fue real ese amor,\n"

    "quizás lo nuestro nunca tuvo solución,\n"

    "quizás somos dos almas sin dirección.\n"

    "Pero igual aquí estoy recordándote,\n"

    "en cada canción que suena dedicándote,\n"

    "quizás el tiempo cure esta herida,\n"

    "quizás vuelvas a ser parte de mi vida."))



pila2.push(SeccionAudio("Verso 3 — Wisin", 28,

    "Wisin al micrófono, historia real,\n"

    "lo que se fue con el viento sin igual,\n"

    "quizás mañana todo sea diferente,\n"

    "quizás el amor regrese de repente.\n"

    "Pero mientras tanto el beat no para,\n"

    "y yo te busco en cada nueva madrugada,\n"

    "quizás, quizás, la vida nos da otra oportunidad\n"

    "y encontremos juntos nuestra libertad."))



pila2.push(SeccionAudio("Coro Final", 38,

    "Quizás, quizás, quizás,\n"

    "nunca sabremos lo que pudo pasar,\n"

    "quizás, quizás, quizás,\n"

    "el destino nos quiso separar.\n"

    "Quizás, quizás, quizás,\n"

    "aún te busco aunque ya no estás,\n"

    "quizás, quizás, quizás,\n"

    "solo dime si vuelves o te vas."))



pila2.push(SeccionAudio("Outro", 14,

    "— Beat se desvanece suavemente —\n"

    "Quizás... quizás...\n"

    "Tony Dize, Ken-Y, Wisin...\n"

    "La Melodía de la Calle, 2008..."))



pila2.mostrar()

cola2 = convertir_pila_a_cola(pila2, "Cola Quizás")

cola2.mostrar()

cola2.mostrar_letras()





# ============================================================

# PISTA 3: "Gata Fiera" - Trébol Clan ft. Héctor "El Father" & Joan

# Álbum: Los Bacatranes | Año: 2004

# Género: Reggaetón / Dembow Old School

# Estructura real: Intro → Coro → Sección Héctor → Coro →

# Sección Joan → Verso Trébol Clan →

# Coro Final → Outro

# ============================================================

separador("PISTA 3: Gata Fiera — Trébol Clan ft. Héctor 'El Father' & Joan")



pila3 = Pila("Fiera")



pila3.push(SeccionAudio("Intro con Dembow", 14,

    "— Dembow old school pesado —\n"

    "Trébol Clan en la casa...\n"

    "Héctor El Father, Joan...\n"

    "Los Bacatranes, 2004..."))



pila3.push(SeccionAudio("Coro de Entrada", 30,

    "Ella llega al lugar y provoca a todos,\n"

    "se mueve, se suelta y los deja locos,\n"

    "gata fiera que no se deja atrapar,\n"

    "envuelve a los hombres y los hace llorar.\n"

    "Gata fiera, fiera, fiera,\n"

    "a mí no me vas a aruñar,\n"

    "gata fiera, fiera, fiera,\n"

    "conmigo no vas a jugar."))



pila3.push(SeccionAudio("Verso 1 — Héctor El Father", 34,

    "Oye tú, gata fiera, ¿qué es lo que te crees?\n"

    "que estás bregando con cualquiera que se rinde a tus pies,\n"

    "conmigo eso no va, aquí las reglas son al revés,\n"

    "y aunque uses tus trucos yo no caigo esta vez.\n"

    "Traicionera por naturaleza, eso ya se sabe,\n"

    "pero conmigo ese cuento ya no cabe,\n"

    "gata fiera que cree que todo se le debe,\n"

    "va a aprender que no todo en la vida se le cede."))



pila3.push(SeccionAudio("Coro Central", 30,

    "Ella llega al lugar y provoca a todos,\n"

    "se mueve, se suelta y los deja locos,\n"

    "gata fiera que no se deja atrapar,\n"

    "envuelve a los hombres y los hace llorar.\n"

    "Gata fiera, fiera, fiera,\n"

    "a mí no me vas a aruñar,\n"

    "gata fiera, fiera, fiera,\n"

    "conmigo no vas a jugar."))



pila3.push(SeccionAudio("Verso 2 — Joan", 30,

    "Joan en la pista y esto se calienta,\n"

    "gata fiera que a todos los tormenta,\n"

    "primero seduce y luego te revienta,\n"

    "pero conmigo ese juego no se cuenta.\n"

    "Nació en el barrio, creció con actitud,\n"

    "su mirada es fuego, su flow es virtud,\n"

    "pero yo no me pierdo ante su quietud,\n"

    "gata fiera, aquí mando yo, esa es la verdad."))



pila3.push(SeccionAudio("Verso 3 — Trébol Clan", 32,

    "Trébol Clan al frente desde los 90 siempre,\n"

    "gata fiera que a todos los sorprende,\n"

    "se mueve en la pista y el barrio se enciende,\n"

    "pero nadie la atrapa aunque cualquiera pretende.\n"

    "Gata maúlla cuando sale con la suya,\n"

    "cree que el mundo entero siempre le influye,\n"

    "pero el Trébol Clan no se rinde ni huye,\n"

    "en este dembow nadie nos destruye."))



pila3.push(SeccionAudio("Coro Final", 30,

    "Ella llega al lugar y provoca a todos,\n"

    "se mueve, se suelta y los deja locos,\n"

    "gata fiera que no se deja atrapar,\n"

    "envuelve a los hombres y los hace llorar.\n"

    "Gata fiera, fiera, fiera,\n"

    "a mí no me vas a aruñar,\n"

    "gata fiera, fiera, fiera,\n"

    "conmigo no vas a jugar."))



pila3.push(SeccionAudio("Outro Fade-out", 16,

    "— Dembow se desvanece —\n"

    "Gata fiera... fiera...\n"

    "Trébol Clan, Héctor El Father, Joan...\n"

    "Los Bacatranes, 2004..."))



pila3.mostrar()

cola3 = convertir_pila_a_cola(pila3, "Cola Fiera")

cola3.mostrar()

cola3.mostrar_letras()





# ============================================

# RESUMEN FINAL

# ============================================

separador("RESUMEN FINAL DE LAS 3 PISTAS")



colas = [

    ("1", "Me Pones en Tensión", "Zion & Lennox ft. The Noise", cola1.tamanio()),

    ("2", "Quizás", "Tony Dize ft. Ken-Y & Wisin", cola2.tamanio()),

    ("3", "Gata Fiera", "Trébol Clan ft. Héctor & Joan", cola3.tamanio()),

]



print(f"\n {'#':<4} {'Título':<24} {'Artista':<32} {'Secciones'}")

print(" " + "─" * 68)

for num, titulo, artista, secciones in colas:

    print(f" {num:<4} {titulo:<24} {artista:<32} {secciones}")

print(" " + "─" * 68)



total = sum(s for _, _, _, s in colas)

print("=" * 54)