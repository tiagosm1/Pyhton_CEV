print('=-'*20)
print('10 termos de uma PA')
print('=-'*20)
pt = int(input('Insira o primeiro termo da PA: '))
raz = int(input('Insira a razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print(' {} -> '.format(termo), end='')
    termo = termo + raz
    cont += 1