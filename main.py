from tkinter import *
import tkinter.font as tkFont

class Ball:

    def __init__(self, tk, color):
        self.x = -3
        self.y = -3

        self.field = {"height" : canvas.winfo_height(), "width" : canvas.winfo_width()}

        self.canvas = canvas
        self.form = canvas.create_oval(890, 390, 910, 410, fill = color)
    def draw(self):
        self.canvas.move(self.form, self.x, self.y)

    def position(self):
        position = self.canvas.coords(self.form)
        return position


class Raquette:

    def __init__(self, tk, color, Xpos, width):
        self.up = -(canvas.winfo_height() * (1/16))
        self.down = canvas.winfo_height() * (1/16)
        self.canvas = canvas
        self.field = self.canvas.winfo_height()
        self.form = canvas.create_rectangle(Xpos -5, canvas.winfo_height()/2 - width, Xpos + 5, canvas.winfo_height()/2 + width, fill= color)

    def move(self, yMove):
        self.canvas.move(self.form, 0, yMove)

    def position(self):
        return self.canvas.coords(self.form)

def move_raquette(e):

    if e.keysym == "Up":
        raquette1.move(raquette1.up)
    if e.keysym == "Down":
        raquette1.move(raquette1.down)
    if e.keysym == "a" or e.keysym == "A":
        raquette2.move(raquette2.up)
    if e.keysym == "q" or e.keysym == "Q":
        raquette2.move(raquette2.down)




def draw():

    ball.draw()

    #*****BALLE ET COLLISION MURS*****

    if (ball.position()[0] <= 0 or ball.position()[2] >= ball.field["width"]):
        ball.x *= -1

    if (ball.position()[1] <= 0 or ball.position()[3] >= ball.field["height"]):
        ball.y *= -1

    #*****COLLISION BALLE RAQUETTE*****
    rayon_balle = (ball.position()[2] - ball.position()[0])/2
    #*RAQUETTE GAUCHE*

    if(ball.position()[0] < canvas.winfo_width() * (3/32) and ball.position()[0] > canvas.winfo_width() * (3/32) - 5):

        if(ball.position()[1]+rayon_balle > raquette1.position()[1] and ball.position()[1]+rayon_balle < raquette1.position()[3]):

            print(True)
            ball.x *= -1

    #*RAQUETTE DROITE

    if (ball.position()[2] > canvas.winfo_width() * (29 / 32) and ball.position()[2] < canvas.winfo_width() * (29 / 32) + 5):

        if (ball.position()[3] - rayon_balle > raquette2.position()[1] and ball.position()[1] - rayon_balle < raquette2.position()[3]):

            print(True)
            ball.x *= -1

    #*****RAQUETTES ET MOUVEMENT RAQUETTES*****

    if(raquette1.position()[1] < 0):
        raquette1.move(raquette1.position()[1] * -1)

    if(raquette1.position()[3] > canvas.winfo_height()):
        raquette1.move((raquette1.position()[3] - canvas.winfo_height())*-1)

    if (raquette2.position()[1] < 0):
        raquette2.move(raquette2.position()[1] * -1)

    if (raquette2.position()[3] > canvas.winfo_height()):
        raquette2.move((raquette2.position()[3] - canvas.winfo_height()) * -1)

    #*****POINTS*****

    #*AFFICHAGE DES POINTS*
    score_droite = 0
    score_gauche = 0

    font = tkFont.Font(family="FixedSys", size=80, weight="bold", slant="roman")
    canvas.create_text(canvas.winfo_width()*(3/8), canvas.winfo_height()*(1/8),font=font, fill="white", text=score_gauche)

    canvas.create_text(canvas.winfo_width()*(5/8), canvas.winfo_height()*(1/8),font=font, fill="white", text=score_droite)

    tk.after(10, draw)

#*****PRESSETS FENETRE TK*****

tk = Tk()
tk.title("Pong Game")
tk.resizable(0, 0)
canvas = Canvas(tk, width=1280, height=720, bg="#000")
canvas.pack()
tk.update()


#*****LIGNE MILIEU*****

for i in range(0, 30):
    if(i % 2 == 0):
        pass
    else:
        canvas.create_line(canvas.winfo_width()/2, canvas.winfo_height() * ((5+i)/40), canvas.winfo_width()/2, canvas.winfo_height() * ((5+i)/40) +20, fill="#888", width=2)

#*LIGNES DE BUT

canvas.create_line(0, 0, 0, canvas.winfo_height(), width=20, fill="#AAA")
canvas.create_line(canvas.winfo_width(), 0, canvas.winfo_width(), canvas.winfo_height(), width=20, fill="#AAA")

#*****LIGNES TERRAIN JOUEURS

canvas.create_line(canvas.winfo_width() * (3/32), 0, canvas.winfo_width() * (3/32), canvas.winfo_height(), fill="white")
canvas.create_line(canvas.winfo_width() * (29/32), 0, canvas.winfo_width() * (29/32), canvas.winfo_height(), fill="white")

#*****DESSIN BALLE*****
ball = Ball(tk, "#fff")

#*****DESSIN RAQUETTES JOUEURS*****

raquette1 = Raquette(tk, "#fff", canvas.winfo_width() * (3/32), canvas.winfo_height() * (1/16))

#*AJOUT DES CONTROLES DES RAQUETTES
tk.bind_all("<Key>", move_raquette)

raquette2 = Raquette(tk, "#fff", canvas.winfo_width() * (29/32), canvas.winfo_height() * (1/16))

#*FRAME*
draw()

tk.mainloop()