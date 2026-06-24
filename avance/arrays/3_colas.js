// #region Cola_Pro_JS
class ColaImpresion {
    #items = {};
    #frente = 0;
    #atras = 0;

    // Encolar (Enqueue)
    encolar(documento) {
        this.#items[this.#atras] = documento;
        this.#atras++;
        console.log(`Documento "${documento}" en cola.`);
    }

    // Desencolar (Dequeue) - O(1) real
    desencolar() {
        if (this.isEmpty()) return null;

        const item = this.#items[this.#frente];
        delete this.#items[this.#frente]; // Limpieza de memoria
        this.#frente++;
        console.log(`Imprimiendo: ${item}...`);
        return item;
    }

    isEmpty() {
        return this.#atras - this.#frente === 0;
    }
}

// Uso
const impresora = new ColaImpresion();
impresora.encolar("Tesis_Final.pdf");
impresora.encolar("Diagrama_Arquitectura.png");
impresora.desencolar();
impresora.desencolar();
impresora.desencolar();
// #endregion