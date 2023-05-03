#Define posições:
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range (tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for a in range (tamanho):
            posicoes.append([linha + a, coluna])
    return posicoes          

#Preenche frota:
def preenche_frota(dicio_frota, nome_navio, linha_navio, coluna_navio, orientacao_navio, tamanho_navio):
    if nome_navio not in dicio_frota:
        dicio_frota[nome_navio] = [define_posicoes(linha_navio, coluna_navio, orientacao_navio, tamanho_navio)]
    else:
        dicio_frota[nome_navio].append(define_posicoes(linha_navio, coluna_navio, orientacao_navio, tamanho_navio))
    return dicio_frota

#Faz jogada:
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

#Posiciona frota:
def posiciona_frota(dicio_frota):
    grade = [0]*10 #igual ModSim
    for i in range(len(grade)):
        grade[i] = [0]*10
    for direcao in dicio_frota.values():
        for a in direcao:
            for i in a:
                linha = i[0]
                coluna = i[1]
                grade[linha][coluna] = 1
    return grade

#Quantas embarcações afundadas?
def afundados(dicio_frota, tabuleiro):
    num_afundados = 0
    afundou = False
    for direcao in dicio_frota.values():
        for i in direcao:
            for b in i:
                linha = b[0]
                coluna = b[1]
                if tabuleiro[linha][coluna] == 'X':
                    afundou = True
                else:
                    afundou = False
                    break
            if afundou == True:
                num_afundados += 1
    return num_afundados

def posicao_valida(dicio_navios,linha,coluna,orientacao,tamanho):
    navio = define_posicoes(linha,coluna,orientacao,tamanho)
    for n in navio:
        if n[0] < 0 or n[1]<0 or n[0]>9 or n[1]>9:
            return False
        for i in dicio_navios.values():
            for j in range(len(i)):
                if n in i[j]:
                    return False
    if dicio_navios == {}:
        return True
    return True