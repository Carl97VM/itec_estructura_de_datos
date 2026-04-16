import time
import os

CYAN        = '\033[96m'
VERDE       = '\033[32m'
AMARILLO    = '\033[33m'
MAGENTA     = '\033[35m'
NEGRITA     = '\033[1m'
RESET       = '\033[0m'

class pila:
    def _init_(self):
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
        "texto": "When you were here before\nCouldn't look you in the eye\nYou're just like an angel\nYour skin makes me cry",
        "espera": 3,
        "color": CYAN
    },
    {
        "texto": "You float like a feather\nIn a beautiful world\nAnd I wish I was special\nYou're so very special",
        "espera": 3,
        "color": VERDE
    },
    {
        "texto": "And I'm a creep\nI'm a weirdo\nWhat the hell am I doing here?\nI don't belong here",
        "espera": 3,
        "color": AMARILLO
    },
    {
        "texto": "I don't care if it hurts\nI wanna have control\nI want a perfect body\nI want a perfect soul",
        "espera": 3,
        "color": MAGENTA
    },
    {
        "texto": "I want you to notice\nWhen I'm not around\nYou're so very special\nI wish I was special",
        "espera": 3,
        "color": NEGRITA
    },
    {
        "texto": "But I'm a creep\nI'm a weirdo\nWhat the hell am I doing here?\nWhen I don't belong here, oh, oh",
        "espera": 3,
        "color": CYAN
    },
    {
        "texto": "She's running out again\nShe's running out\nShe run, run, run, run\nRun\nRun",
        "espera": 3,
        "color": VERDE
    },
    {
        "texto": "Whatever makes you happy\nWhatever you want\nYou're so very special\nI wish I was special",
        "espera": 3,
        "color": AMARILLO
    },
    {
        "texto": "But I'm a creep\nI'm a weirdo\nWhat the hell am I doing here?\nI don't belong here\nI don't belong here",
        "espera": 3,
        "color": MAGENTA
    }
]

def reproducir_karaoke():
    pila_karaoke = pila()
    
    for linea in reversed(cancion):
        pila_karaoke.apilar(linea)
            
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{MAGENTA}{NEGRITA} PREPARANDO LISTA DE CANCION: CREEP - RADIOHEAD\n")
    time.sleep(2)
    
    while not pila_karaoke.esta_vacia():
        linea_actual = pila_karaoke.desapilar()
        
        texto = linea_actual["texto"]
        espera = linea_actual["espera"]
        color = linea_actual["color"]
        
    print(f"{color}{texto}{RESET}")
    time.sleep(espera)

if _name_ == "_main_":
        reproducir_karaoke()