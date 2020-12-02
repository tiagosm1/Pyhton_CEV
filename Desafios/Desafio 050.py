som = 0
cont = 0
for c in range(1, 7):
    n = int(input('Insira 6 números inteiros:'))
    if n %2 == 0:
        som += n
        cont += 1
print('Considerando somente os {} números pares inseridos a soma é: {}'.format(cont, som))