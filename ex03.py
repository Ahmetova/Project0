a = int(input())
b = int(input())
h = int(input())

if a > b:
    print('Неверно указаны временные рамки. Введите новые значения A и B')
    a = int(input())
    b = int(input())

if h < a:
    print('Недосып')
elif h <= b:
    print('Это нормально')
else:
    print('Пересып')