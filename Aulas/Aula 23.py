'''
try:
    a = int(input('Numerador:'))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Erro encontrado: {erro.__class__} ')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre, obrigado"')
'''

try:
    a = int(input('Numerador:'))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('TIVEMOS UM PROBLEMA COM OS TIPOS DE DADOS QUE VOĈE DIGITOU')
except ZeroDivisionError:
    print('NÃO É POSSIVEL DIVIDIR O VALOR POR ZERO')
except KeyboardInterrupt:
    print('O USUÁRIO PREFERIU NÃO INFORMAR OS DADOS')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre, obrigado"')