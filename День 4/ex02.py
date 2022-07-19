print('Введите геномную последовательность без пробелов (набор букв):')
text = input()

# Проверка наличия гуанина и цитозина
flag_g = 0
flag_c = 0
for i in range(0, len(text)):
    if text[i] == 'g' or text[i] == 'G':
        flag_g = 1
    elif text[i] == 'c' or text[i] == 'C':
        flag_c = 1

if flag_g == 0 or flag_c == 0:
    print('В геномной последовательности должны содержаться гуанин (g/G) и цитозин (c/C). Введите новую последовательность:')
    text = input()

# Подсчет g и c
count = 0
for i in range(0, len(text)):
    if text[i] == 'g' or text[i] == 'G' or text[i] == 'c' or text[i] == 'C':
        count += 1

print('GC-состав:', count*100/len(text))