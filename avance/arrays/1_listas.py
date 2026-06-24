# #region Listas
tareas = ["Estudiar Big O", "Comprar café"]

# Añadir (O(1) al final)
tareas.append("Practicar Quicksort")

# Eliminar una tarea específica (O(n))
tareas.remove("Comprar café")

# Acceder por índice (O(1))
print(f"La primera tarea es: {tareas[0]}")

# Listar todas (O(n))
print("Lista de tareas:", tareas)
# #endregion 

# #region Tuplas
# Tupla: Datos fijos
ubicacion_sensor = (-19.0333, -65.2627) # Sucre, Bolivia

# Lista: Datos que crecen
mediciones = [22.5, 23.0, 21.8]

# Intento de cambio
# ubicacion_sensor[0] = -20.0 
mediciones.append(24.1)
print(f"Sensor en {ubicacion_sensor} - Última medición: {mediciones[-1]}°C")
# #endregion

# #region Lista de Tuplas
inventario = [
    (101, "Tubos de ensayo", 50),
    (102, "Placas de Petri", 30),
    (103, "Reactivo pH", 10)
]

def actualizar_stock(lista_inv, id_producto, nuevo_stock):
    for i in range(len(lista_inv)):
        id_p, nombre, stock = lista_inv[i]
        if id_p == id_producto:
            lista_inv[i] = (id_p, nombre, nuevo_stock)
            print(f"Stock de {nombre} actualizado a {nuevo_stock}.")
            return
    print("Producto no encontrado.")

actualizar_stock(inventario, 102, 45)
print("Inventario final:", inventario)
# #endregion