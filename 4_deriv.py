# ejemplo 4 Función cuadrática
# RILB

from manim import *

class derivada(Scene):
    def construct(self):
        #Ejes cartesianos
        ejes = Axes(
            x_range=[-5,5,1],
            y_range=[-5,10,1],
            axis_config={"include_numbers": True}
        )
        # Etiquetas
        etiquetas = ejes.get_axis_labels(x_label="x", y_label="y")
        
        # Definición de Funciones
        funcion = ejes.plot(lambda x: x**2, color=BLUE, x_range=[-3,3])
        derivada =ejes.plot(lambda x: 2*x, color=RED, x_range=[-3,3])
        
        # Nombres
        label_funcion = ejes.get_graph_label(funcion, label="y=x^2", direction=UP)
        label_derivada = ejes.get_graph_label(derivada, label="y'=2x", direction=DOWN)
        
        # Animaciones 
        self.play(Create(ejes), Write(etiquetas))
        self.play(Create(funcion), Write(label_funcion))
        self.wait(2)
        self.play(Create(derivada), Write(label_derivada))
        self.wait(2)
