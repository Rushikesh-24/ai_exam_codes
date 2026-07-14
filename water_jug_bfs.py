# Water Jug Problem - BFS (shortest solution)

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

    pour = min(x, capB - y)                     # Pour A -> B
    successors.append((x - pour, y + pour))

    pour = min(y, capA - x)                      # Pour B -> A
    successors.append((x + pour, y - pour))

    return successors

start = (0, 0)

open_list = [(start, None)]
close_list = []

while open_list:
    state, parent = open_list.pop(0)         # pop(0) -> BFS
    if any(state == x[0] for x in close_list):
        continue
    close_list.append((state, parent))
    if state[0] == target or state[1] == target:
        print("Goal Found!")
        break
    for succ in get_successors(state):
        if not any(succ == x[0] for x in close_list):
            open_list.append((succ, state))

path = []
last_state = close_list[-1][0]
if last_state[0] == target or last_state[1] == target:
    current = last_state
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