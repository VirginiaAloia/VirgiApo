from tkinter import *
from tkinter import ttk


def button_press():
        global color_change
        color_change +=1
        color_1["background"] = lista_colori[color_change % len(lista_colori)]

root = Tk()
root.title("Selettore colore")

root.minsize(500, 300)

frame = ttk.Frame(root, borderwidth=5,relief="ridge")

frame.grid(column=0, row=0, sticky=(N,S,W,E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

color_change = 0
lista_colori = ["red", "blue", "yellow"]

color_1 = ttk.Label(frame, text="color", anchor=CENTER, background=lista_colori[color_change])

button_1 = ttk.Button(frame, text="Switch color", command=button_press)

color_1.grid(column=0, row=0, sticky=(N,S,W,E))
button_1.grid(column=0, row=1, sticky=(N,S,W,E))

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)

root.mainloop()