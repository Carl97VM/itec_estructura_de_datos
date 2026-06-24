# Problema: Representa una red de amigos y encuentra si existe una conexión entre dos personas (Búsqueda en Anchura - BFS).

from collections import deque

red_social = {
    'Carlo': ['Juan', 'Ana'],
    'Juan': ['Carlo', 'Pedro'],
    'Ana': ['Carlo', 'Luis'],
    'Pedro': ['Juan'],
    'Luis': ['Ana']
}

def existe_conexion(red, inicio, destino):
    cola = deque([inicio])
    visitados = {inicio}
    
    while cola:
        persona = cola.popleft()
        if persona == destino: return True
        for amigo in red[persona]:
            if amigo not in visitados:
                visitados.add(amigo)
                cola.append(amigo)
    return False

print(f"¿Conexión Carlo -> Pedro?: {existe_conexion(red_social, 'Carlo', 'Pedro')}") # True