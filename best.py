# Best First Search using Open and Close list (node, parent, heuristic)

graph = {}
heuristic = {}

n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)   # Remove if directed graph

nodes = int(input("Enter number of nodes for heuristic values: "))
for _ in range(nodes):
    node, h = input("Enter node and heuristic (e.g. A 5): ").split()
    heuristic[node] = int(h)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(start, None, heuristic[start])]   # (node, parent, h)
close_list = []

iteration = 1
print("Open List :", open_list)
print("Close List:", close_list)
while open_list:
    print(f"\nIteration {iteration}")

    # Pick node with minimum heuristic value
    open_list.sort(key=lambda x: x[2])
    node, parent, h = open_list.pop(0)

    if any(node == x[0] for x in close_list):
        continue
    close_list.append((node, parent, h))
    if node == goal:
        print("Goal Found!")
        break

    for neighbor in graph.get(node, []):
        if not any(neighbor == x[0] for x in close_list):
            open_list.append((neighbor, node, heuristic[neighbor]))

    print("Open List :", open_list)
    print("Close List:", close_list)
    iteration += 1
print("\nFinal Close List:", close_list)

path = []
if any(goal == node for node, _, _ in close_list):
    current = goal
    while current is not None:
        path.append(current)
        for node, parent, h in close_list:
            if node == current:
                current = parent
                break
    path.reverse()
    print("Final Path:", " -> ".join(path))
else:
    print("Goal not found!")