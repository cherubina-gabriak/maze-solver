from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)

    Maze(0, 0, 10, 12, 50, 50, win)

    win.wait_for_close()

main()
