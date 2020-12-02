produtos = ('Lápis', 1.30, 'Caneta', 2.50, 'Borracha', 1.90,
            'Calculadora', 45.60)linha = '='*50
titulo = 'LISTA DE PREÇOS'

print(linha)
print(titulo.center(50))
print(linha)
for pos in range (0, len(produtos)):#tudo que tiver na lista produtos da posição 0 até o ultimo
    if pos %2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f'R$:{produtos[pos]:.>5.2f}')
print(linha)