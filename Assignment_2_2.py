"""QUESTION 2"""

word = input()
temp = ''
for i in range(len(word)-1, -1, -1):
    temp += temp.join(word[i])
print(temp)