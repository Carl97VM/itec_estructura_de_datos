// #region Pila_JS
class Pila {
    #items = [];

    push(item) {
        this.#items.push(item);
    }

    pop() {
        if (this.isEmpty()) return "Underflow";
        return this.#items.pop();
    }

    peek() {
        return this.#items[this.#items.length - 1];
    }

    isEmpty() {
        return this.#items.length === 0;
    }
}

// Aplicación: Validar si una cadena de texto está balanceada
function verificarParentesis(cadena) {
    const pila = new Pila();
    for (let char of cadena) {
        if (char === '(') {
            pila.push(char);
        } else if (char === ')') {
            if (pila.isEmpty()) return false;
            pila.pop();
        }
    }
    return pila.isEmpty();
}

console.log(verificarParentesis("(())")); // true
console.log(verificarParentesis("(()"));  // false
// #endregion