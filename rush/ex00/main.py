
from checkmate import checkmate


def main():

    # Test Case 1: King ถูก Pawn โจมตี
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)  # Success


    # Test Case 2: King ไม่ถูกโจมตี
    board2 = """\
....
.K..
...P
....\
"""
    checkmate(board2)  # Fail


    # Test Case 3: Queen อยู่แนวทแยงกับ King
    # แต่มี Rook ขวางทางอยู่ จึงโจมตี King ไม่ได้
    board3 = """\
Q...
.R..
..K.
....\
"""
    checkmate(board3)  # Fail


    # Test Case 4: King ถูก Bishop โจมตีในแนวทแยง
    board4 = """\
B.......
........
........
...K....
........
........
........
........\
"""
    checkmate(board4)  # Success


    # Test Case 5: King ถูก Pawn โจมตี
    board5 = """\
....
.K..
P...
....\
"""
    checkmate(board5)  # Success


    # Test Case 6: กระดานไม่มี King
    # เป็นกรณีข้อมูลไม่ถูกต้อง จึง return โดยไม่ crash
    board6 = """\
R...
....
..P.
....\
"""
    checkmate(board6)


    # Test Case 7: กระดานไม่เป็นสี่เหลี่ยมจัตุรัส
    # จึง return โดยไม่ crash
    board7 = """\
R..
.K.
..P.
....\
"""
    checkmate(board7)


if __name__ == "__main__":
    main()