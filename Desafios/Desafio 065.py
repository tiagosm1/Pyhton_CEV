resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor  = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digtou {} e amédia foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi  {}'.format(maior, menor))
