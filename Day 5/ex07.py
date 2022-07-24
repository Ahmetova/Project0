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
    words.append(string[i].split())

for i in range(0, len(words)):
    if words[i][0] == 'север':
        y1 = int(words[i][1])
    elif words[i][0] == 'юг':
        y2 = int(words[i][1])
    elif words[i][0] == 'запад':
        x2 = int(words[i][1])
    elif words[i][0] == 'восток':
        x1 = int(words[i][1])

print(x1-x2, y1-y2)