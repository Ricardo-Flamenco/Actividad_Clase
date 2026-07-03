import tkinter as tk
import random

ANCHO = 400
ALTO = 400
TAM = 20

ventana = tk.Tk()
ventana.title("Snake")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

gusano = [(100,100)]
direccion = "Right"

comida = (
    random.randrange(0, ANCHO, TAM),
    random.randrange(0, ALTO, TAM)
)

def dibujar():
    canvas.delete("all")

    canvas.create_rectangle(
        comida[0], comida[1],
        comida[0]+TAM, comida[1]+TAM,
        fill="red"
    )

    for x,y in gusano:
        canvas.create_rectangle(
            x,y,x+TAM,y+TAM,
            fill="lime"
        )

def mover():
    global comida

    x,y = gusano[0]

    if direccion=="Right":
        x += TAM
    elif direccion=="Left":
        x -= TAM
    elif direccion=="Up":
        y -= TAM
    elif direccion=="Down":
        y += TAM

    if x<0 or x>=ANCHO or y<0 or y>=ALTO:
        canvas.create_text(
            200,200,
            text="GAME OVER",
            fill="white",
            font=("Arial",20)
        )
        return

    gusano.insert(0,(x,y))

    if (x,y)==comida:
        comida=(
            random.randrange(0,ANCHO,TAM),
            random.randrange(0,ALTO,TAM)
        )
    else:
        gusano.pop()

    dibujar()
    ventana.after(400,mover)

def tecla(event):
    global direccion

    if event.keysym=="Right":
        direccion="Right"
    elif event.keysym=="Left":
        direccion="Left"
    elif event.keysym=="Up":
        direccion="Up"
    elif event.keysym=="Down":
        direccion="Down"

ventana.bind("<Key>",tecla)

dibujar()
mover()

ventana.mainloop()