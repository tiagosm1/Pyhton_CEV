num = int(input('Digite um número inteiro:'))
print(''' Escolha a opção para conversão:
[1] Converter para binário
[2] Converter para octal
[3] converter para hexadecimal''')
opcao = int(input('Sua Opção:'))
if opcao == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)))
elif opcao == 3:
    print('O npumero {} convertido para hexadecimal é {}'.format(num, hex(num)))
else:
    print('Esta não é uma opção válida!!')