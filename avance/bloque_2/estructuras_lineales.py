# Desafío: "Simulador de Navegación Web (Pila)".
# Usa una pila para simular el botón "Atrás" de un navegador.

historial = []

def visitar_pagina(url):
    historial.append(url)
    print(f"Visitando: {url}")

def boton_atras():
    if len(historial) > 1:
        historial.pop()
        print(f"Regresando a: {historial[-1]}")
    else:
        print("No hay más páginas en el historial.")