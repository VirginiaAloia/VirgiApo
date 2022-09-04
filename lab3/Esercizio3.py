from tkinter import *
from tkinter import ttk

FILE = "./data/sabato.txt"
USE_LISTBOX = True



def text_visual(frame, poesia):

    text_box = Text(frame)
    text_box.grid(column=0, row=0, sticky=(N, S, W, E))
    for line in poesia:
        text_box.insert(END, line + "\n")

    scroll_bar = ttk.Scrollbar(frame, orient=VERTICAL, command=text_box.yview)
    scroll_bar.grid(column=1, row=0, sticky=(N, S, W, E))

    text_box['yscrollcommand'] = scroll_bar.set


def listbox_version(frame, poesia):

    text = StringVar(value=poesia)

    lst_box = Listbox(frame, listvariable=text, height=10)
    lst_box.grid(column=0, row=0, sticky=(N, S, W, E))

    scroll_bar = ttk.Scrollbar(frame, orient=VERTICAL, command=lst_box.yview)
    scroll_bar.grid(column=1, row=0, sticky=(N, S, W, E))

    lst_box['yscrollcommand'] = scroll_bar.set


poesia = []

with open(FILE, "r") as file:
    for line in file:
        poesia.append(line.strip())


root = Tk()
root.title("Sabato")
frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0, sticky=(N, S, W, E))

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


if USE_LISTBOX:
    listbox_version(frame, poesia)
else:
    text_visual(frame, poesia)

root.mainloop()
