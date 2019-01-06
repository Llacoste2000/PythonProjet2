from tkinter import *
import tkinter.font as tkFont
import centre
import pickle

entry_limite_points = None
entry_couleur_raquette_1 = None
entry_couleur_raquette_2 = None
entry_couleur_balle = None
entry_vitesse_balle = None
entry_couleur_background = None

with open('param.pkl', 'rb') as paramFileOpen:
    couleur_balle, couleur_raquette_1, couleur_raquette_2, couleur_background, limite_points, vitesse_balle = pickle.load(paramFileOpen)

param = None


def run():

    global param
    global entry_couleur_background
    global entry_limite_points
    global entry_vitesse_balle, entry_couleur_raquette_2
    global entry_couleur_balle
    global entry_couleur_raquette_1

    param = Tk()
    param.title("Pong Game : Paramètres")
    font = tkFont.Font(family="FixedSys", size=16)

    label_limite_points = Label(param, text="Limite de points :", font=font)
    label_limite_points.grid(column=0, row=0, padx=20, pady=5)

    entry_limite_points = Entry(param, font=font)
    entry_limite_points.insert(END, limite_points)
    entry_limite_points.grid(column=1, row=0, padx=20, pady=5)

    label_couleur_raquette_1 = Label(param, text="Couleur Raquette 1 (Gauche) Hexa :", font=font)
    label_couleur_raquette_1.grid(column=0, row=1, padx=20, pady=5)

    entry_couleur_raquette_1 = Entry(param, font=font)
    entry_couleur_raquette_1.insert(END, couleur_raquette_1)
    entry_couleur_raquette_1.grid(column=1, row=1, padx=20, pady=5)

    label_couleur_raquette_2 = Label(param, text="Couleur Raquette 2 (Droite) Hexa :", font=font)
    label_couleur_raquette_2.grid(column=0, row=2, padx=20, pady=5)

    entry_couleur_raquette_2 = Entry(param, font=font)
    entry_couleur_raquette_2.insert(END, couleur_raquette_2)
    entry_couleur_raquette_2.grid(column=1, row=2, padx=20, pady=5)

    label_couleur_balle = Label(param, text="Couleur balle Hexa :", font=font)
    label_couleur_balle.grid(column=0, row=3, padx=20, pady=5)

    entry_couleur_balle = Entry(param, font=font)
    entry_couleur_balle.insert(END, couleur_balle)
    entry_couleur_balle.grid(column=1, row=3, padx=20, pady=5)

    label_vitesse_balle = Label(param, text="Vitesse de la balle :", font=font)
    label_vitesse_balle.grid(column=0, row=4, padx=20, pady=5)

    entry_vitesse_balle = Entry(param, font=font)
    entry_vitesse_balle.insert(END, vitesse_balle)
    entry_vitesse_balle.grid(column=1, row=4, padx=20, pady=5)

    label_couleur_backgroud = Label(param, text="Couleur de l'arrière plant", font=font)
    label_couleur_backgroud.grid(column=0, row=5, padx=20, pady=5)

    entry_couleur_background = Entry(param, font=font)
    entry_couleur_background.insert(END, couleur_background)
    entry_couleur_background.grid(column=1, row=5, padx=20, pady=5)

    boutton_valider = Button(text="Valider", font=font, command=enregistrer)
    boutton_valider.grid(column=1, row=6, padx=20, pady=5)

    mainloop()

def enregistrer():


    global param
    global couleur_background
    global couleur_raquette_2
    global couleur_raquette_1
    global couleur_balle
    global vitesse_balle
    global limite_points

    global entry_couleur_background
    global entry_limite_points
    global entry_vitesse_balle,entry_couleur_raquette_2
    global entry_couleur_balle
    global entry_couleur_raquette_1

    couleur_balle = entry_couleur_balle.get()
    couleur_raquette_1 = entry_couleur_raquette_1.get()
    couleur_raquette_2 = entry_couleur_raquette_2.get()
    vitesse_balle = entry_vitesse_balle.get()
    limite_points = entry_limite_points.get()
    couleur_background = entry_couleur_background.get()

    if (couleur_background == "" or couleur_background == None):
        couleur_background = "#000"

    if (couleur_balle == "" or couleur_balle == None):
        couleur_balle = "#fff"

    if (couleur_raquette_1 == "" or entry_couleur_raquette_1 == None):
        couleur_raquette_1 = "#fff"

    if (couleur_raquette_2 == "" or couleur_raquette_2 == None):
        couleur_raquette_2 = "#fff"

    if (vitesse_balle == "" or vitesse_balle == None):
        vitesse_balle = 8

    if (limite_points == "" or limite_points == None):
        limite_points = 10

    with open('param.pkl', 'wb') as paramFile:
        pickle.dump([couleur_balle, couleur_raquette_1, couleur_raquette_2, couleur_background, str(limite_points), str(vitesse_balle)], paramFile)

    param.destroy()
    centre.run_this()