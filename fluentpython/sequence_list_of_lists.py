# good
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# bad, because the same row is
# appended three times to the board
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'o'
print(weird_board)