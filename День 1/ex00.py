# Ввод данных
x = int(input())
y = int(input())

#def isfloat(x):
#    try:
#        print('Число часов должно быть целое. Введите новое значение')
#        x = int(input())

#def isfloat(y):
#    try:
#        print('Число минут должно быть целое. Введите новое значение')
#        y = int(input())

if y > 60:
    print('Минут должно быть меньше 61. Введите новое значение для минут')
    y = int(input())

print(x * 60 + y)