import tkinter as tk

from view import Board
from controller import Controller

root = tk.Tk()

controller = Controller()
board = Board(root, 500)
board.pack()

board.register_observer(controller)
controller.register_observer(board)

root.mainloop()
