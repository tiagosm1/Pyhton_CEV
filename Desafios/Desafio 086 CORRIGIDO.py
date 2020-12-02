matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
menu = '*-' * 50
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(menu)
for l in  range (0,3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(menu)