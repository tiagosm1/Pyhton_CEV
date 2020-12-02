pessoas = {'Nome': 'Tiago', 'Sexo': 'M', 'Idade': 31}
menu = '*-*'*20
print(menu)

print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(menu)

print(pessoas.keys())
print(menu)

print(pessoas.values())
print(menu)

print(pessoas.items() )
print(menu)

for k in pessoas.keys():
    print(k)
print(menu)

for k in pessoas.values():
    print(k)
print(menu)
del pessoas['Sexo']

pessoas['Nome'] = 'Leandro'

pessoas['Idade'] = '21'

for k, v in pessoas.items():
    print(f'{k} = {v}')
print(menu)