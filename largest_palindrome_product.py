# One of LeetCode's least popular problems
# https://leetcode.com/problems/largest-palindrome-product/
# similar to Project Euler's Largest Palindrome Product
# https://projecteuler.net/problem=4


from time import time

start = time()
def isPalindrome(n):
    return str(n) == str(n)[::-1]

def digits(factorlist,n):
    a,b = factorlist
    return len(str(a)) == n and len(str(b)) == n

def factors(n,ndigits):
    """Returns factors of n that both contain digits digits"""
    for a in range(10**(ndigits)-1,10**(ndigits-1),-1):
        if n % a == 0:
            return digits([a,n//a],ndigits)
    return False

def largestPalindrome(n,testing=False):
    """Return largest palindromic integer that can be
    expressed as the product of two n-digit numbers.
    Like n = 2
    output is 987, which is 99x91.
    The Euler question is when n = 3.
    My first idea is to generate the palindromes
    backwards from 1000x1000.
    Then I thought, just multiply the 3-digit numbers
    backwards and check if they're palindromes."""

    # pals = set()
    #
    # for i in range(10**n,10**(n-1),-1):
    #     for j in range(10 ** n, 10 ** (n - 1), -1):
    #         if isPalindrome(i*j):
    #             pals.add((i,j,i*j))
    #             #if len(pals) > 10:
    #                 #return max(pals)
    # return pals#max(pals)

    """Then I thought, what if I went backwards through the numbers
    and if one is a palindrome, factor it. If the factors are
    n-digit numbers, return it."""

    # startnum = 10**(n) - 1#(10**(n))**2
    # for i in range(startnum,startnum//10,-1):
    #     #generate palindrome:
    #     p = str(i) + str(i)[::-1]
    #     if testing:
    #         print("p:",p)#i,"is a palindrome")
    #     if factors(int(p),n):
    #         return int(p) % 1337

    """Then I used a little algebra to generate the p's.
    Doesn't work."""
    p = 0
    coeffs = [0]*n
    for i in range(n):
        coeffs[i] += 10**i + 10**(2*n-i-1)
    #print(coeffs)

    for a in range(9,0,-1):
        for b in range(9,-1,-1):
            for c in range(9,-1,-1):
                p = sum([a*])


for x in range(2,6):
    print(x,largestPalindrome(x))

print("Time:",round(time()-start,1))