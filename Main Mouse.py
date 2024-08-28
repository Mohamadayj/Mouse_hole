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
window.attributes('-fullscreen', True)

options = ["self", "left", "right", "front", "host"]

image_files = ["hosen png.png", "nima png.png", "moein png.png", "ahmad png.png",
               "hosen 2 png.png", "iman 2 png.png", "mmd 2 png.png", "sadegh2 png.png"]

images = {}
list_radio = []
x = tk.IntVar()
percent = tk.StringVar()
score = 0
played = 0

WIDTH = 1360
HEIGHT = 768
xVel = 0.08
yVel = 0.2
size_x = 600
size_y = 600

for file in image_files:
    image = Image.open(file)
    image = image.resize((size_x, size_y), Image.Resampling.LANCZOS)
    images[file] = ImageTk.PhotoImage(image)

image_hosen = images["hosen png.png"]
image_hosen2 = images["hosen 2 png.png"]
image_nima = images["nima png.png"]
image_moein = images["moein png.png"]
image_ahmad = images["ahmad png.png"]
image_iman2 = images["iman 2 png.png"]
image_mmd2 = images["mmd 2 png.png"]
image_sadegh2 = images["sadegh2 png.png"]


def ask_quit():
    pm_quit = messagebox.askyesno(title="Quit", message="Are you sure you want to quit?")
    if pm_quit:
        window.destroy()


def choice():

    global score
    selected_index = x.get()

    if selected_index == index_of_random:
        score += 1
    elif selected_index != -1:
        score -= 1

    label_score.config(text=f"Score: {score}")

    if 0 < score <= 20:
        bar["value"] = score * 2.5
    elif score <= 0:
        bar["value"] = 0
    elif score > 20:
        bar["value"] = 100

    percent.set("Progress: " + str(float(bar["value"])) + "%")


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

        radiobutton = tk.Radiobutton(window, text=options[index], variable=x, value=index,
                                     command=choice, font=("Impact", 15), indicatoron=True, padx=10,
                                     width=15)
        radiobutton.grid(sticky="e")
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
    check_window.attributes('-fullscreen', True)
    check_window.title("Check Window")

    frame_check = tk.Frame(check_window, bg="yellow", bd=2, relief="sunken", width=100)
    frame_check.grid(row=0, column=0)

    canvas_check = tk.Canvas(check_window, width=WIDTH, height=HEIGHT)
    canvas_check.grid(row=2, column=0)

    class Animation:
        def __init__(self, canvas, image, x, y, xVel, yVel):
            self.canvas = canvas
            self.image = self.canvas.create_image(x, y, image=image)
            self.xVel = xVel
            self.yVel = yVel

        def move(self):
            coordinates = self.canvas.coords(self.image)
            if (coordinates[0] >= (self.canvas.winfo_width())) or coordinates[0] < 0:
                self.xVel = -self.xVel
            if (coordinates[1] >= (self.canvas.winfo_height())) or coordinates[1] < 0:
                self.yVel = -self.yVel
            self.canvas.move(self.image, self.xVel, self.yVel)
            self.canvas.after(10, self.move)

    def choose_pic(picture, locx, locy):
        anim = Animation(canvas_check, picture, locx, locy, xVel, yVel)
        anim.move()
        check_window.update()

    if score < 1:
        canvas_check.create_text(100, 100, text="Score 5 for the first prize",
                                 font=("Comic Sans", 15), anchor=W)

    else:
        bar_value = score * 2.5

        tuple_images = [
            (5, 10, image_hosen, 0, 0),
            (10, 15, image_nima, 400, 0),
            (15, 20, image_moein, 800, 0),
            (20, 25, image_sadegh2, 1000, 0),
            (25, 30, image_ahmad, 400, 0),
            (30, 35, image_hosen2, 800, 0),
            (35, 40, image_mmd2, 0, 0),
            (40, 45, image_iman2, 400, 0)
        ]

        for start, end, pic_tup, x, y in tuple_images:
            if start <= bar_value < end:
                choose_pic(pic_tup, x, y)
                break

    def back_command():
        user_response = messagebox.askyesno(title="Confirmation",
                                      message="Are you sure you want to go back?")

        if user_response:
            check_window.destroy()

    back_button = tk.Button(frame_check, text="Back Button", bg="black", fg="red",
                            font=("Comic Sans", 15), activebackground="black", activeforeground="red",
                            command=back_command)
    back_button.grid(row=1, column=0)


button_check = tk.Button(window, text="Check Prize", bg="black", fg="red", font=("Comic Sans", 15),
                         activebackground="black", activeforeground="red", command=check_command)
button_check.grid(row=6, column=0)

button_quit = tk.Button(window, text="Quit", bg="black", fg="red", font=("Comic Sans", 15),
                        activebackground="black", activeforeground="red", command=ask_quit)
button_quit.grid(row=7, column=0)


window.mainloop()
