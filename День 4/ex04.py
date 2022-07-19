print('Введие список чисел через пробел:')

mylist = list(map(int, input().split()))

sumlist =[]

if len(mylist) == 1:
    sumlist.append(mylist[0])
else:
    for i in range(0, len(mylist)):
        if i == 0:
            sumlist.append(mylist[i + 1] + mylist[-1])
        elif i == (len(mylist) - 1):
            sumlist.append(mylist[i - 1] + mylist[0])
        else:
            sumlist.append(mylist[i + 1] + mylist[i - 1])

print(*sumlist, sep=' ')