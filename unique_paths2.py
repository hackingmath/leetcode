from collections import deque

def uniquePathsWithObstaclesBFS(obstacleGrid):
    m,n = len(obstacleGrid),len(obstacleGrid[0])
    ways = 0#set()
    q = deque()
    q.append((0,0))
    while q:
        loc = q.popleft()
        #loc = path[-1]
        #print("loc:",loc)
        if loc[0] >= m or loc[1] >= n:
            continue
        if obstacleGrid[loc[0]][loc[1]] == 1:
            continue
        if loc[0] >= m or loc[1] >= n:
            continue
        if loc == (m-1,n-1):
            #print("dest reached!")
            ways += 1
            continue
        else:

            for w in ((1,0),(0,1)):
                #path2 = path[:]
                new = (loc[0]+w[0],loc[1]+w[1])
                #path2.append(new)
                #pathlist.append(path)
                #pathlist.append(new)
                q.append(new)
    return ways#len(ways)

def uniquePathsWithObstacles(obstacleGrid):
    m,n = len(obstacleGrid),len(obstacleGrid[0])
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[m-1][n-1] = 1
    print(dp)
    for a in range(m-1,-1,-1):
        for b in range(n-1,-1,-1):
            if obstacleGrid[a][b] == 1:
                dp[a][b] = 0
            else:
                dp[a][b] += dp[a+1][b] + dp[a][b+1]
            #except:
            #    pass
            print(a,b,dp[a][b])
    return dp[0][0]

print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,1],[0,0]]))