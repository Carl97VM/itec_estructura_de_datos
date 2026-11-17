import os
import time
import tkinter as tk
from tkinter import ttk, messagebox


# ==============================================================================
# LÓGICA DE BÚSQUEDA AVANZADA (PORTALES 99 Y FACTOR ESTAMINA)
# ==============================================================================

VALOR_PORTAL = 99
ESTAMINA_INICIAL = 10

MODOS_DE_BUSQUEDA = {
    "libre4": "Solo 4 direcciones (arriba, abajo, izquierda, derecha)",
    "libre8": "8 direcciones (incluye diagonales)",
    "vertical": "Solo vertical (arriba y abajo)",
    "cruzado_x": "Cruzado en X (diagonales)",
    "zigzag": "Movimiento en zigzag (alternando horizontal y vertical)",
    "lineal": "Solo horizontal (izquierda y derecha)",
}


def obtener_direcciones(modo_busqueda):
    rectas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonales = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    if modo_busqueda == "libre4":
        return rectas
    if modo_busqueda in ("libre8", "lineal"):
        return rectas + diagonales
    if modo_busqueda == "vertical":
        return [(1, 0)]
    if modo_busqueda == "cruzado_x":
        return diagonales
    if modo_busqueda == "zigzag":
        return [(1, -1), (1, 1)]
    return rectas


def es_movimiento_permitido(movimiento, direccion_anterior, modo_busqueda):
    if direccion_anterior is None or direccion_anterior == "portal":
        return True
    if modo_busqueda == "zigzag":
        return movimiento[1] != direccion_anterior[1]
    if modo_busqueda == "lineal":
        return movimiento == direccion_anterior
    return True


def costo_estamina_movimiento(movimiento):
    """
    Modificación B (Estamina):
      - Movimientos en cruz (arriba, abajo, izq, der): consumen 1 punto.
      - Movimientos en diagonal (cruzado_x / diagonales): consumen 2 puntos.
      - Salto por portal: consume 1 punto (cuenta como 1 movimiento).
    """
    if movimiento == "portal":
        return 1
    df, dc = movimiento
    if df != 0 and dc != 0:
        return 2
    return 1


def encontrar_otro_portal(matriz, fila, col):
    """Devuelve la coordenada (f, c) del otro portal 99 en la matriz."""
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == VALOR_PORTAL and (i, j) != (fila, col):
                return (i, j)
    return None


def esta_en_lista(coordenada, lista):
    for f, c in lista:
        if f == coordenada[0] and c == coordenada[1]:
            return True
    return False


def movimientos_validos(fila, col, n, modo_busqueda, direccion_anterior, visitados, matriz=None):
    """
    Modificación A (Portales):
      Si la celda actual es un portal (99), el único movimiento válido siguiente
      es aparecer inmediatamente en la coordenada del otro 99 (si no fue visitado).
    """
    if matriz is not None and matriz[fila][col] == VALOR_PORTAL:
        destino_portal = encontrar_otro_portal(matriz, fila, col)
        if destino_portal is not None and not esta_en_lista(destino_portal, visitados):
            return [(destino_portal[0], destino_portal[1], "portal")]
        return []

    validos = []
    for mov in obtener_direcciones(modo_busqueda):
        if not es_movimiento_permitido(mov, direccion_anterior, modo_busqueda):
            continue
        nueva_fila, nueva_columna = fila + mov[0], col + mov[1]
        if 0 <= nueva_fila < n and 0 <= nueva_columna < n:
            if not esta_en_lista((nueva_fila, nueva_columna), visitados):
                validos.append((nueva_fila, nueva_columna, mov))
    return validos


def valor_real_celda(valor):
    """El valor 99 de un portal no debe sumarse a la suma total."""
    return 0 if valor == VALOR_PORTAL else valor


def buscar_caminos_recursivo(
    matriz,
    n,
    fila,
    col,
    objetivo,
    suma_actual,
    estamina_actual,
    camino,
    visitados,
    modo_busqueda,
    movimientos_requeridos,
    mejor_camino,
    historial_eventos=None,
    modo_movimientos="exacto",
    direccion_anterior=None,
):
    valor_celda = valor_real_celda(matriz[fila][col])
    suma_actual += valor_celda
    camino.append((fila, col))
    visitados.append((fila, col))
    pasos_actuales = len(camino)

    if historial_eventos is not None:
        historial_eventos.append(("avanzar", list(camino), suma_actual, estamina_actual))

    # PODA 1: Si nos quedamos sin estamina negativa (movimiento inválido)
    if estamina_actual < 0:
        if historial_eventos is not None:
            historial_eventos.append(("poda_estamina", list(camino), suma_actual, estamina_actual))
        camino.pop()
        visitados.pop()
        return

    # PODA 2: Si nos pasamos de la suma objetivo
    if suma_actual > objetivo:
        if historial_eventos is not None:
            historial_eventos.append(("poda", list(camino), suma_actual, estamina_actual))
        camino.pop()
        visitados.pop()
        return

    # PODA 3: Límite de movimientos
    if movimientos_requeridos > 0 and pasos_actuales > movimientos_requeridos:
        if historial_eventos is not None:
            historial_eventos.append(("poda", list(camino), suma_actual, estamina_actual))
        camino.pop()
        visitados.pop()
        return

    # PODA 4: Ya existe un camino más corto
    busca_mas_corto = (movimientos_requeridos == 0) or (modo_movimientos == "maximo")
    if busca_mas_corto and mejor_camino[0] is not None:
        if pasos_actuales >= len(mejor_camino[0]):
            if historial_eventos is not None:
                historial_eventos.append(("poda", list(camino), suma_actual, estamina_actual))
            camino.pop()
            visitados.pop()
            return

    # CASO DE ÉXITO: La suma coincide con el objetivo
    if suma_actual == objetivo:
        if movimientos_requeridos > 0 and modo_movimientos == "exacto":
            if pasos_actuales == movimientos_requeridos:
                mejor_camino[0] = list(camino)
                if historial_eventos is not None:
                    historial_eventos.append(("encontrado", list(camino), suma_actual, estamina_actual))
                camino.pop()
                visitados.pop()
                return
        else:
            min_pasos = 2 if objetivo == 0 else 1
            if pasos_actuales >= min_pasos:
                if mejor_camino[0] is None or pasos_actuales < len(mejor_camino[0]):
                    mejor_camino[0] = list(camino)
                    if historial_eventos is not None:
                        historial_eventos.append(("encontrado", list(camino), suma_actual, estamina_actual))
                camino.pop()
                visitados.pop()
                return

    # Modificación B: Si la estamina llegó a 0 antes de alcanzar el objetivo, el camino muere
    if estamina_actual <= 0:
        if historial_eventos is not None:
            historial_eventos.append(("sin_estamina", list(camino), suma_actual, estamina_actual))
        camino.pop()
        visitados.pop()
        return

    vecinos = movimientos_validos(
        fila, col, n, modo_busqueda, direccion_anterior, visitados, matriz=matriz
    )

    for nueva_f, nueva_c, mov in vecinos:
        costo_mov = costo_estamina_movimiento(mov)
        nueva_estamina = estamina_actual - costo_mov
        if nueva_estamina < 0:
            continue

        buscar_caminos_recursivo(
            matriz,
            n,
            nueva_f,
            nueva_c,
            objetivo,
            suma_actual,
            nueva_estamina,
            camino,
            visitados,
            modo_busqueda,
            movimientos_requeridos,
            mejor_camino,
            historial_eventos,
            modo_movimientos,
            direccion_anterior=mov,
        )
        if movimientos_requeridos > 0 and modo_movimientos == "exacto" and mejor_camino[0] is not None:
            camino.pop()
            visitados.pop()
            return

    if historial_eventos is not None:
        historial_eventos.append(("retroceder", list(camino), suma_actual, estamina_actual))
    camino.pop()
    visitados.pop()


def resolver_matriz(
    matriz,
    objetivo,
    modo_busqueda="libre4",
    movimientos_requeridos=0,
    modo_movimientos="exacto",
    estamina_inicial=ESTAMINA_INICIAL,
):
    n = len(matriz)
    mejor_camino = [None]
    historial_eventos = []

    for i in range(n):
        for j in range(n):
            if objetivo == 0 and valor_real_celda(matriz[i][j]) != 0:
                continue

            buscar_caminos_recursivo(
                matriz=matriz,
                n=n,
                fila=i,
                col=j,
                objetivo=objetivo,
                suma_actual=0,
                estamina_actual=estamina_inicial,
                camino=[],
                visitados=[],
                modo_busqueda=modo_busqueda,
                movimientos_requeridos=movimientos_requeridos,
                mejor_camino=mejor_camino,
                historial_eventos=historial_eventos,
                modo_movimientos=modo_movimientos,
            )

            if movimientos_requeridos > 0 and modo_movimientos == "exacto" and mejor_camino[0] is not None:
                break
        if movimientos_requeridos > 0 and modo_movimientos == "exacto" and mejor_camino[0] is not None:
            break

    return mejor_camino[0], historial_eventos


# ==============================================================================
# ANIMACIÓN POR CONSOLA
# ==============================================================================

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def animar_en_consola(
    matriz,
    objetivo,
    modo_busqueda="libre4",
    movimientos_requeridos=0,
    modo_movimientos="exacto",
    pausa=0.08,
):
    n = len(matriz)
    mejor_camino, eventos = resolver_matriz(
        matriz, objetivo, modo_busqueda, movimientos_requeridos, modo_movimientos
    )

    paso_salto = max(1, len(eventos) // 80)

    for idx, (tipo, camino_actual, suma_actual, estamina_restante) in enumerate(eventos):
        if idx % paso_salto != 0 and tipo != "encontrado":
            continue

        limpiar_consola()
        print("=" * 64)
        print("   ANIMACIÓN EN CONSOLA - PORTALES (99) Y ESTAMINA (10)")
        print("=" * 64)
        modo_mov = f"Exactamente {movimientos_requeridos}" if movimientos_requeridos > 0 else "Mínimo posible"
        print(f" Objetivo Suma: {objetivo} | Movimientos: {modo_mov}")
        print(f" Modo de Búsqueda: {MODOS_DE_BUSQUEDA.get(modo_busqueda, modo_busqueda)}")
        print(
            f" Estado: {tipo.upper():12s} | Suma: {suma_actual:2d} | "
            f"Estamina restante: {estamina_restante:2d}/{ESTAMINA_INICIAL} | Pasos: {len(camino_actual)}"
        )
        print("-" * 64)

        for i in range(n):
            linea = "   "
            for j in range(n):
                if (i, j) in camino_actual:
                    orden = camino_actual.index((i, j)) + 1
                    etiqueta = "P*" if matriz[i][j] == VALOR_PORTAL else f"{matriz[i][j]:2d}"
                    linea += f"[{etiqueta}#{orden}] "
                else:
                    etiqueta = "99(P)" if matriz[i][j] == VALOR_PORTAL else f" {matriz[i][j]:2d}  "
                    linea += f" {etiqueta} "
            print(linea)
        print("=" * 64)
        time.sleep(pausa if tipo != "encontrado" else pausa * 4)

    print("\n" + "=" * 64)
    if mejor_camino:
        coste_total = sum(valor_real_celda(matriz[f][c]) for f, c in mejor_camino)
        print(" ¡RESULTADO FINAL ÓPTIMO ENCONTRADO!")
        print(f" -> Cantidad de movimientos (celdas): {len(mejor_camino)}")
        print(f" -> Suma total (portales 99 valen 0): {coste_total}")
        print("\n Secuencia paso a paso:")
        for idx, (f, c) in enumerate(mejor_camino):
            val = matriz[f][c]
            if val == VALOR_PORTAL:
                etiqueta = " (PORTAL 99 -> Suma +0)"
            elif val == 0:
                etiqueta = " (COSTE 0)"
            else:
                etiqueta = ""
            print(f"   Movimiento {idx + 1}: ({f}, {c}) -> Valor: {val}{etiqueta}")
    else:
        print(f" [!] No se encontró ningún camino con suma {objetivo} dentro del límite de estamina.")
    print("=" * 64)


# ==============================================================================
# VENTANA EMERGENTE INTERACTIVA CON ANIMACIÓN (TKINTER)
# ==============================================================================

class VentanaMatrizPortalesEstamina:
    def __init__(self, root, matriz_inicial):
        self.root = root
        self.root.title("Búsqueda Avanzada - Portales (99) y Estamina (10)")
        self.root.geometry("900x650")
        self.root.configure(bg="#1e1e2e")

        self.matriz = [fila[:] for fila in matriz_inicial]
        self.n = len(self.matriz)
        self.animando = False
        self.after_id = None

        self._construir_interfaz()
        self._dibujar_tablero()

    def _construir_interfaz(self):
        header = tk.Frame(self.root, bg="#181825", pady=10)
        header.pack(fill=tk.X)
        tk.Label(
            header,
            text="Búsqueda en Matriz: Portales (99) + Estamina (10 pts)",
            font=("Segoe UI", 15, "bold"),
            fg="#cdd6f4",
            bg="#181825",
        ).pack()

        main_frame = tk.Frame(self.root, bg="#1e1e2e", padx=15, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.frame_tablero = tk.Frame(main_frame, bg="#1e1e2e")
        self.frame_tablero.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

        panel_ctrl = tk.Frame(main_frame, bg="#313244", padx=15, pady=15, width=320)
        panel_ctrl.pack(side=tk.RIGHT, fill=tk.Y)
        panel_ctrl.pack_propagate(False)

        estilo_lbl = {"bg": "#313244", "fg": "#cdd6f4", "font": ("Segoe UI", 10, "bold")}

        tk.Label(panel_ctrl, text="Suma Objetivo:", **estilo_lbl).pack(anchor="w")
        self.var_objetivo = tk.IntVar(value=10)
        tk.Spinbox(
            panel_ctrl, from_=0, to=100, textvariable=self.var_objetivo,
            font=("Segoe UI", 11), width=10
        ).pack(anchor="w", pady=(2, 10))

        tk.Label(panel_ctrl, text="¿En cuántos movimientos? (0 = Más corto):", **estilo_lbl).pack(anchor="w")
        self.var_movimientos = tk.IntVar(value=0)
        tk.Spinbox(
            panel_ctrl, from_=0, to=25, textvariable=self.var_movimientos,
            font=("Segoe UI", 11), width=10
        ).pack(anchor="w", pady=(2, 8))

        tk.Label(panel_ctrl, text="Modo de Búsqueda:", **estilo_lbl).pack(anchor="w")
        self.var_modo_busqueda = tk.StringVar(value=MODOS_DE_BUSQUEDA["libre8"])
        ttk.Combobox(
            panel_ctrl,
            textvariable=self.var_modo_busqueda,
            values=list(MODOS_DE_BUSQUEDA.values()),
            state="readonly",
            font=("Segoe UI", 9),
        ).pack(fill=tk.X, pady=(2, 8))

        self.var_modo_mov = tk.StringVar(value="exacto")
        frame_modo = tk.Frame(panel_ctrl, bg="#313244")
        frame_modo.pack(anchor="w", pady=(0, 8))
        tk.Radiobutton(
            frame_modo, text="Exactos", variable=self.var_modo_mov, value="exacto",
            bg="#313244", fg="#cdd6f4", selectcolor="#45475a", font=("Segoe UI", 9)
        ).pack(side=tk.LEFT, padx=(0, 8))
        tk.Radiobutton(
            frame_modo, text="Máximo", variable=self.var_modo_mov, value="maximo",
            bg="#313244", fg="#cdd6f4", selectcolor="#45475a", font=("Segoe UI", 9)
        ).pack(side=tk.LEFT)

        tk.Label(panel_ctrl, text="Velocidad de Animación (ms):", **estilo_lbl).pack(anchor="w")
        self.scale_velocidad = tk.Scale(
            panel_ctrl, from_=10, to=400, orient=tk.HORIZONTAL,
            bg="#313244", fg="#cdd6f4", highlightthickness=0, troughcolor="#45475a"
        )
        self.scale_velocidad.set(110)
        self.scale_velocidad.pack(fill=tk.X, pady=(2, 12))

        tk.Button(
            panel_ctrl, text="▶ Buscar y Animar Camino",
            command=self.iniciar_busqueda,
            bg="#a6e3a1", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=6, cursor="hand2"
        ).pack(fill=tk.X, pady=4)

        tk.Button(
            panel_ctrl, text="⏹ Detener / Limpiar",
            command=self.reiniciar_vista,
            bg="#f38ba8", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=5, cursor="hand2"
        ).pack(fill=tk.X, pady=4)

        tk.Frame(panel_ctrl, bg="#45475a", height=2).pack(fill=tk.X, pady=10)
        self.lbl_estado = tk.Label(
            panel_ctrl,
            text=f"Listo. Estamina inicial: {ESTAMINA_INICIAL} pts.\n"
                 f"Cruz: -1 pt | Diagonal: -2 pts | Portal 99: teletransporte (+0 suma).",
            bg="#313244", fg="#f9e2af", font=("Segoe UI", 9),
            wraplength=285, justify="left"
        )
        self.lbl_estado.pack(anchor="w", pady=4)

        leyenda = (
            "Leyenda:\n"
            "• Morado: Portal (99) - Teletransporte\n"
            "• Azul: Coste 0\n"
            "• Amarillo: Explorando\n"
            "• Rojo: Poda / Sin Estamina\n"
            "• Verde: Camino óptimo"
        )
        tk.Label(
            panel_ctrl, text=leyenda,
            bg="#313244", fg="#bac2de", font=("Segoe UI", 9), justify="left"
        ).pack(anchor="w", side=tk.BOTTOM)

    def _color_base_celda(self, val):
        if val == VALOR_PORTAL:
            return "#583780", "\n(Portal)"
        if val == 0:
            return "#1e3a5f", "\n(Coste 0)"
        return "#313244", ""

    def _dibujar_tablero(self):
        for widget in self.frame_tablero.winfo_children():
            widget.destroy()

        self.celdas_ui = [[None for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.frame_tablero.rowconfigure(i, weight=1)
            for j in range(self.n):
                self.frame_tablero.columnconfigure(j, weight=1)
                valor = self.matriz[i][j]
                bg, extra = self._color_base_celda(valor)

                lbl = tk.Label(
                    self.frame_tablero,
                    text=f"{valor}{extra}",
                    font=("Segoe UI", 13, "bold"),
                    bg=bg,
                    fg="#cdd6f4",
                    relief=tk.RAISED,
                    bd=2,
                )
                lbl.grid(row=i, column=j, sticky="nsew", padx=4, pady=4)
                self.celdas_ui[i][j] = lbl

    def reiniciar_vista(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.animando = False
        for i in range(self.n):
            for j in range(self.n):
                val = self.matriz[i][j]
                bg, extra = self._color_base_celda(val)
                self.celdas_ui[i][j].config(text=f"{val}{extra}", bg=bg, fg="#cdd6f4")
        self.lbl_estado.config(text=f"Tablero reiniciado. Estamina inicial: {ESTAMINA_INICIAL} pts.")

    def _obtener_modo_busqueda(self):
        text = self.var_modo_busqueda.get()
        for key, desc in MODOS_DE_BUSQUEDA.items():
            if desc == text:
                return key
        return "libre4"

    def iniciar_busqueda(self):
        self.reiniciar_vista()
        objetivo = self.var_objetivo.get()
        mov_req = self.var_movimientos.get()
        modo_mov = self.var_modo_mov.get()
        modo_busqueda = self._obtener_modo_busqueda()

        mejor_camino, eventos = resolver_matriz(
            self.matriz,
            objetivo=objetivo,
            modo_busqueda=modo_busqueda,
            movimientos_requeridos=mov_req,
            modo_movimientos=modo_mov,
        )

        self.animando = True
        if len(eventos) > 250:
            paso = len(eventos) // 180
            eventos_filtrados = [
                ev for idx, ev in enumerate(eventos)
                if idx % paso == 0 or ev[0] == "encontrado"
            ]
        else:
            eventos_filtrados = eventos

        self._reproducir_evento(eventos_filtrados, 0, mejor_camino, objetivo, mov_req)

    def _reproducir_evento(self, eventos, indice, mejor_camino, objetivo, mov_req):
        if not self.animando:
            return

        if indice >= len(eventos):
            self._mostrar_resultado_final(mejor_camino, objetivo, mov_req)
            self.animando = False
            return

        tipo, camino, suma_actual, estamina_actual = eventos[indice]

        for i in range(self.n):
            for j in range(self.n):
                val = self.matriz[i][j]
                bg, extra = self._color_base_celda(val)
                self.celdas_ui[i][j].config(text=f"{val}{extra}", bg=bg, fg="#cdd6f4")

        for paso_idx, (f, c) in enumerate(camino):
            val = self.matriz[f][c]
            if tipo == "encontrado":
                color = "#a6e3a1"
                fg = "#11111b"
            elif tipo in ("poda", "poda_estamina", "sin_estamina") and paso_idx == len(camino) - 1:
                color = "#f38ba8"
                fg = "#11111b"
            else:
                color = "#f9e2af"
                fg = "#11111b"

            etiqueta = "99(P)" if val == VALOR_PORTAL else f"{val}"
            self.celdas_ui[f][c].config(
                text=f"{etiqueta}\n[Paso {paso_idx + 1}]",
                bg=color,
                fg=fg,
            )

        self.lbl_estado.config(
            text=f"Explorando ({indice + 1}/{len(eventos)})...\n"
                 f"Estado: {tipo.upper()}\n"
                 f"Suma actual: {suma_actual} / {objetivo}\n"
                 f"Estamina restante: {estamina_actual} / {ESTAMINA_INICIAL}\n"
                 f"Movimientos: {len(camino)}"
        )

        pausa = self.scale_velocidad.get()
        if tipo == "encontrado":
            pausa = max(pausa * 3, 350)

        self.after_id = self.root.after(
            pausa,
            lambda: self._reproducir_evento(eventos, indice + 1, mejor_camino, objetivo, mov_req),
        )

    def _mostrar_resultado_final(self, mejor_camino, objetivo, mov_req):
        for i in range(self.n):
            for j in range(self.n):
                val = self.matriz[i][j]
                bg, extra = self._color_base_celda(val)
                self.celdas_ui[i][j].config(text=f"{val}{extra}", bg=bg, fg="#6c7086")

        if mejor_camino:
            for idx, (f, c) in enumerate(mejor_camino):
                val = self.matriz[f][c]
                etiqueta = "99 (Portal)" if val == VALOR_PORTAL else f"{val}"
                self.celdas_ui[f][c].config(
                    text=f"{etiqueta}\n★ Paso {idx + 1}",
                    bg="#a6e3a1",
                    fg="#11111b",
                )
            self.lbl_estado.config(
                text=f"¡CAMINO ÓPTIMO ENCONTRADO!\n"
                     f"• Suma lograda: {objetivo}\n"
                     f"• Movimientos usados: {len(mejor_camino)}\n"
                     f"• Ruta: {mejor_camino}"
            )
        else:
            self.lbl_estado.config(
                text=f"No se encontró camino con suma {objetivo} y estamina {ESTAMINA_INICIAL}."
            )


if __name__ == "__main__":
    # Matriz 5x5 con exactamente dos portales (99) y celdas de coste 0
    matriz_prueba = [
        [1,  0,  3, 99,  5],
        [4,  0,  1,  2,  0],
        [0,  5,  0,  8,  2],
        [2,  0,  3,  0,  4],
        [6, 99,  0,  5,  1],
    ]

    print("=" * 64)
    print(" MATRIZ AVANZADA - PORTALES (99) Y FACTOR ESTAMINA (10)")
    print("=" * 64)
    print(" 1. Abrir Ventana Emergente Interactiva (Recomendado)")
    print(" 2. Ejecutar Animación en Consola")
    print("=" * 64)

    try:
        opcion = input("Selecciona una opción (Enter para Ventana Emergente [1]): ").strip()
    except EOFError:
        opcion = "2"

    if opcion == "2":
        animar_en_consola(matriz_prueba, objetivo=10, modo_busqueda="libre8", pausa=0.05)
    else:
        root = tk.Tk()
        app = VentanaMatrizPortalesEstamina(root, matriz_prueba)
        root.mainloop()
