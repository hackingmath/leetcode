def maxDigit(num):
    return max([int(n) for n in str(num)])


def maxSum(nums):
    output = -1
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            m1,m2 = maxDigit(nums[i]),maxDigit(nums[j])
            if m1 != m2:
                continue
            else:
                output = max(sum([nums[i],nums[j]]),output)
    return output

a = [51,71,17,24,42]
b = [1,2,3,4]
print(maxSum(a))
print(maxSum(b))
