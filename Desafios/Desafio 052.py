n = int(input("Insira um número inteiro:"))
tot = 0
for c in range (1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes (por 1 e por ele mesmo)'.format(n, tot))
if tot ==2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo!')
