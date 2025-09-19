# de Manim Examples - version en español
# https://docs.manim.community/en/stable/examples.html

from manim import *
import numpy as np
import math

class AnimarPi(Scene):
    def construct(self):
        # ---------- Crear una cuadrícula 10x10 de símbolos \pi ----------
        filas, columnas = 10, 10
        simbolo = MathTex(r"\pi")  # símbolo que vamos a replicar
        # crear N copias y colocarlas en una grilla
        grid = VGroup(*[simbolo.copy() for _ in range(filas * columnas)])
        grid.arrange_in_grid(rows=filas, cols=columnas, buff=0.2)
        grid.set_height(4)  # ajustar la altura total de la grilla
        self.add(grid)

        # ---------- Animar aplicando métodos (sintaxis .animate) ----------
        # Mover la cuadrícula hacia la izquierda
        self.play(grid.animate.shift(LEFT))
        self.wait(0.5)

        # (Sintaxis histórica, rara vez necesaria hoy): self.play(grid.shift, LEFT)
        # Recomendado: usar .animate siempre que sea posible
        self.play(grid.animate.shift(RIGHT))  # ejemplo alternativo
        self.wait(0.3)

        # Cambiar el color completo con animación
        self.play(grid.animate.set_color(YELLOW))
        self.wait(0.4)

        # Aplicar un degradado por submobjetos
        self.play(grid.animate.set_color_by_gradient(BLUE, GREEN))
        self.wait(0.5)

        # Cambiar la altura total (se anima el escalado)
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait(0.5)

        # ---------- Transformaciones no lineales ----------
        # Aplicar una función compleja (trata puntos como números complejos)
        # Atención: np.exp puede enviar puntos muy lejos; si ves artefactos, reducir el efecto.
        self.play(grid.animate.apply_complex_function(np.exp), run_time=4)
        self.wait(0.6)

        # Aplicar una función R^3 -> R^3 (deformación personalizada)
        self.play(
            grid.animate.apply_function(
                lambda p: np.array(
                    [
                        p[0] + 0.5 * math.sin(p[1]),
                        p[1] + 0.5 * math.sin(p[0]),
                        p[2],
                    ]
                )
            ),
            run_time=4,
        )
        self.wait(1)
