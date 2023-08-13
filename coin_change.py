from collections import deque

def change2(amount,coins):
    combs = {(0,0,0)}
    ways = 0
    for i,coin in enumerate(coins):
        if coin > amount:
            continue
        if coin == amount:
            ways += 1
        if coin < amount:
            ways += change(amount-coin,coins)
    return ways

def change3(amount,coins):
    #def bfs():
    ways = set()
    q = deque()
    q.append(tuple([0 for i in range(len(coins))]))
    while q:
        comb = q.popleft()
        _sum = sum([comb[i]*coins[i] for i in range(len(comb))])
        if _sum > amount:
            continue
        elif _sum == amount:
            print("comb:",comb)
            ways.add(tuple(comb))
        else:
            for i in range(len(coins)):
                new = [comb[j]+1 if j==i else comb[j] for j in range(len(comb))]
                q.append(new)
    return len(ways)

def change(amount,coins):
    n = len(coins)
    memo = [[-1] * (amount + 1) for i in range(n)]

    def numberOfWays(i, amount):
        if amount == 0: return 1
        if i == n: return 0
        if memo[i][amount] != -1:
            return memo[i][amount]
        if coins[i] > amount:
            memo[i][amount] = numberOfWays(i + 1, amount)
        else:
            memo[i][amount] = numberOfWays(i,amount - coins[i]) + numberOfWays(i+1,amount)
        return memo[i][amount]
    return numberOfWays(0,amount)

print(change(5,[1,2,5]))
