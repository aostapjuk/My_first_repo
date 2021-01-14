from tkinter import *
from random import randint
import time

oval_id = None
x, y, r = 10, 20, 10
dx, dy = 10, 10
scores = 0


def tick():
    global  x, y, dx, dy
    time_label.after(200, tick)
    time_label['text'] = time.strftime('%H:%M:%S')
    if oval_id is not None:
        x += dx
        y += dy
        if x+r >= 639 or x-r <= 0:
            dx = -dx
        if y+r >= 439 or y-r <= 0:
            dy = -dy
        c.coords(oval_id, x - r, y - r, x + r, y + r)

def start_game():
    global oval_id, scores
    scores = 0
    scores_text["text"] = "Ваши очки: 0"
    if oval_id is None:
        oval_id = c.create_oval(x-r, y-r, x+r, y+r, fill='red')
    else:
        print('ПРЕДУПРЕЖДЕНИЕ! Игра ещё не началась!')


def delete_ball():
    global oval_id
    c.delete(oval_id)
    oval_id = None


def click_handler(event):
    global x, y, r, scores
    if oval_id:
        if (event.x-x) ** 2 + (event.y-y) ** 2 <= r ** 2:
            print('Попал!')
            scores += 1
            scores_text["text"] = "Ваши очки: " + str(scores)
            r = randint(10, 30)
            x = randint(0+r, 639-r)
            y = randint(0+r, 479-r)
            c.coords(oval_id, x-r, y-r, x+r, y+r)
        else:
            print('Не попал!')


root = Tk('Игра "Поймай шарики"')
root.geometry('640x480')

buttons_panel = Frame(root, bg='gray')
buttons_panel.pack(fill=BOTH)
button_start = Button(buttons_panel, text='Start', command=start_game)
button_start.pack(side=LEFT)
button_stop = Button(buttons_panel, text='Stop', command=delete_ball)
button_stop.pack(side=LEFT)

time_label = Label(buttons_panel, font='sans 20')
time_label.pack(side=LEFT)

scores_text = Label(buttons_panel, text='Ваши очки: 0')
scores_text.pack(side=RIGHT)

c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)
c.bind('<Button>', click_handler)

time_label.after_idle(tick)

root.mainloop()
