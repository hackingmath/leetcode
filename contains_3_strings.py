from itertools import permutations
def merge(a,b):
    longest = 0
    for i in range(1,len(a)+1):
        if a[-i:] == b[:i]:
            print(a[-i:] == b[:i])
            longest = max(longest,i)
            print("longest:",longest)
    if longest:
        return a[:-longest]+b
    else:
        return a + b

def minimumString(a, b, c):
    first = 'z' * 100
    for d, e, f in permutations([a, b, c], 3):
        print(d, e, f)
        if d in f and e in f:
            return f
        if d + e == f or merge(d, e) == f:
            return f
        if d in f:
            s = merge(e,f)
        elif e in f:
            s = merge(d,f)
        elif f in d:
            s = merge(d,e)
        elif d == e:
            s = merge(d,f)
        else:
            s = merge(merge(d, e), f)
        print(s)
        if len(s) < len(first):
            first = s
            # print('new first',first)
        elif len(s) == len(first):
            if s < first:
                first = s
                # print('newer first', first)
    return first



print(minimumString('aba','c','b'))
#print(minimumString('abc','bca','aaa'))
#print(merge('a','ac'))
