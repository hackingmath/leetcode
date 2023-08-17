from collections import deque

def maxSlidingWindow(nums,k):
    # for i in range(0, len(nums) - k + 1):
    #     nums[i] = max(nums[i:k + i])
    # return nums[:len(nums) - k + 1]
    # sliding window try 8/16/23
    # out = list()
    # c
    # m = max(nums[i:j])
    # out.append(m)
    # while j < len(nums):
    #     i += 1
    #     j += 1
    #     print("1:",i, j, out)
    #     if nums[j-1] > m:
    #         m = nums[j-1]
    #         out.append(m)
    #         continue
    #     elif nums[i - 1] == m:
    #         m = max(nums[i:j])
    #     out.append(m)
    #     print("2:",i,j,out)
    # return out
    q = deque()
    out = list()
    for i, n in enumerate(nums):
        while q and nums[q[-1]] < n:
            q.pop()
        q.append(i)
        if q[0] == i-k:
            q.popleft()
        if i>=k-1:
            out.append(nums[q[0]])
    return out




print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))