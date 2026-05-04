# 🧩 Maze Game (Python)

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um jogo de labirinto utilizando **Python**, com foco na utilização de **matrizes** para representação do ambiente.

O jogador deve encontrar a saída do labirinto evitando colisões com paredes, enquanto acumula pontos com base em seu desempenho.

---

## 🎯 Objetivo

Atender aos requisitos acadêmicos:

* Utilização de estruturas de dados (matrizes)
* Implementação de regras e pontuação
* Manipulação de arquivos (ranking)
* Interação com o usuário

---

## 🚀 Funcionalidades

### 🎮 Gameplay

* Movimentação com `W A S D`
* Labirinto gerado automaticamente a cada partida
* Caminho garantido até a saída
* Caminhos alternativos e becos sem saída
* Sistema de colisão com paredes
* Condição de vitória e Game Over

---

### 🧠 Sistema de pontuação

Pontuação baseada em:

* Número de passos
* Tempo gasto
* Quantidade de erros

---

### 🏆 Ranking

* Salvamento em arquivo `ranking.txt`
* Leitura automática
* Ordenação por pontuação
* Exibição dos Top 10 jogadores

---

### 🖥️ Interface

O projeto possui duas versões:

#### 💻 Terminal

* Interface via console
* Menu inicial interativo
* Exibição do labirinto em texto

#### 🪟 Tkinter (Interface Gráfica)

* Interface visual com grid
* Movimentação por teclado
* Feedback com pop-ups
* Menu, ranking e gameplay integrados

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Tkinter
* Manipulação de arquivos (`.txt`)
* Programação estruturada

---

## 📂 Estrutura do projeto

```
📁 projeto-labirinto
│
├── main.py        # Lógica do jogo (terminal + funções reutilizáveis)
├── app.py         # Interface gráfica (Tkinter)
├── ranking.txt    # Dados dos jogadores (ignorado no git)
├── README.md
```

---

## ▶️ Como executar

### 🔹 Versão Terminal

```bash
python main.py
```

### 🔹 Versão Gráfica

```bash
python app.py
```

---

## 📌 Melhorias futuras

* Interface mais avançada (animações)
* Sistema de níveis/dificuldade
* Melhor organização com orientação a objetos
* Persistência em banco de dados

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos.

