#https://leetcode.com/problems/sliding-window-maximum/
#
with open('sliding_window.txt','r') as f:
    data = f.read().split(',')#[int(x) for x in f.readline().split()]
    print(data[:4],data[-5:])
    nums = list()
    for n in data:
        n = n.replace('[','')
        n = n.replace(']','')
        n = n.replace('\n','')
        nums.append(int(n))
    print(nums[:4],nums[-5:])

def maxSlidingWindow(nums, k):
    # output = list()
    # maxk = 0
    # for i in range(len(nums)-k+1):
    #     maxk = max(nums[i:i+k])
    #     output.append(maxk)
    # return output
    #nums = tuple(nums)
    n = len(nums)
    print("len(nums)",n)
    #return [max(nums[i:i + k]) for i in range(n - k + 1)]
    for i in range(n-k+1):
        m = max(nums[i:i+k])
        #print(m)

print(maxSlidingWindow(nums,50000))