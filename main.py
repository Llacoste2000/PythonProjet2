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

class Raquette:

    def __init__(self):
        pass


tk = Tk()
tk.title("Pong Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=1280, height=720, bg="#000")
canvas.pack()
tk.update()

#ligne du milieu

for i in range(0, 30):
    print(True)
    if(i % 2 == 0):
        pass
    else:
        canvas.create_line(canvas.winfo_width()/2, canvas.winfo_height() * ((5+i)/40), canvas.winfo_width()/2, canvas.winfo_height() * ((5+i)/40) +20, fill="#888", width=2)

#lignes but

canvas.create_line(0, 0, 0, canvas.winfo_height(), width=20, fill="#AAA")
canvas.create_line(canvas.winfo_width(), 0, canvas.winfo_width(), canvas.winfo_height(), width=20, fill="#AAA")



ball = Ball(tk, "#fff")

ball.x = 3
ball.y = 3

while True:

    #BALLE ET COLLISION MURS

    if(ball.position()[0] <= 0 or ball.position()[2] >= ball.field["width"]):
        ball.x *= -1

    if (ball.position()[1] <= 0 or ball.position()[3] >= ball.field["height"]):
        ball.y *= -1





    ball.draw()
    tk.update()
    time.sleep(0.01)