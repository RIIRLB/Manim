# Segundo ejemplo
# RILB

from manim import *

class circulos(Scene):
    def construct(self):
        circ_1 = Circle(radius=1)
        circ_2 = Circle(radius=1.5, color=GREEN_B)
        circ_3 = Circle(radius=1, color= BLUE_E, fill_opacity=0.5)
        
        grupo_circ = Group(circ_1, circ_2,circ_3).arrange(buff=1)
        self.add(grupo_circ)
# contribucion de Mates Mike
#        self.play(Create(circ_1))
#        self.wait(1)
#        self.play(Transform(circ_1, circ_2))
#        self.wait(1)
#        self.play(Transform(circ_1, circ_3))
#        self.wait(2)
