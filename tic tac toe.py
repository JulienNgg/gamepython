import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * (5 * len(row) + 1))

def check_winner(board):
    # Check rows and columns
    for i in range(5):
        if all(board[i][j] == board[i][j+1] != ' ' for j in range(4)) or \
           all(board[j][i] == board[j+1][i] != ' ' for j in range(4)):
            return True

    # Check diagonals
    if all(board[i][i] == board[i+1][i+1] != ' ' for i in range(4)) or \
       all(board[i][4-i] == board[i+1][3-i] != ' ' for i in range(4)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, row, col, player):
    if 0 <= row < 5 and 0 <= col < 5 and board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Invalid move. Try again.")
        return False

def computer_move(board):
    empty_cells = [(i, j) for i in range(5) for j in range(5) if board[i][j] == ' ']
    return random.choice(empty_cells)

def tic_tac_toe_5x5_single_player():
    board = [[' ' for _ in range(5)] for _ in range(5)]
    player = 'X'

    print("Welcome to 5x5 Tic Tac Toe (Single Player)!\n")
    print_board(board)

    while True:
        if player == 'X':
            row = int(input("Enter row (0, 1, 2, 3, or 4): "))
            col = int(input("Enter column (0, 1, 2, 3, or 4): "))
            if player_move(board, row, col, player):
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    print_board(board)
                    player = 'O'
        else:
            print("Computer's turn:")
            row, col = computer_move(board)
            player_move(board, row, col, player)

            if check_winner(board):
                print_board(board)
                print("Computer wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                print_board(board)
                player = 'X'

if __name__ == "__main__":
    tic_tac_toe_5x5_single_player()
