import tkinter


def hello():
    print('Left click')


def by(event):
    print('Good by!')


root = tkinter.Tk()
button1 = tkinter.Button(master=root, text='Click me!')
button1.pack()
button1["command"] = hello
root.bind("<Button-3>", by)
root.mainloop()
