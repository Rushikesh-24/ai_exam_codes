# Tic Tac Toe using Minimax with Evaluation Function
# e(n) = ways X can still win - ways O can still win

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

def evaluate(b):
    x_ways = 0
    o_ways = 0
    for x, y, z in win_pos:
        line = [b[x], b[y], b[z]]
        if 'O' not in line:      # X can still win this line
            x_ways += 1
        if 'X' not in line:      # O can still win this line
            o_ways += 1
    return x_ways - o_ways

def minimax(b, depth, is_max, max_depth):
    result = check_winner(b)
    if result == 'X':
        return 100
    elif result == 'O':
        return -100
    elif result == 'Draw':
        return 0

    if depth == max_depth:
        return evaluate(b)          # use e(n) when depth limit reached

    if is_max:                       # X is maximizer
        best = -1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = max(best, minimax(b, depth + 1, False, max_depth))
                b[i] = ' '
        return best
    else:                            # O is minimizer
        best = 1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = min(best, minimax(b, depth + 1, True, max_depth))
                b[i] = ' '
        return best

def best_move(max_depth):
    best_val = -1000
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False, max_depth)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Game loop
print("Tic Tac Toe: Computer is X (Maximizer), You are O (Minimizer)")
max_depth = int(input("Enter search depth limit (e.g. 9 for full search): "))
print_board()

while True:
    move = best_move(max_depth)
    board[move] = 'X'
    print(f"\nComputer plays at {move}")
    print_board()

    if check_winner(board):
        print("Result:", check_winner(board))
        break

    pos = int(input("Enter your move (0-8): "))
    if board[pos] != ' ':
        print("Invalid move, try again.")
        continue
    board[pos] = 'O'

    if check_winner(board):
        print_board()
        print("Result:", check_winner(board))
        break