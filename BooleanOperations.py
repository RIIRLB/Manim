# Operaciones Booleanas
from manim import *

# Creamos una clase que hereda de ThreeDScene.
class BooleanOperations(ThreeDScene):
    def construct(self):
        # Creamos la primera elipse azul con relleno semitransparente
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)  # La movemos a la izquierda

        # Hacemos una copia de ellipse1, pero en rojo, y la movemos a la derecha
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)

        # Título de la animación
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)

        # Agrupamos título y elipses y lo movemos a la izquierda
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)

        # Animamos que aparezca el grupo en escena
        self.play(FadeIn(ellipse_group))

        # =================== INTERSECCIÓN ===================
        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        # Escalamos la intersección y la movemos a la derecha arriba
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        # =================== UNIÓN ===================
        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        # Escalamos y colocamos debajo de la intersección
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        # =================== EXCLUSIÓN ===================
        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        # Escalamos y colocamos debajo de la unión
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        # =================== DIFERENCIA ===================
        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        # Escalamos y lo ponemos a la izquierda de la unión
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))
