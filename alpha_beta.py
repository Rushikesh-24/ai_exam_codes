# Tic Tac Toe using Minimax with Alpha-Beta Pruning

board = [' ' for _ in range(9)]
win_pos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

def check_winner(b):
    for x, y, z in win_pos:
        if b[x] == b[y] == b[z] != ' ':
            return b[x]
    if ' ' not in b:
        return 'Draw'
    return None

def minimax(b, depth, is_max, alpha, beta):
    result = check_winner(b)
    if result == 'O':
        return 1
    elif result == 'X':
        return -1
    elif result == 'Draw':
        return 0

    if is_max:                              # O is maximizer
        best = -1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                val = minimax(b, depth + 1, False, alpha, beta)
                b[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break                    # PRUNE remaining branches
        return best
    else:                                    # X is minimizer
        best = 1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                val = minimax(b, depth + 1, True, alpha, beta)
                b[i] = ' '
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break                    # PRUNE remaining branches
        return best

def best_move():
    best_val = -1000
    move = -1
    alpha, beta = -1000, 1000
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, alpha, beta)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
            alpha = max(alpha, best_val)
    return move

# Game loop
print("Tic Tac Toe: You are X, Computer is O")
print_board()

while True:
    pos = int(input("Enter your move (0-8): "))
    if board[pos] != ' ':
        print("Invalid move, try again.")
        continue
    board[pos] = 'X'

    if check_winner(board):
        print_board()
        print("Result:", check_winner(board))
        break

    move = best_move()
    board[move] = 'O'
    print(f"\nComputer plays at {move}")
    print_board()

    if check_winner(board):
        print("Result:", check_winner(board))
        break