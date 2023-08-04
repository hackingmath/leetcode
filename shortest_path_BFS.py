#From Competitive Programming in Python p. 134
# Aug 2, 2023

from collections import deque
def dist_grid(R,C,A,target,testing=False):
    q = deque()
    q.append((0,0,0)) #x,y,dist
    visited = set()
    while q:
        a = q.popleft()
        visited.add((a[0],a[1]))
        if testing:
            print("a:",a)
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            x2,y2 = a[0] + dx, a[1]+dy
            if testing:
                print("x2,y2:",x2,y2)
            if not (0<=x2<R and 0<=y2<C):
                continue
            if testing:
                print("after checking:",x2,y2)
            if (A[x2][y2] != 1) or ((x2,y2) in visited):
                    continue
            # if testing:
            #         print("indexerror:",x2,y2)
            if (x2,y2) == target:
                return a[2] + 1
            q.append((x2,y2,a[2]+1))

# N=3
# M=4
# A=[[1,0,0,0],
#    [1,1,0,1],
#    [0,1,1,1]]
# X=2
# Y=3
with open('shortest_path_BFS.txt') as f:
    N,M = [int(x) for x in f.readline().split()]
    A = list()
    for _ in range(N):
        A.append([int(x) for x in f.readline().split()])
    X,Y = [int(x) for x in f.readline().split()]

print(dist_grid(N,M,A,(X,Y),True))