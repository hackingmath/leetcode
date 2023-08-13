
def minimizeMax(nums, p):
    n = len(nums)
    nums = sorted(nums)

    def countValidPairs(t):
        """t: threshold"""
        count = 0
        i = 0
        while i <= n - 2:
            if nums[i + 1] - nums[i] <= t:
                count += 1
                i += 1
            i += 1
        return count

    l, r = 0, nums[- 1] - nums[0]
    while l < r:
        print("l,r:",l,r)
        m = l + (r - l) // 2
        if countValidPairs(m) >= p:
            r = m
        else:
            l = m + 1
    return l

print(minimizeMax([10,1,2,7,1,3],2))