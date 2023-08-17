def diff(a,b):
    return (a > 0 and b < 0) or (a < 0 and b > 0)

def collide(a,b):
    a2,b2 = abs(a),abs(b)
    if a2 > b2:
        return a
    elif b2 > a2:
        return b
    else:
        return 0


def asteroidCollision(asteroids):
    while True:
        changes = 0
        for i, a in enumerate(asteroids):
            newlist = list()
            if i < len(asteroids) - 1:
                print(i,a,changes,newlist)
                if diff(a,asteroids[i+1]):
                    changes += 1
                    c = collide(a,asteroids[i+1])
                    if c == 0:

                        continue
                    else:
                        newlist.append(c)

                else:
                    newlist.append(a)
                    continue
        if changes == 0:
            return newlist
        else:
            asteroids = newlist[:]

tests = [[5,10,-5],[8,-8],[10,2,-5]]
for t in tests:
    print("output:",asteroidCollision(t))

