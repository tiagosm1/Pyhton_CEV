numeros = [[],[]]
valor = 0
menu = '*'*100
for c in range(1,8):
    valor = (int(input('Insira os numeros:')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(menu)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados são: {numeros[0]}')
print(f'Os números pares digitados são: {numeros[1]}')
print(menu)



