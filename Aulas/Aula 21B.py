'''
def teste():
    x = 8
    print(f'Na função teste N vale {n}')
    print(f'Na função teste, x vasle {x}')

#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
'''

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a=5
teste(a)
print((f'A fora vale {a}'))