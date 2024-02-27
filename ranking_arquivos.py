def set_ranking (arquivo, pontos, nome, data):

    arq = open(arquivo,"a+")

    string_pontos = str(pontos)
    arq.write((string_pontos) + " ")
    arq.write(nome + " ")
    arq.write(data)
    arq.write("\n")

    arq.close()

def organizador_ranking (arquivo):

    arq = open(arquivo)
    vetor_nomes = []
    vetor_pontos = []

    linhas = arq.readlines()

    for z in linhas:
        linha_atual = z.split()
        vetor_pontos.append(linha_atual[0])
        nome_e_data = linha_atual[1] + ' ' +  linha_atual[2]
        vetor_nomes.append(nome_e_data)

    for i in range(0,len(vetor_pontos)-1):
        menor = i
        for j in range(i+1,len(vetor_pontos)):
            if int(vetor_pontos[j]) > int(vetor_pontos[menor]):
                menor = j
            auxiliar_pontos = vetor_pontos[menor]
            auxiliar_nomes = vetor_nomes[menor]
            vetor_pontos[menor] = vetor_pontos[i]
            vetor_nomes[menor] = vetor_nomes[i]
            vetor_pontos[i] = auxiliar_pontos
            vetor_nomes[i] = auxiliar_nomes

    arq.close()

    arq2 = open(arquivo,'w')
    for x in range(len(vetor_pontos)):
        arq2.write(str(vetor_pontos[x]) + " ")
        arq2.write(str(vetor_nomes[x]))
        arq2.write("\n")

    arq2.close()

def lista_ranking (arquivo):

    arq = open(arquivo)

    linhas = arq.readlines()

    return linhas