number = 1

while number <= 100:
    number = int(input())
    if number > 100:
        print('Вы ввели число большее 100. Конец.')
        break
    if number < 10:
        continue
    print('Число в диапазоне [10, 100]:',number)