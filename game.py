from tkinter import *
import tkinter.font as tkFont
import random
import pickle
import menu
import final

winner = None
temps = 0
points_1 = 0
points_2 = 0

with open('param.pkl', 'rb') as paramFileOpen:
    couleur_balle, couleur_raquette_1, couleur_raquette_2, couleur_background, limite_points, vitesse_balle = pickle.load(paramFileOpen)

limite_score = int(limite_points)

score_droite = 0
score_gauche = 0

game, gamecnv, ball, raquette1, raquette2 = None, None, None, None, None

class Ball:

    def __init__(self, tk, color):
        self.x = int(vitesse_balle)
        self.y = int(vitesse_balle)

        self.field = {"height": gamecnv.winfo_height(), "width": gamecnv.winfo_width()}

        self.form = gamecnv.create_oval(gamecnv.winfo_width() / 2 - 10, gamecnv.winfo_height() / 2 - 10, gamecnv.winfo_width() / 2 + 10, gamecnv.winfo_height() / 2 + 10, fill=color)

    def position(self):
        position = gamecnv.coords(self.form)
        return position

    def setPosition(self, x1, y1, x2, y2, x, y):
        gamecnv.coords(self.form, x1, y1, x2, y2)
        self.x = x
        self.y = y

    def draw(self):
        gamecnv.move(self.form, self.x, self.y)



class Raquette:

    def __init__(self, tk, color, Xpos, width):
        self.canvas = gamecnv
        self.up = -(self.canvas.winfo_height() * (1/16))
        self.down = self.canvas.winfo_height() * (1/16)
        self.field = self.canvas.winfo_height()
        self.form = self.canvas.create_rectangle(Xpos -5, self.canvas.winfo_height()/2 - width, Xpos + 5, self.canvas.winfo_height()/2 + width, fill= color)

    def move(self, yMove):
        self.canvas.move(self.form, 0, yMove)

    def position(self):
        return self.canvas.coords(self.form)

def move_game(e):

    global raquette1
    global raquette2
    global game

    if e.keysym == "Escape":
        game.destroy()
        menu.run()

    if e.keysym == "Up":
        raquette2.move(raquette2.up)
    if e.keysym == "Down":
        raquette2.move(raquette2.down)
    if e.keysym == "a" or e.keysym == "A":
        raquette1.move(raquette1.up)
    if e.keysym == "q" or e.keysym == "Q":
        raquette1.move(raquette1.down)

def draw():

    global limite_score
    global score_droite
    global score_gauche

    global winner
    global temps
    global points_1
    global points_2

    global game
    global gamecnv
    global ball
    global raquette1
    global raquette2

    if (score_gauche == limite_score ):
        game.destroy()
        winner = 1
        save_score()

    if(score_droite == limite_score):
        game.destroy()
        winner = 2
        save_score()

    rayon_balle = (ball.position()[2] - ball.position()[0]) / 2

    #*****BALLE ET COLLISION MURS*****

    #*RE-DESSIN DE TOUTES LES LIGNES*
    #*COLLISION POINTS (MURS BUTS)*
    #*MUR DE GAUCHE*
    if (ball.position()[0] <= 0):
        score_droite += 1

        #*CLEAR DES SCORES*

        gamecnv.create_rectangle(0, gamecnv.winfo_height()*(1/8)-40, gamecnv.winfo_width(), gamecnv.winfo_height()*(1/8)+40, fill=couleur_background, width=0)

        #*RE-DESSIN DES SCORES*
        font = tkFont.Font(family="FixedSys", size=80, weight="bold", slant="roman")
        gamecnv.create_text(gamecnv.winfo_width() * (3 / 8), gamecnv.winfo_height() * (1 / 8), font=font, fill=couleur_raquette_1, text=score_gauche)

        gamecnv.create_text(gamecnv.winfo_width() * (5 / 8), gamecnv.winfo_height() * (1 / 8), font=font, fill=couleur_raquette_2, text=score_droite)

        #*LIGNE MILIEU*

        for i in range(0, 30):

            if (i % 2 == 0):
                pass
            else:
                gamecnv.create_line(gamecnv.winfo_width() / 2, gamecnv.winfo_height() * ((5 + i) / 40), gamecnv.winfo_width() / 2, gamecnv.winfo_height() * ((5 + i) / 40) + 20, fill="#888", width=2)

        #*LIGNES TERRAIN JOUEURS*

        gamecnv.create_line(gamecnv.winfo_width() * (3 / 32), 0, gamecnv.winfo_width() * (3 / 32), gamecnv.winfo_height(), fill="white")
        gamecnv.create_line(gamecnv.winfo_width() * (29 / 32), 0, gamecnv.winfo_width() * (29 / 32), gamecnv.winfo_height(), fill="white")

        #*LIGNES DE BUT*

        gamecnv.create_line(0, 0, 0, gamecnv.winfo_height(), width=20, fill="#AAA")
        gamecnv.create_line(gamecnv.winfo_width(), 0, gamecnv.winfo_width(), gamecnv.winfo_height(), width=20, fill="#AAA")

        angle = random.randint(1, 2)
        if(angle == 1) : angle = -1
        else : angle = 1

        ball.setPosition(gamecnv.winfo_width() / 2 - 10, gamecnv.winfo_height() / 2 - 10, gamecnv.winfo_width() / 2 + 10, gamecnv.winfo_height() / 2 + 10, ball.x, angle * ball.y)

        gamecnv.tag_raise(ball.form)
        gamecnv.tag_raise(raquette2.form)
        gamecnv.tag_raise(raquette1.form)


    if (ball.position()[2] >= ball.field["width"]):
        score_gauche += 1

        # *CLEAR DES SCORES*

        gamecnv.create_rectangle(0, gamecnv.winfo_height() * (1 / 8) - 40, gamecnv.winfo_width(), gamecnv.winfo_height() * (1 / 8) + 40, fill=couleur_background, width=0)

        # *RE-DESSIN DES SCORES*
        font = tkFont.Font(family="FixedSys", size=80, weight="bold", slant="roman")
        gamecnv.create_text(gamecnv.winfo_width() * (3 / 8), gamecnv.winfo_height() * (1 / 8), font=font, fill=couleur_raquette_1, text=score_gauche)

        gamecnv.create_text(gamecnv.winfo_width() * (5 / 8), gamecnv.winfo_height() * (1 / 8), font=font, fill=couleur_raquette_2, text=score_droite)

        # *LIGNE MILIEU*

        for i in range(0, 30):

            if (i % 2 == 0):
                pass
            else:
                gamecnv.create_line(gamecnv.winfo_width() / 2, gamecnv.winfo_height() * ((5 + i) / 40),
                                    gamecnv.winfo_width() / 2, gamecnv.winfo_height() * ((5 + i) / 40) + 20,
                                    fill="#888", width=2)

        # *LIGNES TERRAIN JOUEURS*

        gamecnv.create_line(gamecnv.winfo_width() * (3 / 32), 0, gamecnv.winfo_width() * (3 / 32),
                            gamecnv.winfo_height(), fill="white")
        gamecnv.create_line(gamecnv.winfo_width() * (29 / 32), 0, gamecnv.winfo_width() * (29 / 32),
                            gamecnv.winfo_height(), fill="white")

        # *LIGNES DE BUT*

        gamecnv.create_line(0, 0, 0, gamecnv.winfo_height(), width=20, fill="#AAA")
        gamecnv.create_line(gamecnv.winfo_width(), 0, gamecnv.winfo_width(), gamecnv.winfo_height(), width=20,
                            fill="#AAA")

        angle = random.randint(1, 2)
        if (angle == 1):
            angle = -1
        else:
            angle = 1

        ball.setPosition(gamecnv.winfo_width() / 2 - 10, gamecnv.winfo_height() / 2 - 10,
                         gamecnv.winfo_width() / 2 + 10, gamecnv.winfo_height() / 2 + 10, -ball.x, angle * ball.y)

        gamecnv.tag_raise(ball.form)
        gamecnv.tag_raise(raquette2.form)
        gamecnv.tag_raise(raquette1.form)




    #*COLLISION MURS HAUT ET BAS

    if (ball.position()[1] <= 0 or ball.position()[3] >= ball.field["height"]):
        ball.y *= -1


    #*****COLLISION BALLE RAQUETTE*****
    #*RAQUETTE GAUCHE*

    if(ball.position()[0] < gamecnv.winfo_width() * (3/32) and ball.position()[0] > gamecnv.winfo_width() * (3/32) - 15):

        if(ball.position()[1]+rayon_balle > raquette1.position()[1] and ball.position()[1]+rayon_balle < raquette1.position()[3]):
            ball.x *= -1

    #*RAQUETTE DROITE

    if (ball.position()[2] > gamecnv.winfo_width() * (29 / 32) and ball.position()[2] < gamecnv.winfo_width() * (29 / 32) + 15):

        if (ball.position()[3] - rayon_balle > raquette2.position()[1] and ball.position()[1] - rayon_balle < raquette2.position()[3]):
            ball.x *= -1

    #*****RAQUETTES ET MOUVEMENT RAQUETTES*****

    if(raquette1.position()[1] < 0):
        raquette1.move(raquette1.position()[1] * -1)

    if(raquette1.position()[3] > gamecnv.winfo_height()):
        raquette1.move((raquette1.position()[3] - gamecnv.winfo_height())*-1)

    if (raquette2.position()[1] < 0):
        raquette2.move(raquette2.position()[1] * -1)

    if (raquette2.position()[3] > gamecnv.winfo_height()):
        raquette2.move((raquette2.position()[3] - gamecnv.winfo_height()) * -1)

    ball.draw()
    temps += 1
    print(temps)
    game.after(17, draw)

def run():
    global game
    global gamecnv
    global ball
    global raquette1
    global raquette2

    # *****PRESSET FENETRE*****

    game = Tk()
    game.bind_all("<Key>", move_game)
    game.title("Pong Game")
    game.resizable(0, 0)
    gamecnv = Canvas(game, width=1280, height=720, bg=couleur_background)
    print(couleur_background)
    gamecnv.pack()
    game.update()

    # *****LIGNE DU MILIEU*****

    for i in range(0, 30):

        if (i % 2 == 0):
            pass
        else:
            gamecnv.create_line(gamecnv.winfo_width() / 2, gamecnv.winfo_height() * ((5 + i) / 40),
                                gamecnv.winfo_width() / 2, gamecnv.winfo_height() * ((5 + i) / 40) + 20, fill="#888",
                                width=2)

    # *****LIGNES DE BUT*****

    gamecnv.create_line(0, 0, 0, gamecnv.winfo_height(), width=20, fill="#AAA")
    gamecnv.create_line(gamecnv.winfo_width(), 0, gamecnv.winfo_width(), gamecnv.winfo_height(), width=20, fill="#AAA")

    # *****LIGNES TERRAIN JOUEURS

    gamecnv.create_line(gamecnv.winfo_width() * (3 / 32), 0, gamecnv.winfo_width() * (3 / 32), gamecnv.winfo_height(),
                        fill="white")
    gamecnv.create_line(gamecnv.winfo_width() * (29 / 32), 0, gamecnv.winfo_width() * (29 / 32), gamecnv.winfo_height(),
                        fill="white")

    # *****DESSIN BALLE*****

    ball = Ball(game, couleur_balle)

    # *****DESSIN RAQUETTES*****

    raquette1 = Raquette(game, couleur_raquette_1, gamecnv.winfo_width() * (3 / 32), gamecnv.winfo_height() * (1 / 16))
    raquette2 = Raquette(game, couleur_raquette_2, gamecnv.winfo_width() * (29 / 32), gamecnv.winfo_height() * (1 / 16))

    # *****AFFICHAGE POINTS BASE*****
    font = tkFont.Font(family="FixedSys", size=80, weight="bold", slant="roman")
    gamecnv.create_text(gamecnv.winfo_width() * (3 / 8), gamecnv.winfo_height() * (1 / 8), font=font, fill=couleur_raquette_1,
                        text=score_gauche)

    gamecnv.create_text(gamecnv.winfo_width() * (5 / 8), gamecnv.winfo_height() * (1 / 8), font=font, fill=couleur_raquette_2,
                        text=score_droite)

    draw()

    game.mainloop()

def save_score():

    global temps
    global score_gauche
    global score_droite
    global winner
    global game

    time = round(temps * 0.034, 2)


    with open('score.pkl', 'wb') as scoreFile:
        pickle.dump([time, score_droite, score_gauche, winner], scoreFile)

    with open('score.pkl', 'rb') as openScoreFile:
        print(pickle.load(openScoreFile))

    final.run()
    game.destroy()