n1 = soma = 0
while n1 != 999:
    n1 = int(input('Digite a sequência de numeros:'))
    soma += n1
    if n1 == 999:
        soma -= 999
print('A soma dos valores digitados é: {} '.format(soma))