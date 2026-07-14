# A* Search using Open and Close list (node, parent, g, h, f)

graph = {}
heuristic = {}

n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v, w = input("Enter edge (u v weight): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))   # Remove if directed graph

nodes = int(input("Enter number of nodes for heuristic values: "))
for _ in range(nodes):
    node, h = input("Enter node and heuristic (e.g. A 5): ").split()
    heuristic[node] = int(h)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# Each entry: (node, parent, g, h, f)
open_list = [(start, None, 0, heuristic[start], 0 + heuristic[start])]
close_list = []

iteration = 1
print("Open List :", open_list)
print("Close List:", close_list)

while open_list:
    print(f"\nIteration {iteration}")

    open_list.sort(key=lambda x: x[4])          # sort by f value
    node, parent, g, h, f = open_list.pop(0)

    close_list.append((node, parent, g, h, f))

    if node == goal:
        print("Goal Found!")
        break

    for neighbor, weight in graph.get(node, []):
        new_g = g + weight
        new_h = heuristic[neighbor]
        new_f = new_g + new_h

        # Check if neighbor already in close_list
        in_close = next((x for x in close_list if x[0] == neighbor), None)
        if in_close:
            if new_g < in_close[2]:                        # better path found
                close_list.remove(in_close)
                open_list.append((neighbor, node, new_g, new_h, new_f))
            continue

        # Check if neighbor already in open_list
        in_open = next((x for x in open_list if x[0] == neighbor), None)
        if in_open:
            if new_g < in_open[2]:                          # better path found
                open_list.remove(in_open)
                open_list.append((neighbor, node, new_g, new_h, new_f))
        else:
            open_list.append((neighbor, node, new_g, new_h, new_f))

    print("Open List :", open_list)
    print("Close List:", close_list)
    iteration += 1

print("\nFinal Close List:", close_list)

path = []
if any(goal == x[0] for x in close_list):
    current = goal
    while current is not None:
        path.append(current)
        for node, parent, g, h, f in close_list:
            if node == current:
                current = parent
                break
    path.reverse()
    print("Final Path:", " -> ".join(path))
else:
    print("Goal not found!")