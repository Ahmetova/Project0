print('Введите количество биологов и инфарматиков:')

a = int(input())
b = int(input())

# Проверка ввода данных
if a <= 0 or b <= 0:
    print('В командах может быть только положительное количество игроков. Введите новые значения:')
    a = int(input())
    b = int(input())

maxim = max(a, b)

flag = 0
while flag == 0:
    if (maxim % a == 0) and (maxim % b == 0):
        answer = maxim
        flag = 1
    else:
        maxim += 1

print('Наименьшее общее кратное:', answer)