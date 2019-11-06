from sys import maxsize
from .node import Node


def min_max(node, depth, is_maximising_player):
    if depth == 0 or len(node.children) == 0:
        return node.score
    if is_maximising_player:
        value = -maxsize
        for child in node.children:
            value = max(value, min_max(child, depth - 1, False))
        return value
    else:
        value = maxsize
        for child in node.children:
            value = min(value, min_max(child, depth - 1, True))
        return value


def best_move(player, board):
    print(board)
    node = Node(player, board, 0)
    print([child.board for child in node.children])
    max_value, move = -maxsize, None
    for child in node.children:
        score = min_max(child, 3, False)
        print(score)
        if score >= max_value:
            max_value = score
            move = child.move

    return move
