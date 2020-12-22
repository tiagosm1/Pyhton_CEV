c = ('\033[m','\033[0;30;41m')



def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou biblioteca >'))
    if comando.upper()== 'FIM':
        break
    else:
        ajuda(comando)
titulo("Até logo", 1)