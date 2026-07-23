m,n = input("enter the size of conatiner a and b").split()
m = int(m)
n = int(n)
depth_limit =4
open = [((0,0),0)]
close=[]
parent={}
goal = int(input("Enter the goal"))
parent[open]=None
def generate(current):
    neighbours =[]
    neighbours.append((current[0],0)) 
    neighbours.append((0,current[1])) 
    neighbours.append((m,current[1])) #fill a
    neighbours.append((current[0],n)) #fill b
    if current[0]+current[1]<=n:
        neighbours.append((0,current[0]+current[1]))
    else:
        neighbours.append((current[0]-(n-current[1]),n))
    if current[0]+current[1]<=m:
        neighbours.append((current[0]+current[1],0))
    else:
        neighbours.append((m,current[1]-(m-current[0])))
    return neighbours

while open:
    current,depth = open.pop()
    # depth bound remove this if then normal dfs and above if pop(0) then bfs
    if depth==depth_limit:
        continue
    if any(current==x for x in close):
        continue
    close.append(current)
    if current[0]==goal or current[1] == goal:
        path=[]
        while current is not None:
            path.append(current)
            current=parent[current]
        path.reverse()
        print("goal found")
        break
    neighbours = generate(current)
    for state in neighbours:
        if not any(state == x for x in close):
            open.append((state,depth_limit+1))
            parent[state]=open
    
print(open,close)