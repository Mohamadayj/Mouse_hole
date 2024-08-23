import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import threading
from PIL import ImageTk, Image
from tkinter import messagebox

window = tk.Tk()
window.title("Mouse in Hole")
# window.attributes('-fullscreen', True)
window.state('zoomed')
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
# print(width, height)

options = ["self", "left", "right", "front", "host"]
list_radio = []
x = tk.IntVar()
percent = tk.StringVar()
score = 0
played = 0

image_hosen = Image.open("hosen 1.ico")
image_hosen = ImageTk.PhotoImage(image_hosen)
WIDTH = 1500
HEIGHT = 1500
xVel = 2
yVel = 2
image_width = image_hosen.width()
image_height = image_hosen.height()


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

    global index_of_random, played

    played += 1

    label_played.config(text=f"Times Played: {played}")

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

label_played = tk.Label(window, text=f"Times Played: {played}", fg="red", bg="black",
                        font=("Comic Sans", 15), height=2, width=14)
label_played.grid(row=2, column=0)

label_score = tk.Label(window, text=f"Score: {score}", fg="red", bg="black", font=("Comic Sans", 15),
                    height=2, width=14)
label_score.grid(row=3, column=0)

bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=340)
bar.grid(row=4, column=0)

bar_label = tk.Label(window, textvariable=percent)
bar_label.grid(row=5, column=0)


def check_command():
    check_window = tk.Toplevel()
    check_window.state('zoomed')
    check_window.title("Check Window")

    frame_check = tk.Frame(check_window, bg="yellow", bd=2, relief="sunken", width=100)
    frame_check.grid(row=0, column=0)

    def back_command():
        user_response = messagebox.askyesno(title="Confirmation",
                                      message="Are you sure you want to go back?")

        if user_response:
            check_window.destroy()

    back_button = tk.Button(frame_check, text="Back Button", bg="black", fg="red",
                            font=("Comic Sans", 15), activebackground="black", activeforeground="red",
                            command=back_command)
    back_button.grid(row=1, column=0)

    canvas_check = tk.Canvas(check_window, width=WIDTH, height=HEIGHT)
    canvas_check.grid(row=2, column=0)

    if score < 1:
        canvas_check.create_text(100, 100, text="Score 10 for the prize",
                                 font=("Comic Sans", 15))

    elif score >= 1:

        imagee = canvas_check.create_image(100, 100, image=image_hosen)

        # def animation():
        #
        #     global xVel, yVel
        #
        #     coordinates = tk.Canvas.coords(imagee)
        #
        #     if (coordinates[0] > (WIDTH - image_width)) or coordinates[0] < 0:
        #         xVel = -xVel
        #     if (coordinates[1] > (HEIGHT - image_height)) or coordinates[1] < 0:
        #         yVel = -yVel
        #
        #     canvas_check.move(image_hosen, xVel, yVel)
        #     check_window.update()
        #     check_window.after(10, animation)
        #
        # animation()

        class Ball:
            def __init__(self, canvas, x, y, xVel, yVel):
                self.canvas = tk.Canvas
                self.image = tk.Canvas.create_image(x, y, image=image_hosen)
                self.xVel = xVel
                self.yVel = yVel

            def move(self):
                coordinates = self.canvas.coords(self.image)
                if (coordinates[2] >= (self.canvas.winfo_width())) or coordinates[0] < 0:
                    self.xVel = -self.xVel
                if (coordinates[3] >= (self.canvas.winfo_height())) or coordinates[1] < 0:
                    self.yVel = -self.yVel
                self.canvas.move(self.image, self.xVel, self.yVel)

        imagee = Ball(imagee, 0, 0, xVel, yVel)
        imagee.move()
        check_window.update()


button_check = tk.Button(window, text="Check Prize", bg="black", fg="red", font=("Comic Sans", 15),
                         activebackground="black", activeforeground="red", command=check_command)
button_check.grid(row=6, column=0)


window.mainloop()
