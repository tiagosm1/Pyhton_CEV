r1 = float(input('Insira o valor da primeira reta: '))
r2 = float(input('Insira o valor da segunda reta: '))
r3 = float(input('Insira o valor da terceira reta: '))

if r1 <= 0 or r2 <= 0 or r3 <= 0:
    print('Os valores não podem ser negativos!!!')

if r1 >= r2+r3 or r2 >= r1+r3 or r3 >= r1+r2:
    print('Os valores não podem formar um triangulo!!!')
else:
    print('Os valores formam um triangulo!!')