import os
import time
import random


# Parametros iniciais:
def parametros_iniciais():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem-vindo ao Labirinto!")
    print("Instruções: Use w/a/s/d para mover para cima/esquerda/baixo/direita. \nEncontre a saída (🚪) para vencer o jogo. Cuidado com as paredes (#)!")
    nome_jogador = input("Digite seu nome: ")
    print(f"Bem-vindo ao Labirinto, {nome_jogador}!")
    input("Pressione Enter para começar...")
    tempo_inicial = time.time()

    return tempo_inicial, nome_jogador

tempo_inicial, nome_jogador = parametros_iniciais()
    
    # Utilitario para limpar a tela:
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Sistema de pontuação:
def sistema_pontuacao(passos, tempo_gasto, erros):
    pontos = max(0, 5000 - (passos * 10 + int(tempo_gasto) * 5 + erros * 50))
    if pontos < 0:
        pontos = 0
    return pontos

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
    for _ in range(tamanho):
        #pegando um ponto que já é caminho
        while True:
            x = random.randint(1, tamanho - 2)
            y = random.randint(1, tamanho - 2)
            if labirinto[x][y] == '.':
                break

        # Escolher uma direção aleatória para abrir um caminho
        direcao = random.choice(['w', 'a', 's', 'd'])

        comprimento = random.randint(2, 8)  # Comprimento do novo caminho

        for _ in range(comprimento):
            if direcao == 'w' and x > 1:
                x -= 1
            elif direcao == 's' and x < tamanho - 2:
                x += 1
            elif direcao == 'a' and y > 1:
                y -= 1
            elif direcao == 'd' and y < tamanho - 2:
                y += 1

            if not (1 <= x < tamanho - 1 and 1 <= y < tamanho - 1):
                break  # Evitar sair dos limites do labirinto

            if labirinto[x][y] == '#':
                labirinto[x][y] = '.'  # Abrir caminho
            else:
                break  # Parar se encontrar um caminho já aberto
    return labirinto

labirinto = gerar_labirinto(20)

def mostrar_labirinto(matriz):
    for linha in matriz:
        print(' '.join(linha))


# Movimentação do jogador

def encontrar_jogador(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 'P':
                return i, j
    return None

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

passos = 0
erros = 0
max_erros = 5


while True:

    limpar_tela()
    mostrar_labirinto(labirinto)

    comando = input("Digite o comando (w/a/s/d para mover, q para sair): ").lower()
    
    if comando == 'q':
        print("Saindo do jogo. Até a próxima!")
        break
    
    if comando not in ['w', 'a', 's', 'd']:
        print("Comando inválido! Use w/a/s/d para mover ou q para sair.")
        continue
    else: 
        passos += 1
    
    resultado = mover_jogador(labirinto, comando)

    if resultado == 'Vitória':
        print(f"Parabéns, {nome_jogador}! Você encontrou a saída!")
        print("😍🥳🎉🎉🎉")
        print(f"Passos dados: {passos}")
        print(f"Tempo gasto: {time.time() - tempo_inicial:.2f} segundos")
        print(f"Erros cometidos: {erros}")
        tempo_gasto = time.time() - tempo_inicial
        pontos = sistema_pontuacao(passos, tempo_gasto, erros)
        print(f"Pontos obtidos: {pontos}")

        break  

    elif resultado == 'parede':
        limpar_tela()
        print("😢💥")
        print("Você bateu em uma parede! Tente outro caminho.")
        print(f"Erros: {erros + 1}/{max_erros}")
        mostrar_labirinto(labirinto)
        input("Pressione Enter para continuar...")
        erros += 1
        
        if erros == max_erros:
            limpar_tela()
            print("Você excedeu o número máximo de erros. Game Over! 💣😥")
            break
    else:
        print("Comando inválido! Use w/a/s/d para mover ou q para sair.")





  