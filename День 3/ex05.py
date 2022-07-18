print('Введите список из 6-ти чисел через пробел:')

mylist = list(map(int, input().split()))

if len(mylist) != 6:
    print('Написано же! Шесть чисел! Введите новые числа:')
    mylist = list(map(int, input().split()))

flag = 0
for i in range(0, len(mylist)):
    if (mylist[i] < 0) or (mylist[i] > 9):
        flag = 1

if flag == 1:
    print('Все числа должны находиться в диапазоне [0, 9]. Введите новые числа:')
    mylist = list(map(int, input().split()))

if (mylist[0] + mylist[1] + mylist[2]) == (mylist[3] + mylist[4] + mylist[5]):
    print('Счастливый')
else:
    print('Обычный')