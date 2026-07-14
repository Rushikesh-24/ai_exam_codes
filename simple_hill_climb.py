# Simple Hill Climbing (moves to FIRST better neighbor found)

graph = {}
heuristic = {}

n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

nodes = int(input("Enter number of nodes for heuristic values: "))
for _ in range(nodes):
    node, h = input("Enter node and heuristic (e.g. A 5): ").split()
    heuristic[node] = int(h)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

close_list = []
current = start
parent = None
iteration = 1

while True:
    print(f"\nIteration {iteration}")
    close_list.append((current, parent, heuristic[current]))
    print("Close List:", close_list)

    if current == goal:
        print("Goal Found!")
        break

    next_node = None
    for nb in graph.get(current, []):
        if heuristic[nb] < heuristic[current]:      # first improving neighbor
            next_node = nb
            break

    if next_node is None:
        print("Stuck at local minimum. Stopping.")
        break

    parent = current
    current = next_node
    iteration += 1

print("\nFinal Close List:", close_list)