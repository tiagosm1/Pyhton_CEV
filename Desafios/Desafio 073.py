time = ('Internacional', 'Flamengo', 'Atlético-MG','Fluminense', 'São Paulo', 'Santos',
        'Palmeiras', 'Fortaleza', 'Grêmio', 'Ceará', 'Atlético-GO',
        'Sport', 'Corinthians', 'Bahia', 'Bragantino', 'Botafogo',
        'Vasco', 'Athletico-PR', 'Coritiba', 'Goiás')
print('='*50)
print('Tabela dos times do brasileirão - 26/10/2020')
print('='*50)
print(f'Os 5 primeiros colocados são:{time[0:5]} ')
print('='*50)
print(f'Os últimos 4 colocados são:{time[16:21]}' )
print('='*50)
print(f'Os times em ordem alfabética são: {sorted(time)}')
print('='*50)
print(f'O São Paulo está na {time.index("São Paulo")+1}ª posição')
print('='*50)
