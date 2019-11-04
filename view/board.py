import tkinter as tk

from observer import *


class Board(tk.Canvas, Observer, Observable):

    def __init__(self, master, size, *args, **kwargs):
        tk.Canvas.__init__(self, master, width=size, height=size)
        Observable.__init__(self)

        self._size = size

    def _init_ui(self):
        pass

    @property
    def cell_size(self):
        return int(self['width'])

    def _grid_to_coords(self, i, j):
        return i * self.cell_size, j * self.cell_size
