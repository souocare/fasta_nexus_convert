def cabecalho(fasta):
    '''
     -> Faz o print do Início do ficheito nexux, calculando nesta função o número de taxas,
      nucleotidos, gap e missing.
    :parameter fasta: recebe as sequencias e os seus nomes
    :return: retorna o print que contém o inicio do ficheiro nexus
    '''

    # Calcula o número de taxas usando o número de chaves que existem
    taxa = 0
    for k in fasta.keys():
        taxa+=1

    # Calcula a quantidade de Nucleotidos, Missing e Gap total que existe na sequencia
    for v in fasta.values():
        NCHAR = len(v)
        break

    global start_nexus

    # Faz um "print" do inicio do nexus, que contém a informação, antes do alinhamento das sequêncis no Nexus
    start_nexus = "#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX={} NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n".format(taxa,NCHAR)

    return start_nexus