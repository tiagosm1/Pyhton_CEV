#n1 = int(input("Insira o valor em metro para converter em centimetros e milimetros: "))
#cen = n1/100
#mil = n1/1000
#print('O valor inserido em centrimetros é: {} e em Milímetros é {},'.format(cen, mil))

medida = float(input('Insira a medida em metros: '))
km = medida/1000
hm = medida/100
dc = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000

print('A medida de {} m\n corresponde a\n {} Km\n {} Hm\n {} Dm\n {} Dc\n {} Cm\n {} mm'.format(medida, km, hm, dc, dm, cm, mm))
