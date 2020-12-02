from time import sleep
import emoji
print('Contagem regressiva para o ano novo:')
for c in range (10, 0, -1):
    sleep(1)
    print(c)
print('=-'*20)
print('FELIZ ANO NOVO')
print(emoji.emojize(':fireworks:'*25))
print('=-'*20)
