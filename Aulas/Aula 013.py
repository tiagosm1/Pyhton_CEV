'''
#repete os prints
for c in range (1, 11):
    print('OI')
print ('Fim')
'''

'''
#contagem regresiva de 1 em 1 até o 0
for c in range (9, 0, -1):
    print(c)
print ('Fim')
'''


'''
#contagem progressiva pulando de 2 em 2
for c in range (1, 11, 2):
    print(c)
print ('Fim')
'''

'''
#contagem regressiva até o numero inseiro no input
n = int(input('Digite um número:'))
for c in range(0, n+1):
    print(c)
print('FIM')
'''



'''
#conta apartir do input de inicio até o fim pelo passo desejado
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')
'''


'''
#Recebe valores repetidas vezes dentro do range
for c in range (0, 3):
    n = int(input("Digite um valor:"))
print('FIM')
'''

#faz uma somatória dos numeros recebidos
s = 0
for c in range (0, 3):
    n = int(input("Digite um valor:"))
    s += n
print(' A somatória dos números inseridos é: {}.'.format(s))
print('FIM')

]