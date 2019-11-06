from model import Matrix
from model.player import Player


def evaluate_board(board: Matrix, player: Player):
    alignments = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    # Count the horizontal alignments
    y = 0
    while y < board.height:
        x = 0
        while x < board.width:
            aligned_pieces = _count_horizontals_right(board, player, x, y)
            x += aligned_pieces + 1
            try:
                alignments[aligned_pieces] += 1
            except KeyError:
                if aligned_pieces:
                    alignments[4] += 1
        y += 1

    # Count the vertical alignments
    x = 0
    while x < board.width:
        y = 0
        while y < board.height:
            aligned_pieces = _count_verticals_top(board, player, x, y)
            y += aligned_pieces + 1
            try:
                alignments[aligned_pieces] += 1
            except KeyError:
                if aligned_pieces:
                    alignments[4] += 1
        x += 1

    # Count the diagonal alignments in the two directions
    #Top Right
    x = 0
    while x < board.width:
        y = 0
        while y < board.height:
            if x == 0 or y == 0:
                aligned_pieces = _count_diagonals_top_right(board, player, x, y)
                try:
                    alignments[aligned_pieces] += 1
                except KeyError:
                    if aligned_pieces:
                        alignments[4] += 1
            y += 1
        x += 1
    #Top left
    x = 0
    while x < board.width:
        y = 0
        while y < board.height:
            if x == board.width - 1 or y == 0:
                aligned_pieces = _count_diagonals_top_left(board, player, x, y)
                try:
                    alignments[aligned_pieces] += 1
                except KeyError:
                    if aligned_pieces:
                        alignments[4] += 1
            y += 1
        x += 1

    del alignments[1]
    return alignments


def _count_horizontals_right(board: Matrix, target: Player, x: int, y: int) -> int:
    player = board[x, y]
    next_cell = player

    if player is not target:
        return 0

    count = 0
    while x < board.width and next_cell == player:
        count += 1
        x += 1
        try:
            next_cell = board[x, y]
        except IndexError:
            break

    return count


def _count_verticals_top(board: Matrix, target: Player, x: int, y: int) -> int:
    player = board[x, y]
    next_cell = player

    if player is not target:
        return 0

    count = 0
    while y < board.height and next_cell == player:
        count += 1
        y += 1
        try:
            next_cell = board[x, y]
        except IndexError:
            break

    return count


def _count_diagonals_top_right(board: Matrix, target: Player, x: int, y: int) -> int:
    count = 0
    next_cell = player = None
    started = False
    while y < board.height and x < board.width and (not started or next_cell is player):
        if not started:
            player = board[x, y]
            started = player is target
        if started:
            count += 1
        y += 1
        x += 1
        try:
            next_cell = board[x, y]
        except IndexError:
            break
    return count


def _count_diagonals_top_left(board: Matrix, target: Player, x: int, y: int) -> int:
    count = 0
    next_cell = player = None
    started = False
    while y < board.height and x >= 0 and (not started or next_cell is player):
        if not started:
            player = board[x, y]
            started = player is target
        if started:
            count += 1
        y += 1
        x -= 1
        try:
            next_cell = board[x, y]
        except IndexError:
            break
    return count
