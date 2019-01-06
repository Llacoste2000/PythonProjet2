from tkinter import *
import tkinter.font as tkFont
import pickle

with open('score.pkl', 'rb') as openScoreFile:
    time, score_droite, score_gauche, winner = pickle.load(openScoreFile)


def run():

    global final
    global time

    final = Tk()
    final.title("Pong Game : Menu")
    final.resizable(0, 0)
    canvas = Canvas(final, width=1280, height=720, bg="#000")

    font = tkFont.Font(family="FixedSys", size=80, weight="bold", slant="roman")

    canvas.create_text(1280/2, 720 * (1/4), font=font, text="Gagnant : joueur "+str(winner), fill="#fff")

    canvas.create_text(1280*(1/3), 720 * (2 / 4), font=font, text=str(score_gauche), fill="#fff")
    canvas.create_text(1280 * (2 / 3), 720 * (2 / 4), font=font, text=str(score_droite), fill="#fff")

    minute = 0

    while(time >= 60):

        time = time - 60
        minute += 1



    canvas.create_text(1280 / 2, 720* (3/4), font=font, text=str(minute)+"\""+str(time)+"'", fill="#fff")

    canvas.pack()

    final.update()

    final.mainloop()