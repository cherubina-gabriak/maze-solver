from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_wall = Line(Point(x1, y1), Point(x2, y1))
        self._draw_wall(top_wall, self.has_top_wall)

        right_wall = Line(Point(x2, y1), Point(x2, y2))
        self._draw_wall(right_wall, self.has_right_wall)

        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        self._draw_wall(bottom_wall, self.has_bottom_wall)

        left_wall = Line(Point(x1, y1), Point(x1, y2))
        self._draw_wall(left_wall, self.has_left_wall)

    def _draw_wall(self, wall, has_wall):
        if self._win is None:
            return
        if has_wall:
            self._win.draw_line(wall)
        else: 
            self._win.draw_line(wall, "white")
            
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        half_center = abs(self._x2 - self._x1) // 2
        start_y =  half_center + self._y1 
        start_x =  half_center + self._x1 

        half_center2 = abs(to_cell._x2 - to_cell._x1) // 2
        end_y = half_center2 + to_cell._y1  
        end_x = half_center2 + to_cell._x1 

        color = "red"
        if undo:
            color = "gray"

        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(line, color)

    def __repr__(self):
        return f"Cell (x1: {self._x1}, y1: {self._y1}, x2: {self._x2}, y2: {self._y2})"
