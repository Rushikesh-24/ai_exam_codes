# Water Jug Problem - DFS (all solutions)

capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
target = int(input("Enter required quantity: "))

def get_successors(state):
    x, y = state
    successors = []
    successors.append((capA, y))              # Fill A
    successors.append((x, capB))               # Fill B
    successors.append((0, y))                   # Empty A
    successors.append((x, 0))                   # Empty B

    # Pour A -> B
    pour = min(x, capB - y)
    successors.append((x - pour, y + pour))

    # Pour B -> A
    pour = min(y, capA - x)
    successors.append((x + pour, y - pour))

    return successors

start = (0, 0)
solution_count = 0

def dfs(state, path, visited):
    global solution_count
    path.append(state)
    if state[0] == target or state[1] == target:
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