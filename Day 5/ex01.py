import math

def vvod():
    while True:
        try:
            n = int(input())
        except ValueError:
            print('Число должно быть целым и положительным. Введите новое число:')
        else:
            return n
            break

def function(x):
    return round(math.exp(x), 3)

n = -1
while n <= 0:
    n = vvod()

data = []
for i in range(n):
    data.append(float(input()))

for i in range(n):
    print(function(data[i]))


