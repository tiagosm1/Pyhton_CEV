'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print ('A soma é: {}'.format(s))
print((f'A soma dos númerosé: {s}'))'''

nome = 'jose'
idade  = 75
salario = 987.3
print(f'O {nome} tem {idade}')
print(f'O {nome:*^20} tem {idade} e ganha R$:{salario:.2f}')