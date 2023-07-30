def predictTheWinner(nums):
    p1,p2 = 0,0
    one = True
    while nums:
        choice = max(nums[0], nums[-1])
        if one:
            p1 += choice
            one = False
        else:
            p2 += choice
            one = True
        nums.remove(choice)
        print("p1,p2:",p1,p2)
    return p1 >= p2

tests = [[1,5,2],[1,5,233,7]]
for t in tests:
    print(predictTheWinner(t))


