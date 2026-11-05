import os
import time
import tkinter as tk
from tkinter import ttk, messagebox


# ==============================================================================
# LÓGICA DE BÚSQUEDA MEJORADA (COSTE 0, LÍMITE DE MOVIMIENTOS Y CAMINO MÁS CORTO)
# ==============================================================================

MODOS_DE_BUSQUEDA = {
    "libre4": "Solo 4 direcciones (arriba, abajo, izquierda, derecha)",
    "libre8": "8 direcciones (incluye diagonales)",
    "vertical": "Solo vertical (arriba y abajo)",
    "cruzado_x": "Cruzado en X (diagonales)",
    "zigzag": "Movimiento en zigzag (alternando horizontal y vertical)",
    "lineal": "Solo horizontal (izquierda y derecha)",
} 

def obtener_direcciones(modo_busqueda):
    rectas = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    diagonales = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales
    """Devuelve los vectores de movimiento (4 u 8 direcciones)."""
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
    return rectas  # Por defecto, solo 4 direcciones
    #     return [
    #         (-1, 0), (1, 0), (0, -1), (0, 1),   # Arriba, Abajo, Izquierda, Derecha
    #         (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
    #     ]
    # return [
    #     (-1, 0), (1, 0), (0, -1), (0, 1)        # Solo Horizontal y Vertical
    # ]
    
def es_movimiento_permitido(movimiento, direccion_anterior, modo_busqueda):
    if direccion_anterior is None:
        return True  # Primer movimiento permitido
    if modo_busqueda == "zigzag":
        return movimiento[1] != direccion_anterior[1]  # Alternar entre horizontal y vertical
    if modo_busqueda == "lineal":
        return movimiento == direccion_anterior  # Solo horizontal
    return True

def movimientos_validos(fila, col, n, modo_busqueda, direccion_anterior, visitados):
    validos = []
    for mov in obtener_direcciones(modo_busqueda):
        if not es_movimiento_permitido(mov, direccion_anterior, modo_busqueda):
            continue
        nueva_fila, nueva_columna = fila + mov[0], col + mov[1]
        if 0 <= nueva_fila < n and 0 <= nueva_columna < n:
            if not esta_en_lista((nueva_fila, nueva_columna), visitados):
                validos.append((nueva_fila, nueva_columna, mov))
    return validos

def esta_en_lista(coordenada, lista):
    """Comprueba si una tupla (fila, col) ya fue visitada."""
    for f, c in lista:
        if f == coordenada[0] and c == coordenada[1]:
            return True
    return False


def buscar_caminos_recursivo(
    matriz,
    n,
    fila,
    col,
    objetivo,
    suma_actual,
    camino,
    visitados,
    modo_busqueda,
    movimientos_requeridos,
    mejor_camino,
    historial_eventos=None,
    modo_movimientos="exacto",
    direccion_anterior=None
):
    """
    Explora recursivamente (Backtracking) soportando:
      - Celdas con coste 0 (no aumentan la suma, pero cuentan como 1 paso).
      - Objetivo de coste 0 (caminos formados únicamente por celdas de valor 0).
      - Control de movimientos:
          * movimientos_requeridos == 0: busca el camino más corto global.
          * modo_movimientos == 'exacto': busca alcanzar el objetivo en exactamente N movimientos.
          * modo_movimientos == 'maximo': busca el camino más corto en a lo sumo N movimientos.
    """
    valor_celda = matriz[fila][col]
    suma_actual += valor_celda
    camino.append((fila, col))
    visitados.append((fila, col))
    pasos_actuales = len(camino)

    # Registrar evento de avance para la animación
    if historial_eventos is not None:
        historial_eventos.append(("avanzar", list(camino), suma_actual))

    # PODA 1: Si nos pasamos de la suma objetivo (y todos los valores son >= 0)
    if suma_actual > objetivo:
        if historial_eventos is not None:
            historial_eventos.append(("poda", list(camino), suma_actual))
        camino.pop()
        visitados.pop()
        return

    # PODA 2: Si el usuario definió un límite de movimientos y ya lo superamos
    if movimientos_requeridos > 0 and pasos_actuales > movimientos_requeridos:
        if historial_eventos is not None:
            historial_eventos.append(("poda", list(camino), suma_actual))
        camino.pop()
        visitados.pop()
        return

    # PODA 3: Si buscamos el camino más corto (sin límite o con límite máximo)
    # y ya somos igual o más largos que el mejor hallado hasta ahora
    busca_mas_corto = (movimientos_requeridos == 0) or (modo_movimientos == "maximo")
    if busca_mas_corto and mejor_camino[0] is not None:
        if pasos_actuales >= len(mejor_camino[0]):
            if historial_eventos is not None:
                historial_eventos.append(("poda", list(camino), suma_actual))
            camino.pop()
            visitados.pop()
            return

    # CASO DE ÉXITO: La suma coincide con el objetivo
    if suma_actual == objetivo:
        # Si se pidió un número EXACTO de movimientos, verificamos que coincida
        # (Si aún faltan movimientos, no cortamos: puede avanzar por celdas vecinas de coste 0)
        if movimientos_requeridos > 0 and modo_movimientos == "exacto":
            if pasos_actuales == movimientos_requeridos:
                mejor_camino[0] = list(camino)
                if historial_eventos is not None:
                    historial_eventos.append(("encontrado", list(camino), suma_actual))
                camino.pop()
                visitados.pop()
                return
        else:
            # Buscamos el camino más corto (con al menos 2 celdas si objetivo == 0 para ver recorrido)
            min_pasos = 2 if objetivo == 0 else 1
            if pasos_actuales >= min_pasos:
                if mejor_camino[0] is None or pasos_actuales < len(mejor_camino[0]):
                    mejor_camino[0] = list(camino)
                    if historial_eventos is not None:
                        historial_eventos.append(("encontrado", list(camino), suma_actual))
                camino.pop()
                visitados.pop()
                return

    # # Explorar vecinos
    # movimientos = obtener_direcciones(modo_busqueda)
    # for mov_f, mov_c in movimientos:
    #     nueva_f = fila + mov_f
    #     nueva_c = col + mov_c

    #     if 0 <= nueva_f < n and 0 <= nueva_c < n:
    #         if not esta_en_lista((nueva_f, nueva_c), visitados):
    #             buscar_caminos_recursivo(
    #                 matriz,
    #                 n,
    #                 nueva_f,
    #                 nueva_c,
    #                 objetivo,
    #                 suma_actual,
    #                 camino,
    #                 visitados,
    #                 modo_busqueda,
    #                 movimientos_requeridos,
    #                 mejor_camino,
    #                 historial_eventos,
    #                 modo_movimientos
    #             )
    #             # Si pedían movimientos exactos y ya hallamos uno, podemos terminar antes
    #             if movimientos_requeridos > 0 and modo_movimientos == "exacto" and mejor_camino[0] is not None:
    #                 camino.pop()
    #                 visitados.pop()
    #                 return
    
    for nueva_f, nueva_c, mov in movimientos_validos(fila, col, n, modo_busqueda, direccion_anterior, visitados):
        buscar_caminos_recursivo(
            matriz,
            n,
            nueva_f,
            nueva_c,
            objetivo,
            suma_actual,
            camino,
            visitados,
            modo_busqueda,
            movimientos_requeridos,
            mejor_camino,
            historial_eventos,
            modo_movimientos,
            direccion_anterior=mov
        )
        # Si pedían movimientos exactos y ya hallamos uno, podemos terminar antes
        if movimientos_requeridos > 0 and modo_movimientos == "exacto" and mejor_camino[0] is not None:
            camino.pop()
            visitados.pop()
            return

    # Backtracking (retroceso)
    if historial_eventos is not None:
        historial_eventos.append(("retroceder", list(camino), suma_actual))
    camino.pop()
    visitados.pop()


def resolver_matriz(
    matriz,
    objetivo,
    modo_busqueda="libre4",
    movimientos_requeridos=0,
    modo_movimientos="exacto"
):
    """
    Recorre todas las celdas de inicio posibles y devuelve:
      - mejor_camino: lista de coordenadas (fila, col) del camino más corto o exacto.
      - historial_eventos: pasos grabados para reproducir la animación.
    """
    n = len(matriz)
    mejor_camino = [None]
    historial_eventos = []

    for i in range(n):
        for j in range(n):
            # Si buscamos coste 0 total, solo tiene sentido iniciar en una celda de valor 0
            if objetivo == 0 and matriz[i][j] != 0:
                continue

            buscar_caminos_recursivo(
                matriz=matriz,
                n=n,
                fila=i,
                col=j,
                objetivo=objetivo,
                suma_actual=0,
                camino=[],
                visitados=[],
                modo_busqueda=modo_busqueda,
                movimientos_requeridos=movimientos_requeridos,
                mejor_camino=mejor_camino,
                historial_eventos=historial_eventos,
                modo_movimientos=modo_movimientos
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


def animar_en_consola(matriz, objetivo, modo_busqueda="libre4", movimientos_requeridos=0, modo_movimientos="exacto", pausa=0.08):
    """Ejecuta la búsqueda y muestra una animación paso a paso en la terminal."""
    n = len(matriz)
    mejor_camino, eventos = resolver_matriz(
        matriz, objetivo, modo_busqueda, movimientos_requeridos, modo_movimientos
    )

    # Limitar cantidad de frames en consola para que no sea eterno si hay muchos pasos
    paso_salto = max(1, len(eventos) // 80)

    for idx, (tipo, camino_actual, suma_actual) in enumerate(eventos):
        if idx % paso_salto != 0 and tipo != "encontrado":
            continue

        limpiar_consola()
        print("=" * 58)
        print("   ANIMACIÓN EN CONSOLA - BÚSQUEDA DE CAMINO MÁS CORTO")
        print("=" * 58)
        modo_mov = "Exactamente " + str(movimientos_requeridos) if movimientos_requeridos > 0 else "Mínimo posible (Más corto)"
        print(f" Objetivo Suma: {objetivo} | Movimientos: {modo_mov}")
        print(f" Modo de Busqueda: {MODOS_DE_BUSQUEDA.get(modo_busqueda, modo_busqueda)}")
        print(f" Estado: {tipo.upper():12s} | Suma actual: {suma_actual:2d} | Pasos: {len(camino_actual)}")
        print("-" * 58)

        for i in range(n):
            linea = "   "
            for j in range(n):
                if (i, j) in camino_actual:
                    orden = camino_actual.index((i, j)) + 1
                    linea += f"[{matriz[i][j]:2d}#{orden}] "
                else:
                    linea += f"  {matriz[i][j]:2d}   "
            print(linea)
        print("=" * 58)
        time.sleep(pausa if tipo != "encontrado" else pausa * 4)

    # Resultado final en consola
    print("\n" + "=" * 58)
    if mejor_camino:
        coste_total = sum(matriz[f][c] for f, c in mejor_camino)
        ceros_usados = sum(1 for f, c in mejor_camino if matriz[f][c] == 0)
        print(" ¡RESULTADO FINAL ÓPTIMO ENCONTRADO!")
        print(f" -> Cantidad de movimientos (celdas): {len(mejor_camino)}")
        print(f" -> Coste / Suma total: {coste_total}")
        print(f" -> Celdas de coste 0 utilizadas: {ceros_usados}")
        print("\n Secuencia paso a paso:")
        for idx, (f, c) in enumerate(mejor_camino):
            etiqueta_cero = " (COSTE 0 - GRATIS)" if matriz[f][c] == 0 else ""
            print(f"   Movimiento {idx + 1}: ({f}, {c}) -> Valor: {matriz[f][c]}{etiqueta_cero}")

        print("\n Matriz con el camino más corto resaltado:")
        for i in range(n):
            linea = "   "
            for j in range(n):
                if (i, j) in mejor_camino:
                    linea += f"[{matriz[i][j]:2d}] "
                else:
                    linea += "  .  "
            print(linea)
    else:
        print(f" [!] No se encontró ningún camino con suma {objetivo} y la restricción dada.")
    print("=" * 58)


# ==============================================================================
# VENTANA EMERGENTE INTERACTIVA CON ANIMACIÓN (TKINTER)
# ==============================================================================

class VentanaMatrizMejorada:
    def __init__(self, root, matriz_inicial):
        self.root = root
        self.root.title("Búsqueda de Caminos Más Cortos y Coste 0 - Matriz Mejorada")
        self.root.geometry("880x640")
        self.root.configure(bg="#1e1e2e")

        self.matriz = [fila[:] for fila in matriz_inicial]
        self.n = len(self.matriz)
        self.animando = False
        self.after_id = None

        self._construir_interfaz()
        self._dibujar_tablero()

    def _construir_interfaz(self):
        # Título superior
        header = tk.Frame(self.root, bg="#181825", pady=10)
        header.pack(fill=tk.X)
        tk.Label(
            header,
            text="Visualizador de Caminos Más Cortos en Matrices (con Coste 0)",
            font=("Segoe UI", 15, "bold"),
            fg="#cdd6f4",
            bg="#181825"
        ).pack()

        # Contenedor principal
        main_frame = tk.Frame(self.root, bg="#1e1e2e", padx=15, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Panel izquierdo: Tablero de la matriz
        self.frame_tablero = tk.Frame(main_frame, bg="#1e1e2e")
        self.frame_tablero.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

        # Panel derecho: Controles y explicación
        panel_ctrl = tk.Frame(main_frame, bg="#313244", padx=15, pady=15, width=320)
        panel_ctrl.pack(side=tk.RIGHT, fill=tk.Y)
        panel_ctrl.pack_propagate(False)

        estilo_lbl = {"bg": "#313244", "fg": "#cdd6f4", "font": ("Segoe UI", 10, "bold")}

        # 1. Suma Objetivo
        tk.Label(panel_ctrl, text="Suma / Coste Objetivo (0 perm.):", **estilo_lbl).pack(anchor="w")
        self.var_objetivo = tk.IntVar(value=10)
        tk.Spinbox(
            panel_ctrl, from_=0, to=100, textvariable=self.var_objetivo,
            font=("Segoe UI", 11), width=10
        ).pack(anchor="w", pady=(2, 10))

        # 2. En cuántos movimientos encontrar el objetivo
        tk.Label(panel_ctrl, text="¿En cuántos movimientos?", **estilo_lbl).pack(anchor="w")
        tk.Label(
            panel_ctrl,
            text="(0 = Buscar el camino MÁS CORTO sin límite)",
            bg="#313244", fg="#a6adc8", font=("Segoe UI", 8)
        ).pack(anchor="w")
        self.var_movimientos = tk.IntVar(value=0)
        tk.Spinbox(
            panel_ctrl, from_=0, to=25, textvariable=self.var_movimientos,
            font=("Segoe UI", 11), width=10
        ).pack(anchor="w", pady=(2, 6))
        
        tk.Label(panel_ctrl, text="Modo de Busqueda:", **estilo_lbl).pack(anchor="w")
        self.var_modo_busqueda = tk.StringVar(value=MODOS_DE_BUSQUEDA["libre4"])
        ttk.Combobox(
            panel_ctrl, textvariable=self.var_modo_busqueda, values=list(MODOS_DE_BUSQUEDA.values()), state="readonly", font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(2, 6))

        self.var_modo_mov = tk.StringVar(value="exacto")
        frame_modo = tk.Frame(panel_ctrl, bg="#313244")
        frame_modo.pack(anchor="w", pady=(0, 8))
        tk.Radiobutton(
            frame_modo, text="Exactos", variable=self.var_modo_mov, value="exacto",
            bg="#313244", fg="#cdd6f4", selectcolor="#45475a",
            activebackground="#313244", activeforeground="#cdd6f4", font=("Segoe UI", 9)
        ).pack(side=tk.LEFT, padx=(0, 8))
        tk.Radiobutton(
            frame_modo, text="Máximo (Más corto ≤ N)", variable=self.var_modo_mov, value="maximo",
            bg="#313244", fg="#cdd6f4", selectcolor="#45475a",
            activebackground="#313244", activeforeground="#cdd6f4", font=("Segoe UI", 9)
        ).pack(side=tk.LEFT)

        # 3. Diagonales
        self.var_diagonales = tk.BooleanVar(value=False)
        tk.Checkbutton(
            panel_ctrl,
            text="Permitir Diagonales (8 direcciones)",
            variable=self.var_diagonales,
            bg="#313244", fg="#cdd6f4", selectcolor="#45475a",
            activebackground="#313244", activeforeground="#cdd6f4",
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(0, 10))

        # 4. Velocidad de animación
        tk.Label(panel_ctrl, text="Velocidad de Animación (ms):", **estilo_lbl).pack(anchor="w")
        self.scale_velocidad = tk.Scale(
            panel_ctrl, from_=10, to=400, orient=tk.HORIZONTAL,
            bg="#313244", fg="#cdd6f4", highlightthickness=0, troughcolor="#45475a"
        )
        self.scale_velocidad.set(90)
        self.scale_velocidad.pack(fill=tk.X, pady=(2, 12))

        # Botones de acción
        btn_iniciar = tk.Button(
            panel_ctrl, text="▶ Buscar y Animar Camino",
            command=self.iniciar_busqueda,
            bg="#a6e3a1", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=6, cursor="hand2"
        )
        btn_iniciar.pack(fill=tk.X, pady=4)

        btn_solo_coste_cero = tk.Button(
            panel_ctrl, text="⚡ Demo: Camino de Coste 0",
            command=self.demo_coste_cero,
            bg="#89b4fa", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=6, cursor="hand2"
        )
        btn_solo_coste_cero.pack(fill=tk.X, pady=4)

        btn_detener = tk.Button(
            panel_ctrl, text="⏹ Detener / Limpiar",
            command=self.reiniciar_vista,
            bg="#f38ba8", fg="#11111b", font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT, pady=5, cursor="hand2"
        )
        btn_detener.pack(fill=tk.X, pady=4)

        # Panel de estado / resultados
        tk.Frame(panel_ctrl, bg="#45475a", height=2).pack(fill=tk.X, pady=10)
        self.lbl_estado = tk.Label(
            panel_ctrl,
            text="Listo. Haz clic en una celda para cambiar su valor (puedes poner 0) o inicia la búsqueda.",
            bg="#313244", fg="#f9e2af", font=("Segoe UI", 9),
            wraplength=285, justify="left"
        )
        self.lbl_estado.pack(anchor="w", pady=4)

        # Leyenda de colores
        leyenda = (
            "Leyenda:\n"
            "• Azul: Celdas con Coste 0 (Gratis)\n"
            "• Amarillo: Explorando camino\n"
            "• Rojo: Poda / Retroceso (Backtracking)\n"
            "• Verde: ¡Camino más corto / óptimo!"
        )
        tk.Label(
            panel_ctrl, text=leyenda,
            bg="#313244", fg="#bac2de", font=("Segoe UI", 9), justify="left"
        ).pack(anchor="w", side=tk.BOTTOM)

    def _dibujar_tablero(self):
        for widget in self.frame_tablero.winfo_children():
            widget.destroy()

        self.celdas_ui = [[None for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.frame_tablero.rowconfigure(i, weight=1)
            for j in range(self.n):
                self.frame_tablero.columnconfigure(j, weight=1)
                valor = self.matriz[i][j]
                color_fondo = "#313244" if valor != 0 else "#1e3a5f"
                texto_extra = "\n(Coste 0)" if valor == 0 else ""

                lbl = tk.Label(
                    self.frame_tablero,
                    text=f"{valor}{texto_extra}",
                    font=("Segoe UI", 14, "bold"),
                    bg=color_fondo,
                    fg="#cdd6f4",
                    relief=tk.RAISED,
                    bd=2,
                    cursor="hand2"
                )
                lbl.grid(row=i, column=j, sticky="nsew", padx=4, pady=4)
                # Permitir clic para alternar valor (útil para probar coste 0 en vivo)
                lbl.bind("<Button-1>", lambda e, f=i, c=j: self._cambiar_valor_celda(f, c))
                self.celdas_ui[i][j] = lbl

    def _cambiar_valor_celda(self, f, c):
        if self.animando:
            return
        # Cicla entre 0 y 9 al hacer clic
        self.matriz[f][c] = (self.matriz[f][c] + 1) % 10
        self.reiniciar_vista()

    def reiniciar_vista(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.animando = False
        for i in range(self.n):
            for j in range(self.n):
                val = self.matriz[i][j]
                bg = "#1e3a5f" if val == 0 else "#313244"
                extra = "\n(Coste 0)" if val == 0 else ""
                self.celdas_ui[i][j].config(text=f"{val}{extra}", bg=bg, fg="#cdd6f4")
        self.lbl_estado.config(text="Tablero reiniciado. Puedes editar celdas haciendo clic sobre ellas.")

    def demo_coste_cero(self):
        """Configura un ejemplo claro donde se busca objetivo de coste 0 en 4 movimientos."""
        self.reiniciar_vista()
        self.var_objetivo.set(0)
        self.var_movimientos.set(4)
        self.var_modo_mov.set("exacto")
        self.var_modo_busqueda.set(MODOS_DE_BUSQUEDA["libre4"])
        self.iniciar_busqueda()
        
    def _obtener_modo_busqueda(self):
        text = self.var_modo_busqueda.get()
        for key, desc in MODOS_DE_BUSQUEDA.items():
            if desc == text:
                return key
        return "libre4"  # Valor por defecto si no se encuentra

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
            modo_movimientos=modo_mov
        )

        # También imprimimos en consola el resumen
        print("\n" + "=" * 55)
        print(f"BÚSQUEDA EJECUTADA -> Objetivo: {objetivo} | Movimientos req.: {mov_req or 'Mínimo (Más corto)'}")
        print(f"Modo de búsqueda: {MODOS_DE_BUSQUEDA[modo_busqueda]}")
        if mejor_camino:
            print(f"Camino óptimo ({len(mejor_camino)} movimientos): {mejor_camino}")
        else:
            print("No se encontró camino con esos parámetros.")
        print("=" * 55)

        self.animando = True
        # Si hay demasiados eventos, muestreamos para que la animación dure unos segundos
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

        tipo, camino, suma_actual = eventos[indice]

        # Restaurar colores base
        for i in range(self.n):
            for j in range(self.n):
                val = self.matriz[i][j]
                bg = "#1e3a5f" if val == 0 else "#313244"
                extra = "\n(Coste 0)" if val == 0 else ""
                self.celdas_ui[i][j].config(text=f"{val}{extra}", bg=bg, fg="#cdd6f4")

        # Colorear el camino que se está evaluando
        for paso_idx, (f, c) in enumerate(camino):
            val = self.matriz[f][c]
            if tipo == "encontrado":
                color = "#a6e3a1"  # Verde éxito
                fg = "#11111b"
            elif tipo == "poda" and paso_idx == len(camino) - 1:
                color = "#f38ba8"  # Rojo poda
                fg = "#11111b"
            else:
                color = "#f9e2af"  # Amarillo exploración
                fg = "#11111b"

            self.celdas_ui[f][c].config(
                text=f"{val}\n[Paso {paso_idx + 1}]",
                bg=color,
                fg=fg
            )

        self.lbl_estado.config(
            text=f"Explorando ({indice + 1}/{len(eventos)})...\n"
                 f"Estado: {tipo.upper()}\n"
                 f"Suma actual: {suma_actual} / {objetivo}\n"
                 f"Movimientos actuales: {len(camino)}"
        )

        pausa = self.scale_velocidad.get()
        if tipo == "encontrado":
            pausa = max(pausa * 3, 350)

        self.after_id = self.root.after(
            pausa,
            lambda: self._reproducir_evento(eventos, indice + 1, mejor_camino, objetivo, mov_req)
        )

    def _mostrar_resultado_final(self, mejor_camino, objetivo, mov_req):
        # Limpiar tablero
        for i in range(self.n):
            for j in range(self.n):
                val = self.matriz[i][j]
                bg = "#1e3a5f" if val == 0 else "#313244"
                extra = "\n(Coste 0)" if val == 0 else ""
                self.celdas_ui[i][j].config(text=f"{val}{extra}", bg=bg, fg="#6c7086")

        if mejor_camino:
            ceros = sum(1 for f, c in mejor_camino if self.matriz[f][c] == 0)
            for idx, (f, c) in enumerate(mejor_camino):
                val = self.matriz[f][c]
                etiqueta_cero = " (Coste 0)" if val == 0 else ""
                self.celdas_ui[f][c].config(
                    text=f"{val}{etiqueta_cero}\n★ Paso {idx + 1}",
                    bg="#a6e3a1",
                    fg="#11111b"
                )
            self.lbl_estado.config(
                text=f"¡CAMINO ÓPTIMO ENCONTRADO!\n"
                     f"• Suma lograda: {objetivo}\n"
                     f"• Movimientos usados: {len(mejor_camino)}\n"
                     f"• Celdas de Coste 0 usadas: {ceros}\n"
                     f"• Ruta: {mejor_camino}"
            )
        else:
            self.lbl_estado.config(
                text=f"No se encontró ningún camino que sume {objetivo} "
                     f"con {'exactamente ' + str(mov_req) + ' movimientos' if mov_req > 0 else 'esos parámetros'}."
            )


# ==============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# ==============================================================================

if __name__ == "__main__":
    # Matriz de prueba 5x5 que incluye celdas con Coste 0
    matriz_prueba = [
        [1, 0, 3, 0, 5],
        [4, 0, 1, 2, 0],
        [0, 5, 0, 8, 2],
        [2, 0, 3, 0, 4],
        [6, 1, 0, 5, 1]
    ]

    print("=" * 60)
    print(" MATRIZ MEJORADA - CAMINOS MÁS CORTOS Y COSTE 0")
    print("=" * 60)
    print(" 1. Abrir Ventana Emergente Interactiva (Recomendado)")
    print(" 2. Ejecutar Animación en Consola")
    print("=" * 60)

    try:
        opcion = input("Selecciona una opción (Enter para Ventana Emergente [1]): ").strip()
    except EOFError:
        opcion = "1"

    if opcion == "2":
        claves_modo = list(MODOS_DE_BUSQUEDA.keys())
        try:
            obj = int(input("Ingresa la suma objetivo (ej. 10 o 0): ") or "10")
            movs = int(input("¿En cuántos movimientos? (0 = Camino más corto automático): ") or "0")
            print("Modos de búsqueda disponibles:")
            for idx, clave in enumerate(claves_modo, start=1):
                print(f"  {idx}. {MODOS_DE_BUSQUEDA[clave]}")
            eleccion = int(input(f"Selecciona el modo de búsqueda (1-{len(claves_modo)}): ") or "1")
            modo = claves_modo[eleccion - 1] if 1 <= eleccion <= len(claves_modo) else "libre4"
        except ValueError:
            obj, movs, modo = 10, 0, "libre4"

        animar_en_consola(
            matriz_prueba,
            objetivo=obj,
            modo_busqueda=modo,
            movimientos_requeridos=movs,
            pausa=0.08
        )
    else:
        root = tk.Tk()
        app = VentanaMatrizMejorada(root, matriz_prueba)
        root.mainloop()
