from tkinter import *
from random import randint
import time

# Режим игры - игра идёт или нет.
game_began = False
'''oval_id = None
x, y, r = 10, 20, 10
dx, dy = 10, 10'''
scores = 0
single_ball = [10, 20, 5, 3, 1, None]
sleep_time = 50     # ms

def tick():
    time_label.after(sleep_time, tick)
    time_label['text'] = time.strftime('%H:%M:%S')
    if game_began:
        ball_step(single_ball)


def button_start_game_handler():
    global game_began
    if not game_began:
        start_game()
        game_began = True


def button_stop_game_handler():
    global game_began
    if game_began:
        stop_game()
        game_began = False


def start_game():
    global single_ball
    ball_create(single_ball)


def stop_game():
    ball_delete(single_ball)


def ball_step(ball):
    """
    Сдвигает шарик ball в соответствии с его скоростью.
    :param ball: это список (x, y, dx, dy, r, oval_id)
    """
    global x, y, dx, dy, r, oval_id
    x, y, dx, dy, r, oval_id = ball
    if oval_id is not None:
        x += dx
        y += dy
        if x+r >= 639 or x-r <= 0:
            dx = -dx
        if y+r >= 439 or y-r <= 0:
            dy = -dy
        c.coords(oval_id, x - r, y - r, x + r, y + r)
    ball[:] = x, y, dx, dy, r, oval_id


def ball_create(ball):
    global scores
    scores = 0
    scores_text["text"] = "Ваши очки: 0"
    x, y, dx, dy, r, oval_id = ball
    if oval_id is None:
        r = randint(10, 30)
        x = randint(0 + r, 639 - r)
        y = randint(0 + r, 479 - r)
        oval_id = c.create_oval(x-r, y-r, x+r, y+r, fill='red')
    ball[:] = x, y, dx, dy, r, oval_id


def ball_delete(ball):
    x, y, dx, dy, r, oval_id = ball
    c.delete(oval_id)
    oval_id = None
    ball[:] = x, y, dx, dy, r, oval_id


root = Tk('Игра "Поймай шарики"')
root.geometry('640x480')

buttons_panel = Frame(root, bg='gray')
buttons_panel.pack(fill=BOTH)
button_start = Button(buttons_panel, text='Start', command=button_start_game_handler)
button_start.pack(side=LEFT)
button_stop = Button(buttons_panel, text='Stop', command=button_stop_game_handler)
button_stop.pack(side=LEFT)

time_label = Label(buttons_panel, font='sans 20')
time_label.pack(side=LEFT)

scores_text = Label(buttons_panel, text='Ваши очки: 0')
scores_text.pack(side=RIGHT)

c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)

time_label.after_idle(tick)
root.mainloop()
