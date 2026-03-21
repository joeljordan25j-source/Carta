import turtle
import math

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Una Rosa Amarilla para Ti")

t = turtle.Turtle()
t.speed(0) # Velocidad máxima de dibujo para la animación

def dibujar_estrella(x, y, tamaño):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    for _ in range(5):
        t.forward(tamaño)
        t.right(144)

# Decoración de fondo: Estrellas
dibujar_estrella(-200, 200, 10)
dibujar_estrella(150, 250, 15)
dibujar_estrella(-150, -150, 12)
dibujar_estrella(200, -100, 8)

# Dibujo del tallo
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)
t.color("green")
t.width(4)
t.forward(200)

# Dibujo de la hoja
t.right(90)
t.fillcolor("green")
t.begin_fill()
t.circle(40, 90)
t.left(90)
t.circle(40, 90)
t.end_fill()
t.left(135)
t.forward(30)
t.left(180)
t.forward(30)
t.setheading(90)
t.forward(50)

# Animación de los pétalos de la rosa
t.color("yellow")
t.width(2)

def dibujar_petalo(radio, angulo):
    t.fillcolor("#FFFF00") # Amarillo intenso
    t.begin_fill()
    for _ in range(2):
        t.circle(radio, angulo)
        t.left(180 - angulo)
    t.end_fill()

# Capas de pétalos para dar detalle
posiciones = [
    (10, 100, 150), 
    (10, 80, 100),
    (10, 60, 80)
]

for petalos, radio, angulo in posiciones:
    for _ in range(petalos):
        dibujar_petalo(radio, angulo)
        t.left(360 / petalos)

# Centro de la rosa (Naranja para profundidad)
t.color("#FFD700")
t.penup()
t.goto(-5, 50)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Texto decorativo con animación
t.penup()
t.goto(0, -250)
t.color("yellow")
t.write("Para alguien especial", align="center", font=("Arial", 18, "bold italic"))

t.hideturtle()
screen.mainloop()
