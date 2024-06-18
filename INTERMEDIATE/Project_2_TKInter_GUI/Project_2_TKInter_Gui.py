import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial, 24"))
my_label.pack(side="left")

import turtle

tim = turtle.Turtle()
tim.write("Some Text")



window.mainloop()