from sys import maxsize
from copy import deepcopy

from model import evaluate_board, add_piece


class Node:
    def __init__(self, player, board, move=0):
        self.player = player
        self.board = deepcopy(board)
        self.move = move

    @property
    def score(self):
        return _board_score(self.board, self.player) - _board_score(self.board, -self.player)

    @property
    def children(self):
        children = []
        for i in range(self.board.width):
            x, y = add_piece(deepcopy(self.board), i, -self.player)
            if (x, y) == (-1, -1):
                pass
            else:
                new_board = deepcopy(self.board)
                new_board[x, y] = self.player
                children.append(Node(-self.player, new_board, i))
        return children


def _board_score(board, player):
    evaluation = evaluate_board(board, player)
    return maxsize * evaluation[4] + 100 * evaluation[3] + 1 * evaluation[2]
