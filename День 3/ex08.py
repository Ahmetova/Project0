print('Введите диапазон (два числа) через пробел:')

diap = list(map(int, input().split()))

# Создание списка значений
def create_list(l):
    list = []
    for i in range(l[0], l[1]):
        list.append(i)
    list.append(l[1])
    return list

# Проверка, что диапазон введен верно
if diap[0] > diap[1]:
    print('В диапазоне первое число должно быть меньше второго. Введите новые значения через пробел:')
    diap = list(map(int, input().split()))

# Создание списка значений
data = create_list(diap)

# Проверка на наличие в диапазоне числе, кратных трем
flag = 0
for i in range(0, len(data)):
    if (data[i] % 3) == 0:
        flag = 1

if flag == 0:
    print('В диапазоне нет чисел, делящихся на 3 без остатка. Введите новый диапазон через пробел:')
    diapnew = list(map(int, input().split()))
    data = create_list(diapnew)

# Вычисление среднего арифметического
sum = 0
count = 0
for i in range(0, len(data)):
    if (data[i] % 3) == 0:
        sum += + data[i]
        count += 1

print(round(sum/count, 1))