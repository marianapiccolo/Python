"""

 Snake game
 
"""


# ======================================================================
#
#   M A I N 
#
# ======================================================================
def main():
    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()

    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols = int(input('Número de colunas do tabuleiro: '))
    x0 = int(input('Posição x inicial da cobrinha : '))
    y0 = int(input('Posição y inicial da cobrinha : '))
    t = int(input('Tamanho da cobrinha           : '))

    # Verifica se corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cabeça
    if x0 - (t - 1) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")

    else:
        ''' Inicia a variável d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t - 1:
            d = d * 10 + 2
            i = i + 1

        # Laço que controla a interação com o jogador
        direcao = 1
        while direcao != 5:
            # mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d)

            # lê o número do próximo movimento que será executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu próximo movimento: "))

            if direcao != 5:
                # atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

    print()
    print("Tchau!")


# ======================================================================

def num_digitos(n):
    """ (int) -> int

    Devolve o número de dígitos de um número.

    ENTRADA
    - n: número a ser verificado 

    """

    # variaveis auxiliares
    numero_de_digitos = 0
    loop = True

    # faz loop enquanto a divisao inteira nao zerar
    while loop:
        numero_de_digitos=numero_de_digitos+1
        if n//10 == 0:
            loop = False

        n=n//10

    # retorna o numero de digitos
    return numero_de_digitos


# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrário.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça

    """

    # varia x0,y0 (inicialmente na cabeca) enquanto existir direcao
    while not fim(d):
        # verifica se os pontos coincidem
        if x==x0 and y==y0:
            return True

        # seta proximo ponto em x0,y0 (obs: inverte direcao para obter corpo)
        direcao_corpo = inverter_direcao(d%10)
        if direcao_corpo==1:
            x0=x0-1
        elif direcao_corpo==2:
            x0=x0+1
        elif direcao_corpo==3:
            y0=y0-1
        else:
            y0=y0+1

        # proximo d
        d = d//10

    # verifica ultimo ponto
    if x == x0 and y == y0:
        return True

    # se chegou aqui entao nao está ocupada
    else:
        return False


# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça

    """

    # tabuleiro sem as bordas superiores/inferiores
    tabuleiro = ""
    y=0
    while y<nlinhas:
        # parede esquerda
        tabuleiro=tabuleiro+"\n#"

        # campo de jogo
        x=0
        while x<ncols:

            if pos_ocupada(nlinhas,ncols,x,y,x0,y0,d) and x==x0 and y==y0:
                tabuleiro=tabuleiro+"C"
            elif pos_ocupada(nlinhas,ncols,x,y,x0,y0,d) and (x!=x0 or y!=y0):
                tabuleiro=tabuleiro+"*"
            else:
                tabuleiro=tabuleiro+"."
            x=x+1

        # parede direita
        tabuleiro=tabuleiro+"#"
        y=y+1

    #bordas superiores e inferiores no print
    total_colunas = ncols+2
    print("#"*total_colunas + tabuleiro + "\n" + "#"*total_colunas)

# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direção dada.    
    A função devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento é impossível (pois a cobra vai colidir consigo mesma ou
    com a parede), então a função devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃO COM SI MESMA" ou "COLISÃO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    - direcao: direção na qual a cabeça deve ser movida

    """

    # posicao da cabeca caso haja movimento
    if direcao==1:
        x=x0-1
        y=y0
    elif direcao==2:
        x=x0+1
        y=y0
    elif direcao==3:
        x=x0
        y=y0-1
    else:
        x=x0
        y=y0+1

    # verifica se a nova cabeca colidiu com parede
    if eh_borda(nlinhas,ncols,x,y):
        print("COLISÃO COM A PAREDE")
        return x0,y0,d

    # verifica se ha colisao com o proprio corpo
    if pos_ocupada(nlinhas,ncols,x,y,x0,y0,d):
        print("COLISÃO COM SI MESMA")
        return x0, y0, d

    # nao colidiu, logo retorna posicao e d novos
    return x,y,mudar_d(d,direcao)

# ======================================================================
def fim(n):
    if n==0:
        return True
    else:
        return False

# ======================================================================
def inverter_direcao(direcao):
    if direcao == 1:
        return 2

    if direcao == 2:
        return 1

    if direcao == 3:
        return 4

    if direcao == 4:
        return 3

# ======================================================================

def eh_borda(nlinhas,ncols,x,y):
    if x==-1 or x==ncols or y==-1 or y==nlinhas:
        return True
    else:
        return False

# ======================================================================

def mudar_d(d_atual, direita):
    d_atual=10*d_atual
    d=d_atual + direita

    tamanho_d = num_digitos(d)
    d=d % 10**(tamanho_d - 1)

    return d

# ======================================================================




main()     