from random import randint
print('Jogo do PAR ou ÍMPAR!!!')
v=0
while True:
    jogador = int(input('Faça sua jogada: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer par ou impar: ')).strip().upper()[0]
        print(f'Você escolheu {jogador} e o computador {computador}. Total = {total}')
        print('Deu par' if total %2 == 0 else 'Deu impar' )
    if tipo == 'P':
        if total%2 == 0:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total%2 == 1:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente?')
print(f'GAME OVER, você venceu {v} vezes!')
