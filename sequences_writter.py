def seq_writter(fasta):
    '''
    -> Alinha todas as sequências
    :param fasta: Recebe o número de sequências e os seus nomes
    :return: Retorna a sequência alinhada
    '''
    sequences=""

    #A variável maior vai receber o maior nome que existe de todos os nomes das sequências
    #Se o nome da maior espécie for maior que 99, tudo para a frente será cortado e o maior apenas vai ter 99 caracteres
    maior=""
    for k,v in fasta.items():
        if len(k)>len(maior):
            maior = k
        if len(maior) >=99:
            maior = maior[:99]

    # Vai percorrer todos os nomes e sequencias e se o nome for maior que 99 caracteres, tudo para a frente de 99 será cortado
    # À variável maior será retirado o número de cada nome para cada iteração, para calcular o número de espaçoes em branco para
    #alinha os nomes e cada sequência será alinhada
    for k,v in fasta.items():
        if len(k) >=99:
            k = k[:98]
        qualquer = len(maior) -1
        tamanho = qualquer - len(k)
        sequences+=" "*tamanho + "{}  {}".format(k,v) + "\n"

    return sequences
