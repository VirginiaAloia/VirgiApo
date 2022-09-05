from tkinter import *
from tkinter import ttk

score_dict = {}


def insert_player():
    if player.get == "":
        return
    try:
        score_dict[player.get().strip()] = float(score.get())
    except ValueError as err:
        return

    score_list = [(score, player) for player, score in score_dict.items()]
    score_list.sort(reverse=True)

    leaderboard_box.delete(0, leaderboard_box.size() - 1)
    for s, p in score_list[:3]:
        leaderboard_box.insert(END, "{}: {}". format(p, s))


root = Tk()
root.title("Classifica giocatori")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)


frame1 = ttk.Frame(root, borderwidth=5, relief="ridge")
frame1.grid(column=0, row=0, sticky=(N, S, W, E))

frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)

frame2 = ttk.Frame(root, borderwidth=5, relief="ridge")
frame2.grid(column=0, row=1, sticky=(N, S, W, E))

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)


player = StringVar()
score = StringVar()

player_list = StringVar()

player_entry = Entry(frame1, textvariable=player)
player_entry.grid(column=1, row=0, sticky=(N, S, W, E))

score_entry = ttk.Entry(frame1, textvariable=score)
score_entry.grid(column=1, row=1, sticky=(N, S, W, E))

player_label = ttk.Label(frame1, text="Nome: ")
player_label.grid(column=0, row=0, sticky=(N, S, W, E))

score_label = ttk.Label(frame1, text="Punteggio: ")
score_label.grid(column=0, row=1, sticky=(N, S, W, E))

insert_button = ttk.Button(frame1, text="Inserisci", command=insert_player)
insert_button.grid(column=2, row=0, rowspan=2, sticky=(N, S, W, E))

leaderboard = StringVar()
leaderboard_box = Listbox(frame2, listvariable=leaderboard, height=3)
leaderboard_box.grid(column=0, row=0, columnspan=3, sticky=(N, S, W, E))

root.mainloop()
