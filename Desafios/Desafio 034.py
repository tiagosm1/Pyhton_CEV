salario = float(input('Digite seu salário: '))
n1 = float
n2 = float
if salario >= 1250.00:
    n1 = (salario*10 /100) + salario
    print('Seu salário com aumento de 10% é de R$ {}'.format(n1))
else:
    salario <= 1250.00
    n2 = (salario*15 /100) + salario
    print('Seu salário com aumento de 15% é de R$ {}'.format(n2))
