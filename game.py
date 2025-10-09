# Jogo da velha
# Autor: Ygor Felix

# criação de uma lista para representar o tabuleiro
campo = [1,2,3,4,5,6,7,8,9]

# função para imprimir o tabuleiro, para não precisar ficar repetindo o código
def board(campo):
    print(f"{campo[0]} | {campo[1]} | {campo[2]} \n" 
          f"---------\n"
          f"{campo[3]} | {campo[4]} | {campo[5]}\n" 
          f"---------\n"
          f"{campo[6]} | {campo[7]} | {campo[8]}")
board(campo)

# O computador joga na posição 5
print("O computador jogou:")
campo[4] = 'X'
board(campo)

jogada = int(input("Sua vez. Escolha um número: "))

campo[jogada - 1] = 'O'
print("Você jogou:")
board(campo)
