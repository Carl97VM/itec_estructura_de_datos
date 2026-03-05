from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Venta:
    id: int
    producto: str
    cantidad: int
    precio_unitario: float

    # Metodo para calcular el total
    def total(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"ID: {self.id}, Producto: {self.producto}, Cantidad: {self.cantidad}, Precio Unitario: {self.precio_unitario}, Total: {self.total()}"

    def __repr__(self):
        return f"Venta({self.id}, {self.producto}, {self.cantidad}, {self.precio_unitario})"  

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
        precio_unitario: Optional[float] = None):
        for venta in self.pila:
            if venta.id == id:
                if producto:
                    venta.producto = producto
                if cantidad:
                    venta.cantidad = cantidad
                if precio_unitario:
                    venta.precio_unitario = precio_unitario
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



# Jayvan - Crear
# Johan Actualizar
# Jose Eliminar
# Teresa y Tania - Buscar
# Marvin - nada