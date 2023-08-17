import math
from collections import deque

def updateMatrix1(mat):
    ROWS, COLS = len(mat), len(mat[0])
    dp = dict()
    for r,row in enumerate(mat):
        for c,col in enumerate(row):
            if col == 0:
                dp[(r,c)] = 0
            else:
                dp[(r,c)] = math.inf
    out = [[-1]*COLS for _ in range(ROWS)]
    print(dp)
    for x in range(ROWS):
        for y in range(COLS):
            if dp[(x,y)] == 0:
                out[x][y] = 0
                continue
            nbs = list()
            # if y > 0:
            #     nbs.append(dp[(x,y-1)])
            # if x > 0:
            #     nbs.append(dp[(x-1,y)])
            if y < COLS-1:
                nbs.append(dp[(x, y + 1)])
            if x < ROWS-1:
                nbs.append(dp[(x + 1, y)])
            if nbs:
                dp[(x,y)] = min(nbs)
                out[x][y] = dp[(x,y)]
    for x in range(ROWS-1,-1,-1):
        for y in range(COLS-1,-1,-1):
            # if dp[(x,y)] == math.inf:
            #     nbs = list()
            if y > 0:
                nbs.append(dp[(x, y - 1)])
            if x > 0:
                nbs.append(dp[(x - 1, y)])
            # if y < COLS - 1:
            #     nbs.append(dp[(x, y + 1)])
            # if x < ROWS - 1:
            #     nbs.append(dp[(x + 1, y)])
            if nbs:
                dp[(x, y)] = min(dp[(x,y)],min(nbs))
            out[x][y] = 1+dp[(x, y)]
    return out

def updateMatrix2(mat):
    ROWS, COLS = len(mat), len(mat[0])
    def countSteps(r,c,st):
        if mat[r][c] == 0:
            return 0
        if st > ROWS:
            return st
        nbs = list()
        if c > 0:
            nbs.append(countSteps(r, c - 1,st+1))
        if r > 0:
            nbs.append(countSteps(r-1, c,st+1))
        if c < COLS - 1:
            nbs.append(countSteps(r, c + 1,st+1))
        if r < ROWS - 1:
            nbs.append(countSteps(r + 1, c,st+1))

        return 1 + min(nbs)

    out = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            out[r][c] = countSteps(r,c,0)
    return out#[countSteps(x,y) for y in range(COLS) for x in range(ROWS)]

def updateMatrix(mat):
    ROWS, COLS = len(mat), len(mat[0])
    q = deque()
    # for r,row in enumerate(mat):
    #     for c,col in enumerate(row):
    #         if col == 0:
    #             dp[(r,c)] = 0
    #         else:
    #             dp[(r,c)] = math.inf
    out = [[math.inf]*COLS for _ in range(ROWS)]
    #print(out)
    #put all 0's in deque
    for x in range(ROWS):
        for y in range(COLS):
            if mat[x][y] == 0:
                out[x][y] = 0
                q.append((x,y))
    while q:
        x,y = q.popleft()
        #nbs = list()
        if y > 0:
            if mat[x][y-1] == 0:
                pass
            elif out[x][y-1] > 1 + out[x][y]:
                out[x][y-1] = 1 + out[x][y]
                q.append((x,y-1))
        if x > 0:
            if mat[x - 1][y] == 0:
                pass
            elif out[x - 1][y] > 1 + out[x][y]:
                out[x - 1][y] = 1 + out[x][y]
                q.append((x-1, y))
        if y < COLS-1:
            if mat[x][y + 1] == 0:
                pass
            elif out[x][y + 1] > 1 + out[x][y]:
                out[x][y + 1] = 1 + out[x][y]
                q.append((x, y + 1))
        if x < ROWS-1:
            if mat[x + 1][y] == 0:
                pass
            elif out[x + 1][y] > 1 + out[x][y]:
                out[x + 1][y] = 1 + out[x][y]
                q.append((x + 1, y))
    return out

#print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

print(updateMatrix([[1,1,0,0,1,0,0,1,1,0],
                    [1,0,0,1,0,1,1,1,1,1],
                    [1,1,1,0,0,1,1,1,1,0],
                    [0,1,1,1,0,1,1,1,1,1],
                    [0,0,1,1,1,1,1,1,1,0],
                    [1,1,1,1,1,1,0,1,1,1],
                    [0,1,1,1,1,1,1,0,0,1],
                    [1,1,1,1,1,0,0,1,1,1],
                    [0,1,0,1,1,0,1,1,1,1],
                    [1,1,1,0,1,0,1,1,1,1]]))

"""[[2, 1, 0, 0, 1, 0, 0, 1, 1, 0], 
    [1, 0, 0, 1, 0, 1, 1, 2, 2, 1], 
    [1, 1, 1, 0, 0, 1, 2, 3, 1, 0], 
    [0, 1, 2, 1, 0, 1, 2, 3, 2, 1], 
    [0, 0, 1, 2, 1, 2, 1, 2, 1, 0], 
    [1, 1, 2, 3, 2, 1, 0, 1, 1, 1], 
    [0, 1, 2, 3, 3, 1, 1, 0, 0, 1], 
    [1, 2, 1, 2, 1, 0, 0, 1, 1, 2], 
    [0, 1, 0, 1, 1, 0, 1, 2, 2, 3], 
    [1, 2, 1, 0, 1, 0, 1, 2, 3, 4]]"""