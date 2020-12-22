from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Ver cadastro', 'Cadastrar', 'Sair'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('Erro! Opção inválida!')
    sleep(2)