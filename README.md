# Manim

Algunas cosas extras de Manim

##### Figuras 2D en Manim ######

Estas son las clases más comunes de formas bidimensionales que puedes crear directamente en Manim:

Circle() → Círculo

Ellipse() → Elipse

Square() → Cuadrado

Rectangle() → Rectángulo

RoundedRectangle() → Rectángulo redondeado

Polygon(*points) → Polígono (cualquier cantidad de vértices)

RegularPolygon(n=...) → Polígono regular (ej. triángulo, pentágono, hexágono…)

Triangle() → Triángulo equilátero

Line(start, end) → Línea

DashedLine(start, end) → Línea discontinua

Arc() → Arco de circunferencia

ArcBetweenPoints(p1, p2) → Arco entre dos puntos

Annulus(inner_radius=..., outer_radius=...) → Anillo (círculo hueco)

Sector() → Sector circular (rebanada de pizza)

Dot() → Punto

Arrow(start, end) → Flecha

DoubleArrow(start, end) → Flecha doble

CurvedArrow(start, end) → Flecha curva

CurvedDoubleArrow(start, end) → Flecha curva doble

CubicBezier(points) → Curva de Bézier

VMobject() → Base para crear formas personalizadas (dibujando con puntos)



##### Transformaciones de Manim #####

Transform(obj1, obj2) → cambia una figura en otra.

ReplacementTransform(obj1, obj2) → reemplazo visual.

FadeIn, FadeOut → aparecer o desaparecer.

Rotate, Scale, Shift, Stretch → deformaciones geométricas.



##### Colores en Manim (algunos) #####

WHITE

BLACK

BLUE, BLUE_E, BLUE_D, BLUE_C, BLUE_B, BLUE_A

RED, RED_E, RED_D, RED_C, RED_B, RED_A

GREEN, GREEN_E, GREEN_D, GREEN_C, GREEN_B, GREEN_A

YELLOW, YELLOW_E, YELLOW_D, YELLOW_C, YELLOW_B, YELLOW_A

ORANGE

PURPLE

PINK

GRAY, LIGHT_GRAY, DARK_GRAY

TEAL

MAROON

GOLD
