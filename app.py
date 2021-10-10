from tkinter import *
import tkinter as tk
import hands

app = Tk(className="Handy app")
app.geometry("600x700")
x = 400


def test():
    hands.main(1, "sound")


def mouse():
    hands.main(2, "mouse")


def calculator():
    hands.main(1, "calculator")


def frame0():
    fram0 = tk.Frame(app, width=600, height=100, relief=SUNKEN, bd=10)
    tk.Label(fram0, text="The Handy app", font=('Helvetica', 20, 'bold')).place(x=200)
    tk.Label(fram0,
             text="Welkom bij deze app je kan hier verschillende functies met je hand bekijken als je niet weet hoe het werkt").place(
        y=40, x=0)
    tk.Label(fram0, text="kan je op de tutorial klikken").place(y=60, x=0)
    fram0.grid(row=0, column=0)


def frame1():
    fram1 = tk.Frame(app, width=600, height=200, relief=SUNKEN, bd=10, bg='#3b74d1')
    tk.Label(fram1, text="Mouse", font=('Helvetica', 20, 'bold'), bg='#3b74d1').place(x=0)
    tk.Button(fram1, text="Move mouse", command=mouse, width=20).place(x=x, y=10)
    tk.Button(fram1, text="Tutorial", command="tutorialMouse", width=20).place(x=x, y=50)
    fram1.grid(row=1, column=0)


def frame2():
    fram2 = tk.Frame(app, width=600, height=200, relief=SUNKEN, bd=10, bg='#3b74d1')
    tk.Label(fram2, text="Sound", font=('Helvetica', 20, 'bold'), bg='#3b74d1').place(x=0)
    tk.Button(fram2, text="Use sound", command=test, width=20).place(x=x, y=10)
    tk.Button(fram2, text="Tutorial", command="tutorialSound", width=20).place(x=x, y=50)
    fram2.grid(row=2, column=0)


def frame3():
    fram3 = tk.Frame(app, width=600, height=200, relief=SUNKEN, bd=10, bg='#3b74d1')
    tk.Label(fram3, text="Count", font=('Helvetica', 20, 'bold'), bg='#3b74d1').place(x=0)
    tk.Button(fram3, text="Count", command=calculator, width=20).place(x=x, y=10)
    fram3.grid(row=3, column=0)


frame0()
frame1()
frame2()
frame3()

app.mainloop()
