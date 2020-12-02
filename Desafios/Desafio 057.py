sexo = str(input('Digite o sexo: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Você digitou {}, valor incorreto, tente novamente: '.format(sexo))).upper()
print('FIM')
