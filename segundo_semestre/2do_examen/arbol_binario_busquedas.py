class NodoLibro:
    def __init__(self, codigo, titulo, autor, cantidad):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.izq = None
        self.der = None


class ArbolBiblioteca:
    def __init__(self):
        self.raiz = None

    # 1. Insertar un libro
    def insertar(self, codigo, titulo, autor, cantidad):
        if self.raiz == None:
            self.raiz = NodoLibro(codigo, titulo, autor, cantidad)
            print(f"[+] Libro creado como raíz: {titulo}")
        else:
            self._insertar_recursivo(
                self.raiz,
                codigo,
                titulo,
                autor,
                cantidad
            )

    def _insertar_recursivo(self, nodo, codigo, titulo, autor, cantidad):
        if codigo < nodo.codigo:
            if nodo.izq is None:
                nodo.izq = NodoLibro(codigo, titulo, autor, cantidad)
                print(f"[+] Libro insertado a la izquierda de {nodo.codigo}")
            else:
                self._insertar_recursivo(
                    nodo.izq,
                    codigo,
                    titulo,
                    autor,
                    cantidad
                )

        elif codigo > nodo.codigo:
            if nodo.der is None:
                nodo.der = NodoLibro(codigo, titulo, autor, cantidad)
                print(f"[+] Libro insertado a la derecha de {nodo.codigo}")
            else:
                self._insertar_recursivo(
                    nodo.der,
                    codigo,
                    titulo,
                    autor,
                    cantidad
                )

        else:
            print("[!] El código ya existe")

    # 2. Buscar un libro
    def buscar(self, codigo):
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo, codigo):
        if nodo is None:
            return None

        if codigo == nodo.codigo:
            return nodo

        if codigo < nodo.codigo:
            return self._buscar_recursivo(nodo.izq, codigo)
        else:
            return self._buscar_recursivo(nodo.der, codigo)

    # 3. Mostrar libros en inorden
    def mostrar_inorden(self):
        if self.raiz is None:
            print("La biblioteca está vacía")
            return

        print("\n--- LIBROS ORDENADOS POR CÓDIGO ---")
        self._inorden(self.raiz)
        print("-----------------------------------")

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izq)

            print(
                f"Código: {nodo.codigo} | "
                f"Título: {nodo.titulo} | "
                f"Autor: {nodo.autor} | "
                f"Cantidad: {nodo.cantidad}"
            )

            self._inorden(nodo.der)

    # 4. Mostrar libros en preorden
    def mostrar_preorden(self):
        print("\n--- RECORRIDO PREORDEN ---")
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo is not None:
            print(f"{nodo.codigo} - {nodo.titulo}")
            self._preorden(nodo.izq)
            self._preorden(nodo.der)

    # 5. Buscar el libro con menor código
    def buscar_minimo(self):
        if self.raiz is None:
            return None

        actual = self.raiz

        while actual.izq is not None:
            actual = actual.izq

        return actual

    # 6. Buscar el libro con mayor código
    def buscar_maximo(self):
        if self.raiz is None:
            return None

        actual = self.raiz

        while actual.der is not None:
            actual = actual.der

        return actual

    # 7. Actualizar la cantidad disponible
    def actualizar_cantidad(self, codigo, nueva_cantidad):
        libro = self.buscar(codigo)

        if libro is None:
            print("[!] Libro no encontrado")
            return False

        libro.cantidad = nueva_cantidad
        print("[+] Cantidad actualizada correctamente")
        return True

    # 8. Eliminar un libro
    def eliminar(self, codigo):
        if self.buscar(codigo) is None:
            print("[!] El libro no existe")
            return False

        self.raiz = self._eliminar_recursivo(self.raiz, codigo)
        print("[+] Libro eliminado")
        return True

    def _eliminar_recursivo(self, nodo, codigo):
        if nodo is None:
            return None

        if codigo < nodo.codigo:
            nodo.izq = self._eliminar_recursivo(nodo.izq, codigo)

        elif codigo > nodo.codigo:
            nodo.der = self._eliminar_recursivo(nodo.der, codigo)

        else:
            # Caso 1: no tiene hijos
            if nodo.izq is None and nodo.der is None:
                return None

            # Caso 2: solo tiene hijo derecho
            if nodo.izq is None:
                return nodo.der

            # Caso 3: solo tiene hijo izquierdo
            if nodo.der is None:
                return nodo.izq

            # Caso 4: tiene dos hijos
            sucesor = self._buscar_minimo_desde(nodo.der)

            nodo.codigo = sucesor.codigo
            nodo.titulo = sucesor.titulo
            nodo.autor = sucesor.autor
            nodo.cantidad = sucesor.cantidad

            nodo.der = self._eliminar_recursivo(
                nodo.der,
                sucesor.codigo
            )

        return nodo

    def _buscar_minimo_desde(self, nodo):
        actual = nodo

        while actual.izq is not None:
            actual = actual.izq

        return actual


def mostrar_libro(libro):
    if libro is None:
        print("[!] Libro no encontrado")
        return

    print("\nLibro encontrado")
    print(f"Código: {libro.codigo}")
    print(f"Título: {libro.titulo}")
    print(f"Autor: {libro.autor}")
    print(f"Cantidad: {libro.cantidad}")


def cargar_datos_iniciales(arbol):
    arbol.insertar(50, "Python Básico", "Ana López", 4)
    arbol.insertar(30, "Estructuras de Datos", "Luis Pérez", 2)
    arbol.insertar(70, "Bases de Datos", "María Díaz", 5)
    arbol.insertar(20, "Algoritmos", "Carlos Ruiz", 3)
    arbol.insertar(40, "Programación Web", "Sofía Vargas", 6)
    arbol.insertar(60, "Redes de Computadoras", "Pedro Salas", 1)
    arbol.insertar(80, "Sistemas Operativos", "Laura Gómez", 2)


def menu():
    arbol = ArbolBiblioteca()
    cargar_datos_iniciales(arbol)

    while True:
        print("\n" + "=" * 40)
        print("        SISTEMA DE BIBLIOTECA")
        print("=" * 40)
        print("1. Insertar libro")
        print("2. Buscar libro")
        print("3. Mostrar recorrido inorden")
        print("4. Mostrar recorrido preorden")
        print("5. Ver libro con menor código")
        print("6. Ver libro con mayor código")
        print("7. Actualizar cantidad")
        print("8. Eliminar libro")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                codigo = int(input("Código: "))
                titulo = input("Título: ")
                autor = input("Autor: ")
                cantidad = int(input("Cantidad: "))

                arbol.insertar(codigo, titulo, autor, cantidad)

            except ValueError:
                print("[!] Código y cantidad deben ser números")

        elif opcion == "2":
            try:
                codigo = int(input("Código a buscar: "))
                libro = arbol.buscar(codigo)
                mostrar_libro(libro)

            except ValueError:
                print("[!] El código debe ser numérico")

        elif opcion == "3":
            arbol.mostrar_inorden()

        elif opcion == "4":
            arbol.mostrar_preorden()

        elif opcion == "5":
            libro = arbol.buscar_minimo()
            mostrar_libro(libro)

        elif opcion == "6":
            libro = arbol.buscar_maximo()
            mostrar_libro(libro)

        elif opcion == "7":
            try:
                codigo = int(input("Código del libro: "))
                cantidad = int(input("Nueva cantidad: "))
                arbol.actualizar_cantidad(codigo, cantidad)

            except ValueError:
                print("[!] Los valores deben ser numéricos")

        elif opcion == "8":
            try:
                codigo = int(input("Código a eliminar: "))
                arbol.eliminar(codigo)

            except ValueError:
                print("[!] El código debe ser numérico")

        elif opcion == "9":
            print("Programa finalizado")
            break

        else:
            print("[!] Opción inválida")


if __name__ == "__main__":
    menu()





# Instrucciones para los estudiantes
# Corrige el programa para que pueda:

# Crear correctamente el árbol.

# Insertar libros sin perder nodos.

# Rechazar códigos duplicados.

# Buscar libros por código.

# Mostrar correctamente el recorrido inorden.

# Mostrar correctamente el recorrido preorden.

# Obtener el libro de menor código.

# Obtener el libro de mayor código.

# Actualizar la cantidad disponible.

# Eliminar libros en los siguientes casos:

# Nodo hoja.

# Nodo con un solo hijo izquierdo.

# Nodo con un solo hijo derecho.

# Nodo con dos hijos.

# Evitar que el programa se cierre ante datos inválidos.

# Mantener el orden del árbol después de cada operación.

# Errores sugeridos para insertar
# Puedes entregar el código anterior tal como está o agregar algunos errores controlados para aumentar la dificultad.


# Pruebas obligatorias
# Los estudiantes deben probar estas operaciones:

# text

# 1. Buscar el libro 40.
# 2. Buscar el libro 99.
# 3. Insertar un libro con código 45.
# 4. Intentar insertar nuevamente el código 45.
# 5. Mostrar el recorrido inorden.
# 6. Consultar el mínimo.
# 7. Consultar el máximo.
# 8. Actualizar la cantidad del libro 30.
# 9. Eliminar el libro 20.
# 10. Eliminar el libro 30.
# 11. Eliminar el libro 50.
# 12. Mostrar nuevamente el recorrido inorden.
# La salida inorden correcta después de cargar los datos iniciales debe mostrar los códigos en este orden:

# text

# 20, 30, 40, 50, 60, 70, 80
# Si se inserta el código 45, el orden esperado será:

# text

# 20, 30, 40, 45, 50, 60, 70, 80
# Preguntas de análisis
# ¿Por qué el código menor que el nodo actual se inserta a la izquierda?

# ¿Qué sucede si se permiten códigos duplicados?

# ¿Qué diferencia existe entre recorrido inorden y preorden?

# ¿Por qué es necesario reasignar self.raiz después de eliminar?

# ¿Qué ocurre al eliminar un nodo hoja?

# ¿Qué ocurre al eliminar un nodo con dos hijos?

# ¿Qué función cumple el sucesor inorden?

# ¿Por qué la búsqueda puede ser más rápida que recorrer todos los nodos?

# ¿Qué pasa si los códigos se insertan siempre ordenados?

# ¿Qué complejidad tendría el árbol si queda completamente desequilibrado?

# Errores esperados
# Algunos errores deben producir:

# text

# NameError
# text

# AttributeError
# text

# RecursionError
# o resultados incorrectos sin producir excepciones. Esto es útil porque obliga al estudiante a diferenciar entre errores de sintaxis, errores de ejecución y errores lógicos. En estructuras recursivas, una causa frecuente de fallos es no devolver o reasignar correctamente el nodo actualizado durante la recursión.
# stackoverflow
# +1

# Criterio de evaluación
# Criterio	Puntos
# Corrección de la clase NodoLibro	10
# Inserción recursiva	15
# Búsqueda	10
# Recorrido inorden	10
# Recorrido preorden	10
# Mínimo y máximo	10
# Actualización de cantidades	10
# Eliminación de los cuatro casos	20
# Menú y validación de datos	5
# Total	100
