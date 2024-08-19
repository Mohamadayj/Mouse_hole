from tkinter import *
from tkinter.ttk import *
import random
from functions import *
import time
import threading

options = ["self", "left", "right", "front", "host"]

window = Tk()
window.title("Mouse in Hole")
# window.attributes('-fullscreen', True)
window.state('zoomed')

x = IntVar()
score = 0
percent = StringVar()
list_radio = []
response = []


def choice():
    print(f"x.get: {x.get()}")
    return x.get()


def new_game():
    global score

    turn_choice = random.choice(options)
    index_of_random = options.index(turn_choice)
    print(f"index of random: {index_of_random}")

    label_turn = Label(window, text=turn_choice, font=("Arial", 20), fg="yellow", bg="black",
                       padx=20, pady=20, relief=RAISED, width=15, height=2)
    label_turn.grid(row=0, column=0)
    label_turn.update()

    for index in range(len(options)):
        radiobutton = Radiobutton(window, text=options[index], variable=x, value=index, command=choice,
                                  padx=10, font=("Impact", 15), indicatoron=True, width=15)
        radiobutton.grid()
        radiobutton.update()
        list_radio.append(radiobutton)

    def destruction():
        label_turn.destroy()
        response.clear()
        for i in list_radio:
            i.destroy()

    timer = threading.Timer(2, destruction)
    timer.start()

    score = 0
    if index_of_random == x.get():
        score += 1

    print(f"score: {score}")

    return score


new_window_button = Button(window, text="New Game", font=("Comic Sans", 15), fg="red", bg="black",
                     activebackground="black", activeforeground="red", command=new_game,
                           height=2, width=14)
new_window_button.grid(row=1, column=0, sticky="NSEW")
#new_window_button.grid_rowconfigure()

label_score = Label(window, text=f"Score: {score}", fg="red", bg="black", font=("Comic Sans", 15),
                    height=2, width=14)
label_score.grid(row=2, column=0)
label_score.update()

bar = Progressbar(window, orient=HORIZONTAL, length=140)
bar["value"] += score * 10
bar.grid(row=3, column=0)

bar_label = Label(window, textvariable=percent)
percent.set("Progress: " + str(int(bar["value"])) + "%")
bar_label.grid(row=4, column=0)


window.mainloop()
