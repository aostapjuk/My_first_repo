from tkinter import *

oval_id = None

def create_ball():
    global oval_id
    if oval_id is None:
        oval_id = c.create_oval(10, 10, 100, 100, fill='red')
    else:
        print('ПРЕДУПРЕЖДЕНИЕ! Овал уже создан. Не надо нажимать эту кнопку!')


def delete_ball():
    global oval_id
    c.delete(oval_id)
    oval_id = None


def click_handler(event):
    print(event.x, event.y)
    if oval_id:
        c.coords(oval_id, event.x-5, event.y-5, event.x+5, event.y+5)


root = Tk('Главное окно')
root.geometry('640x480')
buttons_panel = Frame()
buttons_panel.pack(side=TOP, anchor='nw')
button_start = Button(buttons_panel, text='Start', command=create_ball)
button_start.pack(side=LEFT)
button_stop = Button(buttons_panel, text='Stop', command=delete_ball)
button_stop.pack(side=LEFT)

c = Canvas(root, width=640, height=400, bg='white')
c.pack(fill=BOTH, expand=1)
c.bind('<Button>', click_handler)

root.mainloop()
