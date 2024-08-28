import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import threading
from PIL import ImageTk, Image
from tkinter import messagebox
from moviepy.editor import VideoFileClip

window = tk.Tk()
window.title("Mouse in Hole")
window.attributes('-fullscreen', True)

main_frame = tk.Frame(window, width=600, height=800)
main_frame.pack(expand=True, anchor=CENTER)

options = ["self", "left", "right", "front", "host"]

image_files = ["hosen png.png", "nima png.png", "moein png.png", "ahmad png.png",
               "hosen 2 png.png", "iman 2 png.png", "mmd 2 png.png", "sadegh2 png.png"]

images = {}
x = tk.IntVar()
percent = tk.StringVar()

WIDTH = 1360
HEIGHT = 768
score = 0
played = 0

xVel = 0.08
yVel = 0.2
size_x = 600
size_y = 600
size_vidx = 400
size_vidy= 400

item_width = 40
item_height = 1
item_padx = 10
item_pady = 5
item_fg = "black"
item_bg = "lightblue"

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


def help_command():

    help_window = tk.Toplevel()
    help_window.attributes('-fullscreen', True)
    help_window.title("Help Window")

    help_frame = tk.Frame(help_window, width=600, height=800)
    help_frame.pack(expand=True, anchor=CENTER)

    help_label1 = tk.Label(help_frame, text="Each 5 Percent provides you with a new prize",
                           font=("Arial", 30), width=item_width, height=item_height,
                           bg=item_bg, fg=item_fg)
    help_label1.pack(padx=item_padx, pady=item_pady)

    help_label2 = tk.Label(help_frame, text="Score 50 awards the ultimate prize",
                           font=("Arial", 30), width=item_width, height=item_height,
                           bg=item_bg, fg=item_fg)
    help_label2.pack(padx=item_padx, pady=item_pady)

    back_button = tk.Button(help_window, text="Back Button", bg=item_bg, fg=item_fg,
                            font=("Comic Sans", 15), activebackground=item_bg,
                            activeforeground=item_fg, relief=RAISED,
                            width=item_width, height=item_height,
                            command=lambda: help_window.destroy())
    back_button.pack(side="bottom", padx=item_padx, pady=item_pady)


def new_game():

    global index_of_random, played
    list_radio = []

    def disable_radio_buttons():
        for rb in list_radio:
            rb.config(state=tk.DISABLED)

    def enable_radio_buttons():
        for rb in list_radio:
            rb.config(state=tk.NORMAL)

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
        elif score > 40:
            bar["value"] = 100

        percent.set("Progress: " + str(float(bar["value"])) + "%")

        disable_radio_buttons()

    enable_radio_buttons()

    played += 1

    label_played.config(text=f"Times Played: {played}")

    turn_choice = random.choice(options)
    index_of_random = options.index(turn_choice)

    for game in range(1):
        game = tk.Toplevel()
        game.title("New Game")
        game.geometry(f"{size_x}x{size_y}")

        frame_game = tk.Frame(game, width=size_x, height=size_y)
        frame_game.pack()

        label_turn = tk.Label(frame_game, text=turn_choice, font=("Arial", 20),
                              fg=item_fg, bg=item_bg, relief=tk.RAISED,
                              width=item_width, height=item_height)
        label_turn.grid(row=0, column=0, padx=item_padx, pady=item_pady)
        label_turn.update()
        # PAD X,Y = 20

        for index in range(len(options)):

            radiobutton = tk.Radiobutton(frame_game, text=options[index], variable=x, value=index,
                                         command=choice, font=("Impact", 15), indicatoron=True,
                                         width=item_width, height=item_height)
            radiobutton.grid(padx=item_padx, pady=item_pady)
            radiobutton.update()
            list_radio.append(radiobutton)

    def destruction():
        game.destroy()

    timer = threading.Timer(2, destruction)
    timer.start()


new_window_button = tk.Button(main_frame, text="New Game", fg=item_fg, bg=item_bg,
                              font=("Comic Sans", 15), command=new_game,
                              activebackground=item_bg, activeforeground=item_fg,
                              height=item_height, width=item_width, relief=RAISED)
new_window_button.grid(row=4, column=0, sticky="NSEW", padx=item_padx, pady=item_pady)

label_played = tk.Label(main_frame, text=f"Times Played: {played}", fg="blue", bg=item_bg,
                        font=("Comic Sans", 15), height=item_height, width=item_width)
label_played.grid(row=3, column=0, padx=item_padx, pady=item_pady)

label_score = tk.Label(main_frame, text=f"Score: {score}", fg="blue", bg=item_bg,
                       font=("Comic Sans", 15), height=item_height, width=item_width)
label_score.grid(row=2, column=0, padx=item_padx, pady=item_pady)

bar = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=450)
bar.grid(row=0, column=0, padx=item_padx, pady=item_pady)

bar_label = tk.Label(main_frame, textvariable=percent, text="Progress: ")
bar_label.grid(row=1, column=0)


def check_command():

    bar_value = score * 2.5

    check_window = tk.Toplevel()
    check_window.attributes('-fullscreen', True)
    check_window.title("Check Prize Window")

    check_frame = tk.Frame(check_window, width=1000, height=100)
    check_frame.pack(expand=True, anchor="n")

    canvas_check = tk.Canvas(check_window, width=WIDTH, height=HEIGHT)
    canvas_check.pack()

    class VideoPlayer(tk.Label):
        def __init__(self, master, path, size=(size_vidx, size_vidy), delay=10):
            tk.Label.__init__(self, master)
            self.delay = delay
            self.clip = VideoFileClip(path).resize(size)
            self.frames = [ImageTk.PhotoImage(Image.fromarray(frame))
                           for frame in self.clip.iter_frames()]
            self.index = 0
            self.update_frame()

        def update_frame(self):
            if self.frames:
                self.config(image=self.frames[self.index])
                self.index = (self.index + 1) % len(self.frames)
                self.after(self.delay, self.update_frame)

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

    def open_prize():

        if score < 49:
            messagebox.showerror("ERROR", "Please Score 50 for the prize")
            return None

        else:

            last_window = tk.Toplevel()
            last_window.title("Hooray")
            last_window.attributes('-fullscreen', True)

            video_label = VideoPlayer(last_window, "vid_hosen.mp4", size=(size_vidx, size_vidy))
            video_label.pack()

            def last_destruction():
                last_window.destroy()
                check_window.destroy()

            timer = threading.Timer(10, last_destruction)
            timer.start()

    if score < 1:
        label_check = tk.Label(check_frame, text="Score 5 for the first prize",
                               font=("Comic Sans", 30), fg=item_fg, bg=item_bg,
                               height=item_height, width=item_width, anchor="center")
        label_check.grid(row=1, column=0, padx=item_padx, pady=item_pady, columnspan=2)

    elif score >= 1:

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

    back_button = tk.Button(check_frame, text="Back Button", bg=item_bg, fg=item_fg,
                            font=("Comic Sans", 15), activebackground=item_bg,
                            activeforeground=item_fg, command=back_command,
                            height=item_height, width=item_width, relief=RAISED)
    back_button.grid(row=0, column=0, padx=item_padx, pady=item_pady)

    last_button = tk.Button(check_frame, text="OPEN PRIZE", bg=item_bg, fg=item_fg,
                            font=("Comic Sans", 15), activebackground=item_bg,
                            activeforeground=item_fg, command=open_prize,
                            height=item_height, width=item_width, relief=RAISED)
    last_button.grid(row=0, column=1, padx=item_padx, pady=item_pady)


button_check = tk.Button(main_frame, text="Check Prize", fg=item_fg, bg=item_bg, font=("Comic Sans", 15),
                         activebackground=item_bg, activeforeground=item_fg, command=check_command,
                         height=item_height, width=item_width, relief=RAISED)
button_check.grid(row=5, column=0, padx=item_padx, pady=item_pady)

button_help = tk.Button(main_frame, text="Help Button", fg=item_fg, bg=item_bg, font=("Comic Sans", 15),
                        activebackground=item_bg, activeforeground=item_fg, command=help_command,
                        height=item_height, width=item_width, relief=RAISED)
button_help.grid(row=6, column=0, padx=item_padx, pady=item_pady)

button_quit = tk.Button(main_frame, text="Quit", fg=item_fg, bg=item_bg, font=("Comic Sans", 15),
                        activebackground=item_bg, activeforeground=item_fg, command=ask_quit,
                        height=item_height, width=item_width, relief=RAISED)
button_quit.grid(row=7, column=0, padx=item_padx, pady=item_pady)


window.mainloop()
