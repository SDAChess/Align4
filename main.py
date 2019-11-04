import tkinter as tk

from view import Board

root = tk.Tk()
Board(root, 500).pack()
root.mainloop()
