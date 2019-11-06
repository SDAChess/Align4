from . import Matrix
from .rules import evaluate_board
from .player import Player


class Game:
    def __init__(self):
        self._matrix = Matrix(7, 6, Player.Null)
        self._player = Player.Player1

    def _switch_player(self):
        self._player = -self._player

    def add_piece(self, x):
        x, y = add_piece(self._matrix, x, self._player)
        if (x, y) != (-1, -1):
            self._switch_player()
            return x, y
        return -1, -1

    @property
    def winner(self):
        for player in (Player.Player1, Player.Player2):
            if evaluate_board(self._matrix, player)[4] >= 1:
                return player
        return Player.Null if self._is_full else None

    @property
    def current_player(self):
        return self._player

    @property
    def _is_full(self):
        for i in range(self._matrix.width):
            for j in range(self._matrix.height):
                if self._matrix[i, j] != Player.Null:
                    pass
                else:
                    return False
        return True


def add_piece(board, x, player: Player):
    y = board.height - 1
    while y > 0 and board[x, y - 1] is Player.Null:
        y -= 1

    if board[x, y] is Player.Null:
        board[x, y] = player
        return x, y

    return -1, -1
