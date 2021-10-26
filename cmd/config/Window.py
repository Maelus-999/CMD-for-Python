from tkinter import *
import tkinter as tk

def terminal():
    sys = tk.Tk()
    sys.title("error TND01")

    cmd = Text(sys)
    cmd.insert(INSERT, "Erreur TND01 pour plus d'info merci de regarder le wiki qui est disponible sur le github")
    cmd.pack()



    sys.mainloop()
