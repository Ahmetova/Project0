print('Введите ДНК последовательность без пробелов (набор букв):')
text = input()

data = []

i = 1
while i <= len(text):
    if i == (len(text)) or len(text) == 0:
        data.append(text[-1])
        data.append(1)
        i += 1
    elif text[i] != text[i - 1]:
        data.append(text[i - 1])
        data.append(1)
        i += 1
    else:
        count = 0
        j = i
        while text[j] == text[j - 1]:
            count += 1
            j += 1
            if j >= len(text):
                break
        data.append(text[i])
        data.append(count + 1)
        i = j + 1

print(*data, sep='')
