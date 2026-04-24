import time
import os

CYAN     = "/033[96m"
VERDE    = "/033[32m"
AMARILLO = "/033[33m"
MAGENTA  = "/033[35m"
NEGRITA  = "/033[1m"
RESET   = "/033[0m"

class Pila:
    def __init__(self):
        self.item = []
   
    def apilar(self, item):
        self.item.append(item)
   
    def desapilar(self):
        if not self.esta_vacia():
            return self.item.pop()
        return None
   
    def esta_vacia(self):
            return len(self.item) ==0
       
cancion = [
    {
        "texto": "Empezó de cero a ser lo que querían\nLas muñecas, y dar siempre la razón\nLa obediencia y la ternura, le decían\nSer rebelde era un asunto del varón",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Y empezaron a romperse los botones\nY una curva que no estaba, apareció\nUn escote en lugar de los listones\nY la niña, aquella tarde, se perdió",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Es mujer porque lo siente en todas partes\nPorque Venus se lo dijo aquella vez\nNo le digan que no puede, sabe arañar cuando no quiere\nY también cuando lo quiere un poco más",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Ella\nElla\nElla es mujer porque lo siente al respirar",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Su primera vez, fue un fiasco inolvidable\nQue duró lo que un bostezo en un sillón\nSin pericia, el sexo es tan desagradable\nQue quedó buscando alguna explicación",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Ser sutil, se lo aprendió a las mariposas\nY el amor lo conoció en la decepción\nLa engañó el mismo que le mandaba rosas\nEstá hecha de tanta equivocación",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Siente como dardos las miradas entre damas, mientras gritan: Solidaridad\nTiempo de resaca en la ventana, vientos grises, qué difícil es vivir con la verdad\nElla no es ni débil ni enemiga\nY el amor fue siempre lo mejor que le pasó",
        "espera": 2,
        "color": "MAGENTA"
    },
    {
        "texto": "Es mujer y se defiende como puede\nNo es tan fácil desplazarse por ahí\nNi enemiga, ni domada, ni con miedo\nNo es panfleto, ni venganza, ni rencor\nSolo mujer",
        "espera": 2,
        "color": "MAGENTA"
    }
]
def reproducir_karaoke():
    Pila_karaoke = Pila()
   
    for linea in reversed(cancion):
        Pila_karaoke.apilar(linea)
       
    os.system("cls" if os.name == "no" else "clear")
   
    print(f"{MAGENTA}{NEGRITA}PREPARADO LISTA DE CANCION: MUJER BY RICARDO ARJONA\n")
    time.sleep(2)
   
    while not Pila_karaoke.esta_vacia():
        linea_actual = Pila_karaoke.desapilar()
       
        texto = linea_actual["texto"]
        espera = linea_actual["espera"]
        color = linea_actual["color"]
       
        print(f"{color}{texto}{RESET}")
        time.sleep(espera)
       
       
   
if __name__ == "__main__":
    reproducir_karaoke()