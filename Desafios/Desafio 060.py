'''n = int(input('Digite o valor de n: '))
fat = 1
i = 2
while i <= n:
    fat = fat * i
    i = i + 1
print('O valor de {}! é {}: '.format(n, fat))'''

from math import factorial
n = int(input('Digite o valor para saber seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

