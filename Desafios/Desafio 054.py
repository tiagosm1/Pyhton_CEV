from datetime import date
anoatual = (date.today().year)
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Insira o ano de nascimento da {}ª pessoa:'.format(c)))
    idade = anoatual - nasc
    if idade >= 21:
        totmaior += 1#contador
    else:
        totmenor += 1
print('Dentro das pessoas inseridas {} são maiores e {} são menores'.format(totmaior, totmenor))


