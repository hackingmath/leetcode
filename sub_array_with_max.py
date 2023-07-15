#https://www.codechef.com/START98D/problems/MAXABC

def subarray_max(arr):
    if all([n <= 0 for n in arr]):
        return 0
    tot = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)+1):
            tot = max(tot,sum(arr[i:j]))
    return tot

def create_subarray(a,b):
    pass


tests = [[1,2,3],[4,-1,5,6,-2,3],[12]]

for t in tests:
    print(subarray_max(t))