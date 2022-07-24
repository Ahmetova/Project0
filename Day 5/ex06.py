import numpy as np


def vvod():
    while True:
        try:
            n = int(input())
        except ValueError:
            print('Число должно быть целым и положительным. Введите новое число:')
        else:
            return n
            break


n = -1
while n <= 0:
    n = vvod()

words = []
for i in range(n):
    words.append(input().lower())

m = -1
while m <= 0:
    m = vvod()

string = []
for i in range(m):
    string.append(input().lower())

sentence = []
for i in range(0, len(string)):
    sentence.append(string[i].split())

mistakes = []
for i in range(0, len(sentence)):
    for j in range(0, len(sentence[i])):
        if sentence[i][j] not in words:
            mistakes.append(sentence[i][j])

# print(*np.unique(mistakes))

for i in range(0, len(np.unique(mistakes))):
    print(np.unique(mistakes)[i])