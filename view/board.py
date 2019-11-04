import tkinter as tk

from model import Matrix
from observer import Observable, Observer


class Board(tk.Canvas, Observer, Observable):

    def __init__(self, master, width, *args, **kwargs):
        tk.Canvas.__init__(self, master, width=width, height=width / 7 * 6, *args, **kwargs)
        Observable.__init__(self)

        self._width = width
        self._circles = Matrix(7, 6)
        self._init_ui()

    def _init_ui(self):
        for j in range(6):
            for i in range(7):
                x, y = self._grid_to_coords(i, j)
                self.create_oval(x + 1, y + 1, x + self._cell_size - 1, y + self._cell_size - 1, fill='white')

    @property
    def _height(self):
        return self._cell_size * 6

    @property
    def _cell_size(self):
        return int(self['width']) // 7

    def _grid_to_coords(self, i, j):
        return i * self._cell_size, j * self._cell_size

    def notify(self, _, *args, **kwargs):
        x, y = kwargs["x"], kwargs["y"]
        color = 'red' if kwargs["player"] == 1 else 'yellow'
