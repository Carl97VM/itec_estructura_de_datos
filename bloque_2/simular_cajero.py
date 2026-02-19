from collections import deque

def simulador_turnos(clientes):
    cola = deque(clientes)
    while cola:
        proximo = cola.popleft() # O(1) en deque
        print(f"Atendiendo a: {proximo}")

# Por qué: Usar list.pop(0) es O(n). Usar deque.popleft() es O(1). 
# Es vital enseñar a elegir la herramienta correcta en Python.