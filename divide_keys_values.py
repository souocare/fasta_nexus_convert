from itertools import groupby

def fasta_rearrange(fasta):
    '''
    Procurar todos os nomes e sequências, e colocar num dicionário, a partir do ficheiro fasta que é aceite como argumento
    :param fasta: recebe o ficheiro fasta
    :return:
    '''
    with open(fasta, "r") as fasta:
        groups = groupby(fasta, key=lambda x: not x.startswith(">")) # procura os nomes começados por >
        fasta_file = {} # cria um dicionario vazio
        for k, v in groups:
            if not k:
                key, val = list(v)[0].replace('\n', ''), "".join(map(str.rstrip, next(groups)[1])) #em cada valor da lista, o 'enter' é substituido por nada				
                fasta_file[key] = val # coloca no dicionarios os valores e as chaves

    novo = {k.replace('>', ''): v for k, v in fasta_file.items()} # faz replace ao > por nada
