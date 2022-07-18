print('Введите два числа и операцию:')

x = float(input())
y = float(input())
sign = input()

if sign == '+':
    print(x + y)
elif sign == '-':
    print(x - y)
elif sign == '/':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x / y)
elif sign == '*':
    print(x * y)
elif sign == 'mod':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x % y)
elif sign == 'pow':
    print(x ** y)
elif sign == 'div':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x // y)
