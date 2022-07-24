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

string = []
for i in range(n):
    string.append(input())

words = []
for i in range(0, len(string)):
    words.append(string[i].split(";"))

# Составим список команд
comands1 = []
for i in range(0, len(words)):
    comands1.append(words[i][0])
    comands1.append(words[i][2])

comands = np.unique(comands1)

all_plays = [0, 0, 0]
win = [0, 0, 0]
dead_heat = [0, 0, 0]
losing = [0, 0, 0]
count = []

for i in range(0, len(comands)):
    all_plays[i] = comands1.count(comands[i])

for j in range(len(comands)):
    for i in range(0, n):
        if comands[j] == words[i][0]:
            if int(words[i][1]) > int(words[i][3]):
                win[j] += 1
            elif int(words[i][1]) < int(words[i][3]):
                losing[j] += 1
            else:
                dead_heat[j] += 1
        elif comands[j] == words[i][2]:
            if int(words[i][1]) < int(words[i][3]):
                win[j] += 1
            elif int(words[i][1]) > int(words[i][3]):
                losing[j] += 1
            else:
                dead_heat[j] += 1

for i in range(len(comands)):
    print(comands[i], ':', all_plays[i], win[i], dead_heat[i], losing[i], win[i]*3+dead_heat[i])