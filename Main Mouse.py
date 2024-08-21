import tkinter as tk
from tkinter import ttk
import random
import threading
from PIL import ImageTk, Image
from tkinter import messagebox

options = ["self", "left", "right", "front", "host"]

window = tk.Tk()
window.title("Mouse in Hole")
# window.attributes('-fullscreen', True)
window.state('zoomed')

x = tk.IntVar()
percent = tk.StringVar()
list_radio = []
image_hosen = Image.open("hosen 1.ico")
image_hosen = ImageTk.PhotoImage(image_hosen)
score = 0


def choice():
    global score
    selected_index = x.get()

    if selected_index == index_of_random:
        score += 1
    elif selected_index != -1:
        score -= 1

    label_score.config(text=f"Score: {score}")

    if 0 < score <= 10:
        bar["value"] = score * 10
    elif score <= 0:
        bar["value"] = 0
    elif score > 10:
        bar["value"] = 100

    percent.set("Progress: " + str(int(bar["value"])) + "%")


def new_game():
    global index_of_random

    turn_choice = random.choice(options)
    index_of_random = options.index(turn_choice)

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
        for i in list_radio:
            i.destroy()

    timer = threading.Timer(2, destruction)
    timer.start()


new_window_button = tk.Button(window, text="New Game", font=("Comic Sans", 15), fg="red", bg="black",
                     activebackground="black", activeforeground="red", command=new_game,
                           height=2, width=14)
new_window_button.grid(row=1, column=0, sticky="NSEW")
# new_window_button.grid_rowconfigure()

label_score = tk.Label(window, text=f"Score: {score}", fg="red", bg="black", font=("Comic Sans", 15),
                    height=2, width=14)
label_score.grid(row=2, column=0)

bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=340)
bar.grid(row=3, column=0)

bar_label = tk.Label(window, textvariable=percent)
bar_label.grid(row=4, column=0)


def check_command():
    check_window = tk.Toplevel()
    check_window.state('zoomed')

    frame_check = tk.Frame(check_window, bg="yellow", bd=2, relief="sunken", width=100)
    frame_check.grid(row=0, column=0)

    canvas_check = tk.Canvas(check_window)
    canvas_check.create_image(100, 100, image=image_hosen)
    canvas_check.grid(row=10)

    def back_command():
        user_response = messagebox.askyesno(title="Confirmation",
                                      message="Are you sure you want to go back?")

        if user_response:
            check_window.destroy()

    back_button = tk.Button(frame_check, text="Back Button", bg="black", fg="red", font=("Comic Sans", 15),
                            activebackground="black", activeforeground="red", command=back_command)
    back_button.grid(row=1, column=0)


button_check = tk.Button(window, text="Check Button", bg="black", fg="red", font=("Comic Sans", 15),
                         activebackground="black", activeforeground="red", command=check_command)
button_check.grid(row=5, column=0)

window.mainloop()
