import math
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != ' ':
            return line[0]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10
    elif winner == 'O':
        return 10
    elif is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game\n")
    print_board(board)

    while True:
        # Player Move
        x, y = map(int, input("Enter your move (row col): ").split())
        if board[x][y] == ' ':
            board[x][y] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
        
        if check_winner(board):
            print_board(board)
            print("Player wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI Move
        move = best_move(board)
        board[move[0]][move[1]] = 'O'
        print("AI Move:")
        print_board(board)
        
        if check_winner(board):
            print("AI wins!")
            break
        
        if is_full(board):
            print("It's a draw!")
            break

play_game()
