print('Введите число:')
n = int(input())

if n < 0:
    print('Число должно быть положительным! Введите новое значение:')
    n = int(input())

data = []
j = 1

while len(data) != n:
    for i in range(1, j+1):
        data.append(j)
        if len(data) == n:
            print(data)
            break
    j += 1
