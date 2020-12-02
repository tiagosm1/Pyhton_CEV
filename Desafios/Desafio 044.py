preco = float(input('Insira o valor do produto: '))
print('1 - Á VISTA - DINHEIRO/CHEQUE')
print('2 - Á VISTA - CARTÃO')
print('3 - ATÉ 2X CARTÃO')
print('4 - MAIS DE 3X CARTÃO')
condicao = int(input('Insira a condição de pagamento:'))
if condicao == 1:
    precocomdesconto = preco * 0.1
    valorapagar = preco - precocomdesconto
    print('O valor a pagar é de R$: {:.2f} com 10% de desconto!'.format(valorapagar))
elif condicao == 2:
    precocomdesconto = preco * 0.05
    valorapagar = preco - precocomdesconto
    print('O valor a pagar é de R$: {:.2f} com 5% de desconto!'.format(valorapagar))
elif condicao == 3:
    print('O valor a ser pago é de R$: {} sem desconto!'.format(preco))
elif condicao == 4:
    precocomacrecimo = preco * 0.20
    valorapagar = precocomacrecimo + preco
    print('O valor a pagar é de R${} com acrécimo de 20%!'.format(valorapagar))


