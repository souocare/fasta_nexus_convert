#a função vai requisitar 2 valores para que a funçãu funcione: ngen e outgroup
def mrbayes_blockwriter(ngen, outgroup):
    global mrbayes_final  
	#vai colocar a variável global para depois ser usada no main.py
	
    end = "  ;\nEND;\n\n"
	#vai colocar numa variável, a string apresentada
	
    mrbayes = "begin mrbayes;\n  set autoclose=yes\n" \
              "  outgroup {};\n" \
              "  mcmp ngen={} printfre=1000 samplefreq=100 diagnfre=1000 nchains=4 savebrlens=yes filename=MyRun01;\n" \
              "  mcmc;" \
              "  sumt filename=MyRun01;\n" \
              "end;".format(outgroup, ngen)
	#vai colocar numa variável, a string apresentada. o 'format' serve para colocar valores na string.

    mrbayes_final = end+mrbayes
	#juntar numa variável, as duas variáveis criadas
	
	
    return mrbayes_final
	#retornar a variável