from observer import Observer, Observable
from model import Game
from algorithm import best_move


class Controller(Observable, Observer):
    def __init__(self):
        Observable.__init__(self)
        self._game = Game()

    def notify(self, _, *args, **kwargs):
        x, y = kwargs["x"], kwargs["y"]
        x, y = self._game.add_piece(x)
        if (x, y) != (-1, -1):
            self.notify_observers(x=x, y=y, player=self._game.current_player, winner=self._game.winner)

        move = best_move(self._game._player, self._game._matrix)
        x, y = self._game.add_piece(move)
        if (x, y) != (-1, -1):
            self.notify_observers(x=x, y=y, player=self._game.current_player, winner=self._game.winner)
