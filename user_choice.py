from check_win import check_win
from board import print_board

def user_choice(board):
    turn = 0
    playing = True

    print_board(board)
    while playing:
        if turn < 9:
            if turn % 2 == 0:
                replace = 'x'
            else:
                replace = 'O'
            
            try:
                rep_choice = int(input(f"Choose a number to replace with: {replace} :"))
                if board[rep_choice]  == 'x' or  board[rep_choice] =='o':
                    print("\nTry again\n")
                else:

                    board[rep_choice] = replace
                    print_board(board)
                    winner = check_win(board)

                    if winner:
                        print("You won!")
                        playing = False

                    else:
                        turn +=1

            except ValueError:
                print("Wrong value!")
        else:
            print("game ended!")
            playing = False
