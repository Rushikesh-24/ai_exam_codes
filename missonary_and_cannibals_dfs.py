# Missionaries and Cannibals - DFS (different M and C)

M = int(input("Enter number of missionaries: "))
C = int(input("Enter number of cannibals: "))

def is_valid(x, y):
    if x < 0 or x > M or y < 0 or y > C:
        return False
    left_m, left_c = M - x, C - y     # left side
    right_m, right_c = x, y            # right side
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
solution_count = 0

def dfs(state, path, visited):
    global solution_count
    path.append(state)
    if state == goal:
        solution_count += 1
        print(f"Solution {solution_count}:", " -> ".join(str(s) for s in path))
    else:
        visited.add(state)
        for nxt in get_successors(state):
            if nxt not in visited:
                dfs(nxt, path, visited)
        visited.remove(state)
    path.pop()

print("All Solutions (DFS):\n")
dfs(start, [], set())
if solution_count == 0:
    print("No solution exists")