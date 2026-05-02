import tkinter as tk
import time
from tkinter import messagebox
from main import (
    gerar_labirinto,
    mover_jogador,
    sistema_pontuacao,
    salvar_ranking
)

janela = tk.Tk()

janela.title("Labirinto")
janela.geometry("634x679") # Ajuste o tamanho da janela conforme necessário


def tela_menu():

    for widget in janela.winfo_children():
        widget.destroy()

    titulo = tk.Label(
        janela,
        text="LABIRINTO",
        font=("Arial", 24)
    )

    titulo.pack(pady=20)

    botao_jogar = tk.Button(
        janela,
        text="Jogar",
        width=20,
        command=iniciar_jogo
    )

    botao_jogar.pack(pady=10)

    botao_ranking = tk.Button(
        janela,
        text="Ranking",
        width=20,
        command=tela_ranking
    )

    botao_ranking.pack(pady=10)

    botao_sair = tk.Button(
        janela,
        text="Sair",
        width=20,
        command=janela.destroy
    )

    botao_sair.pack(pady=10)

def tela_ranking():

    for widget in janela.winfo_children():
        widget.destroy()

    titulo = tk.Label(
        janela,
        text="🏆 RANKING DOS JOGADORES 🏆",
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=20)

    frame_ranking = tk.Frame(janela)

    frame_ranking.pack()

    cabecalho = tk.Label(
        frame_ranking,
        text="POS  NOME                PONTOS    PASSOS    TEMPO    ERROS",
        font=("Courier", 12, "bold")
    )

    cabecalho.pack(anchor="w")

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

            ranking.sort(
                key=lambda jogador: jogador["pontos"],
                reverse=True
            )

            for posicao, jogador in enumerate(ranking[:10], start=1):

                texto = (
                    f"{posicao:<5}"
                    f"{jogador['nome'][:20]:<20}"
                    f"{jogador['pontos']:<10}"
                    f"{jogador['passos']:<10}"
                    f"{jogador['tempo']:<10}"
                    f"{jogador['erros']}"
                )

                linha_label = tk.Label(
                    frame_ranking,
                    text=texto,
                    font=("Courier", 12)
                )

                linha_label.pack(anchor="w")

    except FileNotFoundError:

        vazio = tk.Label(
            janela,
            text="Nenhum ranking salvo ainda.",
            font=("Arial", 14)
        )

        vazio.pack(pady=20)

    botao_voltar = tk.Button(
        janela,
        text="Voltar",
        width=20,
        command=tela_menu
    )

    botao_voltar.pack(pady=30)

from tkinter import simpledialog

def iniciar_jogo():
    global erros
    global labirinto
    global passos
    global tempo_inicial
    global nome_jogador

    nome_jogador = simpledialog.askstring(
        "Nome do jogador",
        "Digite seu nome:"
    )

    if not nome_jogador:
        return

    messagebox.showinfo(
        "Bem-vindo ao Labirinto!",
        f"Olá, {nome_jogador}! 👋\n\n"
        "INSTRUÇÕES:\n"
        "• Use W A S D para se mover\n"
        "• Encontre a porta verde 🚪\n"
        "• Evite bater nas paredes\n"
        "• Você perde ao atingir 5 erros\n\n"
        "Boa sorte! 🍀"
    )

    erros = 0
    passos = 0

    tempo_inicial = time.time()

    labirinto = gerar_labirinto(20)

    desenhar_labirinto()

def desenhar_labirinto():

    for widget in janela.winfo_children():
        widget.destroy()

    for i, linha in enumerate(labirinto):

        for j, coluna in enumerate(linha):

            if coluna == '#':
                cor = "black"

            elif coluna == '.':
                cor = "white"

            elif coluna == '◉':
                cor = "deepskyblue"

            elif coluna == '🚪':
                cor = "green"

            label = tk.Label(
                janela,
                bg=cor,
                width=4,
                height=2,
                relief="solid",
                borderwidth=1
            )

            label.grid(row=i, column=j)
    info = tk.Label(
    janela,
    text=f"👤 {nome_jogador} | 👣 Passos: {passos} | 💥 Erros: {erros}/5",
    font=("Arial", 12, "bold")
    )

    info.grid(row=21, column=0, columnspan=20, pady=10)

def mover(event):
    global erros
    global passos

    tecla = event.keysym

    direcao = None

    if tecla == 'w':
        direcao = 'w'

    elif tecla == 's':
        direcao = 's'

    elif tecla == 'a':
        direcao = 'a'

    elif tecla == 'd':
        direcao = 'd'

    if direcao:
        passos += 1
        resultado = mover_jogador(labirinto, direcao)

        if resultado == 'Vitória':
            
            tempo_gasto = time.time() - tempo_inicial

            pontos = sistema_pontuacao(
                passos,
                tempo_gasto,
                erros
            )

            salvar_ranking(
                nome_jogador,
                pontos,
                passos,
                tempo_gasto,
                erros
            )

            messagebox.showinfo(
                "Vitória",
                f"🎉 VOCÊ VENCEU 🎉\n\n"
                f"Jogador: {nome_jogador}\n"
                f"Pontos: {pontos}\n"
                f"Passos: {passos}\n"
                f"Tempo: {tempo_gasto:.2f}s\n"
                f"Erros: {erros}"
            )

            tela_menu()
            return


        elif resultado == 'parede':
            erros += 1
            messagebox.showwarning("Aviso", f"💥 Parede! Erros: {erros}/5")

            if erros >= 5:

                messagebox.showerror(
                    "Fim de jogo",
                    f"💀 GAME OVER 💀\n\n"
                    f"Jogador: {nome_jogador}\n"
                    f"Passos: {passos}"
                )

                tela_menu()
                return

        desenhar_labirinto()






# desenhar_labirinto()
tela_menu()
janela.bind("<Key>", mover)
janela.focus_force()
janela.mainloop()
