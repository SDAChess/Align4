import tkinter as tk
from tkinter import messagebox

from model import Matrix, Player
from observer import Observable, Observer


class Board(tk.Canvas, Observer, Observable):

    def __init__(self, master, width, *args, **kwargs):
        tk.Canvas.__init__(self, master, width=width, height=width / 7 * 6, *args, **kwargs)
        Observable.__init__(self)

        self._width = width
        self._shape_ids = Matrix(7, 6)

        self._init_ui()
        self.bind('<Button-1>', self._on_click)

    def _init_ui(self):
        for j in range(6):
            for i in range(7):
                x, y = self._grid_to_coords(i, j)
                shape_id = self.create_oval(x + 1, y + 1, x + self._cell_size - 1, y + self._cell_size - 1, fill='white')
                self._shape_ids[i, j] = shape_id

    @property
    def _height(self):
        return self._cell_size * 6

    @property
    def _cell_size(self):
        return int(self['width']) // 7

    def _grid_to_coords(self, i, j):
        return i * self._cell_size, int(self["height"]) - (j + 1) * self._cell_size

    def _coords_to_grid(self, x, y):
        return x // self._cell_size, y // self._cell_size

    def _on_click(self, event):
        x, y = self._coords_to_grid(event.x, event.y)
        self.notify_observers(x=x, y=y)

    def notify(self, _, *args, **kwargs):
        x, y = kwargs["x"], kwargs["y"]
        player = kwargs["player"]
        self.itemconfig(self._shape_ids[x, y], fill=player.color)

        winner = kwargs["winner"]
        if winner:
            message = "Egalité" if winner == Player.Null else f'Le joueur {player} a gagné'
            messagebox.showinfo('Fin la partie', message)
            exit(0)
