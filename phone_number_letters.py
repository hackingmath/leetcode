from itertools import combinations

def letterCombinations2(digits):
    if len(digits) == 0: return []
    LETTERS = [None,None,"abc","def",'ghi',"jkl","mno","pqrs","tuv","wxyz"]
    output = list()
    digits = [int(x) for x in digits]
    length = len(digits)

    if length == 1: return [letter for letter in LETTERS[digits[0]]]
    output_length = 1 #product of number of letters for each digit
    for i in length(length):
        output_length *= len(LETTERS[i])
    for d in digits:
        n_letters = len(LETTERS[d])
        n_others = output_length/n_letters
        strings = []

        for i in range(n_letters):
            string = ''
            string += 0

from itertools import product

def letterCombinations(digits):
    LETTERS = [None, None, "abc", "def", 'ghi', "jkl", "mno", "pqrs", "tuv", "wxyz"]
    digits = [int(x) for x in digits]
    if len(digits) == 1: return [letter for letter in LETTERS[digits[0]]]
    if len(digits)==2:
        return [''.join(s) for s in list(product(LETTERS[digits[0]],LETTERS[digits[1]]))]
    if len(digits)==3:
        return [''.join(s) for s in list(product(LETTERS[digits[0]],LETTERS[digits[1]],LETTERS[digits[2]]))]
    if len(digits)==4:
        return [''.join(s) for s in list(product(LETTERS[digits[0]],LETTERS[digits[1]],LETTERS[digits[2]],LETTERS[digits[3]]))]

print(len(letterCombinations('234')))