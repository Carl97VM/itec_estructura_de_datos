import time  #importar tiempo
import os #importar sistema operativo

#Sirve para dar colores al texto
CYAN      = "\033[36m"
VERDE     = "\033[32m"
AMARILLO  = "\033[33m"
AZUL      = "\033[34m"
BLANCO    = "\033[37m"
MAGENTA   = "\033[35m"
NEGRITA   = "\033[1m"
RESET     = "\033[0m" #Restablecer al estilo normal del texto

# Definición de una clase llamada Pila (estructura tipo stack)
class Pila:
    def __init__(self):                 # Constructor, inicializa la pila vacía
        self.item = []                  # Lista interna que almacenará los elementos

    def apilar(self, item):             # Método para agregar un elemento a la pila
        self.item.append(item)          

    def desapilar(self):                # Método para quitar el último elemento de la pila
        if not self.esta_vacia():       # Verifica que la pila no esté vacía
            return self.item.pop()      # Devuelve y elimina el último elemento
        return None                     # Si está vacía, devuelve None
    
    def esta_vacia(self):               # Método para comprobar si la pila está vacía
        return len(self.item) == 0

# Lista que contiene los párrafos de la canción con texto, tiempo de espera y color    
cancion = [
    { "texto": "Acaramelaitos, pico con pico, beso con beso", "espera": 3, "color": AZUL},
    { "texto": "Ahí me tienes en embeleso", "espera": 2, "color": VERDE},
    { "texto": "Ya falta un pelo pa' enamorarme", "espera": 3, "color": AZUL},
    { "texto": "COQUETA", "espera": 9, "color": VERDE},
    { "texto": "HAY MI CORAZON", "espera": 8, "color": VERDE},
    { "texto": "SUAVECITO", "espera": 16, "color": VERDE},
    
        
    {  "texto": "Suave que no resisto tanto cariño", "espera": 5, "color": AMARILLO},
    {  "texto": "No me apapaches tanto corazoncito", "espera": 4, "color": BLANCO},
    {  "texto": "No me hagas cucharita en la madrugada", "espera": 4, "color": BLANCO},
    {  "texto": "Si después me enamoro no digas nada", "espera": 3, "color": AZUL},
    {  "texto": "Yo me conozco bien y queda muy poco", "espera": 2, "color": NEGRITA},
    {  "texto": "Pa´ que tus besos me vuelvan loco", "espera": 3, "color": AZUL},
    {  "texto": "Y de mi locura te haré culpable eeeeh", "espera": 3, "color": AMARILLO},
    {
        "texto": "Esa sonrisa dulce que me hipnotiza\nHace que yo respire de prisa\nQue perras ganas de ir a besarte,\nY ese cuerpo coqueto que me provoca\nNi porque quiera cierro la boca\nAy por pensar en acariciarte",
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "No me llenes de besos mi pobre vida\nPorque después ya no habrá salida\nQuedas guardada aquí en mi pecho\nTrata de no matarme con tu mirada\nYo enamorado y tu enamorada\nDespués no digas que está mal hecho\nTrata de no matarme con tu mirada\nNo seas así desconsiderada\nDespués no digas que está mal hecho",
        "espera": 2,
        "color": AMARILLO
    },
    {
        "texto": "Acaramelaitos, pico con pico, beso con beso\nAhí me tienes en embeleso\nYa falta un pelo pa' enamorarme\nCoqueta y picarona me voy rindiendo poco a poquito\nToy mirando por tus ojitos\nSi sueño no quiero despertarme.",
        "espera": 2,
        "color": AMARILLO
    }
]

# Función principal que reproduce el karaoke
def reproducir_karaoke():                                
    pila_karaoke = Pila()                                # Crea una pila vacía para almacenar los versos

    for linea in reversed(cancion):                      # Inserta los versos en la pila en orden inverso
        pila_karaoke.apilar(linea)

    os.system("cls" if os.name == "nt" else "clear")     # Limpia la pantalla (cls en Windows, clear en Linux/Mac)

# Muestra mensaje inicial en magenta y negrita
    print(f"{MAGENTA}{NEGRITA} PREPARANDO LA LISTA DE CANCION: HEREDERO - Coqueta (Letra/Lyrics)\n")
    time.sleep(2)                                        # Pausa de 3 segundos antes de empezar

# Mientras la pila no esté vacía, va mostrando cada verso
    while not pila_karaoke.esta_vacia():
        linea_actual = pila_karaoke.desapilar()          # Saca el siguiente verso de la pila

        texto = linea_actual["texto"]                    # Obtiene el texto del verso
        espera = linea_actual["espera"]                  # Obtiene el tiempo de espera
        color = linea_actual["color"]                    # Obtiene el color asignado
        
 # Imprime el verso con el color correspondiente y luego lo resetea
        print(f"{color}{texto}{RESET}")
        time.sleep(espera)

# Punto de entrada del programa
if __name__ == "__main__":
    reproducir_karaoke()