valorcasa = float(input('Insira o valor do imóvel:'))
salario = float(input('Insira o seu salário:'))
anos = float(input('Em quantos anos deseja pagar?'))
mes = anos * 12
valorprestacao = valorcasa / mes
if valorprestacao >= salario*0.30:
    print('O valor da prestação é R$:{:.2f} e excede o máximo de 30% do seu salário !! \033[7;31m NÃO APROVADO\033[7;31m'.format(valorprestacao))
elif valorprestacao <= salario*0.30:
    print('O valor da prestação é de R$:{:.2f} e seu crédito está: \033[32mAPROVADO'.format(valorprestacao))