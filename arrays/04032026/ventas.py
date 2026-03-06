from dataclasses import dataclass
from typing import List, Optional
from time import asctime, localtime, strftime
from datetime import datetime

@dataclass
class Venta:
    id: int
    producto: str
    cantidad: int
    precio_unitario: float
    fecha_registro: str
    fecha_actualizacion: Optional[str]

    # Metodo para calcular el total
    def total(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"ID: {self.id}, Producto: {self.producto}, Cantidad: {self.cantidad}, Precio Unitario: {self.precio_unitario}, Total: {self.total()}, Fecha de Registro: {self.fecha_registro}, Fecha de Actualizacion: {self.fecha_actualizacion}"

    def __repr__(self):
        return f"Venta({self.id}, {self.producto}, {self.cantidad}, {self.precio_unitario}, {self.fecha_registro}, {self.fecha_actualizacion})"  

class RegistrarVentas:
    def __init__(self):
        self.pila: List[Venta] = []

    # C.R.U.D
    # Create, Read, Update, Delete
    # Crear, Leer, Actualizar, Eliminar

    # Crear
    def agregar_venta(self, venta):
        self.pila.append(venta)
        print(f"Venta Agregada exitosamente: {venta}")

    # Leer
    def listar_ventas(self):
        if not self.pila:
            print("No hay ventas registradas")
        else:
            print("\nLista de ventas:")
            for venta in self.pila:
                print(venta)

    # Actualizar
    def actualizar_venta(self, 
        id: int, 
        producto: Optional[str] = None,
        cantidad: Optional[int] = None,
        precio_unitario: Optional[float] = None,
        fecha_actualizacion: Optional[str] = None):
        for venta in self.pila:
            if venta.id == id:
                if producto:
                    venta.producto = producto
                if cantidad:
                    venta.cantidad = cantidad
                if precio_unitario:
                    venta.precio_unitario = precio_unitario
                if fecha_actualizacion:
                    modificar_fecha = localtime()
                    fecha_actualizacion = strftime("%Y-%m-%d %H:%M", modificar_fecha)
                    venta.fecha_actualizacion = fecha_actualizacion
                print(f"Venta {id} actualizada exitosamente")
                return
        print(f"Venta no encontrada")

    # Eliminar
    def eliminar_venta(self, id: int):
        for venta in self.pila:
            if venta.id == id:
                self.pila.remove(venta)
                print(f"Venta {id} eliminada exitosamente")
                return
        print(f"Venta no encontrada")

    def eliminar_ultima_venta(self):
        if self.pila:
            venta = self.pila.pop()
            print(f"Venta eliminada: {venta}")
        else:
            print("No hay ventas para eliminar.")



# Jayvan - Crear
# Johan Actualizar
# Jose Eliminar
# Teresa y Tania - Buscar
# Marvin - nada

if __name__ == "__main__":
    registro = RegistrarVentas()

    # Crear ventas
    ahora = localtime()
    fecha_guardar = strftime("%Y-%m-%d %H:%M", ahora)
    registro.agregar_venta(Venta(1, "Pilas AA", 10, 2.5, fecha_guardar, None))
    registro.agregar_venta(Venta(2, "Pilas AAA", 5, 3.0, fecha_guardar, None))

    # Leer ventas
    registro.listar_ventas()

    # Actualizar venta
    modificar = localtime()
    fecha_actualizacion = strftime("%Y-%m-%d %H:%M", modificar)
    registro.actualizar_venta(
        1, 
        cantidad=15, 
        fecha_actualizacion=fecha_actualizacion
    )

    # Eliminar última venta
    registro.eliminar_ultima_venta()

    # Eliminar por ID
    registro.eliminar_venta(1)

    # Listar nuevamente
    registro.listar_ventas()