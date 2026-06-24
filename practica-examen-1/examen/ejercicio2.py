import os
from collections import deque

class Commit:
    def __init__(self, id_commit, mensaje):
        self.id = id_commit
        self.mensaje = mensaje
    def __repr__(self):
        return f"{{ID:{self.id}, Msg:'{self.mensaje}'}}"

class ControlVersiones:
    def __init__(self, capacidad_stash=3):
        self.commits = []          # Pila
        self.redo = []             # Pila
        self.stash = deque(maxlen=capacidad_stash) # Cola con límite
        self.contador_ids = 1

    def commit(self, mensaje):
        nuevo_commit = Commit(self.contador_ids, mensaje)
        self.commits.append(nuevo_commit)
        self.contador_ids += 1
        self.redo = [] # Limpiar pila redo
        print(f"Commit realizado: {nuevo_commit}")

    def revert(self):
        if self.commits:
            commit_a_revertir = self.commits.pop()
            self.redo.append(commit_a_revertir)
            print(f"Revert ejecutado: {commit_a_revertir}")
        else:
            print("No hay commits para revertir.")
    
    def redo_op(self):
        if self.redo:
            commit_a_rehacer = self.redo.pop()
            self.commits.append(commit_a_rehacer)
            print(f"Redo ejecutado: {commit_a_rehacer}")
        else:
            print("Nada que rehacer.")

    def stash_op(self):
        if self.commits:
            # Regla: No usar acceso aleatorio (index -1). 
            # Sacamos, clonamos y devolvemos para mantener la integridad.
            ultimo = self.commits.pop()
            self.stash.append(ultimo)
            self.commits.append(ultimo)
            print(f"Estado {ultimo} guardado en Stash.")
        else:
            print("No hay commits para hacer stash.")

    def apply_stash(self):
        if self.stash:
            commit_recuperado = self.stash.popleft()
            self.commit(f"Aplicado de Stash: {commit_recuperado.mensaje}")
        else:
            print("Stash vacío.")

    def mostrar(self):
        print(f"\n--- ESTADO DEL CONTROL DE VERSIONES ---")
        print(f"Pila Commits: {self.commits}")
        print(f"Pila Redo:    {self.redo}")
        print(f"Cola Stash:   {list(self.stash)}")
        print(f"Total operado: {len(self.commits) + len(self.redo) + len(self.stash)}")

def menu():
    cv = ControlVersiones(capacidad_stash=2) # Capacidad limitada
    while True:
        print("\n=== SISTEMA DE CONTROL DE VERSIONES ===")
        print("1. Commit \n 2. Revert \n 3. Redo \n 4. Stash \n 5. Apply Stash \n 6. Mostrar \n 0. Salir")
        op = input("Opción: ")
        if op == '1': cv.commit(input("Mensaje: "))
        elif op == '2': cv.revert()
        elif op == '3': cv.redo_op()
        elif op == '4': cv.stash_op()
        elif op == '5': cv.apply_stash()
        elif op == '6': cv.mostrar()
        elif op == '0': break

if __name__ == "__main__":
    menu()