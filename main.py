from tkinter import *
import time

class Ball:

    def __init__(self, tk, color):
        self.x = 0
        self.y = 0

        self.field = {"height" : canvas.winfo_height(), "width" : canvas.winfo_width()}

        self.canvas = canvas
        self.form = canvas.create_oval(390, 390, 410, 410, fill = color)
        #self.canvas.move(self.form, 400, 400)
    def draw(self):
        self.canvas.move(self.form, self.x, self.y)

    def position(self):
        position = self.canvas.coords(self.form)
        return position


tk = Tk()
tk.title("Pong Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=1280, height=720, bg="#000")
canvas.pack()
tk.update()

canvas.create_line(canvas.winfo_width()/2, canvas.winfo_height() * (1/10), canvas.winfo_width()/2, canvas.winfo_height() * (9/10), width=2, fill="#fff", dash=(40, 10))

ball = Ball(tk, "#fff")

ball.x = 3
ball.y = 3

while True:

    #BALLE ET COLLISION MURS 

    print(ball.x, ball.field["width"])
    print(ball.y, ball.field["height"])

    print(ball.position())

    if(ball.position()[0] <= 0 or ball.position()[2] >= ball.field["width"]):
        ball.x *= -1

    if (ball.position()[1] <= 0 or ball.position()[3] >= ball.field["height"]):
        ball.y *= -1

    ball.draw()

    tk.update()
    time.sleep(0.01)