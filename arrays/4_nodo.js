// #region Listas_Enlazadas_JS
class Nodo {
    constructor(dato) {
        this.dato = dato;
        this.siguiente = null;
    }
}

class ListaEnlazada {
    constructor() {
        this.cabeza = null;
    }

    // Insertar al final (O(n) si no tenemos puntero al 'cola')
    insertarAlFinal(dato) {
        const nuevoNodo = new Nodo(dato);
        if (!this.cabeza) {
            this.cabeza = nuevoNodo;
            return;
        }
        let actual = this.cabeza;
        while (actual.siguiente) {
            actual = actual.siguiente;
        }
        actual.siguiente = nuevoNodo;
    }

    imprimir() {
        let actual = this.cabeza;
        let salida = "";
        while (actual) {
            salida += `[${actual.dato}] -> `;
            actual = actual.siguiente;
        }
        console.log(salida + "null");
    }
}

const miLista = new ListaEnlazada();
miLista.insertarAlFinal("Dato 1");
miLista.insertarAlFinal("Dato 2");
miLista.imprimir(); // [Dato 1] -> [Dato 2] -> null
// #endregion