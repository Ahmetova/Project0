n = int(input())

if n<1900 and n>3000:
    print('Год должен быть от 1900 до 3000. Введите новое значение')
    n = int(input())

if n % 4 != 0:
    print('Обычный')
elif n % 100 == 0 and n % 400 != 0:
    print('Обычный')
else:
    print('Високосный')