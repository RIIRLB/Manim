# Primer ejemplo en Manim
# RILB
from manim import *

class Hola(Scene):
    def construct(self):
        text = Text("Hola mundo, estoy usando Manim")
        self.play(Write(text))
        self.wait(2)


# python -m manim -p -qh "C:\Users\narut\OneDrive\Escritorio\EXP\hola.py" Hola 