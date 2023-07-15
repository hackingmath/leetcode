alpha = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
tests = ['apple',
         'schtschurowskia',
         'polish',
         'tryst',
         'cry']
#T = input()
for w in tests:#i in range(int(T)):
    easy = True
    n = len(w)#int(input())  # number of letters
    if n < 4:
        print("YES")
        continue
    streak = 0
    #w = input()  # word
    for i in range(n - 3):
        print(w[i:i+4])
        if all([letter not in vowels for letter in w[i:i + 4]]):
            easy = False
            break
    if easy:
        print("YES")
    else:
        print("NO")