from tkinter import *
import tkinter as tk
import hands
import os


app = Tk(className="Handy app")
app.geometry("600x700")
app.resizable(0, 0)
x = 400


def sound():
    hands.main(1, "sound")


def canvas():
    def myFunction(event):
        x, y = event.x, event.y
        if canvas.old_coords:
            x1, y1 = canvas.old_coords
            canvas.create_line(x, y, x1, y1)
        canvas.old_coords = x, y

    top = Toplevel()
    top.title('Canvas')
    canvas = tk.Canvas(top, bg="white", height=300, width=500)
    canvas.pack()
    canvas.old_coords = None
    top.bind('<Motion>', myFunction)


def mouse():
    hands.main(1, "mouse")


def count():
    hands.main(1, "count")


def tutorialSound():
    os.startfile('video\\volume.mp4')


def tutorialMouse():
    os.startfile('video\\mouse.mp4')


def tutorialCount():
    os.startfile('video\\count.mp4')


def frame0():
    fram0 = tk.Frame(app, width=600, height=100, relief=SUNKEN, bd=10)
    tk.Label(fram0, text="The Handy app", font=('Helvetica', 20, 'bold')).place(x=200)
    tk.Label(fram0,
             text="Welkom bij deze app je kan hier verschillende functies met je hand bekijken als je niet weet hoe het werkt").place(
        y=40, x=0)
    tk.Label(fram0, text="kan je op de tutorial klikken. Om een programma uit te gaan klik q").place(y=60, x=0)
    fram0.grid(row=0, column=0)


def frame1():
    fram1 = tk.Frame(app, width=600, height=200, relief=SUNKEN, bd=10, bg="#db16b1")
    tk.Label(fram1, text="Mouse", font=('Helvetica', 20, 'bold'), bg='#db16b1').place(x=0)
    tk.Button(fram1, text="Move mouse", command=mouse, width=20).place(x=x, y=10)
    tk.Button(fram1, text="Open Canvas", command=canvas, width=20).place(x=x, y=50)
    tk.Button(fram1, text="Tutorial", command=tutorialMouse, width=20).place(x=x, y=90)
    fram1.grid(row=1, column=0)


def frame2():
    fram2 = tk.Frame(app, width=600, height=200, relief=SUNKEN, bd=10, bg='#8afa20')
    tk.Label(fram2, text="Sound", font=('Helvetica', 20, 'bold'), bg='#8afa20').place(x=0)
    tk.Button(fram2, text="Use sound", command=sound, width=20).place(x=x, y=10)
    tk.Button(fram2, text="Tutorial", command=tutorialSound, width=20).place(x=x, y=50)
    fram2.grid(row=2, column=0)


def frame3():
    fram3 = tk.Frame(app, width=600, height=200, relief=SUNKEN, bd=10, bg='#3b74d1')
    tk.Label(fram3, text="Count", font=('Helvetica', 20, 'bold'), bg='#3b74d1').place(x=0)
    tk.Button(fram3, text="Count", command=count, width=20).place(x=x, y=10)
    tk.Button(fram3, text="Tutorial", command=tutorialCount, width=20).place(x=x, y=50)
    fram3.grid(row=3, column=0)


frame0()
frame1()
frame2()
frame3()

app.mainloop()
