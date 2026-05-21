import os

def menu_operaciones():
    while True:
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("===========================")
        print("=== Menú de Operaciones ===")
        print("===========================")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        print("===========================")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if(opcion == '5'):
            print("Has seleccionado Salir, Saliendo del programa.")
            break
        
        # elif(opcion == '1'):
        #     print("Has seleccionado Sumar.")
        #     # Aquí puedes agregar la lógica para sumar
        # elif(opcion == '2'):
        #     print("Has seleccionado Restar.")
        #     # Aquí puedes agregar la lógica para restar
        # elif(opcion == '3'):
        #     print("Has seleccionado Multiplicar.")
        #     # Aquí puedes agregar la lógica para multiplicar
        # elif(opcion == '4'):
        #     print("Has seleccionado Dividir.")
        #     # Aquí puedes agregar la lógica para dividir
        # else:
        #     print("Opción no válida. Por favor, seleccione una opción válida.")
        
        if opcion in ['1', '2', '3', '4']:
            print("Has seleccionado una operación matemática.")
            # Aquí puedes agregar la lógica para realizar la operación seleccionada
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                match opcion:
                    case '1':
                        resultado = num1 + num2
                        print(f"El resultado de la suma es: {resultado}")
                    case '2':
                        resultado = num1 - num2
                        print(f"El resultado de la resta es: {resultado}")
                    case '3':
                        resultado = num1 * num2
                        print(f"El resultado de la multiplicación es: {resultado}")
                    case '4':
                        if num2 != 0:
                            resultado = num1 / num2
                            print(f"El resultado de la división es: {resultado}")
                        else:
                            print("Error: No se puede dividir por cero.")
                    case _:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu_operaciones()