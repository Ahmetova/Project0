import math

print('Введите стороны треугольника:')

a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0 or a < 0 or b < 0 or c < 0:
    print('Стороны треугольника всегда больше 0. Введите новые значения:')
    a = int(input())
    b = int(input())
    c = int(input())

if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print('Сумма любых двух сторон должна быть больше третьей. Иначе такого треугольника не существует. Введите новые значения:')
    a = int(input())
    b = int(input())
    c = int(input())

# Полупериметр
p = (a + b + c) / 2

print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
