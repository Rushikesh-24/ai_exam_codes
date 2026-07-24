n = int(input("Enter the number of queens"))
board = [[' ' for _ in range(n)] for _ in range(n)]
for row in board:
    print(row)
    
def safe(row,column):
    for i in range(n):
        if board[row][i] == 'Q':
            return False
    for i in range(n):
            if board[i][column] == 'Q':
                return False
    i=row-1
    j=column-1
    k = row+1
    while i>=0 and j>=0 and k<n:
        if board[i][j]=='Q':
            return False
        if board[k][j]=='Q':
            return False
        i-=1
        j-=1
        k+=1
    i=row+1
    j=column+1
    k= row -1
    while i<n and j<n and k>=0:
        if board[i][j]=='Q':
            return False
        if board[k][j]=='Q':
            return False
        i+=1
        j+=1
        k-=1
    return True
count =1    
def score(row):
    global count
    if  row == n:
        print("Solution count : ",count)
        count+=1
        for row in board:
            print(row)
        return True
    else:
        for i in range(n):
            if safe(row,i):
                board[row][i] = 'Q'
                score(row+1)
                board[row][i]=' '
                
score(0)