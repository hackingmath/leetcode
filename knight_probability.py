def knightProbability(n,k,row,column):
    """nxn chessboard, knight starts at (row,col)
    and makes k moves. Return probability of still being on
    the chessboard."""
    pos = (row,column)
    positions = list()
    positions.append(pos)
    moves = [[1,2],[-1,2],[-1,-2],[1,-2],
             [2,1],[2,-1],[-2,-1],[-2,1]]
    for i in range(k):
        newpositions = list()#positions#[::]
        for p in positions:
            newpos = [[p[0] + j[0],p[1] + j[1]] for j in moves]
            for np in newpos:
                if 0 <= np[0] < n and 0 <= np[1] < n:
                    newpositions.append(tuple(np))
        positions = newpositions[::]

    print(newpositions)
    l = len(newpositions)
    return l / 8**k

print(knightProbability(3,2,0,0))

