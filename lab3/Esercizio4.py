from tkinter import *
from tkinter import ttk


def set_increment(*args):
    spin_box["increment"] = float(increment_box.get())


root = Tk()
root.title("Contatore a step")
root.resizable(True,False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0, sticky=(N, S, W, E))

frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

stat_value = 0
increment_value = [1, 2, 4, 8]
value = StringVar(value=stat_value)
increment = StringVar(value=increment_value[0])

val_label = ttk.Label(frame, text="VALUE: ")
val_label.grid(column=0, row=0, sticky=(N, S, W, E))

increment_label = ttk.Label(frame, text="INCREMENT: ")
increment_label.grid(column=0, row=1, sticky=(N, S, W, E))

spin_box = ttk.Spinbox(frame, from_=stat_value, to=100, textvariable=value, increment=increment_value[0], wrap=True)
spin_box.grid(column=1, row=0, sticky=(N, S, W, E))
spin_box.state(["readonly"])

increment_box = ttk.Spinbox(frame, values=increment_value, textvariable=increment, command=set_increment)
increment_box.grid(column=1, row=1, sticky=(N, S, W, E))
increment_box.state(["readonly"])

root.mainloop()
