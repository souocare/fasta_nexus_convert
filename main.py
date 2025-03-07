#importação argv para obter as variáveis do utilizar . E ainda, fazer o import dos vários modules
from sys import argv
import mrbayes, divide_keys_values, cabecalho, sequences_writter


fasta_file_from_user = argv[1]
ngen = argv[2]
outgroup = argv[3]
#em cima, obtem-se as variáveis do user


new_key_values = divide_keys_values.fasta_rearrange(fasta_file_from_user)
#corre o module 'divide_keys_values', correndo a função 'fasta_rearrange', dando à funçãoo, a variável fasta_file_from_user. Quando o programa correr, vai ser obtida uma variável 'novo'

new_header = cabecalho.cabecalho(new_key_values)
#corre o module 'cabecalho', correndo a função 'cabecalho', dando à função a variável obtida da função acima, obtendo a variável 'start_nexus'

new_sequence = sequences_writter.seq_writter(new_key_values)
#corre o module 'sequences_writter', correndo a função 'seq_writter', dando à função a variável obtida da função acima, obtendo a variável 'sequences'

nexus_writter= new_header + new_sequence
#na variavel nexus_writter, juntamos as várias variáveis obtidas anteriormente

nexus_file= open("nexus_file.nex", "w+")
#criação do ficheiro nexus

nexus_file.write(nexus_writter)
#escrever a variável 'nexus_writter' no ficheiro

print(nexus_file)

nexus_file.close()
#fecha o ficheiro



