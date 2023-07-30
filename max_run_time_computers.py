def maxRunTime(n,batteries):
    batteries.sort(reverse=True)
    extra_power = sum(batteries[n:])
    left,right = 1,sum(batteries)//n
    res = 1
    while left <= right:
        mid = (left+right)//2
        total_power = extra_power
        for i in range(n):
            total_power += min(batteries[i],mid)
        if total_power//n >= mid:
            res = max(res,mid)
            left = mid + 1
        else:
            right = mid - 1
    return res

print(maxRunTime(2,[3,3,3]))
