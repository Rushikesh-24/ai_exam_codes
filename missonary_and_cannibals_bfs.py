# Missionaries and Cannibals - BFS (different M and C)

M = int(input("Enter number of missionaries: "))
C = int(input("Enter number of cannibals: "))

def is_valid(x, y):
    if x < 0 or x > M or y < 0 or y > C:
        return False
    left_m, left_c = M - x, C - y
    right_m, right_c = x, y
    if left_m > 0 and left_m < left_c:
        return False
    if right_m > 0 and right_m < right_c:
        return False
    return True

def get_successors(state):
    x, y, side = state
    successors = []
    for dm in range(3):
        for dc in range(3):
            if 1 <= dm + dc <= 2:
                if side == 'L':
                    nx, ny = x + dm, y + dc
                    if is_valid(nx, ny):
                        successors.append((nx, ny, 'R'))
                else:
                    nx, ny = x - dm, y - dc
                    if is_valid(nx, ny):
                        successors.append((nx, ny, 'L'))
    return successors

start = (0, 0, 'L')
goal = (M, C, 'R')

open_list = [(start, None)]
close_list = []

while open_list:
    state, parent = open_list.pop(0)
    if any(state == x[0] for x in close_list):
        continue
    close_list.append((state, parent))
    if state == goal:
        print("Goal Found!")
        break
    for succ in get_successors(state):
        if not any(succ == x[0] for x in close_list):
            open_list.append((succ, state))

path = []
if any(goal == s for s, _ in close_list):
    current = goal
    while current is not None:
        path.append(current)
        for s, p in close_list:
            if s == current:
                current = p
                break
    path.reverse()
    print("Shortest Path:")
    for step in path:
        print(step)
else:
    print("No solution exists")