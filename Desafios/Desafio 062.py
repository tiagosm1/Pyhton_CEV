print('=-'*20)
print('Termos de uma PA')
print('=-'*20)
pt = int(input('Insira o primeiro termo da PA: '))
raz = int(input('Insira a razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais deseja?'))
print('FIM')
