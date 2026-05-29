# def area_circulo():
#     print(f"{AMARILLO}Calcular el área de un círculo{RESET}")
#     try:
#         radio = float(input(f"{VERDE}Ingrese el radio: {RESET}"))
#         area = math.pi * radio**2
#         print(f"{CYAN}El área es: {area}{RESET}")
#     except ValueError:
#         print(f"{ROJO}Ingrese un número válido{RESET}")
       
# def factorial_numero():
#     print(f"{AMARILLO}Factorial de un número{RESET}")
#     try:
#         numero = int(input(f"{VERDE}Ingrese un número entero: {RESET}"))

#         resultado = math.factorial(numero)

#         print(f"{CYAN}El factorial es: {resultado}{RESET}")
#     except ValueError:
#         print(f"{ROJO}Ingrese un número entero válido{RESET}")

# def raiz_cuadrada():
#     print(f"{AMARILLO}Calcular raíz cuadrada{RESET}")

#     try:
#         numero = float(input(f"{VERDE}Ingrese un número: {RESET}"))

#         if numero < 0:
#             print(f"{ROJO}No se puede calcular raíz de números negativos{RESET}")
#         else:
#             resultado = math.sqrt(numero)
#             print(f"{CYAN}La raíz cuadrada es: {resultado}{RESET}")

#     except ValueError:
#         print(f"{ROJO}Ingrese un número válido{RESET}")

# def calcular_promedio():
#     print(f"{AMARILLO}Calcular promedio{RESET}")

#     try:
#         cantidad = int(input(f"{VERDE}¿Cuántos números desea ingresar?: {RESET}"))

#         suma = 0

#         for i in range(cantidad):
#             numero = float(input(f"Ingrese el número {i+1}: "))
#             suma += numero

#         promedio = suma / cantidad

#         print(f"{CYAN}El promedio es: {promedio}{RESET}")

#     except ValueError:
#         print(f"{ROJO}Ingrese un número válido{RESET}")



# COBINACION DE CONSOLA Y MENU

import os
import math

def menu_operaciones():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
       
        print("===========================")
        print("=== Menu de operaciones ===")
        print("===========================")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Calcular hipotenusa")
        print("6. Raíz cuadrada")
        print("7. Factorial")
        print("8. Promedio")
        print("9. Salir")
        print("===========================")
       
        opcion = input("Seleccione una opcion (1-9): ")
       
        if opcion == '9':
            print("Has seleccionado salir, saliendo del programa.")
            break
       
        # Operaciones básicas
        if opcion in ['1','2','3','4']:
            try:
                num1 = float(input("Ingrese el primer numero: "))
                num2 = float(input("Ingrese el segundo numero: "))
               
                match opcion:
                    case '1':
                        resultado = num1 + num2
                        print(f"Resultado: {resultado}")
                    case '2':
                        resultado = num1 - num2
                        print(f"Resultado: {resultado}")
                    case '3':
                        resultado = num1 * num2
                        print(f"Resultado: {resultado}")
                    case '4':
                        if num2 != 0:
                            resultado = num1 / num2
                            print(f"Resultado: {resultado}")
                        else:
                            print("Error: No se puede dividir entre cero.")
            except ValueError:
                print("Error: Ingrese un numero valido.")
       
        # Hipotenusa
        elif opcion == '5':
            try:
                cateto1 = float(input("Ingrese el primer cateto: "))
                cateto2 = float(input("Ingrese el segundo cateto: "))
                hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
                print(f"La hipotenusa es: {hipotenusa}")
            except ValueError:
                print("Error: Ingrese numeros validos.")
       
        # Raíz cuadrada
        elif opcion == '6':
            try:
                numero = float(input("Ingrese un numero: "))
                if numero < 0:
                    print("Error: No se puede calcular raiz de un numero negativo.")
                else:
                    print(f"La raiz cuadrada es: {math.sqrt(numero)}")
            except ValueError:
                print("Error: Ingrese un numero valido.")
       
        # Factorial
        elif opcion == '7':
            try:
                numero = int(input("Ingrese un numero entero: "))
                if numero < 0:
                    print("Error: No se puede calcular factorial de un numero negativo.")
                else:
                    print(f"El factorial es: {math.factorial(numero)}")
            except ValueError:
                print("Error: Ingrese un numero entero valido.")
       
        # Promedio
        elif opcion == '8':
            try:
                cantidad = int(input("¿Cuantos numeros desea ingresar?: "))
                suma = 0
                for i in range(cantidad):
                    n = float(input(f"Ingrese numero {i+1}: "))
                    suma += n
                print(f"El promedio es: {suma/cantidad}")
            except ValueError:
                print("Error: Ingrese valores validos.")
       
        else:
            print("Opcion no valida. Intente nuevamente.")
       
        input("Presione Enter para continuar...")
       
if __name__=="__main__":
    menu_operaciones()