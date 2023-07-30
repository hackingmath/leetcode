
def countCompleteSubarrays(nums):
    d = len(set(nums)) #number of distinct elements
    output = 0
    for i in range(len(nums)):
        j = d
        while i + j < len(nums)+2:
            subarr = nums[i:i+j-1]
            if len(set(subarr)) == d:
                print(subarr)
                output += 1
            j += 1
    return output

print(countCompleteSubarrays([1,3,1,2,2]))