# Steepest Ascent Hill Climbing (moves to BEST neighbor found)

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

    # Evaluate ALL neighbors, pick the one with the smallest heuristic
    neighbors = graph.get(current, [])
    better_neighbors = [(nb, heuristic[nb]) for nb in neighbors if heuristic[nb] < heuristic[current]]

    if not better_neighbors:
        print("Stuck at local minimum. Stopping.")
        break

    better_neighbors.sort(key=lambda x: x[1])   # sort ALL better neighbors
    next_node, next_h = better_neighbors[0]      # pick the BEST (steepest) one

    parent = current
    current = next_node
    iteration += 1

print("\nFinal Close List:", close_list)