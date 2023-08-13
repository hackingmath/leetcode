def validPartition1(nums):
    n = len(nums)
    #if n < 4: return False
    def valid(nums2):
        n = len(nums2)
        if n < 2: return False
        if n == 2:
            return nums2[0] == nums2[1]
        if n == 3:
            if all([i == nums2[0] for i in nums2]):
                return True
            if (nums2[2]-nums2[1]) == (nums2[1] - nums2[0]) == 1:
                return True
            print("diffs not 1")
            return False
        return False
    if valid(nums[:2]):
        if len(nums[2:]) > 3:
            if validPartition(nums[2:]): return True
        else:
            if valid(nums[2:]): return True
    if valid(nums[:3]):
        if n == 3: return True
        if len(nums[3:]) > 3:
            if validPartition(nums[3:]): return True
        else:
            if valid(nums[3:]): return True
    return False

def validPartition2(nums):
    n = len(nums)
    if n < 2: return False
    if n == 2:
        return nums[0] == nums[1]
    if n == 3:
        if all([i == nums[0] for i in nums]):
            return True
        if nums[2] - nums[1] == nums[1] - nums[0] == 1:
            return True
        return False
    else:
        return (validPartition2(nums[:2]) and validPartition2(nums[2:])) or \
            (validPartition2(nums[:3]) and validPartition2(nums[3:]))

def validPartition(nums):
    

print(validPartition2([4,4,4,5,6]))
print(validPartition2([1,1,1,2]))
print(validPartition2([803201,803201,803201,803201,803202,803203]))
print(validPartition2([10,20,30]))
print(validPartition2([473928,473929,473930]))