tab = c = 0
while True:
    num = int(input('Escolha um número para saber sua tabuada:'))
    if num <= 0:
        break
    for c in range (0, 11):
        print(f'{num} x {c:2} = {num*c:2}')
print('Programa encerrado!')
