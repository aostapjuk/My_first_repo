from graphics import *
from time import sleep
win_width = 600
win_height = 500

x, y = win_width//2, win_height//2
r = 20
dx, dy = 1, 1
win = GraphWin('Animation', win_width, win_height)
ball = Circle(Point(x, y), r)
ball.setFill('green')
ball.draw(win)
while True:
    x += dx
    y += dy
    ball.move(dx, dy)
    ball.setFill(color_rgb(x%256, y%256, 100))
    if x + r > win_width or x - r < 0:
        dx = -dx
    if y + r > win_height or y - r < 0:
        dy = -dy
    sleep(0.01)
