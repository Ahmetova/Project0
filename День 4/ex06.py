print('Введие список чисел через пробел:')

mylist = list(map(int, input().split()))

data = []

for i in range(0, len(mylist)-1):
    for j in range(i+1, len(mylist)):
        if mylist[i] == mylist[j]:
            data.append(mylist[i])

print(set(data))
