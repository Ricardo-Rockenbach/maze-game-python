import os
import time


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
        print("Parabéns! Você encontrou a saída!")
        return 'Vitória'
    
    if matriz[nova_i][nova_j] != '#':
        matriz[i][j] = '.'
        matriz[nova_i][nova_j] = 'P'
        return 'Moveu'
    return 'parede'

while True:
    comando = input("Digite o comando (w/a/s/d para mover, q para sair): ").lower()
    resultado = mover_jogador(labirinto, comando)

  