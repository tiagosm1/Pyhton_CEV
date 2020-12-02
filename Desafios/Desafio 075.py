num = (int(input('Digite o primeiro número:')),
        int(input('Digite o segundo número:')),
        int(input('Digite o terceiro número:')),
        int(input('Digite o quarto número:')))
print(f'Você digitou os números {num}.')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu primeiramente na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado!')
print(f'Os números pares digitados foram ', end='')
for par in num:
    if par%2 == 0 :
        print(par)

