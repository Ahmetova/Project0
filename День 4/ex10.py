mylist = []

def function(data):
    newlist = []
    j = 0
    for i in range(0, len(data)):
        if (data[j] % 2) == 0:
            data[j] = round(data[j]/2)
            j += 1
        else:
            del data[j]
    mylist = data

print('Введие список чисел через пробел:')

mylist = list(map(int, input().split()))

function(mylist)

print(mylist)
