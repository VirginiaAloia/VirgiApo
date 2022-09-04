from tkinter import *
from tkinter import ttk


def change_color():
    color_l["background"] = color.get()


root = Tk()
root.title("prova")

root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0,  sticky=(N,S,W,E))
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)


color = StringVar(value="red")
color_l = ttk.Label(frame, text="Color", anchor=CENTER, background=color.get())
r = ttk.Radiobutton(frame, text='Rosso', variable=color, value='red', command=change_color)
y = ttk.Radiobutton(frame, text='Giallo', variable=color, value='yellow', command=change_color)
b = ttk.Radiobutton(frame, text='Blu', variable=color, value='blue', command=change_color)

color_l.grid(column=0, row=0, rowspan=3, sticky=(N,S,W,E))
r.grid(column=1, row=0)
y.grid(column=1, row=1)
b.grid(column=1, row=2)


root.mainloop()
