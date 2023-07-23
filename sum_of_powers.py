#https://leetcode.com/contest/biweekly-contest-109/problems/ways-to-express-an-integer-as-sum-of-powers/
#6922 Ways to Express an Integer as Sum of Powers
# July 22, 2023

def solve(n,x):
    ways = 0
    ways_dict = dict()
    def recurse(n,x,arr):
        if arr[0]**x > n:
            return 0
        output = set()
        output.add(arr[0]**x)
        if (n - arr[0]**x)**(1/x) in arr[1:]:
            return (n - arr[0]**x)**(1/x)

#knapsack problem from Colin's DP video

def knapsackTF(arr,t):
    """True or False"""
    if len(arr) == 1:
        return arr[0] == t
    if t in arr:
        return True
    for i in range(len(arr)):
        return knapsackTF(arr[:i]+arr[i+1:],t-arr[i])

print(knapsackTF([3,5,2,7,9],10))
print(knapsackTF([2,4,6],11))
print(knapsackTF([2,7,3,4,9,5,6,1,8],25))

def knapsack1(coins,amount):
    dp = {i:0 for i in range(amount + 1)}#[0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, amount + 1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
                print(dp)
    return dp[amount]

def knapsack(coins,amount):
    """Trying to make this coin program work on the
    knapsack problem"""
    dp = {i:0 for i in range(amount + 1)}#[0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, amount + 1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
                print(dp)
    return dp[amount]

print(knapsack([1,2,5],5))
print(knapsack([3,5,2,7,9],10))
print(knapsack([2,4,6],11))
print(knapsack([2,7,3,4,9,5,6,1,8],25))

#from Colin's video. I translated it from C++ but I
#don't know how to run it!
arr,t = [3,5,2,7,9],10
ans = {(n,t1) for n in range(len(arr)) for t1 in range(t+1)}
def knapsack2(element,t):
    if target == 0: return 1
    if target < 0: return 0
    if element == 0: return 0
    if ans[element][target] != -1:
        return ans[element][target]
    cur = 0
    cur = max(cur,solve(element-1,target-arr[element-1]))
    cur = max(cur, solve(element - 1, target))
    ans[element][target] = cur
    return cur

#print(knapsack)