mylist = []

# Функция ввода данных
def inputs():
    while True:
        try:
            x = int(input())
            mylist.append(x)
        except (ValueError, EOFError):
            return


inputs()

# Проверка наличия нуля в списке
flag = 0
for i in range(0, len(mylist)):
    if mylist[i] == 0:
        flag = 1

if flag == 0:
    print('В списке нет нуля. Введите новый список:')
    mylist = []
    inputs()

# Расчет
i = 0
sum = 0
while mylist[i] != 0:
    sum = sum + mylist[i]
    i = i + 1

print(sum)