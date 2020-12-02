distancia = float(input("Insira a distância da viagem: "))
v = float
v1 = float
if distancia <= 200:
   v = distancia * 0.5
   print('O valor de sua passagem é R$: {} '.format(v))
else:
    v1 = distancia * 0.45
    print('O valor de sua passagem é R$: {} '.format(v1))
print('----FIM----')