#!/usr/bin/env python3


def checkmate(board):
    if not isinstance(board, str):
        print("Error: Invalid Board")
        return

    rows = board.splitlines()

    while rows and rows[0] == "":
        rows.pop(0)

    while rows and rows[-1] == "":
        rows.pop()

    if not rows:
        print("Error: Wrong Dimension")
        return

    size = len(rows)

    for row in rows:
        if len(row) != size:
            print("Error: Wrong Dimension")
            return

    king_positions = []

    for row_index in range(size):
        for column_index in range(size):
            if rows[row_index][column_index] == "K":
                king_positions.append((row_index, column_index))

    if len(king_positions) != 1:
        print("Error: K Unit -> Possible Number")
        return

    king_row, king_column = king_positions[0]

    pieces = "KQRBP"

    # Pawn
    pawn_row = king_row + 1

    if pawn_row < size:
        for pawn_column in (king_column - 1, king_column + 1):
            if 0 <= pawn_column < size:
                if rows[pawn_row][pawn_column] == "P":
                    print("Success")
                    return

    # Rook / Queen
    straight_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row_move, column_move in straight_directions:
        row = king_row + row_move
        column = king_column + column_move

        while 0 <= row < size and 0 <= column < size:
            square = rows[row][column]

            if square in pieces:
                if square == "R" or square == "Q":
                    print("Success")
                    return

                break

            row += row_move
            column += column_move

    # Bishop / Queen
    diagonal_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for row_move, column_move in diagonal_directions:
        row = king_row + row_move
        column = king_column + column_move

        while 0 <= row < size and 0 <= column < size:
            square = rows[row][column]

            if square in pieces:
                if square == "B" or square == "Q":
                    print("Success")
                    return

                break

            row += row_move
            column += column_move

    print("Fail")