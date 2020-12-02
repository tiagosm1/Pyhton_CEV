num = int(input('Escolha um número para saber sua tabuada:'))
tab = 0
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(num, c, num*c))