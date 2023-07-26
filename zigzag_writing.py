def convert(s, numRows):
    if numRows == 1:
        return s
    moddict = {i:'' for i in range(numRows)}
    multnum = 2*numRows - 2
    for i,v in enumerate(s):
        m = i%multnum
        if m > multnum/2:
            moddict[multnum - m] += v
        else:
            moddict[m] += v

    output = ''
    for a in moddict:
        output += moddict[a]
    return output

print(convert("PAYPALISHIRING",3))
