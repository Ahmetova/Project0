print('Введите время:')

hour = int(input('Час: '))
minute = int(input('Минута: '))

if (hour < 0 or hour > 12) or (minute < 0 or minute > 60):
    print('Час должен находиться в диапазоне [0, 12], а минуты - [0, 60]. Введите новые значения:')
    hour = int(input('Час: '))
    minute = int(input('Минута: '))

# Сопоставим 1 минуту и 1 час с углами
onehour = 30
oneminute = 6

# Часовая стрелка не стоит ровно на часе, когда минута не 0. 
# Поэтому поделим угол одного часа на 60 частей
one_in_hour = 0.5

# Переведем время в углы
newhour = hour * onehour + minute * one_in_hour
newminute = minute * oneminute

# Расчет углами
if newminute >= newhour:
    angle = newminute - newhour
else:
    angle = 360 - (newhour - newminute)

print('Вычисление угла идет от часовой к минутной стрелке по часовой стрелке.')

print(f'Угол равен {angle} градусов.')
