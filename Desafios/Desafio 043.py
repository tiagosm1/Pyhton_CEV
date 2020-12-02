peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))
imc = peso / (altura*altura)
if imc <= 18.5:
    print('Seu IMC é {:.2f} e está abaixo do peso ideal'.format(imc))
elif imc >= 18.6 and imc <= 25:
    print('Seu IMC é {:.2f} e está no seu peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f} e você está com obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida'.format(imc))
