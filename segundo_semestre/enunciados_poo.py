# 1. Cuenta Bancaria
# Crea una clase Cuenta que permita depositar y retirar dinero. Solo se puede retirar si hay saldo suficiente.

# class CuentaBancaria:
#     def __init__(self, titular, saldo_inicial):
#         self.titular = titular
#         self.saldo = saldo_inicial

#     def retirar(self, cantidad):
#         if cantidad <= self.saldo:
#             self.saldo -= cantidad
#             print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
#         else:
#             print("Fondos insuficientes.")

# # Uso
# mi_cuenta = CuentaBancaria("Juan", 100)
# mi_cuenta.retirar(150)
# mi_cuenta.retirar(50)

# 2. Sistema de Calificaciones
# Una clase Estudiante que determina si aprueba o reprueba basado en su nota (aprueba con 60 o más).
# class Estudiante:
#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota

#     def evaluar(self):
#         if self.nota >= 60:
#             return f"{self.nombre} ha APROBADO."
#         else:
#             return f"{self.nombre} ha REPROBADO."

# estudiante1 = Estudiante("Ana", 75)
# print(estudiante1.evaluar())

# 3. Control de Stock (Tienda)
# Una clase Producto que permita comprar artículos solo si hay stock disponible.

# class Producto:
#     def __init__(self, nombre, stock):
#         self.nombre = nombre
#         self.stock = stock

#     def comprar(self, cantidad):
#         if cantidad <= self.stock:
#             self.stock -= cantidad
#             print(f"Compraste {cantidad} {self.nombre}. Quedan {self.stock}.")
#         else:
#             print(f"No hay suficiente stock de {self.nombre}.")

# lapiz = Producto("Lápiz", 10)
# lapiz.comprar(5)
# lapiz.comprar(6)

# 4. Alquiler de Películas
# Una clase Pelicula que verifique la edad del usuario antes de permitir el alquiler.
# class Pelicula:
#     def __init__(self, titulo, edad_minima):
#         self.titulo = titulo
#         self.edad_minima = edad_minima

#     def alquilar(self, edad_usuario):
#         if edad_usuario >= self.edad_minima:
#             print(f"Disfruta la película: {self.titulo}")
#         else:
#             print("Eres demasiado joven para ver esta película.")

# peli = Pelicula("Terror Nocturno", 18)
# peli.alquilar(15)

# 5. Control de Termostato
# Un termostato que no permite que la temperatura suba de 30 grados ni baje de 10.

# class Termostato:
#     def __init__(self, temp_actual):
#         self.temperatura = temp_actual

#     def cambiar_temperatura(self, nueva_temp):
#         if 10 <= nueva_temp <= 30:
#             self.temperatura = nueva_temp
#             print(f"Temperatura ajustada a {self.temperatura}°C")
#         else:
#             print("Error: Temperatura fuera de los límites permitidos.")

# clima = Termostato(20)
# clima.cambiar_temperatura(35)
# clima.cambiar_temperatura(25)

# 6. Autenticación de Usuario
# Una clase que verifica si la contraseña ingresada coincide con la registrada.
# class Usuario:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def login(self, input_user, input_pass):
#         if self.username == input_user and self.password == input_pass:
#             print("Acceso concedido.")
#         else:
#             print("Credenciales incorrectas.")

# user = Usuario("admin", "12345")
# user.login("admin", "0000")
# user.login("admin", "12345")

# 7. Sistema de Ascensor
# Un ascensor que se mueve a un piso deseado, validando que el piso exista en el edificio.
# class Ascensor:
#     def __init__(self, piso_maximo):
#         self.piso_actual = 0
#         self.piso_maximo = piso_maximo

#     def ir_a_piso(self, destino):
#         if 0 <= destino <= self.piso_maximo:
#             self.piso_actual = destino
#             print(f"Ascensor llegó al piso {self.piso_actual}")
#         else:
#             print("Piso inexistente.")

# edificio = Ascensor(10)
# edificio.ir_a_piso(5)
# edificio.ir_a_piso(15)

# 8. Mascota Virtual (Tamagotchi)
# Una mascota que come solo si tiene hambre, cambiando su estado emocional.
# class Mascota:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.hambre = True

#     def alimentar(self):
#         if self.hambre:
#             print(f"{self.nombre} está comiendo. ¡Qué rico!")
#             self.hambre = False
#         else:
#             print(f"{self.nombre} no tiene hambre ahora mismo.")

# perro = Mascota("Firulais")
# perro.alimentar()
# perro.alimentar()

# 9. Coche y Velocidad Límite
# Un coche que acelera pero impide sobrepasar el límite de velocidad del motor (120 km/h).

# Python
# class Coche:
#     def __init__(self, marca):
#         self.marca = marca
#         self.velocidad = 0

#     def acelerar(self, incremento):
#         if self.velocidad + incremento <= 120:
#             self.velocidad += incremento
#             print(f"Acelerando. Velocidad actual: {self.velocidad} km/h")
#         else:
#             print("No puedes superar los 120 km/h.")

# auto = Coche("Toyota")
# auto.acelerar(100)
# auto.acelerar(30)

# 10. Biblioteca Simple
# Un libro que marca su disponibilidad con un booleano y permite prestarlo si está en la biblioteca.

# Python
# class Libro:
#     def __init__(self, titulo):
#         self.titulo = titulo
#         self.disponible = True

#     def prestar(self):
#         if self.disponible:
#             self.disponible = False
#             print(f"Te has llevado el libro: {self.titulo}")
#         else:
#             print(f"El libro '{self.titulo}' ya está prestado.")

# libro1 = Libro("El Principito")
# libro1.prestar()
# libro1.prestar()