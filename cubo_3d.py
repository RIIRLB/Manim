from manim import *

class Cubo3D(ThreeDScene):
    def construct(self):
        # Configura la cámara en 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Crea un cubo
        cubo = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.5)
        self.add(cubo)
        
        # Animación de rotación
        self.play(Rotate(cubo, angle=PI, axis=UP), run_time=2)
        self.play(Rotate(cubo, angle=PI, axis=RIGHT), run_time=2)

        # Mantener en pantalla un poco
        self.wait(1)
 
 #para ejecutar el perograma
 #  python -m manim -p -qh "C:\Users\narut\OneDrive\Escritorio\EXP\cubo_3d.py" Cubo3D 