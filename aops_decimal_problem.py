#for AoPS application
#July 11, 2023

#0.2_ * 7._ = 2._

DIGITS = '0123456789'

for a in DIGITS:
    for b in DIGITS:
        for c in DIGITS:
            if float('0.2'+a) * float('7.'+b) == float("2."+c):
                print(float('0.2'+a),float('7.'+b),float("2."+c))


