print('Введие список чисел через пробел:')

mylist = list(map(int, input().split()))

sum = 0
for i in range(0, len(mylist)):
    sum += mylist[i]

print(sum)
