# import the math module 
import math 


####################################################################################
# TORRE DFE HANOI COM 4 PINOS
####################################################################################

def hanoiQuatroPinos(disco , origem, auxiliar1, auxiliar2, destino, saida, nDisco):
    x=[]
    if disco == 0:
        return
    if disco > 1:

        if disco > 2:
            i = int((math.sqrt(8*disco + 1) - 1)/2)        

        else:
            i = 1


        hanoiQuatroPinos(disco -i, origem, auxiliar2, destino, auxiliar1, saida, nDisco)

        hanoiTresPinos(i, origem, auxiliar2, destino, saida, x)

        hanoiQuatroPinos(disco -i, auxiliar1, auxiliar2, origem, destino, saida, nDisco)


        
    else:
        saida.append((origem, destino))


####################################################################################
# TORRE DFE HANOI COM 3 PINOS
####################################################################################
def hanoiTresPinos(disco, origem, auxiliar, destino, saida, nDisco):
    if disco == 0:
        return
    if disco > 1:

        hanoiTresPinos(disco-1, origem, destino, auxiliar, saida, nDisco)

        if disco-1 == 1:
            nDisco.append(1)

        nDisco.append(disco)

        hanoiTresPinos(1, origem, auxiliar, destino, saida, nDisco)

        hanoiTresPinos(disco-1, auxiliar, origem,  destino, saida, nDisco)
        
        if disco-1 == 1:
            nDisco.append(1)

    else:
        saida.append((origem, destino))



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
        nDisco = []
        # executa a função para a torre de Hanoi de tres pinos e salva 
        # a quantidade de movimentos na variavel movHanoiT
        hanoiTresPinos(i+1, "A", "B", "C", saida, nDisco)
        movHanoiT = len(saida)

        # o vetor saida e contador recebem vazio.
        saida = []
        nDisco = []
        # executa a função para a torre de Hanoi de tres pinos e salva 
        # a quantidade de movimentos na variavel movHanoiQ
        hanoiQuatroPinos(i+1, "A", "B", "C", "D", saida, nDisco)
        movHanoiQ = len(saida)

        # subtrai a quantidade de movimentos da torre quatro pinos 
        # da quantidade de movimentos da torre de tres pinos
        difMovimentos = movHanoiT - movHanoiQ

        # subistitui os valor da matriz na  linha 0 e na posição "i" pelo 
        # valor de i+1, também substitui o valor da matriz na linha 1 posição i
        # pela diferença d emovimentos da torre de hanoi com tres e quatro pinos
        matriz[0][i] = i+1
        matriz[1][i] = difMovimentos

    ##############################################################################
    # imprime a matriz
    for i in range(2):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]}', end=" ")
        print()



##########################################################################
# Função genérica que imprime os valores de um vetor
# a cada interação da posição 0 até o tamanho 
# do vetorum elemento é exibido de acordo com sua posição
def imprimeVetor(v1, v2):
    for i in range(len(v1)):
        print("mova disco " + str(v1[i]) + " do pino " + str(v2[i][0]) + " para o pino " + str(v2[i][1]))
        print(len(v1), len(v2), i)

##########################################################################
# LETRA A

# recebe um numero inteiro digitado pelo usuario
discos = int(input())

# inicializa o vetor saida e contador como vazios
saida = []
nDisco = []
 
# chama a função da torre de hanoi com tres pinos
hanoiTresPinos(discos, "A", "B", "C", saida, nDisco)
# imprime o vetor saida, com os movimentos dos dicos
imprimeVetor(nDisco, saida)
# imprime a quantidade de movimentos necessarios para solução da torre usando
# como base o tamanho do vetor com as posições onde ouveram movimentos dos discos
print(f'Para resolver o jogo Torre de Hanoi com 3 pinos são necessários {len(saida)} movimentos')
print()



# o vetor saida e contador recebem vazio.
saida = []
nDisco = []
hanoiQuatroPinos(discos, "A", "B", "C", "D", saida, nDisco)
imprimeVetor(nDisco,saida)
print(f'Para resolver o jogo Torre de Hanoi com 4 pinos são necessários {len(saida)} movimentos')
print()

# recebe um numero inteiro digitado pelo usuario
numero = int(input())
diferencaMov(numero)