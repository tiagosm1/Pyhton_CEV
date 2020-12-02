numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito')
while True:
    n1 = int(input('Digite um número entre 0 e 20:'))
    if 0 <= n1 <=8:
        break
    print('Tente novamente', end=' ')
print(f'Você digitou o número {numero[n1]}')