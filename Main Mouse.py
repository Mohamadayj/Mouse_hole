import tkinter as tk
from tkinter import ttk
import random
import threading

options = ["self", "left", "right", "front", "host"]

window = tk.Tk()
window.title("Mouse in Hole")
# window.attributes('-fullscreen', True)
window.state('zoomed')

x = tk.IntVar()
percent = tk.StringVar()
list_radio = []
response = []


def choice():
    print(f"x.get: {x.get()}")
    return x.get()


def new_game():

    turn_choice = random.choice(options)
    index_of_random = options.index(turn_choice)
    print(f"index of random: {index_of_random}")

    label_turn = tk.Label(window, text=turn_choice, font=("Arial", 20), fg="yellow", bg="black",
                       padx=20, pady=20, relief=tk.RAISED, width=15, height=2)
    label_turn.grid(row=0, column=0)
    label_turn.update()

    for index in range(len(options)):
        radiobutton = tk.Radiobutton(window, text=options[index], variable=x, value=index, command=choice,
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
    answer_list = []

    if x.get():
        print(f"answer: {x.get()}")
        answer_list.append(x.get())
        print(f"answer list: {answer_list}")

        if index_of_random in answer_list:
            score += 1
            print(score)


new_window_button = tk.Button(window, text="New Game", font=("Comic Sans", 15), fg="red", bg="black",
                     activebackground="black", activeforeground="red", command=new_game,
                           height=2, width=14)
new_window_button.grid(row=1, column=0, sticky="NSEW")
# new_window_button.grid_rowconfigure()

label_score = tk.Label(window, text="Score: X", fg="red", bg="black", font=("Comic Sans", 15),
                    height=2, width=14)
label_score.grid(row=2, column=0)
label_score.update()

bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=140)
bar["value"] += 1 * 10
bar.grid(row=3, column=0)

bar_label = tk.Label(window, textvariable=percent)
percent.set("Progress: " + str(int(bar["value"])) + "%")
bar_label.grid(row=4, column=0)


def check_command():
    check_window = tk.Tk()

    def back_command():
        pass

    back_button = tk.Button(check_window, text="Back Button", bg="black", fg="red", font=("Comic Sans", 15),
                            activebackground="black", activeforeground="red", command=back_command)
    back_button.grid(row=1, column=0)


button_check = tk.Button(window, text="Check Button", bg="black", fg="red", font=("Comic Sans", 15),
                         activebackground="black", activeforeground="red", command=check_command)
button_check.grid(row=5, column=0)

window.mainloop()
