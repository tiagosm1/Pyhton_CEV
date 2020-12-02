from datetime import date
anonascimento = int(input('Insira o ano de nascimento: '))
anoatual = (date.today().year)
idadeatual = anoatual - anonascimento
if idadeatual <=9:
    print('Sua idade é {} anos e sua categoria é MIRIM'.format(idadeatual))
elif idadeatual == 10 or idadeatual <= 14:
    print('Sua idade é {} anos e sua categoria é: INFANTIL'.format(idadeatual))
elif idadeatual == 15 or idadeatual <= 19:
    print('Sua idade é {} anos e sua categoria é: JUNIOR'.format(idadeatual))
elif idadeatual == 20 :
    print('Sua idade é {} anos e sua categoria é: SÊNIOR'.format(idadeatual))
elif idadeatual >= 21:
    print('Sua idade é {} anos e sua categoria é: MASTER'.format(idadeatual))
