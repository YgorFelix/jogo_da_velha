# Jogo da velha
# Autor: Ygor Felix

# criação de uma lista para representar o tabuleiro
campo = [1,2,3,4,5,6,7,8,9]

# função para imprimir o tabuleiro, para não precisar ficar repetindo o código
def board():
    print(f"{campo[0]} | {campo[1]} | {campo[2]} \n" f"{campo[3]} | {campo[4]} | {campo[5]}\n" f"{campo[6]} | {campo[7]} | {campo[8]}")
print (board())