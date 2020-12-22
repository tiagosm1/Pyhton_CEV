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

def linha(tam = 42):
    return "-" * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção:')
    return opc