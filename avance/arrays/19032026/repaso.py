## Clase de Listas: https://docs.python.org/es/3/tutorial/datastructures.html

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# fruits.reverse() ## invierte el orden de la lista
# fruits.append('mango')
# print(fruits)

# for i in fruits:
#     print(i)
# fruits.sort() ## ordena la lista alfabeticamente
# print(fruits)
# fruits.sort(reverse=True) ## ordena la lista alfabeticamente de forma descendente
# print(fruits)


# fruits.pop() ## elimina el ultimo elemento de la lista
# print(fruits)
# fruits.pop(0) ## elimina el elemento en la posicion 2
# print(fruits)
# fruits.remove('apple') ## elimina la primera ocurrencia del elemento
# print(fruits)
# fruits.remove('apple') ## elimina la primera ocurrencia del elemento


# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# print(queue)
# queue.append("Terry")           # Terry arrives
# queue.append("Graham") 
# queue.popleft() ## elimina el primer elemento de la lista
# print(queue)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(matrix)
# matrix = [[row[i] for row in matrix] for i in range(4)]
# print(matrix)

## Repaso de clases y objetos Pilas
# class Estudiante:
#     def __init__(self, nombre, edad, celular, fecha_nacimiento, apellido_paterno, apellido_materno):
#         self.nombre = nombre
#         self.edad = edad
#         self.celular = celular
#         self.fecha_nacimiento = fecha_nacimiento
#         self.apellido_paterno = apellido_paterno
#         self.apellido_materno = apellido_materno

#     def __str__(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Celular: {self.celular}, Fecha de Nacimiento: {self.fecha_nacimiento}, Apellido Paterno: {self.apellido_paterno}, Apellido Materno: {self.apellido_materno}"
    
#     def __mostrar__(self):
#         print(self)

# estudiante = Estudiante("Juan", 20, "123456789", "1990-01-01", "Paterno", "Materno")
# estudiante2 = Estudiante("Carlos", 20, "123456789", "1990-01-01", "Paterno", "Materno")
# estudiante3 = Estudiante("Maria", 20, "123456789", "1990-01-01", "Paterno", "Materno")
# estudiante4 = Estudiante("Ana", 20, "123456789", "1990-01-01", "Paterno", "Materno")
# estudiante5 = Estudiante("Pedro", 20, "123456789", "1990-01-01", "Paterno", "Materno")   
# # print(estudiante)
# # print(estudiante2)
# # print(estudiante3)
# # print(estudiante4)
# # print(estudiante5)

# lista_estudiantes = [estudiante, estudiante2, estudiante3, estudiante4, estudiante5]
# for i in lista_estudiantes:
#     i.__mostrar__()
