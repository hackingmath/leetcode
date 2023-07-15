def longestSubsequence2(arr,difference,testing=False):
    longest, streak = 0, 0
    counting = False
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            if arr[i + j] - arr[i] == difference:
                counting = True
                streak += 1
                if testing:
                    print(i,j,arr[i:i+j+1],streak)
            else:
                if counting:
                    if testing:
                        print(i,j,arr[i:i+j+1],"else")
                    counting = False
                    longest = max(longest,streak)
                    streak = 0
    return longest

from collections import deque
def longestSubsequence(arr,difference,testing=False):
    if difference == 0:
        return max([arr.count(n) for n in arr])
    max_length = 0
    sdict = dict()
    for n in arr:
        if n - difference in sdict:
            sdict[n] = sdict[n - difference] + 1
            max_length = max(max_length, sdict[n - difference] + 1)
            print(n,max_length,sdict)
        else:
            if n not in sdict:
                sdict[n] = 1
                max_length = max(max_length, 1)
                print("else:",n,max_length,sdict)
        if max_length>2:
            print('over 2',n,max_length,sdict)
    return max_length


print(longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8],0,True))