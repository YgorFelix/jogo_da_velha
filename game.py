# Jogo da velha
# Autor: Ygor Felix

#-------------------------------
# --- 1.CONFIGURAÇÃO INICIAL ---
#-------------------------------

# criação de uma lista para representar o tabuleiro
campo = [1,2,3,4,5,6,7,8,9]
# variável para representar que o não acabou
jogo_acabou = False 

#--------------------------
# --- 2.FUNÇÕES DO JOGO ---
#--------------------------

# função para imprimir o tabuleiro, para não precisar ficar repetindo o código
def board(campo):
    print(f"{campo[0]} | {campo[1]} | {campo[2]} \n" 
          f"---------\n"
          f"{campo[3]} | {campo[4]} | {campo[5]}\n" 
          f"---------\n"
          f"{campo[6]} | {campo[7]} | {campo[8]}")

# Função verificação de vitória, em linha, coluna e diagonal
# utilizando if e colocando dentro de uma função
def checar_vitoria():
    if campo[0] == campo[1] == campo[2] or \
        campo[3] == campo[4] == campo[5] or \
        campo[6] == campo[7] == campo[8] or \
        campo[0] == campo[3] == campo[6] or \
        campo[1] == campo[4] == campo[7] or \
        campo[2] == campo[5] == campo[8] or \
        campo[0] == campo[4] == campo[8] or \
        campo[2] == campo[4] == campo[6]:
        # Usando return para retornar True ou False, ao invés de print
        # se qualquer umas dessas condições forem verdadeiras, retorna True
        return True
    return False

#--------------------------
# --- 3.JOGO PRINCIPAL ----
#--------------------------

# O computador joga na posição 5
print("Bem vindo ao jogo da velha!")
print("O computador é o X e você é o O")
print("O computador jogou:")
campo[4] = 'X'

while not jogo_acabou:
    # mostra o tabuleiro atual
    board(campo)

    # ---Vez do Jogador ---

    # Loop para garantir que o jogador escolha uma posição válida
    while True:
        jogada = int(input("Sua vez. Escolha um número: "))
        posicao = jogada - 1

        # checa se a casa está disponível
        if campo[posicao] not in ['X', 'O']:
            campo[posicao] = 'O'
            break
        else:
            print("Posição inválida. Tente novamente.") 

    # checa se o jogador ganhou / acabou
    vencedor = checar_vitoria()
    if vencedor == "O":
        print("Parabéns! Você ganhou!")
        jogo_acabou = True
    elif vencedor == "X":
        print("O computador ganhou!")
        jogo_acabou = True

    # --- Fim de Jogo ---
    board(campo)
    print("Fim de jogo!")

