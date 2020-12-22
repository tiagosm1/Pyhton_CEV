def notas(*n, sit=False):
    '''
    Função para analizar nota e situação ded alunos
    :param n: uma ou mais notas dos alunos
    :param sit: adicionar ou naop a stiuação
    :return: dicionarto com a situação|
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'ruim'
        return r

resp = notas(1, 2.5, 1.5, sit=True)
print(resp)
help(notas)