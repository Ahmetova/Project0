import numpy as np

with open('input_ex03.txt') as f:
    string = f.read().strip().lower()
    words = string.split()
    elements = np.unique(words)
    n = 0
    count = 0
    for i in range(0, len(elements)):
        if words.count(elements[i]) > n:
            n = words.count(elements[i])
            count = i
    myfile = open("output_ex03.txt", "w+")
    myfile.write(str(elements[count]) + ' ' + str(words.count(elements[count])))
