from manim import *

class Escena3D(ThreeDScene):
    def construct(self):
        # Configurar la cámara 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Crear un sistema de ejes 3D
        ejes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={"include_numbers": True}
        )

        # Crear un objeto 3D: una esfera
        esfera = Sphere(radius=1, color=BLUE_E)
        esfera.shift(UP)

        # Animaciones iniciales
        self.play(Create(ejes))
        self.play(FadeIn(esfera))
        
        # Rotar cámara lentamente
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        # Movimiento por ejes
        self.play(esfera.animate.shift(RIGHT * 2), run_time=1)  # X positivo
        self.play(esfera.animate.shift(UP * 2), run_time=1)     # Y positivo
        self.play(esfera.animate.shift(OUT * 2), run_time=1)    # Z positivo (hacia la cámara)
        self.play(esfera.animate.shift(LEFT * 4), run_time=1)   # X negativo
        self.play(esfera.animate.shift(DOWN * 4), run_time=1)   # Y negativo
        self.play(esfera.animate.shift(IN * 4), run_time=1)     # Z negativo (hacia el fondo)

        # Regresar al centro
        self.play(esfera.animate.shift(RIGHT * 2 + UP * 2 + OUT * 2), run_time=1)

        self.wait(2)
