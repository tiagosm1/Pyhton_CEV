lista = list()
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {c}:')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('=='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior número digitado foi o {mai} nas posições:', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')
print(f'O menor número digitado foi o {men} nas posições:', end='')
print()
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
print()


