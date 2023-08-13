import math


def minAbsoluteDifference2(nums,x):
    out = math.inf
    i = 0

    while i + x < len(nums):
        j = x
        while i + j < len(nums):
            print(nums[i],nums[i+j])
            out = min(out,abs(nums[i]-nums[i+j]))
            j += 1
        i += 1

    return out

def minAbsoluteDifference(nums,x):
    out = math.inf

    for i,v in enumerate(nums):
        if i + x < len(nums):
            d = min([abs(v-w) for w in nums[(i+x):]])
            # if i + x >= len(nums) - 1:
            #     break
            # print(v,nums[(i+x):])
            # if v+diff in nums[(i+x):] or v-diff in nums[(i+x):]:
            #     out = min(out,diff)#return diff
            #     if out == 0: return 0
            out = min(out,d)
    return out



print(minAbsoluteDifference([4,3,2,4],2))
print(minAbsoluteDifference([5,3,2,10,15],1))
print(minAbsoluteDifference([1,2,3,4],3))
