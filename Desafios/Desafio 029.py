v = int(input('Insira a velocidade do carro em Km/h: '))
multa = (v-80)
valormulta = multa*7
if v >= 80:
    print('Você foi multado em R$: {:.2f}'.format(valormulta))
else:
    print('Você está dirigindo de maneira segura!')