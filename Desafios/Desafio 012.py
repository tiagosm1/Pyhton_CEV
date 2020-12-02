#n1 = float(input("Insira o valor para dar 5% de desconto R$: "))
#desc = (n1*5)/100
#print('O valor inserido com desconto de 5% é de R$: {:.2f} '.format(desc))

preco = float(input('Qual o preço do produto? R$:'))
novo = preco - (preco*5/ 100)
print('O produto que custava R$:{}, na promoção com desconto de 5% vai custar R$:{:.2f}.'.format(preco, novo))



