from graphics import *

win_width = 600
win_height = 500

def main():
    global win, house_elements
    win = GraphWin('Picture graphics', win_width, win_height)
    house_elements = draw_house(win_width//3, win_height*2//3, 150, 200)
    cursor_point = win.getMouse()
    for elem in house_elements:
        elem.move(50, 0)
    cursor_point = win.getMouse()
    for elem in house_elements:
        elem.move(0, 50)
    cursor_point = win.getMouse()
    win.close()

def draw_house(x0, y0, width, height):
    ''' Функция рисует дом в положении  на холсте.
        x0, y0 - центральная нижняя точка домика
        width, height - ширина и высота.
        return: список нарисованных объектов
    '''
    foundation_height = int(0.1*height)
    walls_height = int(0.5*height)
    walls_width = int(0.9*width)
    roof_height = height - walls_height - foundation_height
    window_height = width//3
    window_width = walls_height//3
    
    foundation = draw_foundation(x0, y0, width, foundation_height)
    walls = draw_walls(x0, y0-foundation_height,
                       walls_width, walls_height)
    house_window = draw_window(x0, y0-foundation_height-walls_height//3,
                               window_height, window_width)
    roof = draw_roof(x0, y0-foundation_height-walls_height, width, roof_height)
    return  foundation + walls + roof + house_window

def draw_foundation(x0, y0, width, height):
    foundation = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    foundation.setWidth(3)
    foundation.setFill('brown')
    foundation.draw(win)
    print('foundation', x0, y0, width, height)
    return [foundation]

def draw_walls(x0, y0, width, height):
    walls = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    walls.setWidth(3)
    walls.setFill('green')
    walls.draw(win)
    print('walls', x0, y0, width, height)
    return [walls]

def draw_window(x0, y0, width, height):
    window = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    window.setWidth(3)
    window.setFill('yellow')
    window.draw(win)
    print('walls', x0, y0, width, height)
    return [window]

def draw_roof(x0, y0, width, height):
    coordinates = [(x0-width//2, y0), (x0, y0-height),
                   (x0+width//2, y0)]
    points = [Point(x, y) for x, y in coordinates]
    roof = Polygon(points)
    roof.setWidth(3)
    roof.setFill('darkred')
    roof.draw(win)
    print('roof', x0, y0, width, height)
    return [roof]

main()
