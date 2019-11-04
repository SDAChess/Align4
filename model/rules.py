from model.matrix import Matrix

board = Matrix(5, 5, 0)

board[(2, 3)] = 1


def count_direct_neighbors(matrix):
    player1_cells = 0
    player2_cells = 0
    is_previous1 = True
    is_previous2 = True

    for i in range(matrix.get_height()):
        if matrix[(2, i)] == 1 and is_previous1:
            player1_cells += 1
            is_previous1 = True
            is_previous2 = True
        elif matrix[(2, i)] == 2 and is_previous2:
            player2_cells += 1
            is_previous2 = True
            is_previous1 = True
        else:
            is_previous1 = True
            is_previous2 = True

    return player1_cells, player2_cells


print(count_direct_neighbors(board))
