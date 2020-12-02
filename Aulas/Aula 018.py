'''galera = [['João', 19], ['Ana', 34], ['Pedro', 45],['Jonas', 23]]'''

'''print(galera)'''

'''for p in galera:
    print(p[0][2])''' #assim imprime somente a letra referente a posiçao do segundo []


'''for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = list()
dado = list()
totmaior = totmenor = 009O0
for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')





