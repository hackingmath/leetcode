def sum_of_n(n, a1, an):
    return n / 2 * (a1 + an)


def missingNumber(nums):
    #sorted_nums = sorted(nums)
    a1,an = min(nums),max(nums)
    n = an-a1+1
    return sum_of_n(n,a1,an)-sum(nums)

#print(sum_of_n(100,1,100))
print(missingNumber([9,6,4,2,3,5,7,0,1]))