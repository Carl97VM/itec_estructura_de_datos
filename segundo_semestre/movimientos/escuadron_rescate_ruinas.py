import tkinter as tk
from tkinter import ttk

# ==============================================================================
# PROYECTO NÚCLEO: "EL ESCUADRÓN DE RESCATE EN LA CIUDAD EN RUINAS"
# ==============================================================================
# Reglas base:
#   - Matriz N x N (6 x 6).
#   - Inicio en (0, 0) y extracción (meta) en (N-1, N-1).
#   - 4 direcciones (Arriba, Abajo, Izquierda, Derecha) con Backtracking.
#   - Interfaz Gráfica (Tkinter) con animación paso a paso + modo consola.
# ==============================================================================

DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ESCENARIOS = {
    "1": {
        "titulo": "1. La Ruta Segura y los Sobrevivientes",
        "descripcion": (
            "Rescata la mayor cantidad de sobrevivientes (100) sin superar "
            "el límite de 20 de radiación acumulada."
        ),
        "matriz": [
            [  1, 100,   3,   4, 100,   2],
            [  2,   5, 100,   2,   3,   4],
            [100,   1,   2, 100,   5,   1],
            [  4,   3, 100,   1,   2, 100],
            [  5, 100,   4,   3, 100,   2],
            [  2,   1,   3, 100,   1,   1],
        ],
        "limite_radiacion": 20,
    },
    "2": {
        "titulo": "2. El Dron de Reconocimiento y los Checkpoints",
        "descripcion": (
            "Llega a la meta (5,5) pasando obligatoriamente por los 3 "
            "Checkpoints sin chocar con muros (1)."
        ),
        "matriz": [
            [0, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        "checkpoints": [(1, 4), (3, 1), (5, 2)],
    },
    "3": {
        "titulo": "3. Las Puertas con Llave",
        "descripcion": (
            "Recoge llaves (-2) para abrir puertas cerradas (-3). Cada llave "
            "abre una puerta; sin llaves no puedes cruzar (-3)."
        ),
        "matriz": [
            [ 0,  0, -3,  0, -2,  0],
            [ 0, -3, -3,  0, -3,  0],
            [-2,  0,  0,  0,  0, -3],
            [ 0, -3, -3, -3,  0,  0],
            [ 0,  0, -2, -3, -3, -3],
            [ 0,  0,  0,  0, -3,  0],
        ],
    },
}


# ==============================================================================
# ALGORITMOS CON REGISTRO DE EVENTOS PARA ANIMACIÓN
# ==============================================================================

def _dfs_sobrevivientes(
    matriz, n, fila, col, radiacion_actual, sobrevivientes_actuales,
    camino, visitados, mejor_estado, eventos, limite_radiacion=20
):
    valor = matriz[fila][col]
    if valor == 100:
        sobrevivientes_actuales += 1
    else:
        radiacion_actual += valor

    if radiacion_actual > limite_radiacion:
        eventos.append((
            "poda", list(camino) + [(fila, col)],
            f"Radiación excedida ({radiacion_actual}/{limite_radiacion})"
        ))
        return

    camino.append((fila, col))
    visitados.append((fila, col))
    eventos.append((
        "avanzar", list(camino),
        f"Sobrevivientes: {sobrevivientes_actuales} | Radiación: {radiacion_actual}/{limite_radiacion}"
    ))

    if fila == n - 1 and col == n - 1:
        mejor_sobr, mejor_rad, _ = mejor_estado
        if (sobrevivientes_actuales > mejor_sobr) or (
            sobrevivientes_actuales == mejor_sobr and radiacion_actual < mejor_rad
        ):
            mejor_estado[0] = sobrevivientes_actuales
            mejor_estado[1] = radiacion_actual
            mejor_estado[2] = list(camino)
            eventos.append((
                "encontrado", list(camino),
                f"¡Nuevo récord! {sobrevivientes_actuales} sobrevivientes (Rad: {radiacion_actual}/{limite_radiacion})"
            ))
        camino.pop()
        visitados.pop()
        return

    for df, dc in DIRECCIONES:
        nf, nc = fila + df, col + dc
        if 0 <= nf < n and 0 <= nc < n and (nf, nc) not in visitados:
            _dfs_sobrevivientes(
                matriz, n, nf, nc, radiacion_actual, sobrevivientes_actuales,
                camino, visitados, mejor_estado, eventos, limite_radiacion
            )

    eventos.append((
        "retroceder", list(camino),
        f"Backtracking desde ({fila}, {col})"
    ))
    camino.pop()
    visitados.pop()


def _dfs_checkpoints(
    matriz, n, fila, col, checkpoints, checkpoints_visitados,
    camino, visitados, eventos
):
    nuevo_cp = list(checkpoints_visitados)
    if (fila, col) in checkpoints and (fila, col) not in nuevo_cp:
        nuevo_cp.append((fila, col))

    camino.append((fila, col))
    visitados.append((fila, col))
    eventos.append((
        "avanzar", list(camino),
        f"Checkpoints visitados: {len(nuevo_cp)}/{len(checkpoints)}"
    ))

    if fila == n - 1 and col == n - 1:
        if len(nuevo_cp) == len(checkpoints):
            eventos.append((
                "encontrado", list(camino),
                f"¡Meta alcanzada con los {len(checkpoints)} Checkpoints!"
            ))
            return True
        eventos.append((
            "poda", list(camino),
            f"Meta rechazada: faltan checkpoints ({len(nuevo_cp)}/{len(checkpoints)})"
        ))
        camino.pop()
        visitados.pop()
        return False

    for df, dc in DIRECCIONES:
        nf, nc = fila + df, col + dc
        if 0 <= nf < n and 0 <= nc < n:
            if matriz[nf][nc] != 1 and (nf, nc) not in visitados:
                if _dfs_checkpoints(
                    matriz, n, nf, nc, checkpoints, nuevo_cp, camino, visitados, eventos
                ):
                    return True

    eventos.append(("retroceder", list(camino), f"Backtracking desde ({fila}, {col})"))
    camino.pop()
    visitados.pop()
    return False


def _dfs_llaves_puertas(
    matriz, n, fila, col, inventario_llaves, camino, visitados, eventos
):
    celda = matriz[fila][col]
    if celda == -2:
        inventario_llaves += 1
    elif celda == -3:
        inventario_llaves -= 1

    camino.append((fila, col))
    visitados.append((fila, col))
    eventos.append((
        "avanzar", list(camino),
        f"Llaves en inventario: {inventario_llaves}"
    ))

    if fila == n - 1 and col == n - 1:
        eventos.append((
            "encontrado", list(camino),
            f"¡Extracción lograda! Llaves restantes: {inventario_llaves}"
        ))
        return True

    for df, dc in DIRECCIONES:
        nf, nc = fila + df, col + dc
        if 0 <= nf < n and 0 <= nc < n and (nf, nc) not in visitados:
            if matriz[nf][nc] == -3 and inventario_llaves == 0:
                continue
            if _dfs_llaves_puertas(
                matriz, n, nf, nc, inventario_llaves, camino, visitados, eventos
            ):
                return True

    eventos.append(("retroceder", list(camino), f"Backtracking desde ({fila}, {col})"))
    camino.pop()
    visitados.pop()
    return False


def resolver_escenario(clave_escenario):
    """Ejecuta el algoritmo del escenario seleccionado y devuelve (camino, eventos, resumen)."""
    datos = ESCENARIOS[clave_escenario]
    matriz = datos["matriz"]
    n = len(matriz)
    eventos = []

    if clave_escenario == "1":
        limite = datos["limite_radiacion"]
        mejor_estado = [-1, float("inf"), None]
        _dfs_sobrevivientes(matriz, n, 0, 0, 0, 0, [], [], mejor_estado, eventos, limite)
        sobr, rad, camino = mejor_estado
        resumen = (
            f"Sobrevivientes rescatados: {sobr}\n"
            f"Radiación acumulada: {rad} / {limite}\n"
            f"Pasos totales: {len(camino)}"
            if camino else "No se encontró ruta válida."
        )
        return camino, eventos, resumen

    if clave_escenario == "2":
        checkpoints = datos["checkpoints"]
        camino = []
        exito = _dfs_checkpoints(matriz, n, 0, 0, checkpoints, [], camino, [], eventos)
        camino_final = camino if exito else None
        resumen = (
            f"Checkpoints visitados: {len(checkpoints)} / {len(checkpoints)}\n"
            f"Pasos totales: {len(camino_final)}"
            if camino_final else "No se encontró ruta con los 3 checkpoints."
        )
        return camino_final, eventos, resumen

    camino = []
    exito = _dfs_llaves_puertas(matriz, n, 0, 0, 0, camino, [], eventos)
    camino_final = camino if exito else None
    if camino_final:
        llaves = sum(1 for f, c in camino_final if matriz[f][c] == -2)
        puertas = sum(1 for f, c in camino_final if matriz[f][c] == -3)
        resumen = (
            f"Llaves recogidas: {llaves}\n"
            f"Puertas abiertas: {puertas}\n"
            f"Pasos totales: {len(camino_final)}"
        )
    else:
        resumen = "No se encontró ruta con llaves suficientes."
    return camino_final, eventos, resumen


# ==============================================================================
# INTERFAZ GRÁFICA MODERNA (TKINTER)
# ==============================================================================

class VentanaEscuadronRescate:
    def __init__(self, root):
        self.root = root
        self.root.title("El Escuadrón de Rescate en la Ciudad en Ruinas")
        self.root.geometry("980x680")
        self.root.configure(bg="#1e1e2e")

        self.escenario_actual = "1"
        self.animando = False
        self.after_id = None

        self._construir_ui()
        self._cargar_escenario("1")

    def _construir_ui(self):
        # Encabezado
        header = tk.Frame(self.root, bg="#181825", pady=12)
        header.pack(fill=tk.X)
        tk.Label(
            header,
            text="EL ESCUADRÓN DE RESCATE EN LA CIUDAD EN RUINAS",
            font=("Segoe UI", 16, "bold"),
            fg="#cdd6f4",
            bg="#181825",
        ).pack()
        tk.Label(
            header,
            text="Inicio: (0, 0)  ➔  Extracción: (5, 5)  |  Backtracking Visual",
            font=("Segoe UI", 10),
            fg="#a6adc8",
            bg="#181825",
        ).pack()

        # Selector superior de los 3 escenarios
        barra_escenarios = tk.Frame(self.root, bg="#1e1e2e", pady=8, padx=15)
        barra_escenarios.pack(fill=tk.X)

        self.botones_escenario = {}
        for clave, info in ESCENARIOS.items():
            btn = tk.Button(
                barra_escenarios,
                text=info["titulo"],
                command=lambda c=clave: self._cargar_escenario(c),
                font=("Segoe UI", 10, "bold"),
                relief=tk.FLAT,
                pady=7,
                padx=10,
                cursor="hand2",
            )
            btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=4)
            self.botones_escenario[clave] = btn

        # Cuerpo principal
        cuerpo = tk.Frame(self.root, bg="#1e1e2e", padx=15, pady=8)
        cuerpo.pack(fill=tk.BOTH, expand=True)

        self.frame_tablero = tk.Frame(cuerpo, bg="#1e1e2e")
        self.frame_tablero.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

        panel = tk.Frame(cuerpo, bg="#313244", padx=16, pady=16, width=330)
        panel.pack(side=tk.RIGHT, fill=tk.Y)
        panel.pack_propagate(False)

        self.lbl_titulo_esc = tk.Label(
            panel, text="", bg="#313244", fg="#89b4fa",
            font=("Segoe UI", 11, "bold"), wraplength=295, justify="left"
        )
        self.lbl_titulo_esc.pack(anchor="w")

        self.lbl_desc_esc = tk.Label(
            panel, text="", bg="#313244", fg="#bac2de",
            font=("Segoe UI", 9), wraplength=295, justify="left"
        )
        self.lbl_desc_esc.pack(anchor="w", pady=(4, 12))

        tk.Label(
            panel, text="Velocidad de animación (ms):",
            bg="#313244", fg="#cdd6f4", font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")
        self.scale_velocidad = tk.Scale(
            panel, from_=5, to=300, orient=tk.HORIZONTAL,
            bg="#313244", fg="#cdd6f4", highlightthickness=0, troughcolor="#45475a"
        )
        self.scale_velocidad.set(45)
        self.scale_velocidad.pack(fill=tk.X, pady=(2, 12))

        tk.Button(
            panel, text="▶ Animar Búsqueda",
            command=lambda: self._iniciar_busqueda(animar=True),
            bg="#a6e3a1", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=7, cursor="hand2"
        ).pack(fill=tk.X, pady=4)

        tk.Button(
            panel, text="⚡ Ver Resultado Directo",
            command=lambda: self._iniciar_busqueda(animar=False),
            bg="#89b4fa", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=7, cursor="hand2"
        ).pack(fill=tk.X, pady=4)

        tk.Button(
            panel, text="⏹ Reiniciar Tablero",
            command=self._reiniciar_tablero,
            bg="#f38ba8", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=6, cursor="hand2"
        ).pack(fill=tk.X, pady=4)

        tk.Frame(panel, bg="#45475a", height=2).pack(fill=tk.X, pady=12)

        self.lbl_estado = tk.Label(
            panel,
            text="Selecciona un escenario y presiona Iniciar.",
            bg="#313244", fg="#f9e2af", font=("Segoe UI", 10),
            wraplength=295, justify="left"
        )
        self.lbl_estado.pack(anchor="w", pady=4)

        self.lbl_leyenda = tk.Label(
            panel, text="", bg="#313244", fg="#bac2de",
            font=("Segoe UI", 9), justify="left", wraplength=295
        )
        self.lbl_leyenda.pack(anchor="w", side=tk.BOTTOM)

    def _cargar_escenario(self, clave):
        self._detener_animacion()
        self.escenario_actual = clave

        for c, btn in self.botones_escenario.items():
            if c == clave:
                btn.config(bg="#89b4fa", fg="#11111b")
            else:
                btn.config(bg="#313244", fg="#cdd6f4")

        info = ESCENARIOS[clave]
        self.lbl_titulo_esc.config(text=info["titulo"])
        self.lbl_desc_esc.config(text=info["descripcion"])

        leyendas = {
            "1": "Leyenda:\n• Azul: Sobreviviente (100)\n• Amarillo: Explorando\n• Rojo: Poda / Retroceso\n• Verde: Mejor ruta de rescate",
            "2": "Leyenda:\n• Morado: Checkpoint obligatorio\n• Gris oscuro: Muro (1)\n• Amarillo: Explorando\n• Verde: Ruta válida con 3 Checkpoints",
            "3": "Leyenda:\n• Dorado: Llave (-2)\n• Naranja: Puerta cerrada (-3)\n• Amarillo: Explorando\n• Verde: Ruta de extracción",
        }
        self.lbl_leyenda.config(text=leyendas[clave])
        self._dibujar_tablero()
        self.lbl_estado.config(text="Tablero listo. Pulsa '▶ Animar Búsqueda' o '⚡ Ver Resultado Directo'.")

    def _estilo_celda_base(self, i, j):
        datos = ESCENARIOS[self.escenario_actual]
        matriz = datos["matriz"]
        n = len(matriz)
        val = matriz[i][j]

        etiqueta_pos = ""
        if (i, j) == (0, 0):
            etiqueta_pos = "\n[INICIO]"
        elif (i, j) == (n - 1, n - 1):
            etiqueta_pos = "\n[META]"

        if self.escenario_actual == "1":
            if val == 100:
                return "#1e3a5f", "#89dceb", f"🧑 100{etiqueta_pos}"
            return "#313244", "#cdd6f4", f"Rad {val}{etiqueta_pos}"

        if self.escenario_actual == "2":
            if (i, j) in datos["checkpoints"]:
                return "#583780", "#f5c2e7", f"★ CP{etiqueta_pos}"
            if val == 1:
                return "#181825", "#6c7086", "█ MURO"
            return "#313244", "#cdd6f4", f"0{etiqueta_pos}"

        # Escenario 3
        if val == -2:
            return "#5c4d1f", "#f9e2af", f"🔑 Llave{etiqueta_pos}"
        if val == -3:
            return "#5c2b29", "#fab387", f"🚪 Puerta{etiqueta_pos}"
        return "#313244", "#cdd6f4", f"Libre{etiqueta_pos}"

    def _dibujar_tablero(self):
        for w in self.frame_tablero.winfo_children():
            w.destroy()

        matriz = ESCENARIOS[self.escenario_actual]["matriz"]
        n = len(matriz)
        self.celdas_ui = [[None for _ in range(n)] for _ in range(n)]

        for i in range(n):
            self.frame_tablero.rowconfigure(i, weight=1)
            for j in range(n):
                self.frame_tablero.columnconfigure(j, weight=1)
                bg, fg, texto = self._estilo_celda_base(i, j)
                lbl = tk.Label(
                    self.frame_tablero,
                    text=texto,
                    font=("Segoe UI", 11, "bold"),
                    bg=bg,
                    fg=fg,
                    relief=tk.RAISED,
                    bd=2,
                )
                lbl.grid(row=i, column=j, sticky="nsew", padx=4, pady=4)
                self.celdas_ui[i][j] = lbl

    def _detener_animacion(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.animando = False

    def _reiniciar_tablero(self):
        self._detener_animacion()
        matriz = ESCENARIOS[self.escenario_actual]["matriz"]
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                bg, fg, texto = self._estilo_celda_base(i, j)
                self.celdas_ui[i][j].config(text=texto, bg=bg, fg=fg)
        self.lbl_estado.config(text="Tablero reiniciado.")

    def _iniciar_busqueda(self, animar=True):
        self._reiniciar_tablero()
        camino_final, eventos, resumen = resolver_escenario(self.escenario_actual)

        if not animar:
            self._mostrar_final(camino_final, resumen)
            return

        # Muestrear si hay demasiados eventos para mantener fluida la animación
        if len(eventos) > 220:
            paso = len(eventos) // 160
            eventos_filtrados = [
                ev for idx, ev in enumerate(eventos)
                if idx % paso == 0 or ev[0] == "encontrado"
            ]
        else:
            eventos_filtrados = eventos

        self.animando = True
        self._reproducir_evento(eventos_filtrados, 0, camino_final, resumen)

    def _reproducir_evento(self, eventos, idx, camino_final, resumen):
        if not self.animando:
            return
        if idx >= len(eventos):
            self._mostrar_final(camino_final, resumen)
            self.animando = False
            return

        tipo, camino, detalle = eventos[idx]
        n = len(ESCENARIOS[self.escenario_actual]["matriz"])

        for i in range(n):
            for j in range(n):
                bg, fg, texto = self._estilo_celda_base(i, j)
                self.celdas_ui[i][j].config(text=texto, bg=bg, fg=fg)

        for paso_idx, (f, c) in enumerate(camino):
            _, _, texto_base = self._estilo_celda_base(f, c)
            primera_linea = texto_base.split("\n")[0]
            if tipo == "encontrado":
                bg = "#a6e3a1"
            elif tipo in ("poda", "retroceder") and paso_idx == len(camino) - 1:
                bg = "#f38ba8"
            else:
                bg = "#f9e2af"
            self.celdas_ui[f][c].config(
                text=f"{primera_linea}\n[#{paso_idx + 1}]",
                bg=bg,
                fg="#11111b",
            )

        self.lbl_estado.config(
            text=f"Paso {idx + 1}/{len(eventos)} ({tipo.upper()})\n{detalle}\nLongitud actual: {len(camino)}"
        )

        pausa = self.scale_velocidad.get()
        if tipo == "encontrado":
            pausa = max(pausa * 4, 400)

        self.after_id = self.root.after(
            pausa, lambda: self._reproducir_evento(eventos, idx + 1, camino_final, resumen)
        )

    def _mostrar_final(self, camino_final, resumen):
        n = len(ESCENARIOS[self.escenario_actual]["matriz"])
        for i in range(n):
            for j in range(n):
                bg, fg, texto = self._estilo_celda_base(i, j)
                self.celdas_ui[i][j].config(text=texto, bg=bg, fg=fg)

        if camino_final:
            for idx, (f, c) in enumerate(camino_final):
                _, _, texto_base = self._estilo_celda_base(f, c)
                primera_linea = texto_base.split("\n")[0]
                self.celdas_ui[f][c].config(
                    text=f"{primera_linea}\n★ Paso {idx + 1}",
                    bg="#a6e3a1",
                    fg="#11111b",
                )
            self.lbl_estado.config(text=f"¡MISIÓN COMPLETADA!\n\n{resumen}")
        else:
            self.lbl_estado.config(text=f"SIN SOLUCIÓN\n\n{resumen}")


# ==============================================================================
# PUNTO DE ENTRADA (INTERFAZ GRÁFICA POR DEFECTO)
# ==============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaEscuadronRescate(root)
    root.mainloop()
