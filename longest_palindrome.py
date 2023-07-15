def longestPalindrome(s,testing=False):
    if len(s) == 1: return s
    longest = 0
    longest_str = None
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            strij = s[i:j]
            if testing:
                print(strij)
            if if strij == strij[::-1]:
                if len(strij) > longest:
                    longest_str = strij
                    longest = len(strij)
    return longest_str

print(longestPalindrome("bb",True))