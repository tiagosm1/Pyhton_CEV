'''num = [8, 2, 3, 4, 5, 6, 7, 15]
num[7] = 0
num.append(9)
num.append(10)
num.insert(0, 1)
num.pop(1)
#num.sort(reverse=True)
print(f'Esta lista possui {len(num)} numeros cadastrados.')
print(num)'''



'''num = []
num.append(1)
num.append(5)
num.append(23)
for c, v in enumerate(num):
    print(f'Os valores da lista são {v} na posição {c}')
print('Fim dos valores')'''


valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Os valores da lista são {v} na posição {c}')
print('Fim dos valores')