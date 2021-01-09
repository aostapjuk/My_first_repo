from tkinter import *


def create_ball():
    c.create_oval(10, 10, 100, 100, fill='red')


root = Tk('Главное окно')
root.geometry('640x480')

c = Canvas(root, width=640, height=400, bg='white')
c.pack()
button_start = Button(root, text='Start', command=create_ball)
button_start.pack()

root.mainloop()
