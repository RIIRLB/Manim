# Tercer ejemplo
# RILB
from manim import *

class CatalogoFiguras(Scene):
    def construct(self):
        # Lista de figuras y nombres
        figuras = [
            (Circle(), "Círculo"),
            (Square(), "Cuadrado"),
            (Triangle(), "Triángulo"),
            (Ellipse(), "Elipse"),
            (Rectangle(), "Rectángulo"),
            (RegularPolygon(6), "Hexágono"),
            (Polygon([-2,0,0],[0,2,0],[2,0,0],[0,-2,0]), "Polígono irregular"),
            (Arc(radius=2, angle=PI/2), "Arco"),
            (Annulus(inner_radius=0.5, outer_radius=1.5), "Anillo"),
            (Sector(angle=PI/3), "Sector circular"),
        ]

        # Colores a usar
        colores = [BLUE, RED, GREEN, ORANGE, PURPLE, PINK, TEAL, GOLD, YELLOW, MAROON]

        # Primera figura
        figura, nombre = figuras[0]
        figura.set_color(colores[0])
        texto = Text(nombre, font_size=32).next_to(figura, DOWN)
        self.play(Create(figura), Write(texto))
        self.wait(1)

        # Transformaciones sucesivas
        for i in range(1, len(figuras)):
            nueva_figura, nuevo_nombre = figuras[i]
            nueva_figura.set_color(colores[i % len(colores)])
            nuevo_texto = Text(nuevo_nombre, font_size=32).next_to(nueva_figura, DOWN)

            # Transformar figura y texto
            self.play(
                Transform(figura, nueva_figura),
                Transform(texto, nuevo_texto),
                run_time=2
            )
            self.play(figura.animate.set_fill(colores[i % len(colores)], opacity=0.5))
            self.wait(1)
