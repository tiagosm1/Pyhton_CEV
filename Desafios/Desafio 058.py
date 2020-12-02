from random import randint
from time import sleep
print('==='* 20)
print('Vou pensar em um número entre 0 e 5.')
print('==='* 20)
n1 = int(input("Em que número eu pensei?"))
n2 = randint(0, 5)#gera número inteiro aleatório entre os ()
cont = 0
print('Processando...')
sleep(2)
while n1 != n2:
    cont += 1
    n1 = int(input('Você errou eu pensei no {} e você no {}! TENTE NOVAMENTE: '.format(n2, n1)))
    n2 = randint(0, 5)  # gera número inteiro aleatório entre os ()
    print('Processando...')
    sleep(2)
    if n1 == n2:
        print('Você ganhou eu pensei no {} e você no {}! Foram {} tentativas para isso.'.format(n2, n1, cont))
    else:
        print('Você perdeu! eu pensei no {} e não no {}'.format(n2, n1))
