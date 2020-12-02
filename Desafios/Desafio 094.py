pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo {M/F}:'))
        if pessoa['sexo'] in 'MmFf':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? {S/N}')).upper()[0]
        if resp in 'SN':
            break
        print('Responda somente S ou N')
    if resp == 'S':
        break
print(f'Ao todos temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print("  ")
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('ENCERRADO')
