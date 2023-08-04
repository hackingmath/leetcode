#geeksforgeeks problem
#August 2, 2023

import math

def shortestDistance(N, M, A,X, Y):
    """N: Number of Rows
    M: Number of Columns
    A: NxM Matrix of 0's and 1's
    X,Y: location of target
    I added XC,YC: current location
    """
    def solve(N,M,A,XC,YC,X,Y):
        if XC < 0 or XC >= N or YC < 0 or YC >= M or A[XC][YC] != 1:
            return math.inf
        if (XC,YC) == (X,Y):
            return 0

        return 1 + min(solve(N,M,A,XC+1,YC,X,Y),
                       solve(N, M, A, XC, YC + 1, X, Y),
                       solve(N,M,A,XC-1,YC,X,Y),
                       solve(N, M, A, XC, YC - 1, X, Y))
    return solve(N,M,A,0,0,X,Y)

N=3
M=4
A=[[1,0,0,0],
   [1,1,0,1],
   [0,1,1,1]]
X=2
Y=3
print(shortestDistance(N,M,A,X,Y))

