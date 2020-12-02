n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
soma = multiplicacao = maior = operacao =  0
while operacao != 5:
    print('''Qual operação você deseja fazer:
    [1] SOMA
    [2] MULTIPLCAÇÃO
    [3] MAIOR
    [4] DIGITAR NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    operacao = int(input('Digite a opção desejada:'))
    if operacao == 1:
        soma = n1 + n2
        print('O resultado da soma de {} e {} é: {:.2f}'.format(n1, n2, soma))
    if operacao == 2:
        multiplicacao = n1 * 2
        print('O resultado da multiplicação de {} e {} é: {:.2f}'.format(n1, n2,multiplicacao))
    if operacao == 3:
        if n1>n2:
            print('O número {} é maior que o que {}'.format(n1, n2))
        if n1<n2:
            print('O número {} é maior que o que {}'.format(n2, n1))
        if n1 == n2:
            print('Não existe valor maior os dois são iguais!!')
if operacao == 4:
    print('Digite os novos números: ')
if operacao != [1,2,3,4]:
    print('Operação {} não existe tente novamente: '.format(operacao))
print('FIM')
