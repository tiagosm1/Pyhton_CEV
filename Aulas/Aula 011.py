#print('\033[0;30;41mOlá mundo')
#print('\033[4;33;44mOlá mundo')
#print('\033[1;35;43mOlá mundo')
#print('\033[30;42mOlá mundo')
#print('\033[7;30mOlá mundo')


#a = 5
#b = 5
#print('Os valores são \033[0;30;41m{} e \033[7;30m{}'.format(1, b))

#nome = 'Tiago'
#print('Olá! Prazer em te conhecer {} {} {}!!!!'.format('\033[4;34m', nome, '\033[m'))

nome = 'Tiago'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Prazer em te conhecer {} {} {}!!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
