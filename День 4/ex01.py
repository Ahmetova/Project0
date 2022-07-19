print('Введите натуральные числа a, b, c ,d:')

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Проверка ввода данных
if a > b or c > d or a > 10 or b > 10 or c > 10 or d > 10:
    print('Ошибка ввода данных. a<=b и c<=d и a,b,c,d<=10. Введите новые значения:')
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

# Списки из диапазонов
list1 = []
list2 = []
for i in range(c, d+1):
    list1.append(i)
for i in range(a, b+1):
    list2.append(i)

print(' ',*list1, sep='\t', end='\n')
for i in range(0, len(list2)):
    print(list2[i], '\t', end='')
    for j in range(0, len(list1)):
        print(list2[i]*list1[j], '\t', end='')
    print(end='\n')