 


####################################################################################
# TORRE DFE HANOI COM 4 PINOS
####################################################################################

def hanoiQuatroPinos(disco , origem, destino, auxiliar1, auxiliar2, saida):
    if disco == 0:
        return
    if disco == 1:
        saida.append((disco, origem, destino))
        return
    else:
        hanoiQuatroPinos(disco-2, origem, auxiliar1, auxiliar2, destino, saida)

        # insere no vetor saida o numero do disco, sua origem e seu destino
        saida.append((disco-1, origem, auxiliar2))
        saida.append((disco, origem, destino))
        saida.append((disco-1, auxiliar2, destino)) 
        
        hanoiQuatroPinos(disco-2, auxiliar1, destino, origem, auxiliar2, saida)
  

####################################################################################
# TORRE DFE HANOI COM 3 PINOS
####################################################################################
def hanoiTresPinos(disco, origem, destino, auxiliar, saida):
    if disco == 0:
        return
    if disco == 1:
        saida.append((disco, origem, destino))
        return
    else: 
        hanoiTresPinos(disco-1, origem, auxiliar, destino, saida)
        # insere no vetor saida o numero do disco, sua origem e seu destino
        saida.append( (disco, origem, destino))
        hanoiTresPinos(disco-1, auxiliar, destino, origem, saida)

##########################################################################
def diferencaMov(n):

    # inicializa uma matriz com 2 linhas e o numero de colunas de acordo 
    # com a entrada do usuario
    matriz = [[0]*numero,[0]*numero]

    ######################################################################
    # LOOP que vai executar a quantidade de vezes de acordo 
    # com a entrada dada pelo usuario anteriormente
    for i in range(0, n):
        # o vetor saida e contador recebem vazio.
        saida = []
        # executa a função para a torre de Hanoi de tres pinos e salva 
        # a quantidade de movimentos na variavel movHanoiT
        hanoiTresPinos(i+1, "A","C","B", saida)
        movHanoiT = len(saida)

        # o vetor saida e contador recebem vazio.
        saida = []
        # executa a função para a torre de Hanoi de quatro pinos e salva 
        # a quantidade de movimentos na variavel movHanoiQ 
        hanoiQuatroPinos(i+1, "A","D","B","C", saida)
        movHanoiQ = len(saida)

        # subtrai a quantidade de movimentos da torre 3 pinos 
        # a quantidade de movimentos da torre de 4 pinos
        difMovimentos = movHanoiT - movHanoiQ

        # subistitui os valor da matriz na  linha 0 e na posição "i" pelo 
        # valor de i+1, também substitui o valor da matriz na linha 1 posição i
        # pela diferença d emovimentos da torre de hanoi com tres e quatro pinos
        matriz[0][i] = i+1
        matriz[1][i] = difMovimentos

    ##############################################################################
    # imprime a matriz com o numero de discos na primeira linha
    # e a diferença da quantidade de passos da torre de hanoi 
    # de 3 pinos para a torre de 4 pinos
    for i in range(2):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]}', end=" ")
        print()





##########################################################################
# Função genérica que imprime os valores de um vetor
# a cada interação da posição 0 até o tamanho 
# do vetorum elemento é exibido de acordo com sua posição
def imprimeVetor(v):
    for i in range(len(v)):
        print ("mova disco " + str(v[i][0]) + " do pino " + str(v[i][1]) + " para o pino " + str(v[i][2]))



##########################################################################
# LETRA A

# recebe um numero inteiro digitado pelo usuario
discos = int(input())

# inicializa o vetor saida como vazio
saida = []
 
# chama a função da torre de hanoi com tres pinos
hanoiTresPinos(discos, "A","C","B", saida)
# imprime o vetor saida que contem o numero do disco sua origem e destino
imprimeVetor(saida)
# imprime a quantidade de movimentos necessarios para solução da torre usando
# como base o tamanho do vetor com as posições onde ouveram movimentos dos discos
print(f'Para resolver o jogo Torre de Hanoi com 3 pinos são necessários {len(saida)} movimentos')
print()

# o vetor saida recebe vazio.
saida = []
hanoiQuatroPinos(discos, "A","D","B","C", saida)
imprimeVetor(saida)
print(f'Para resolver o jogo Torre de Hanoi com 4 pinos são necessários {len(saida)} movimentos')
print()

########################################################################
# LETRA B

# recebe um numero inteiro digitado pelo usuario
numero = int(input())
# chama a função qua calcula a diferença de movimentos 
# da torre de hanoi de 3 pinos para de 4 pinos
diferencaMov(numero)
