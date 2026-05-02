import os
import time
import random

jogador = '◉'
parede  = '#'
caminho  = '.'
saida = '🚪'

    # Utilitario para limpar a tela:
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Sistema de pontuação:
def sistema_pontuacao(passos, tempo_gasto, erros):
    pontos = max(0, 5000 - (passos * 10 + int(tempo_gasto) * 5 + erros * 50))
    if pontos < 0:
        pontos = 0
    return pontos

def salvar_ranking(nome, pontos, passos, tempo_gasto, erros):
    with open("ranking.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{pontos};{passos};{tempo_gasto:.2f};{erros}\n")

def mostrar_ranking():
    limpar_tela()
    print("🏆 RANKING DOS JOGADORES 🏆\n")

    try:
        with open("ranking.txt", "r", encoding="utf-8") as arquivo:
            ranking = []

            for linha in arquivo:
                nome, pontos, passos, tempo, erros = linha.strip().split(";")

                ranking.append({
                    "nome": nome,
                    "pontos": int(pontos),
                    "passos": passos,
                    "tempo": tempo,
                    "erros": erros
                })

            ranking.sort(key=lambda jogador: jogador["pontos"], reverse=True)

            for posicao, jogador in enumerate(ranking[:10], start=1):
                print(
                    f"{posicao}º - {jogador['nome']} | "
                    f"Pontos: {jogador['pontos']} | "
                    f"Passos: {jogador['passos']} | "
                    f"Tempo: {jogador['tempo']}s | "
                    f"Erros: {jogador['erros']}"
                )

    except FileNotFoundError:
        print("Nenhum ranking salvo ainda.")

    input("\nPressione Enter para continuar...")

# Menu inicial:

def menu_inicial():
    while True:
        limpar_tela()

        print("=== LABIRINTO ===")
        print("1 - Jogar")
        print("2 - Ver Ranking")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            limpar_tela()
            break

        elif opcao == '2':
            mostrar_ranking()

        elif opcao == '3':
            limpar_tela()
            exit()

        else:
            print("Opção inválida.")
            input("Pressione Enter...")

# Parametros iniciais:
def parametros_iniciais():
    limpar_tela()
    print("Bem-vindo ao Labirinto!")
    print("Instruções: Use w/a/s/d para mover para cima/esquerda/baixo/direita. \nEncontre a saída (🚪) para vencer o jogo. Cuidado com as paredes (#)!")
    nome_jogador = input("Digite seu nome: ")
    print(f"Bem-vindo ao Labirinto, {nome_jogador}!")
    input("Pressione Enter para começar...")
    tempo_inicial = time.time()

    return tempo_inicial, nome_jogador


# Funções para o jogo:

# geração do mapa

def gerar_labirinto(tamanho):
    labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]
    
    i, j = 1, 1
    fim_i, fim_j = tamanho - 2, tamanho - 2
    labirinto[i][j] = jogador # Posição inicial do jogador

# Fase 01 - Gerar caminho garantido do início ao fim
    while (i, j) != (fim_i, fim_j):
        if random.choice([True, False]):    
            if i < fim_i:
                i += 1
        else:
            if j < fim_j:
                j += 1

        labirinto[i][j] = caminho  # Caminho aberto

    labirinto[fim_i][fim_j] = saida  # Posição da saída

# Fase 02 - Adicionar caminhos aleatórios para aumentar a dificuldade
    for _ in range(tamanho):
        #pegando um ponto que já é caminho
        while True:
            x = random.randint(1, tamanho - 2)
            y = random.randint(1, tamanho - 2)
            if labirinto[x][y] == caminho:
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
                labirinto[x][y] = caminho  # Abrir caminho
            else:
                break  # Parar se encontrar um caminho já aberto
    return labirinto

def mostrar_labirinto(matriz):
    for linha in matriz:
        print(' '.join(linha))

# Movimentação do jogador

def encontrar_jogador(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == jogador:
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

    if not (0 <= nova_i < len(matriz) and 0 <= nova_j < len(matriz[0])): # Impedir de sair dos limites do labirinto
        return 'parede'

    if matriz[nova_i][nova_j] == saida:
        return 'Vitória'

    if matriz[nova_i][nova_j] != parede:
        matriz[i][j] = caminho
        matriz[nova_i][nova_j] = jogador
        return 'Moveu'
    return 'parede'

# Loop principal do jogo:

while True:
    menu_inicial()

    tempo_inicial, nome_jogador = parametros_iniciais()

    labirinto = gerar_labirinto(20)

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

            salvar_ranking(nome_jogador, pontos, passos, tempo_gasto, erros)
            input("Pressione Enter para ver o ranking...")
            mostrar_ranking()
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
                print("💀 GAME OVER 💀")
                print(f"{nome_jogador}, você excedeu o limite de erros!")
                print(f"Passos dados: {passos}")
                print(f"Tempo gasto: {time.time() - tempo_inicial:.2f} segundos")
                input("Pressione Enter para voltar ao menu inicial...")
                break
        else:
            print("Comando inválido! Use w/a/s/d para mover ou q para sair.")





  