from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
anoatual = (date.today().year)
idadeatual = anoatual-nascimento
passou = idadeatual - 18
falta = 18 - idadeatual
if idadeatual == 18:
    print('Você tem {} anos e está na hora de se alistar !'.format(idadeatual))
elif idadeatual >= 18:
    print('Você tem {} anos e não será necessário se alistar! Prazo expirou há {} anos'.format(idadeatual,passou))
elif idadeatual <= 18:
    print('Você tem {} anos e precisa aguardar {} anos para isso !'.format(idadeatual,falta))
