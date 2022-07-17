import cmath
import matplotlib.pyplot as plt
import numpy as np

from decimal import Decimal

# Функция форматирования вывода
def format_float(f):
    d5 = Decimal(str(f));
    return d5.quantize(Decimal(1)) if d5 == d5.to_integral() else d5.normalize()

print('Введите коэффициенты квадратного уравнения:')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

# Подсчет дискриминанта
d = b ** 2 - 4 * a * c

if a == 0 and b == 0:
    print('Решений нет')
elif d == 0:
    print('Дискриминант = 0, следовательно, имеем два одинаковых корня:')
    x1 = -b / (2 * a)

    print('x=', format_float(x1))

    # Построение графика
    y1 = a * x1 * x1 + b * x1 + c

    x = np.linspace((-10 + x1), (x1 + 10), 50)
    y = a * x * x + b * x + c

    plt.plot(x, y)
    plt.plot(x1, y1, 'ro')
    plt.title("График квадратного уравнения")  # заголовок
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()
    plt.show()
elif d > 0:
    print('Дискриминант > 0, следовательно, имеем два действительных корня:')
    x1 = round((-b + d ** (0.5)) / (2 * a), 1)
    x2 = round((-b - d ** (0.5)) / (2 * a), 1)
    print('x_1 =', format_float(x1), ', x_2 =', format_float(x2))

    # Построение графика
    y1 = a * x1 * x1 + b * x1 + c
    y2 = a * x2 * x2 + b * x2 + c

    max1 = max([x1, x2])
    min1 = min([x1, x2])

    x = np.linspace((-10 + min1), (10 + max1), 50)
    y = a * x * x + b * x + c

    plt.plot(x, y)
    plt.plot([x1, x2], [y1, y2], 'ro')
    plt.title("График квадратного уравнения")  # заголовок
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()
    plt.show()
else:
    print('Дискриминант < 0, следовательно, имеем два комплексных корня:')
    d1 = round(-b / (2 * a), 1)
    m1 = round((abs(d) ** (0.5)) / (2 * a), 1)
    d2 = round(-b / (2 * a), 1)
    m2 = round((abs(d) ** (0.5)) / (2 * a), 1)
    print(f'x_1 = {format_float(d1)} + {format_float(m1)}i,',
          f' x_2 = {format_float(d2)} - {format_float(m2)}i')
    # print('x_1 = ', (-b + cmath.sqrt(d)) / (2 * a), ', x_2 = ', (-b - cmath.sqrt(d)) / (2 * a))

    # Построение графика
    plt.plot([d1, d2], [m1, -m2], 'ro')
    plt.title("График комплексных решений")  # заголовок
    plt.xlabel("Rez(x)")  # ось абсцисс
    plt.ylabel("Im(y)")  # ось ординат
    plt.grid()
    plt.show()
