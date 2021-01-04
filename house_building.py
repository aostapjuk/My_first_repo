from graphics import *

win_width = 600
win_height = 500

def main():
    global win
    win = GraphWin('Picture graphics', win_width, win_height)
    draw_house(win_width//3, win_height*2//3, 150, 200)
    cursor_point = win.getMouse()
    win.close()

def draw_house(x0, y0, width, height):
    ''' Функция рисует дом в положении  на холсте.
        x0, y0 - центральная нижняя точка домика
        width, height - ширина и высота.
    '''
    foundation_height = int(0.1*height)
    walls_height = int(0.5*height)
    walls_width = int(0.9*width)
    roof_height = height - walls_height - foundation_height
    window_height = width//3
    window_width = walls_height//3
    
    draw_foundation(x0, y0, width, foundation_height)
    draw_walls(x0, y0-foundation_height,
               walls_width, walls_height)
    draw_window(x0, y0-foundation_height-walls_height//3,
                window_height, window_width)
    draw_roof(x0, y0-walls_height, width, roof_height)

def draw_foundation(x0, y0, width, height):
    foundation = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    foundation.setWidth(3)
    foundation.setFill('brown')
    foundation.draw(win)
    print('foundation', x0, y0, width, height)

def draw_walls(x0, y0, width, height):
    walls = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    walls.setWidth(3)
    walls.setFill('brown')
    walls.draw(win)
    print('walls', x0, y0, width, height)

def draw_window(x0, y0, width, height):
    pass

def draw_roof(x0, y0, width, height):
    pass

main()
