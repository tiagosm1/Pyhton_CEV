nome = str(input('Qual é o seu nome?'))
if nome == 'Tiago':
    print('Esse nome é lindo !!')
elif nome == 'Elaine' or 'Maria' or 'Marcia' or 'Marcos':
    print('Nominho popular!!!')
elif nome in 'Pedro João Victor':
    print('Nome de criança !!!')
else:
    print('Seu nome não tem nada de mais !!!')
print('Tenha um bom dia {}'.format(nome))