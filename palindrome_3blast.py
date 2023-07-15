T = ['aaaaa','abcde','aabcd']
for i in range(len(T)):
    palind = False
    n = len(T[i])
    s = T[i]
    if s == s[::-1]:
        print("YES")
        continue
    for j in range(1,n):
        s2 = s[:j-1]+s[j+2:]
        print("s2:",s2)
        if s2 == s2[::-1]:
            palind = True
            break
    if palind:
        print("YES")
    else:
        print("NO")