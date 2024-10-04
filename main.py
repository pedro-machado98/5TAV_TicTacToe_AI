import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import random
import os

# Variáveis globais para armazenar resultados do relatório
vitorias_jogador_aleatorio = 0
vitorias_jogador_estrategico = 0
vitorias_jogador_humano = 0
empates = 0
jogos_realizados = 0
total_jogos = 0
jogador_x = "Humano"
jogador_o = "Aleatório"

# Função para o jogador aleatório
def jogador_aleatorio():
    jogadas_possiveis = [(i, j) for i in range(3) for j in range(3) if jogo[i][j] == '']
    if jogadas_possiveis:
        return random.choice(jogadas_possiveis)
    return None

# Função para o jogador que não perde (jogadas defensivas)
def jogador_estrategico():
    for i in range(3):
        for j in range(3):
            if jogo[i][j] == '':
                # Tenta fazer a jogada e verifica se vence
                jogo[i][j] = "O"
                if verificar_vencedor_simples("O"):
                    return (i, j)
                jogo[i][j] = ''
    
    for i in range(3):
        for j in range(3):
            if jogo[i][j] == '':
                jogo[i][j] = "X"
                if verificar_vencedor_simples("X"):
                    jogo[i][j] = ''
                    return (i, j)
                jogo[i][j] = ''
    
    return jogador_aleatorio()

def fazer_jogada(linha, coluna):
    global jogador_atual, jogos_realizados

    if jogo[linha][coluna] == '':
        jogo[linha][coluna] = jogador_atual
        botoes[linha][coluna].configure(text=jogador_atual)
        if verificar_vencedor():
            return
        jogador_atual = "O" if jogador_atual == "X" else "X"

        if jogador_atual == "O" and jogador_o != "Humano":
            if jogador_o == "Aleatório":
                jogada = jogador_aleatorio()
            else:
                jogada = jogador_estrategico()
            if jogada:
                fazer_jogada(jogada[0], jogada[1])

        if jogador_atual == "X" and jogador_x != "Humano":
            if jogador_x == "Aleatório":
                jogada = jogador_aleatorio()
            else:
                jogada = jogador_estrategico()
            if jogada:
                fazer_jogada(jogada[0], jogada[1])

def verificar_vencedor():
    global vitorias_jogador_aleatorio, vitorias_jogador_estrategico, vitorias_jogador_humano, empates, jogos_realizados

    combinacoes_vencedoras = (jogo[0], jogo[1], jogo[2],
                              [jogo[i][0] for i in range(3)],
                              [jogo[i][1] for i in range(3)],
                              [jogo[i][2] for i in range(3)],
                              [jogo[i][i] for i in range(3)],
                              [jogo[i][2 - i] for i in range(3)])
    
    for combinacao in combinacoes_vencedoras:
        if combinacao[0] == combinacao[1] == combinacao[2] != '':
            anunciar_vencedor(combinacao[0])
            return True
    
    if all(jogo[i][j] != '' for i in range(3) for j in range(3)):
        anunciar_vencedor("Empate")
        return True

    return False

def verificar_vencedor_simples(jogador):
    combinacoes_vencedoras = (jogo[0], jogo[1], jogo[2],
                              [jogo[i][0] for i in range(3)],
                              [jogo[i][1] for i in range(3)],
                              [jogo[i][2] for i in range(3)],
                              [jogo[i][i] for i in range(3)],
                              [jogo[i][2 - i] for i in range(3)])
    
    for combinacao in combinacoes_vencedoras:
        if combinacao[0] == combinacao[1] == combinacao[2] == jogador:
            return True
    return False

def anunciar_vencedor(jogador):
    global vitorias_jogador_aleatorio, vitorias_jogador_estrategico, vitorias_jogador_humano, empates, jogos_realizados, total_jogos

    if jogador == "Empate":
        empates += 1
        mensagem = "É um empate!"
    else:
        if jogador == "X":
            if jogador_x == "Humano":
                vitorias_jogador_humano += 1
            elif jogador_x == "Aleatório":
                vitorias_jogador_aleatorio += 1
            else:
                vitorias_jogador_estrategico += 1
        else:
            if jogador_o == "Humano":
                vitorias_jogador_humano += 1
            elif jogador_o == "Aleatório":
                vitorias_jogador_aleatorio += 1
            else:
                vitorias_jogador_estrategico += 1
        mensagem = f"Jogador {jogador} venceu!"

    messagebox.showinfo("Fim de Jogo", mensagem)
    jogos_realizados += 1
    gerar_relatorio()

    if jogos_realizados < total_jogos:
        reiniciar_jogo()
    else:
        messagebox.showinfo("Fim da série", "Todas as partidas foram jogadas!")
        reiniciar_jogo()

def reiniciar_jogo():
    global jogo, jogador_atual
    jogo = [['', '', ''] for _ in range(3)]
    jogador_atual = "X"
    for linha in botoes:
        for botao in linha:
            botao.configure(text='')

def gerar_relatorio():
    relatorio = (f"Jogos realizados: {jogos_realizados}\n"
                 f"Vitórias do Jogador Humano: {vitorias_jogador_humano}\n"
                 f"Vitórias do Jogador Aleatório: {vitorias_jogador_aleatorio}\n"
                 f"Vitórias do Jogador Estratégico: {vitorias_jogador_estrategico}\n"
                 f"Empates: {empates}\n\n")
    with open("relatorio_jogo_da_velha.txt", "a") as arquivo:
        arquivo.write(relatorio)

def configurar_jogo():
    global total_jogos, jogador_x, jogador_o

    def salvar_configuracao():
        global total_jogos, jogador_x, jogador_o
        total_jogos = int(entry_jogos.get())
        jogador_x = combo_x.get()
        jogador_o = combo_o.get()
        janela_configuracao.destroy()

    janela_configuracao = tk.Toplevel(root)
    janela_configuracao.title("Configuração do Jogo")

    tk.Label(janela_configuracao, text="Número de Jogos:").grid(row=0, column=0)
    entry_jogos = tk.Entry(janela_configuracao)
    entry_jogos.grid(row=0, column=1)

    tk.Label(janela_configuracao, text="Jogador X (Primeiro):").grid(row=1, column=0)
    combo_x = ttk.Combobox(janela_configuracao, values=["Humano", "Aleatório", "Estratégico"])
    combo_x.grid(row=1, column=1)

    tk.Label(janela_configuracao, text="Jogador O (Segundo):").grid(row=2, column=0)
    combo_o = ttk.Combobox(janela_configuracao, values=["Humano", "Aleatório", "Estratégico"])
    combo_o.grid(row=2, column=1)

    tk.Button(janela_configuracao, text="Salvar", command=salvar_configuracao).grid(row=3, columnspan=2)

# Criar a janela principal
root = tk.Tk()
root.title("Jogo da Velha")
style = Style(theme="flatly")

# Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

config_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Configuração", menu=config_menu)
config_menu.add_command(label="Configurar Jogo", command=configurar_jogo)

# Criar botões para o tabuleiro do jogo com tamanhos maiores e fonte aumentada
botoes = []
for i in range(3):
    linha = []
    for j in range(3):
        botao = tk.Button(root, text='', width=10, height=5, font=('Helvetica', 20),
                          command=lambda i=i, j=j: fazer_jogada(i, j))
        botao.grid(row=i, column=j, padx=5, pady=5)
        linha.append(botao)
    botoes.append(linha)

# Inicializar o tabuleiro do jogo e o jogador atual
jogo = [['', '', ''] for _ in range(3)]
jogador_atual = "X"

root.mainloop()