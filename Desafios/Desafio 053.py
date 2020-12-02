frase = str(input('Escreva a frase para saber se é um polindromo:')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Esta palavra é um palindromo')
else:
    print('Esta palavra NÃO é um palindromo!')
