import random
random.seed(2)
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
def preenche_frota(dicio_frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in dicio_frota:
        dicio_frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
        dicio_frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
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
    grade = [0]*10 
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

#Posição válida
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

#Posicionando frota:
dicio_frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicio_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for embarcacao, qtde in dicio_embarcacoes.items():
    
    for i in range(0, qtde[0]):
        print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if embarcacao != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(dicio_frota, linha,coluna,orientacao,qtde[1]) == False:
                while posicao_valida(dicio_frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota = preenche_frota(dicio_frota, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota = preenche_frota(dicio_frota, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(dicio_frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(dicio_frota, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota = preenche_frota(dicio_frota, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota = preenche_frota(dicio_frota, embarcacao, linha, coluna, orientacao, qtde[1])
    print(dicio_frota)
# Jogadas do jogador 
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)

def monta_tabuleiros(tabuleiro_jogador,  tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        info_jogador = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        info_oponente = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {info_jogador}|     {linha}| {info_oponente}|\n'
    return texto
grade_frota = posiciona_frota(frota)
grade_oponente = posiciona_frota(frota_oponente)
primeiro_ataque_jog = []
primeiro_ataque_opon = []
jogando = True
while jogando == True:
    grade = monta_tabuleiros(grade_frota, grade_oponente)
    print(grade)
    repete = True
    while repete == True:
        linha = True
        coluna = True
        while linha == True:
            linha_do_ataque = int(input('Jogador, qual linha deseja atacar?'))
            if linha_do_ataque < 0 or linha_do_ataque > 9:
                print('Linha inválida')
            else:
                linha = False
        while coluna == True:
            coluna_do_ataque = int(input('Jogador, qual coluna deseja atacar?'))
            if coluna_do_ataque < 0 or coluna_do_ataque > 9:
                print('Coluna inválida!')
            else:
                coluna = False
        novo_ataque = [linha_do_ataque, coluna_do_ataque]
        if novo_ataque in primeiro_ataque_jog:
            print(f'A posição linha {linha_do_ataque} e coluna {coluna_do_ataque} já foi informada anteriormente')
        else:
            repete = False
    primeiro_ataque_jog.append(novo_ataque)
    grade_oponente = faz_jogada(grade_oponente, linha_do_ataque, coluna_do_ataque)
    barcos_afundados = afundados(frota_oponente, grade_oponente)
    if barcos_afundados == 10:
        jogando = False
        print('Parabéns! Você derrubou todos os navios do seu oponente! ;)')
    #Jogadas oponente:
    else:
            segunda_jogada = True
            while segunda_jogada:
                linha1 = random.randint(0, 9)
                coluna2 = random.randint(0, 9)
                ataque_oponente = [linha1, coluna2]
                if ataque_oponente not in primeiro_ataque_opon:
                    print(f'Seu oponente está atacando na linha {linha1} e coluna {coluna2}')
                    primeiro_ataque_opon.append(ataque_oponente)
                    grade_frota = faz_jogada(grade_frota, linha1, coluna2)
                    segunda_jogada = False
            if afundados(frota, grade_frota) == 10:
                jogando = False
                print('Opa! O oponente derrubou toda a sua frota! :( ')