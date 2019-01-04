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
        position = self.canvas.coords(self.form)


tk = Tk()
tk.title("Pong Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=1280, height=720, bg="#000")
canvas.pack()
tk.update()

ball = Ball(tk, "#fff")

ball.x = 3
ball.y = 3

while True:

    ball.draw()

    print(ball.x, ball.field["height"])
    print(ball.y, ball.field["width"])

    if(ball. > ball.field["height"]):
        ball.x = ball.x * -1

    if(ball.y > ball.field["width"]):
        ball.y = ball.y * -1



    tk.update()
    time.sleep(0.001)