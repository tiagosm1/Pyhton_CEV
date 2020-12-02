numeros = list()
pares = list()
impares = list()
menu = '-='*30
while True:
    numeros.append(int(input(f'Digite um número:')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i,v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(menu)
print(f'Os numeros inseridos foram:{numeros}')
print(f'Os pares fora:{pares}')
print(f'Os impares foram: {impares}')
print(menu)
