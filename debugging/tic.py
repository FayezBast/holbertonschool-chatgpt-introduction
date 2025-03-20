#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * (len(row) * 4 - 3))  # Dynamic separator

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Input handling with validation
        try:
            row, col = map(int, input(f"Enter row and column (0-2) for player {player}: ").split())
        except ValueError:
            print("Invalid input! Please enter two numbers between 0 and 2 separated by space.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move! Please enter numbers between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        won, winner = check_winner(board)

        if won:
            print_board(board)
            print(f"🎉 Player {winner} wins! 🎉")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()

