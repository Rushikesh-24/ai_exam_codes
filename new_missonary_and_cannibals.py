m,c = input("enter the no of missonary and cannibals").split()
m = int(m)
c = int(c)
depth_limit =999
open = [((0,0,'L'),0)]
close =[]
parent={}
parent[(0,0,'L')]=None
goal = (m,c,'R')
def safe(state):
    if(state[2]=='R' and state[0]<state[1] and state[0]>0):
        return False
    if(state[2]=='L' and m-state[0] < c-state[1] and m-state[0]>0):
            return False
    if any(state==x for x in close):
        return False
    if any(state==x[0] for x in open):
        return False
    return True

def generate(state):
    neighbour=[]
    if(state[2]=='L'):
        if(m-state[0]>=2 and safe((state[0]+2,state[1],'R'))):
            neighbour.append((state[0]+2,state[1],'R'))
        if(c-state[1]>=2 and safe((state[0],state[1]+2,'R'))):
            neighbour.append((state[0],state[1]+2,'R'))
        if(m-state[0]>=1 and safe((state[0]+1,state[1],'R'))):
            neighbour.append((state[0]+1,state[1],'R'))
        if(c-state[1]>=1 and safe((state[0],state[1]+1,'R'))):
            neighbour.append((state[0],state[1]+1,'R'))
        if(m-state[0]>=1 and c-state[1]>=1 and safe((state[0]+1,state[1]+1,'R'))):
            neighbour.append((state[0]+1,state[1]+1,'R'))
    else:
        if(state[0]>=2 and safe((state[0]-2,state[1],'L'))):
            neighbour.append((state[0]-2,state[1],'L'))
        if(state[1]>=2 and safe((state[0],state[1]-2,'L'))):
            neighbour.append((state[0],state[1]-2,'L'))
        if(state[0]>=1 and safe((state[0]-1,state[1],'L'))):
            neighbour.append((state[0]-1,state[1],'L'))
        if(state[1]>=1 and safe((state[0],state[1]-1,'L'))):
            neighbour.append((state[0],state[1]-1,'L'))
        if(state[0]>=1 and state[1]>=1 and safe((state[0]-1,state[1]-1,'L'))):
            neighbour.append((state[0]-1,state[1]-1,'L'))

    return neighbour

while open:
    current,depth = open.pop()
    if depth >= depth_limit:
        continue
    if any(current==x for x in close):
        continue
    close.append(current)
    if current == goal:
        print("goal found")
        path =[]
        while current is not None:
            path.append(current)
            current=parent[current]
        path.reverse()
        for state in path:
            print(state,end="->")
        break
    for neighbour in generate(current):
        if not any(neighbour == x for x in close):
            open.append(((neighbour),depth+1))
            parent[neighbour]=current
            
