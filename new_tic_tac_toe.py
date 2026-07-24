board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def isFull(board):
    for row in board:
        for element in row:
            if element == ' ':
                return False
    return True

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]

    return None


def minmax(board,isMax):
    w = winner(board)

    if w == 'X':
        return 1
    elif w == 'O':
        return -1
    elif isFull(board):
        return 0

    if isMax:
        best = -999

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minmax(board,False)
                    board[i][j] = ' '
                    best = max(best,score)

    else:
        best = 999

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minmax(board,True)
                    board[i][j] = ' '
                    best = min(best,score)

    return best


def ai(board):
    best = 999
    bi,bj = -1,-1

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'

                # Next turn is X
                score = minmax(board,True)

                board[i][j] = ' '

                if score < best:
                    best = score
                    bi = i
                    bj = j

    return bi,bj


while not isFull(board):

    for row in board:
        print(row)

    if winner(board):
        print("Winner =", winner(board))
        break

    i,j = input("Enter row and column : ").split()
    i = int(i)
    j = int(j)

    if i<0 or i>2 or j<0 or j>2 or board[i][j]!=' ':
        print("Invalid Move")
        continue

    board[i][j] = 'X'

    if winner(board):
        print("Winner = X")
        break

    if isFull(board):
        break

    i,j = ai(board)
    board[i][j] = 'O'

if not winner(board):
    print("Draw")

print("\nFinal Board:")
for row in board:
    print(row)

print("GAME OVER")