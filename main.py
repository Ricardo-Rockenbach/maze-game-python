import os
import time
import random

# Parametros iniciais:
tempo_inicial = time.time()
nome_jogador = input("Digite seu nome: ")
print(f"Bem-vindo ao Labirinto, {nome_jogador}!")
print("Instruções: Use w/a/s/d para mover para cima/esquerda/baixo/direita. \nEncontre a saída (🚪) para vencer o jogo. Cuidado com as paredes (#)!")


# geração do mapa

def gerar_labirinto(tamanho):
    labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]
    
    i, j = 1, 1
    fim_i, fim_j = tamanho - 2, tamanho - 2
    labirinto[i][j] = 'P'  # Posição inicial do jogador

# Fase 01 - Gerar caminho garantido do início ao fim
    while (i, j) != (fim_i, fim_j):
        if random.choice([True, False]):    
            if i < fim_i:
                i += 1
        else:
            if j < fim_j:
                j += 1

        labirinto[i][j] = '.'  # Caminho aberto

    labirinto[fim_i][fim_j] = '🚪'  # Posição da saída

# Fase 02 - Adicionar caminhos aleatórios para aumentar a dificuldade
    for _ in range(tamanho * 3):
        i = random.randint(1, tamanho - 2)
        j = random.randint(1, tamanho - 2)
        
        if labirinto[i][j] == '#':
            labirinto[i][j] = '.'

    return labirinto

def mostrar_labirinto(matriz):
    for linha in matriz:
        print(' '.join(linha))

labirinto = gerar_labirinto(20)


# Movimentação do jogador

def encontrar_jogador(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 'P':
                return (i, j)
         
def mover_jogador(matriz, direcao):
    i, j = encontrar_jogador(matriz)
    nova_i, nova_j = i, j

    if direcao == 'w':
        nova_i -= 1
    elif direcao == 's':
        nova_i += 1
    elif direcao == 'a':
        nova_j -= 1
    elif direcao == 'd':
        nova_j += 1

    if matriz[nova_i][nova_j] == '🚪':
        return 'Vitória'
    
    if matriz[nova_i][nova_j] != '#':
        matriz[i][j] = '.'
        matriz[nova_i][nova_j] = 'P'
        return 'Moveu'
    return 'parede'

erros = 0
max_erros = 5

while True:

    mostrar_labirinto(labirinto)

    comando = input("Digite o comando (w/a/s/d para mover, q para sair): ").lower()
    
    if comando == 'q':
        print("Saindo do jogo. Até a próxima!")
        break
    
    if comando not in ['w', 'a', 's', 'd']:
        print("Comando inválido! Use w/a/s/d para mover ou q para sair.")
        continue
    
    resultado = mover_jogador(labirinto, comando)

    if resultado == 'Vitória':
        print("Parabéns! Você encontrou a saída!")
        print("😍🥳🎉🎉🎉")
        print(f"Tempo gasto: {time.time() - tempo_inicial:.2f} segundos")
        break  
    elif resultado == 'Moveu':
        os.system('cls' if os.name == 'nt' else 'clear')

    elif resultado == 'parede':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("😢💥")
        print("Você bateu em uma parede! Tente outro caminho.")
        erros += 1
        
        if erros == max_erros:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Você excedeu o número máximo de erros. Game Over! 💣😥")
            break
    else:
        print("Comando inválido! Use w/a/s/d para mover ou q para sair.")

  