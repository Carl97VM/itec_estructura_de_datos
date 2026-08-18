class NodoProducto:
    def __init__(self, id_producto, nombre, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.izq = None
        self.der = None

class ArbolInventario:
    def __init__(self):
        self.raiz = None

    # 1. Inserción recursiva
    def insertar(self, id_producto, nombre, cantidad):
        if self.raiz is None:
            self.raiz = NodoProducto(id_producto, nombre, cantidad)
            print(f"[*] Raíz creada: {nombre} (ID: {id_producto})")
        else:
            self._insertar_recursivo(self.raiz, id_producto, nombre, cantidad)

    def _insertar_recursivo(self, nodo_actual, id_producto, nombre, cantidad):
        if id_producto < nodo_actual.id_producto:
            if nodo_actual.izq is None:
                nodo_actual.izq = NodoProducto(id_producto, nombre, cantidad)
                print(f"[*] Insertado a la izquierda de {nodo_actual.id_producto}: {nombre}")
            else:
                self._insertar_recursivo(nodo_actual.izq, id_producto, nombre, cantidad)
        elif id_producto > nodo_actual.id_producto:
            if nodo_actual.der is None:
                nodo_actual.der = NodoProducto(id_producto, nombre, cantidad)
                print(f"[*] Insertado a la derecha de {nodo_actual.id_producto}: {nombre}")
            else:
                self._insertar_recursivo(nodo_actual.der, id_producto, nombre, cantidad)
        else:
            print("[!] El ID del producto ya existe. No se permiten duplicados.")

    # 2. Búsqueda exacta (Complejidad O(log n))
    def buscar(self, id_producto):
        return self._buscar_recursivo(self.raiz, id_producto)

    def _buscar_recursivo(self, nodo_actual, id_producto):
        if nodo_actual is None or nodo_actual.id_producto == id_producto:
            return nodo_actual
        
        if id_producto < nodo_actual.id_producto:
            return self._buscar_recursivo(nodo_actual.izq, id_producto)
        return self._buscar_recursivo(nodo_actual.der, id_producto)

    # 3. Búsqueda del Mínimo (El nodo más a la izquierda)
    def buscar_minimo(self):
        actual = self.raiz
        if actual is None: return None
        while actual.izq is not None:
            actual = actual.izq
        return actual

    # 4. Búsqueda del Máximo (El nodo más a la derecha)
    def buscar_maximo(self):
        actual = self.raiz
        if actual is None: return None
        while actual.der is not None:
            actual = actual.der
        return actual

    # 5. Recorrido Inorden (Muestra los nodos ordenados de menor a mayor ID)
    def mostrar_inventario(self):
        if self.raiz is None:
            print("El inventario está vacío.")
            return
        print("\n--- INVENTARIO ORDENADO POR ID (INORDEN) ---")
        self._inorden(self.raiz)
        print("--------------------------------------------")

    def _inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden(nodo_actual.izq)
            print(f"ID: {nodo_actual.id_producto} | Producto: {nodo_actual.nombre} | Cantidad: {nodo_actual.cantidad}")
            self._inorden(nodo_actual.der)

    # 6. Eliminación de un nodo (Maneja los 3 casos)
    def eliminar(self, id_producto):
        # La función recursiva retorna el nodo actualizado, por lo que reasignamos la raíz
        self.raiz = self._eliminar_recursivo(self.raiz, id_producto)

    def _eliminar_recursivo(self, nodo_actual, id_producto):
        # Si el árbol está vacío o no se encontró el ID
        if nodo_actual is None:
            return nodo_actual

        # Buscar el nodo a eliminar navegando por el árbol
        if id_producto < nodo_actual.id_producto:
            nodo_actual.izq = self._eliminar_recursivo(nodo_actual.izq, id_producto)
        elif id_producto > nodo_actual.id_producto:
            nodo_actual.der = self._eliminar_recursivo(nodo_actual.der, id_producto)
        
        # ¡Nodo encontrado!
        else:
            # Caso 1 y 2: El nodo tiene 0 o 1 hijo
            if nodo_actual.izq is None:
                temp = nodo_actual.der
                nodo_actual = None
                return temp
            elif nodo_actual.der is None:
                temp = nodo_actual.izq
                nodo_actual = None
                return temp

            # Caso 3: El nodo tiene 2 hijos
            # Encontrar el sucesor inorden (el menor de la rama derecha)
            temp = self._obtener_nodo_minimo(nodo_actual.der)

            # Copiar los datos del sucesor al nodo actual
            nodo_actual.id_producto = temp.id_producto
            nodo_actual.nombre = temp.nombre
            nodo_actual.cantidad = temp.cantidad

            # Eliminar el sucesor original de la rama derecha
            nodo_actual.der = self._eliminar_recursivo(nodo_actual.der, temp.id_producto)

        return nodo_actual

    # Función auxiliar para encontrar el nodo más a la izquierda a partir de uno dado
    def _obtener_nodo_minimo(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual


# ==========================================
# MENÚ INTERACTIVO
# ==========================================
def menu():
    arbol = ArbolInventario()
    
    # Datos de prueba iniciales
    arbol.insertar(50, "Laptop", 10)
    arbol.insertar(30, "Mouse", 50)
    arbol.insertar(70, "Monitor", 15)
    arbol.insertar(20, "Teclado", 30) # Para probar casos de eliminación
    arbol.insertar(40, "Audífonos", 25)

    while True:
        print("\n" + "="*30)
        print(" SISTEMA DE INVENTARIO (BST)")
        print("="*30)
        print("1. Agregar un nuevo producto")
        print("2. Buscar producto por ID")
        print("3. Ver producto con el ID más bajo (Mínimo)")
        print("4. Ver producto con el ID más alto (Máximo)")
        print("5. Mostrar todo el inventario (Ordenado)")
        print("6. Eliminar un producto")
        print("7. Salir")
        
        opcion = input("\nElige una opción (1-7): ")

        if opcion == '1':
            try:
                id_prod = int(input("Ingresa el ID (número entero): "))
                nombre = input("Ingresa el nombre del producto: ")
                cantidad = int(input("Ingresa la cantidad en stock: "))
                arbol.insertar(id_prod, nombre, cantidad)
            except ValueError:
                print("[!] Error: El ID y la cantidad deben ser números enteros.")

        elif opcion == '2':
            try:
                id_prod = int(input("Ingresa el ID a buscar: "))
                resultado = arbol.buscar(id_prod)
                if resultado:
                    print(f"\n[+] ENCONTRADO: {resultado.nombre} (Cantidad: {resultado.cantidad})")
                else:
                    print("\n[-] Producto no encontrado en el árbol.")
            except ValueError:
                print("[!] Error: El ID debe ser un número entero.")

        elif opcion == '3':
            minimo = arbol.buscar_minimo()
            if minimo:
                print(f"\n[+] Producto Mínimo -> ID: {minimo.id_producto} | Nombre: {minimo.nombre}")
            else:
                print("\n[-] El árbol está vacío.")

        elif opcion == '4':
            maximo = arbol.buscar_maximo()
            if maximo:
                print(f"\n[+] Producto Máximo -> ID: {maximo.id_producto} | Nombre: {maximo.nombre}")
            else:
                print("\n[-] El árbol está vacío.")

        elif opcion == '5':
            arbol.mostrar_inventario()
            
        elif opcion == '6':
            try:
                id_prod = int(input("Ingresa el ID del producto a eliminar: "))
                # Primero buscamos si existe para dar un mensaje claro
                if arbol.buscar(id_prod):
                    arbol.eliminar(id_prod)
                    print(f"\n[+] Producto con ID {id_prod} eliminado correctamente.")
                else:
                    print(f"\n[-] El producto con ID {id_prod} no existe en el inventario.")
            except ValueError:
                print("[!] Error: El ID debe ser un número entero.")

        elif opcion == '7':
            print("\nSaliendo del sistema... ¡Adiós!")
            break

        else:
            print("\n[!] Opción no válida. Intenta de nuevo.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu()