# #region Cola_Pro_Python
from collections import deque

class ColaBanco:
    def __init__(self):
        # deque está optimizada para agregar/sacar en ambos extremos en O(1)
        self.clientes = deque()

    def llegar(self, nombre):
        print(f"-> Cliente {nombre} ha llegado a la fila.")
        self.clientes.append(nombre)

    def atender(self):
        if not self.clientes:
            return "No hay clientes en espera."
        # popleft() es la operación clave de la cola
        cliente = self.clientes.popleft()
        print(f"✅ Atendiendo a {cliente}...")
        return cliente

# Simulación
banco = ColaBanco()
banco.llegar("Carlo")
banco.llegar("Juan Carlos")
banco.atender() # Atiende a Carlo
banco.atender() # Atiende a Juan Carlos
# #endregion