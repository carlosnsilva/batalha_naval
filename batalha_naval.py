import random
import os
import time
import platform
import sys

'''
ESCRITO POR: Adrianderson, Carlos Nunes e Jorge Ricardo
'''

###   ---------------- Funções ------------------   ###

# -- Bem-vindo -- #

def welcome():
  print()
  print('   ~~~~__/=|=\__~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  print('   ~~~~\_0_0_0_/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~____~~~~~~~~~~')
  print('   ~~~~~~~~~~~~~~~~~~~                   ~~~~|- = |~~~~~~~~~')
  print('   ~~~~~~~____~~~~~~~~   BATALHA NAVAL   ~_____|= |_____~~~~')
  print('   ~~____| __ |_____~~                   ~\__0_|__|__0_/~~~~')
  print('   ~|__0__0___0__0__|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  print('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  print()
  print('Como o jogo funciona: \n')
  print('Batalha naval é um jogo de tabuleiro de dois jogadores,\nno qual os jogadores têm de adivinhar em que quadrados\nestão os navios do oponente. Seu objectivo é derrubar\nos barcos do oponente adversário, ganha quem derrubar\ntodos os navios adversários primeiro.\n')
  print('Antes do início do jogo, cada jogador coloca os seus\nnavios nos quadros, alinhados horizontalmente ou\nverticalmente. A quantidade de navios permitidos é\nigual para ambos jogadores e os navios não podem se\nsobrepor.\n')
  print('Quais navios iram ser utilizados neste jogo?\n')
  print('• Porta-avião (4 células) [P,P,P,P]\n• Cruzador    (3 células) [C,C,C]\n• Submarino   (2 células) [S,S]\n')
  return ' ' 

'''
Função borda recebe a posição que o elemento irá ficar 
e adiciona uma borda ao redor para não deixar um elemento
encostar em outro
'''
def borda(x, y, l_c, len_navio, m):
    status = True

    if(l_c == 0):  # BORDA NA HORIZONTAL
        try:
            if m[x][y-1] != "~":
                #m[x][y-1] = 'b'
                status = False

            for i in range(x, x+1):
                for j in range(y, y+len_navio+2):
                    if m[i-1][j-1] != "~":
                        # m[i-1][j-1] = 'b'
                        status = False

                    if m[i+1][j-1] != "~":
                        # m[i+1][j-1] = 'b'
                        status = False
            if m[x][y+len_navio] != "~":
                #m[x][y+len_navio] = 'b'
                status = False

        except:
            pass

    else:  # BORDA NA VERTICAL
        try:
            if m[x-1][y] != '~':
                #m[x-1][y] = 'b'
                status = False

            for i in range(x, x+len_navio+2):
                for j in range(y, y+1):
                    if m[i-1][j-1] != "~":
                        #m[i-1][j-1] = 'b'
                        status = False

                    if m[i-1][j+1] != "~":
                        #m[i-1][j+1] = 'b'
                        status = False

            if m[x+len_navio][y] != '~':
                #m[x+len_navio][y] = 'b'
                status = False

        except:
            pass

    return status


'''
Dado o ponto gerado aleatoriamente a funçao colisao ira percorrer o espaco 
que vai ser ocupado pelo elemento e verifica se não há nenhum outro elemento nesse lugar
'''
def colisao(x, y, l_c, len_navio, m):

    if l_c == 0:  # verifica pela horizontal
        c = len_navio
        l = 1

    else:  # verifica pela vertical
        l = len_navio
        c = 1
        aux = x
        x = y
        y = aux

    status = True
    for i in range(x, x+l):
        for j in range(y, y+c):
            try:
                if m[i][j] != "~":
                    status = False  # Colisao
            except:  # Fora da borda
                return False

    if status == True:  # Caso o espaço esteja livre chama a função borda
        if borda(x, y, l_c, len_navio, m):
            return True
    else:
        return False  # Caso contrario a função avisa que deve ser gerado outro ponto

# Função que gera um elemento na horizontal
def aleatorio_x(len_navio, n_navio, m):
    posX = random.randint(1, 8)
    posY = random.randint(1, 8)

    s = colisao(posX, posY, 0, len_navio, m)

    if(s == True):
        for i in range(posX, posX+1):
            for j in range(posY, posY+len_navio):
                m[i][j] = n_navio
    else:
        return False

# Função que gera um elemento na vertical
def aleatorio_y(len_navio, n_navio, m):
    posX = random.randint(1, 8)
    posY = random.randint(1, 8)

    s = colisao(posX, posY, 1, len_navio, m)
    if(s == True):
        for i in range(posY, posY+len_navio):
            for j in range(posX, posX+1):
                m[i][j] = n_navio

        print()
    else:
        return False

# Função que adiciona os elementos na matriz
def adicionar_navios(m, lista_tam, qtd_nav, nome):

    for i in range(len(qtd_nav)):
        if(qtd_nav[i] == 0):
            continue
        cont = 0
        while True:
            # SORTEIA POR ADICIONAR ELEMENTO POR aux OU COLUNA
            v = random.randint(0, 1)
            if(v == 0):  # HORIZONTAL
                if aleatorio_x(lista_tam[i], nome[i], m) == False:
                    continue
                else:
                    cont += 1
            else:  # VERTICAL
                if aleatorio_y(lista_tam[i], nome[i], m) == False:
                    continue
                else:
                    cont += 1
            if(cont == qtd_nav[i]):
                break
    return m

#FUNÇÃO QUE GERA A MATRIZ USADA NO JOGO 
def geraMatrizOculta():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append("~")
        matriz.append(linha)
    return matriz

#FUNÇAO QUE GERA A MATRIZ EXIBIDA AO USUÁRIO
def geraMatrizJogo():
    matriz = []
    for i in range(11):
        linha = []
        for j in range(11):
            if(i == 0):
                if(j == 0):
                    cont = '*'
                    aux = cont
                    cont = 0
                    linha.append(aux)
                cont += 1
                if(cont > 10):
                    break
                linha.append(cont)
            else:
                linha.append("~")
        matriz.append(linha)
    lista_alfa = [i for i in range(65, 75)]
    cont = 0
    for j in range(11):
        for i in range(1, 11):
            if(j == 0):
                matriz[i][j] = chr(lista_alfa[cont])
                cont += 1
    return matriz


def exibeMatrizJogo(matriz):
    '''linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end=' | ')
        print()'''
    for i in matriz:
        i = '   '.join(map(str,i))
        print(i)
    print()

#FUNÇÃO PRINCIPAL DO JOGO ONDE SE ENCONTRA A LÓGICA DE COMBATE
def batalha(vez, matriz, matriz_int):
    if platform.system() == 'Windows':
        os.system('cls')    
    elif platform.system() == 'Linux':
        os.system('clear')
        
    #TRECHO PARA FINS DE TESTES (SERÁ DESCOMENTADO NA HORA DA APRESENTAÇÃO)
        
    print()
    for i in matriz:
        i = ' '.join(map(str,i))
        print(i)
    print()
        
    
    print('JOGADOR {} SUA VEZ'.format(vez))
    # EXIBE O CAMPO DE BATALHA
    exibeMatrizJogo(matriz_int)
    print("Insira as coordenadas do tiro no campo de batalha!")
    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    while True:
        linha = input("Linha(A-J): ")
        if linha.upper() not in lista:
            print("coordenada invalida")
            continue
        else:
            linha = int(lista.index(linha.upper()))
        try:
            coluna = input("Coluna(1 - 9): ")
            if(int(coluna) < 1 or int(coluna) > 10):
                print("coordenada invalida!")
                continue
            coluna = int(coluna)
            break
        except:
            print("coordenada invalida!")
            continue

    if matriz[linha][coluna] != "~" and matriz[linha][coluna] != "*":
        matriz_int[linha+1][coluna] = matriz[linha][coluna]
        matriz[linha][coluna] = "*"

        print('\n')
        print("FOGO")
        exibeMatrizJogo(matriz_int)
        time.sleep(3)
        return True

    else:
        matriz_int[linha+1][coluna] = "*"
        vez = 1
        print('\n')
        print("AGUA!!")
        exibeMatrizJogo(matriz_int)
        time.sleep(3)
        return False

def carregar_arq(arquivo,matriz_jog_1,matriz_jog_2, matriz_int1,matriz_int2):
    lista = [matriz_jog_1,matriz_jog_2,matriz_int1,matriz_int2]
    for i in lista:
        if i < lista[2]:
            for j in range(10):
                i.append([])

            for j in i:
                linha = arquivo.readline()
                for k in linha:
                    if k == '\n':
                        break
                    else:
                        j.append(k)
            for j in i:
                print(j)
        else:
            for j in range(11):
                i.append([])

            for j in i:
                linha = arquivo.readline()
                for k in linha:
                    if k == '\n':
                        break
                    else:
                        j.append(k)
            for j in i:
                print(j)
            

    return matriz_jog_1, matriz_jog_2, matriz_int1, matriz_int2

## --------------------------       O JOGO COMEÇA AQUI      ------------------------- ##

lista_tam = [4, 3, 2]
nome = ['P', 'C', 'S']
welcome()

matriz_jog_1 = []
matriz_jog_2 = []
matriz_int1 = []
matriz_int2 = []


while True:

    print('   ..::  MENU DO JOGO  ::..   ')
    print()
    print(' (0) Sair')
    print(' (1) Novo Jogo')
    print(' (2) Continuar Jogo')
    print()

    saber = int(input('Digite a opcão: '))
    if saber == 0:
        break
    elif saber == 1:
        pass
    elif saber == 2:
        try:
            arq = open('arq.txt','r')
            carregar_arq(arq,matriz_jog_1,matriz_jog_2, matriz_int1,matriz_int2)
            break
        except:
            print('\nVocê saiu sem salvar o jogo, um novo jogo será iniciado.\n')
            time.sleep(3)
            


        

    escolha = input('Deseja frota máxima para o jogo ou não? (S)im/(N)ão: ').upper()

    if escolha == 'S':
        qtd_nav = [1, 2, 3]
        cont = 16
        break

    elif escolha == 'N':
        cont = 0
        while True:
            qtd_Paviao = int(input("porta avioes (0 a 1): "))
            if qtd_Paviao < 0 or qtd_Paviao > 1:
                print("Quantidade inválida!")
                continue
            else:
                break
        while True:
            qtd_cruzador = int(input("cruzador (0 a 2): "))
            if qtd_cruzador < 0 or qtd_cruzador > 2:
                print("Quantidade inválida")
                continue
            else:
                break
        while True:
            qtd_submarino = int(input("submarino (1 a 3): "))
            if qtd_submarino < 1 or qtd_submarino > 3:
                print("Quantidade inválida!")
                continue
            else:
                break

        qtd_nav = [qtd_Paviao, qtd_cruzador, qtd_submarino]
        for i in range(3):
            cont = cont + qtd_nav[i] * lista_tam[i]
        break

if saber != 0 and saber != 2:
    cont1 = cont
    cont2 = cont

    # Matriz interface Player 1 e Player 2
    matriz_int1 = geraMatrizJogo()
    matriz_int2 = geraMatrizJogo()

    # Matriz pronta Player 1
    matriz_jog_1 = adicionar_navios(geraMatrizOculta(), lista_tam, qtd_nav, nome)

    # Matriz pronta Player 2
    matriz_jog_2 = adicionar_navios(geraMatrizOculta(), lista_tam, qtd_nav, nome)

    #Função para salvar o jogo VERSÃO 1 Descontinuada
    def salvar_matriz(matriz_jog1,matriz_jog2,matriz_init1,matriz_init2):
        lista = [matriz_jog1,matriz_jog2,matriz_init1, matriz_init2]
        arq = open('arq.txt','w')
        for s in lista:
            l = len(s)
            c = len(s[0])
            for i in range(l):
                for j in range(c):
                    arq.write(str(s[i][j]))
                arq.write('\n')
            arq.write('\n') 
        arq.close()



vez = random.randint(0, 1)  # SORTEIA QUEM COMEÇA O JOGO
while True:

    if saber == 0:
        break

    if vez == 1:
        if batalha(1,matriz_jog_2 , matriz_int1):
            cont1 -= 1
        else:
            vez = 0
    else:
        if batalha(2,matriz_jog_1, matriz_int2):
            cont2 -= 1
        else:
            vez = 1

    if cont1 == 0:
        print('\nJogador 1 venceu!')
        time.sleep(3)
        break
    if cont2 == 0:
        print('\nJogador 2 venceu!')
        time.sleep(3)
        break
    
    save = input("\nVocê Deseja Salvar (S/N): ").upper()
    if save == 'S':
        salvar_matriz(matriz_jog_1,matriz_jog_2, matriz_int1,matriz_int2)
    else:
        pass