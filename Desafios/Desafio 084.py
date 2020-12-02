pessoas = list()
dados = list()
totpessoas = totleve = 0
visual = '*-' *30
while True:
    dados.append(str(input('Digite o nome de pessoa:')))
    totpessoas += 1
    dados.append(int(input('Digite o peso da pessoa:')))
    resp = (str(input('Deseja continuar? [S/N]')))
    pessoas.append(dados[:])
    dados.clear()
    if resp in 'Nn':
        break
print(visual)
for p in pessoas:
    if p[1] >= 80:
        print(f'{p[0]} está acima do peso!')
    else:
        print(f'{p[0]} está abaixo do peso!')
        totleve += 1
print(f'Foram cadastradas {totpessoas} pessoas na lista, sendo {totleve} abaixo dos 80Kg')
print(visual)
