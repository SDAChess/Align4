from model.matrix import Matrix


def evaluate_board(board: Matrix):
    alignments = {}

    # Count the horizontal alignments
    horizontals = 0
    x = y = 0
    while y < board.height:
        while x < board.width:
            aligned_pieces = _count_horizontals_right(board, x, y)
            x += aligned_pieces + 1
            horizontals += aligned_pieces
        y += 1

    # Count the vertical alignments
    verticals = 0
    x = y = 0
    while x < board.width:
        while y < board.height:
            aligned_pieces = _count_verticals_top(board, x, y)
            y += aligned_pieces + 1
            verticals += aligned_pieces
        x += 1

    # Count the diagonal alignments in the two directions


def _count_horizontals_right(board: Matrix, x: int, y: int) -> int:
    player = board[x, y]
    next_cell = player

    if player is 0:
        return 0

    count = 0
    while x < board.width and next_cell is player:
        count += 1
        x += 1
        next_cell = board[x, y]

    return count


def _count_verticals_top(board: Matrix, x: int, y: int) -> int:
    pass


def _count_diagonals_top_right(board: Matrix, x: int, y: int) -> int:
    pass


def _count_diagonals_top_left(board: Matrix, x: int, y: int) -> int:
    pass
