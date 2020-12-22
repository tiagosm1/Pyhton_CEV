def aumentar(preço, taxa = 0):
    res = preço + (preço * taxa/100)
    return res

def diminuir(preço, taxa = 0):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço = 0):
    res = preço * 2
    return res

def metade(preço = 0):
    res = preço / 2
    return res

def moeda(preço, moeda ='R$: '):
    return f"{moeda}{preço:.2f}".replace('.', ',')