#---------Inserçao de varias frases com append:

#with open("primeiro_arquivo.txt", "a") as arquivo:
 #   arquivo.write("\nBazinnngaaaaaa!!")

 #---------Leitura do arquivo txt:
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)