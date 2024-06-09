from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(10, 10, 80, 80)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(80, 10, 160, 80)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(10, 80, 80, 160)

    win.wait_for_close()

main()
