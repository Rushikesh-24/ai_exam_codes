# 8 Puzzle using Best First Search (1D Array)

start = ['1','2','3','4','0','6','7','5','8']

goal = ['1','2','3','4','5','6','7','8','0']

global_idx = 0


# Heuristic Function
def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != goal[i]:
            count += 1
    return count


# Print Board
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Generate Neighbours
def generate_neighbour(state):
    global global_idx

    neighbours = []

    idx = state.index('0')

    moves = []

    if idx >= 3:
        moves.append(idx - 3)

    if idx <= 5:
        moves.append(idx + 3)

    if idx % 3 != 0:
        moves.append(idx - 1)

    if idx % 3 != 2:
        moves.append(idx + 1)

    for move in moves:
        temp = state[:]
        temp[idx], temp[move] = temp[move], temp[idx]

        global_idx += 1
        neighbours.append((temp, heuristic(temp), global_idx))

    return neighbours


# Open List
open_list = [(start, heuristic(start), global_idx)]

# Closed List
closed_list = []

# Parent Dictionary
parent = {}


while open_list:

    open_list.sort(key=lambda x: x[1])

    current = open_list.pop(0)

    if any(current[0] == x[0] for x in closed_list):
        continue

    closed_list.append(current)

    if current[0] == goal:

        print("Goal Found!\n")

        path = []

        while current[0] != start:
            path.append(current)
            current = parent[current[2]]

        path.append(current)

        path.reverse()

        for state in path:
            print_state(state[0])

        break

    neighbours = generate_neighbour(current[0])

    for neighbour in neighbours:

        if not any(neighbour[0] == x[0] for x in closed_list):
            open_list.append(neighbour)
            parent[neighbour[2]] = current