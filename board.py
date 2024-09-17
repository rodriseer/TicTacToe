def print_board(board):
    for i in range(1, 10, 3):
         print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
    print("\n")
