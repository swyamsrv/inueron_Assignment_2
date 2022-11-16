"""QUESTION 1"""
k = 5
for i in range(1, 2*k+1):
    if i > k:
        for j in range(2*k, i, -1):
            print('* ', end='')
        print()
    else:
        for j in range(i):
            print('* ', end='')
        print()

"""QUESTION 2"""

word = input()
temp = ''
for i in range(len(word)-1, -1, -1):
    temp += temp.join(word[i])
print(temp)
