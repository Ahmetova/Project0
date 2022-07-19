print('Введите список через пробел:',end='\n')
a=list(map(int,input().split()))
print(a[::-1])