totamasc = tot18 = tot20 = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digita o sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totamasc += 1
    if sexo == 'F' and idade <20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Temos {totamasc} homens cadastrados.')
print(f'Temos {tot20} mulheres com menos de 20 anos')

