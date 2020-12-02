total = totmil = menorvalor = cont = 0
while True:
    produto = str(input('Digite o produto: '))
    valor = float(input('Digite o valor: '))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1:
        menorvalor = valor
    else:
        if valor < menorvalor:
            menorvalor = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de produtos foi R$: {total:.2f}')
print(f'Foram {totmil} produtos valendo mais de R$:1000,00')
print(f'O menor valor encontrado foi de R$: {menorvalor:.2f}')
