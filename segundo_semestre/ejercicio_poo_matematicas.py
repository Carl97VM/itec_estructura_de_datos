"""
Ejercicio 2: POO con funciones matemáticas y limpieza de datos

Objetivo:
- Practicar programación orientada a objetos usando datos numéricos.
- Implementar limpieza de datos y operaciones matemáticas básicas.

Requisitos:
1. Crear la clase DatosMatematicos con:
   - lista_datos: lista privada de valores numéricos.
   - agregar_dato(valor): agrega un valor.
   - limpiar(): elimina datos no numéricos y valores nulos.
   - promedio(): calcula el promedio.
   - suma(): suma los datos válidos.
   - maximo(): devuelve el valor máximo.
   - minimo(): devuelve el valor mínimo.
   - transformar(funcion): aplica una función matemática a cada dato.
2. Probar la clase con un menú interactivo.
"""

class DatosMatematicos:
    def __init__(self):
        self._lista_datos = []

    def agregar_dato(self, valor):
        self._lista_datos.append(valor)

    def _datos_numericos(self):
        return [valor for valor in self._lista_datos if isinstance(valor, (int, float))]

    def limpiar(self):
        self._lista_datos = self._datos_numericos()
        return self._lista_datos

    def suma(self):
        return sum(self._datos_numericos())

    def promedio(self):
        datos = self._datos_numericos()
        if not datos:
            return None
        return sum(datos) / len(datos)

    def maximo(self):
        datos = self._datos_numericos()
        if not datos:
            return None
        return max(datos)

    def minimo(self):
        datos = self._datos_numericos()
        if not datos:
            return None
        return min(datos)

    def transformar(self, funcion):
        datos = self._datos_numericos()
        self._lista_datos = [funcion(valor) for valor in datos]
        return self._lista_datos

    def mostrar(self):
        if not self._lista_datos:
            print("No hay datos válidos para mostrar.")
            return
        print("Datos actuales:", self._lista_datos)


def menu():
    datos = DatosMatematicos()
    while True:
        print("\n=== Ejercicio POO: Matemáticas y limpieza de datos ===")
        print("1. Agregar dato")
        print("2. Limpiar datos")
        print("3. Mostrar datos")
        print("4. Suma de datos")
        print("5. Promedio de datos")
        print("6. Máximo y mínimo")
        print("7. Aplicar transformación matemática")
        print("8. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            valor = input("Ingrese un valor numérico o texto inválido: ")
            try:
                dato = float(valor) if "." in valor else int(valor)
            except ValueError:
                dato = valor
            datos.agregar_dato(dato)
            print("Dato agregado.")
        elif opcion == "2":
            datos.limpiar()
            print("Datos limpiados. Sólo datos numéricos válidos quedan.")
        elif opcion == "3":
            datos.mostrar()
        elif opcion == "4":
            suma = datos.suma()
            print(f"Suma: {suma}")
        elif opcion == "5":
            promedio = datos.promedio()
            print(f"Promedio: {promedio}" if promedio is not None else "No hay datos numéricos válidos para calcular el promedio.")
        elif opcion == "6":
            maximo = datos.maximo()
            minimo = datos.minimo()
            if maximo is None:
                print("No hay datos numéricos válidos para calcular máximo y mínimo.")
            else:
                print(f"Máximo: {maximo}, Mínimo: {minimo}")
        elif opcion == "7":
            datos.limpiar()
            if not datos._lista_datos:
                print("No hay datos numéricos válidos para transformar. Antes limpie los datos.")
            else:
                print("Transformaciones disponibles:")
                print("1. Elevar al cuadrado")
                print("2. Raíz cuadrada")
                print("3. Multiplicar por 10")
                opcion_trans = input("Seleccione una transformación: ").strip()
                if opcion_trans == "1":
                    datos.transformar(lambda x: x * x)
                    print("Transformación al cuadrado aplicada.")
                elif opcion_trans == "2":
                    datos.transformar(lambda x: x ** 0.5 if x >= 0 else x)
                    print("Transformación de raíz cuadrada aplicada (los valores negativos se mantienen).")
                elif opcion_trans == "3":
                    datos.transformar(lambda x: x * 10)
                    print("Transformación multiplicar por 10 aplicada.")
                else:
                    print("Opción de transformación no válida.")
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    menu()
