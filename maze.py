import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_wall_r(0, 0)
        
    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        
        x1 = self._x1 + (j * self._cell_size_x)
        y1 = self._y1 + (i * self._cell_size_y)

        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_wall_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True

        while True:
            to_visit = []

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0: 
                self._draw_cell(i, j)
                return
            
            direction = to_visit[random.randrange(len(to_visit))]
            new_cell = self._cells[direction[0]][direction[1]];

            # left 
            if direction[0] == i - 1:
                cell.has_left_wall = False
                new_cell.has_right_wall = False
        
            # right
            if direction[0] == i + 1:
                cell.has_right_wall = False
                new_cell.has_left_wall = False

            # up
            if direction[1] == j - 1:
                cell.has_top_wall = False
                new_cell.has_bottom_wall = False

            # down
            if direction[1] == j + 1:
                cell.has_bottom_wall = False
                new_cell.has_top_wall = False

            self._break_wall_r(direction[0], direction[1])

