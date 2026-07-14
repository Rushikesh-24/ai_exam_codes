# DFS using Open and Close list (with parent tracking)

graph = {}

n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)   # Remove if directed graph

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(start, None)]     # (node, parent)
close_list = []

iteration = 1
print("Open List :", open_list)
print("Close List:", close_list)
while open_list:
    print(f"\nIteration {iteration}")
    node, parent = open_list.pop()  
    if any(node == x[0] for x in close_list):
        continue
    close_list.append((node, parent))
    if node == goal:
        print("Goal Found!")
        break
    for neighbor in graph.get(node, []):
        if not any(neighbor == x[0] for x in close_list):
            open_list.append((neighbor, node))
    print("Open List :", open_list)
    print("Close List:", close_list)
    iteration += 1
print("\nFinal Close List:", close_list)

path = []
if any(goal == node for node, _ in close_list):
    current = goal
    while current is not None:
        path.append(current)
        for node, parent in close_list:
            if node == current:
                current = parent
                break
    path.reverse()
    print("Final Path:", " -> ".join(path))
else:
    print("Goal not found!")