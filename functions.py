from tkinter import *


def choice(event):
    mouse = str(event.x) + str(event.y)
    print(mouse)


def self():
    print("You chose self")
    click = "self"
    return click


def left():
    print("You chose left")
    click = "left"
    return click


def right():
    print("You chose right")
    click = "right"
    return click


def front():
    print("You chose front")
    click = "front"
    return click


def host():
    print("You chose host")
    click = "host"
    return click


