#a + 2ab + b = 8, what is a + b?

#after some algebra I got

def b(a):
    return (8-a)/(2*a+1)

for a in range(1,10):
    print(a,b(a),a+2*a*b(a) + b(a),a+b(a))