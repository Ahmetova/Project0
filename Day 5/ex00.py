from collections import Counter
import numpy as np

print('Введие слова через пробел:')
mylist = list(map(str, input().split()))

for i in range(0, len(mylist)):
    mylist[i] = mylist[i].lower()

# Первый способ
# print(Counter(mylist))

# Второй способ
elements = np.unique(mylist)

for i in range(0, len(elements)):
    print(elements[i], mylist.count(elements[i]))
