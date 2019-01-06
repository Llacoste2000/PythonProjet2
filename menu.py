from tkinter import *
import tkinter.font as tkFont
import game
import param

pointerJouer = True
pointerParam = False

tk, canvas = None, None

def move_menu(e):

    global pointerJouer
    global pointerParam

    if e.keysym == "Up":
        pointerJouer = True
        pointerParam = False
    if e.keysym == "Down":
        pointerJouer = False
        pointerParam = True

    if e.keysym == "Return":

        if pointerJouer:
            tk.destroy()
            game.run()
        else:
            tk.destroy()
            param.run()

def menu():

    global canvas
    global tk

    # *POLICES ECRITURE*
    fontJouer = tkFont.Font(family="FixedSys", size=80, weight="bold", slant="roman")

    fontParam = tkFont.Font(family="FixedSys", size=40, weight="bold", slant="roman")

    if (pointerJouer):

        canvas.create_rectangle(0, canvas.winfo_height() * (3 / 4) - 25, canvas.winfo_width(), canvas.winfo_height() * (3 / 4) + 25, fill="#000")

        canvas.create_rectangle(0, canvas.winfo_height() / 2 - 40, canvas.winfo_width(), canvas.winfo_height() / 2 + 40, fill="#fff")

        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=fontJouer, fill="#000", text="JOUER")

        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * (3 / 4), font=fontParam, fill="#fff", text="PARAMETRES")

    if (pointerParam):

        canvas.create_rectangle(0, canvas.winfo_height() / 2 - 40, canvas.winfo_width(), canvas.winfo_height() / 2 + 40, fill="#000")

        canvas.create_rectangle(0, canvas.winfo_height() * (3 / 4) - 25, canvas.winfo_width(), canvas.winfo_height() * (3 / 4) + 25, fill="#fff")

        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=fontJouer, fill="#fff", text="JOUER")

        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * (3 / 4), font=fontParam, fill="#000", text="PARAMETRES")

    tk.after(34, menu)

def run():

    global tk
    global canvas

    tk = Tk()
    tk.bind_all("<Key>", move_menu)
    tk.title("Pong Game : Menu")
    tk.resizable(0, 0)
    canvas = Canvas(tk, width=1280, height=720, bg="#000")
    canvas.pack()
    tk.update()

    menu()

    tk.mainloop()