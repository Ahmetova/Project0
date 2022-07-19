sum = 0
quad_sum = 0
data = []

while quad_sum == 0:
    number = int(input())
    sum += number
    data.append(number)
    if sum == 0:
        for i in range(0, len(data)):
            quad_sum += data[i] ** 2
        print('Сумма квадратов', quad_sum)
        break
