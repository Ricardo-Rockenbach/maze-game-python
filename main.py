import os
import time
import random


labirinto = [
    ['#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', '.', '.', 'S', '#'],
    ['#', '#', '#', '#', '#']
]

def mostrar_labirinto(matriz):
    for linha in matriz:
        print(' '.join(linha))

mostrar_labirinto(labirinto)

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

    if matriz[nova_i][nova_j] == 'S':
        return 'Vitória'
    
    if matriz[nova_i][nova_j] != '#':
        matriz[i][j] = '.'
        matriz[nova_i][nova_j] = 'P'
        return 'Moveu'
    return 'parede'

while True:
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
        break  
    elif resultado == 'Moveu':
        mostrar_labirinto(labirinto)
    elif resultado == 'parede':
        print("Você bateu em uma parede! Tente outro caminho.")
    else:
        print("Comando inválido! Use w/a/s/d para mover ou q para sair.")

  