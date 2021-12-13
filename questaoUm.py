########################################################################
# conta o numero de inverções de posições e retorna umaa lista com
# os indices de cada inversão.
def posicoes(lista):
    saida = []
    cont = 0
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                cont +=1
                saida.append((i+1,j+1))
    return cont, saida

######################################################################
# Verifica a quantidade de e quais são os elementos 
# repitidos e retorna um array com eles.
def ocorrencia(lista):
    saida = []
    for i in range(len(lista)-1):
        ocorrencia = 0
        for j in range(len(lista)):
            if lista[i] == lista[j] and str(lista[i]) not in saida:
                ocorrencia += 1
                if ocorrencia > 1:
                    saida.append(str(lista[i]))

    return saida

#########################################################################
# Inverte a posição dos elementos na lista.
def inverter(lista):
    inicio = 0
    fim = len(lista)-1
    while inicio < fim:
        aux = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = aux

        inicio += 1
        fim -= 1
    return lista

##########################################################################
# Recebe 2 vetores, o inicial e o inverso e calcula a diferença 
# entre os elementos de cada prosição.
def diferenca(v, iv):
    resultado = []
    for i in range(len(v)):
        resultado.append(v[i]-iv[i])
    return resultado

##########################################################################
# Faz uma cópia da lista.
def criarLista(v):
    lista = []
    for chave in v.split(" "):
        lista.append(int(chave))
    return lista

##########################################################################

entrada = input()
#LETRA A
print(f'Os elementos que se repetem são: {ocorrencia(criarLista(entrada))}')

#LETRA B
inversa = inverter(criarLista(entrada))
print (f'Sequência inversa: {inversa}')

#LETRA C
qntInversoes, inversoes = posicoes(criarLista(entrada))
print(f'Há {qntInversoes} inversões, e as posições são: {inversoes}')

#LETRA D
print(f'A sequência obtida da diferença é: {diferenca(criarLista(entrada), inversa)}')


