from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Sua opções são:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Insira sua jogada:'))
sleep(0)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*13)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-='*13)

if computador == 0:
    if jogador == 0:
        print(' EMPATE')
    elif jogador == 1:
         print('JOGADOR VENCE')
    elif jogador == 2:
         print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')

