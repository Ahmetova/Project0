x = int(input())
h = int(input())
m = int(input())

if m > 60:
    print('Минут должно быть меньше 61. Введите новое значение для минут m')
    m = int(input())

minut = h * 60 + m + x

print(minut // 60, end='\n')
print(minut % 60)
