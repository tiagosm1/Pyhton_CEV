def areaterreno(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {l} x {c} é de {a} m²')

tela = '*-*' * 10
print(tela)
print('Controle de terreno.')
print(tela)
l = float(input('Largura (m):'))
c = float(input('Comprimento (m): '))
areaterreno(l, c)