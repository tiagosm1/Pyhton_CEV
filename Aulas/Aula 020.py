'''def titulo(txt):

    print('-'*30)
    print(txt)
    print('-' * 30)

titulo('SISTEMA DE ALUNOS')

titulo('CURSO EM VIDEO')

titulo('MUNDO 3 PYTHON')'''

'''
def soma(a,b):
    print(f'A = {a} + B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

def linha():
    print('-*-'*10)

linha()
soma(4,5)
linha()
soma(8,9)
linha()
soma(2, 1)
'''

'''
def contador(* num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4,4,7,6,2)
'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)
'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)










