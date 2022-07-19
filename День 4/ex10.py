mylist = []

def function(data):
    newlist = []
    j = 0
    for i in range(0, len(data)):
        #rint('len',len(data), 'j=',j)
        if (data[j] % 2) == 0:
            data[j] = round(data[j]/2)
            j += 1
            #rint(data)
        else:
            del data[j]
            #rint(data)
    mylist = data

print('Введие список чисел через пробел:')

mylist = list(map(int, input().split()))

function(mylist)

print(mylist)
