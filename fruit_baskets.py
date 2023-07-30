import random
def totalFruit(fruits,testing=False):
    highest = 0

    for i in range(len(fruits) - 1):
        j = i + 2
        if testing:
            print("i,j:",i,j)

        # find first window with 2 diff nums
        while i + j < len(fruits) and len(set(fruits[i:j + 1])) < 2:

            if testing:
                print("first:",i,j,fruits[i:j+1])
            j += 1
        highest = max(highest, j - i)
        # widen window
        while j < len(fruits) and len(set(fruits[i:j + 1])) == 2:
            if testing:
                print(i,j,fruits[i:j+1])
            highest = max(highest, j - i+1)
            j += 1
    return highest

for k in range(10):
    fruits = [random.choice([1,2,3]) for i in range(k)]
    print(fruits,totalFruit(fruits))

with open("fruit_baskets.txt") as f:
    fruits = f.read()#[int(x) for x in f.read().split()]
    print(len(fruits))#,totalFruit(fruits))