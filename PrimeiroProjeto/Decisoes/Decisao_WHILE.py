"while = enquanto o número impresso for menor que 100, continue imprimindo."
"\t= Ao imprimir, inclua uma tabulação(margem de espaço à esquerda)"
"str(numero) = transformar em o a variaveel numero em texto"

numero=int(input("Digite um número: "))
while numero<100:
    print("\t" + str(numero))
    numero=numero+1
print("Laço encerrado...")
