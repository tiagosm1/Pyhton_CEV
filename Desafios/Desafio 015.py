kmrodado = float(input('Insira a quantidade de KM percorrido: '))
diasaluguel = float(input('Insira a quantidade de dias de aluguel: '))
totalkm = kmrodado*0.15
totaldias = diasaluguel*60
totalgeral = totalkm+totaldias
print(' o seu carro foi alugado por {:.0f} dias e rodou por {} Quilômetros o total a ser pago pelo aluguel é de R$: {:.2f}'.format(diasaluguel, kmrodado, totalgeral ))