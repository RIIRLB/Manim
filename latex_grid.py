# de Manim Examples - version en español
# https://docs.manim.community/en/stable/examples.html

from manim import *

class AperturaManim(Scene):
    def construct(self):
        # Texto inicial con LaTeX
        titulo = Tex(r"Esto se puede hacer con \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(titulo, basel).arrange(DOWN)
        self.play(
            Write(titulo),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        # Transformación de texto
        titulo_transformado = Tex("y se puede transformar a esto")
        titulo_transformado.to_corner(UP + LEFT)
        self.wait(1)
        self.play(
            Transform(titulo, titulo_transformado),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        # Creación de una cuadricula (grid)
        cuadricula = NumberPlane()
        titulo_cuadricula = Tex("Tambien podemos transformar cuadriculas", font_size=72)
        titulo_cuadricula.move_to(titulo_transformado)

        self.add(cuadricula, titulo_cuadricula)  # El título debe estar sobre la cuadricula
        self.play(
            FadeOut(titulo),
            FadeIn(titulo_cuadricula, shift=UP),
            Create(cuadricula, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        # Aplicar función no lineal a la cuadricula
        titulo_cuadricula_transformada = Tex(
            r"Esa fue una función no lineal \\ aplicada a la cuadricula"
        )
        titulo_cuadricula_transformada.move_to(titulo_cuadricula, UL)
        cuadricula.prepare_for_nonlinear_transform()
        self.play(
            cuadricula.animate.apply_function(
                lambda p: p + np.array([
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ])
            ),
            run_time=3,
        )
        self.wait()
