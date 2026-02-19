#/*
# Ejercicio 1: 
# Comparación de Escenarios (Notación Big O)
# Problema: Implementa dos funciones para sumar los primeros $n$ números enteros. Una debe usar un ciclo for y la otra la fórmula matemática de Gauss.
# suma_lineal(n): $O(n)$
# suma_constante(n): $O(1)$
#*/

import time

# O(n) - El tiempo crece proporcional a n
def suma_lineal(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# O(1) - El tiempo es siempre el mismo (Fórmula de Gauss)
def suma_constante(n):
    return (n * (n + 1)) // 2

# Por qué: En programación competitiva o Big Data, una solución O(1) 
# es la diferencia entre un programa que tarda segundos y uno que tarda milisegundos.