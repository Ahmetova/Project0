print('Введите количество программистов:')

n = int(input())

# Списки чисел для окончаний
list1 = [2, 3, 4]
list2 = [12, 13, 14]

if n < 0:
    print('В комнате не может быть отрицательное количество программистов. Введите новое значение:')
    n = int(input())

text = 'программист'

if n % 10 == 1 and n % 100 != 11:
    print(n, text)
elif (n % 100 in list1) and (not n % 100 in list2):
    print(n, text + 'a')
else:
    print(n, text + 'ов')
