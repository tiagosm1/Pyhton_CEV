print('=-'*20)
print('10 termos de uma PA')
print('=-'*20)
pt = int(input('Insira o primeiro termo da PA: '))
raz = int(input('Insira a razão da PA: '))
decimo = print(10 + 1)
for c in range(pt, 11, raz):
    print('{}'.format(c), end=' -> ')
print('ACABOU')