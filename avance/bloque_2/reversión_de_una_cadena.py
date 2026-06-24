#/*
# Ejercicio 2: Reversión de una cadena (Pilas - LIFO)
# Problema: Utiliza una lista de Python como una Pila para invertir el orden de las palabras en una oración.
#*/

def invertir_oracion(oracion):
    pila = oracion.split()
    resultado = []
    
    while len(pila) > 0:
        # pop() elimina y devuelve el último elemento: O(1)
        resultado.append(pila.pop()) 
        
    return " ".join(resultado)

# Por qué: Las Pilas (Stacks) son esenciales para entender la recursividad 
# y funciones de "deshacer" (Undo) en software.