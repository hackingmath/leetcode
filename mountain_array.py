def peakIndexInMountainArray(arr):
    # output = 0
    # for i in range(1, len(arr)):
    #     if arr[i] > arr[i - 1]:  # and arr[i] > arr[i+1]:
    #         continue
    #
    #     return i - 1
    # return -1
    #binary search:
    l,r = 0,len(arr)-1
    while True:
        midx = (l+r)//2 #index of term in middle
        if arr[midx] > arr[midx-1]:#increasing
            if arr[midx] > arr[midx+1]:
                return midx
            l = midx
        else: #decreasing
            r = midx



arrs = [[0,1,0],
        [0,2,1,0],
        [0,10,5,2],
        [3,4,5,1]]

for a in arrs:
    print(peakIndexInMountainArray(a))