def path_is_clear(board, start_row, start_col, end_row, end_col):
    row_step = 0
    col_step = 0

    if end_row > start_row:
        row_step = 1
    elif end_row < start_row:
        row_step = -1

    if end_col > start_col:
        col_step = 1
    elif end_col < start_col:
        col_step = -1

    row = start_row + row_step
    col = start_col + col_step

    while row != end_row or col != end_col:
        if board[row][col] in "PBRQK":
            return False

        row += row_step
        col += col_step

    return True


def checkmate(board):
    if not isinstance(board, str):
        return

    rows = board.splitlines()
    size = len(rows)

    if size == 0:
        return

    for row in rows:
        if len(row) != size:
            return

    king_row = -1
    king_col = -1
    king_count = 0

    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                king_row = row
                king_col = col
                king_count += 1

    if king_count != 1:
        return

    for row in range(size):
        for col in range(size):
            piece = rows[row][col]

            if piece == "P":
                if row - 1 == king_row and abs(col - king_col) == 1:
                    print("Success")
                    return

            elif piece == "B":
                if abs(row - king_row) == abs(col - king_col):
                    if path_is_clear(rows, row, col, king_row, king_col):
                        print("Success")
                        return

            elif piece == "R":
                if row == king_row or col == king_col:
                    if path_is_clear(rows, row, col, king_row, king_col):
                        print("Success")
                        return

            elif piece == "Q":
                straight = row == king_row or col == king_col
                diagonal = abs(row - king_row) == abs(col - king_col)

                if straight or diagonal:
                    if path_is_clear(rows, row, col, king_row, king_col):
                        print("Success")
                        return

    print("Fail")