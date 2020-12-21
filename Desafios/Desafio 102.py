def fatorial(n, show=False):
    '''
    - Calcula o fatorial de un número
    :param n: O Numero a ser calculado
    :param show: Mostar ou nao a conta
    :return: o valor do fatorial dfe um numero n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
            f *= c
    return f


print(fatorial(5, show=True))