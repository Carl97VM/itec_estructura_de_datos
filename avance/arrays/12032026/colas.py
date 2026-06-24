from collections import deque

## Primeros en entrar, primeros en salir (FIFO)
class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, item):
        self.items.append(item) ## Insertar al final

    def desencolar(self):
        if self.items:
            return self.items.popleft() ## Eliminar el primer elemento
        return "La Cola esta vacia"

    def esta_vacio(self):
        return len(self.items) == 0 ## verdadero o Falso

    def ver_frente(self):
        return self.items[0] if not self.esta_vacio() else "La Cola esta vacia"

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# --- PRUEBA DE LA COLA ---

c = Cola()

print("¿Está vacía?", c.esta_vacio())

c.encolar("Ana")
c.encolar("Luis")
c.encolar("Maria")

print("Cola actual:", c)
print("Frente:", c.ver_frente())
print("Tamaño:", c.tamano())

print("\nDesencolando:", c.desencolar())
print("Cola actual:", c)

print("\nDesencolando:", c.desencolar())
print("Desencolando:", c.desencolar())

print("\n¿Está vacía?", c.esta_vacio())
print("Intentando desencolar de cola vacía:", c.desencolar())