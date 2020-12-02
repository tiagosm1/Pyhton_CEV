from random import randint
computador = randint(0, 10)
print('Sou seu  seu computador acabei de pensar em um numero entre 0 e 10')
print('Será que voicê consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1 #o contador de palpite entra quando tiver jogada
    if jogador == computador:
        acertou = True
    elif jogador > computador:
        print('Tente um número menor')
    else:
        print('Tente um número maior.')
print('Acertou em {} palpites'.format(palpite))
