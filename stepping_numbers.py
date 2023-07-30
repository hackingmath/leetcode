def isStepping(n):
    if len(n) == 1:
        return True
    for i,v in enumerate(n):
        if i > 0:
            #print(i)
            if abs(int(v)-int(n[i-1])) != 1:
                return False
        if i < len(n)-1:
            if abs(int(v)-int(n[i+1])) != 1:
                return False
    return True

def countSteppingNumbers(low,high):
    output = 0
    for i in range(int(low),int(high)+1):
        if isStepping(str(i)):
            output += 1
    return output

print(countSteppingNumbers('90','101'))