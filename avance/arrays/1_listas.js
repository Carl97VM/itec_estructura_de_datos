// #region Listas (Arrays)
// En JS, las listas son Arrays mutables.
let tareas = ["Estudiar Big O", "Comprar café"];

// Añadir (O(1) al final)
tareas.push("Practicar Quicksort");

// Eliminar una tarea específica (O(n))
// Buscamos el índice y luego removemos 1 elemento
const indiceABorrar = tareas.indexOf("Comprar café");
if (indiceABorrar !== -1) {
    tareas.splice(indiceABorrar, 1);
}

// Acceder por índice (O(1))
console.log(`La primera tarea es: ${tareas[0]}`);

// Listar todas (O(n))
console.log("Lista de tareas:", tareas);
// #endregion

// #region Simulación de Tuplas (Inmutabilidad)
// Usamos Object.freeze() para que el array sea inmutable como una tupla.
const ubicacionSensor = Object.freeze([-19.0333, -65.2627]); // Sucre, Bolivia [cite: 5, 20]

// Lista de mediciones (Sigue siendo mutable)
let mediciones = [22.5, 23.0, 21.8];

// Intento de cambio (En modo estricto daría error; aquí simplemente no hace nada)
ubicacionSensor[0] = -20.0;

mediciones.push(24.1);
console.log(`Sensor en [${ubicacionSensor}] - Última medición: ${mediciones[mediciones.length - 1]}°C`);
// #endregion

// #region Lista de Objetos (Equivalente a Lista de Tuplas)
// En JS, en lugar de (ID, Nombre, Stock), es más común usar objetos {id, nombre, stock}
let inventario = [
    { id: 101, nombre: "Tubos de ensayo", stock: 50 },
    { id: 102, nombre: "Placas de Petri", stock: 30 },
    { id: 103, nombre: "Reactivo pH", stock: 10 }
];

/**
 * Actualiza el stock de un producto específico
 * Justificación: O(n) por el recorrido de la lista.
 */
function actualizarStock(listaInv, idProducto, nuevoStock) {
    const producto = listaInv.find(p => p.id === idProducto);

    if (producto) {
        producto.stock = nuevoStock;
        console.log(`Stock de ${producto.nombre} actualizado a ${nuevoStock}.`);
    } else {
        console.log("Producto no encontrado.");
    }
}

// Prueba
actualizarStock(inventario, 102, 45);
console.log("Inventario final:", inventario);
// #endregion