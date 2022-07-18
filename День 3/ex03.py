print('Введите три числа:')

a = int(input())
b = int(input())
c = int(input())

# Функция вывода данных
def output(max, min, x):
    print(max, min, x, sep=' ,')

maxim = max([a, b, c])
minim = min([a, b, c])

if a != maxim and a != minim:
    output(maxim, minim, a)
elif b != maxim and b != minim:
    output(maxim, minim, b)
elif c != maxim and c != minim:
    output(maxim, minim, c)
elif a == b and b == c:
    print('Все числа одинаковые:')
    output(maxim, minim, b)
elif a == b:
    print('Имеются одинаковые числа:')
    output(maxim, minim, b)
elif c == b:
    print('Имеются одинаковые числа:')
    output(maxim, minim, b)
elif c == a:
    print('Имеются одинаковые числа:')
    output(maxim, minim, a)