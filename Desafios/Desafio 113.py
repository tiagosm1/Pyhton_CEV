def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRRO: Por favor, digite um número inteiro válido!')
        except (KeyboardInterrupt):
            print('Programa interrompido pelo usuário.')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um numero real válido')
            continue
        except (KeyboardInterrupt):
            print('Usuário escolheu nao digitar o valor.')
            return 0
        else:
            return n

n1 = leiaint('Digite um valor inteiro:')
n2 = leiaint('Digite um valor real:')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

