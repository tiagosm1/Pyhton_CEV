numeros = []
while True:
    n = int(input('Digite um número:'))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso.')
    else:
        print('Numero duplicado. Impossível adicionar.')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
print('='*30)
numeros.sort()
print(numeros)