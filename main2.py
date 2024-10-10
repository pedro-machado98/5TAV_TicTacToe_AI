import random

maxJogadas = 9
jogadas = 0
quemJoga = 1
vitoria = False
tabuleiro = [0] * 15  # Incluindo a posição 14 para vitórias do jogador 2

def menu():
    continuar = 1
    quantidadePartidas = 0
    jogador1 = 'h'  # 'h' = humano / 'a' = aleatório / 'v' = vencedor
    jogador2 = 'h'  # 'h' = humano / 'a' = aleatório / 'v' = vencedor

    while continuar:
        print("\nMenu do Jogo da Velha")
        print("1. Selecionar Jogador 1")
        print("2. Selecionar Jogador 2")
        print("3. Selecionar Quantidade de Partidas")
        print("4. Jogar")
        print("0. Sair")

        try:
            continuar = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")
            continue

        if continuar == 1:
            jogador1 = input("Escolha o tipo de Jogador 1 (h = humano / a = aleatório / c = campeao): ").lower()
        elif continuar == 2:
            jogador2 = input("Escolha o tipo de Jogador 2 (h = humano / a = aleatório / c = campeao): ").lower()
        elif continuar == 3:
            try:
                quantidadePartidas = int(input("Digite a quantidade de partidas que deseja jogar: "))
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro.")
        elif continuar == 4:
            print(f"\n\nIniciando o jogo com Jogador 1 ({jogador1}) e Jogador 2 ({jogador2}) para {quantidadePartidas} partida(s).")
            game(jogador1, jogador2, quantidadePartidas)
        elif continuar == 0:
            print("Saindo...")
        else:
            print("Opção inválida! Tente novamente.")

def simboloJogador(valor):
    return 'X' if valor == 1 else 'O' if valor == 2 else ' '

def checaVencedor():
    combinacoesVitoria = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Linhas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Colunas
        [1, 5, 9], [3, 5, 7]              # Diagonais
    ]

    for combinacao in combinacoesVitoria:
        pos1, pos2, pos3 = combinacao
        if tabuleiro[pos1] == tabuleiro[pos2] == tabuleiro[pos3] != 0:
            return tabuleiro[pos1]  # Retorna 1 se jogador 1 venceu, ou 2 se jogador 2 venceu

    return 0  # Retorna 0 se não houver vencedor

def exibeTabuleiro():
    print(f"{simboloJogador(tabuleiro[1])} | {simboloJogador(tabuleiro[2])} | {simboloJogador(tabuleiro[3])}      1|2|3")
    print(f"{simboloJogador(tabuleiro[4])} | {simboloJogador(tabuleiro[5])} | {simboloJogador(tabuleiro[6])}      4|5|6")
    print(f"{simboloJogador(tabuleiro[7])} | {simboloJogador(tabuleiro[8])} | {simboloJogador(tabuleiro[9])}      7|8|9")

def limpaTabuleiro():
    for i in range(0, 10):
        tabuleiro[i] = 0
    tabuleiro[11] = 0  # Resetando o resultado da partida

def jogadorAleatorio():
    global quemJoga
    while True:
        posicao = random.randint(1, 9)
        if tabuleiro[posicao] == 0:
            tabuleiro[posicao] = quemJoga
            print(f"Jogador {quemJoga} ({'X' if quemJoga == 1 else 'O'}) jogou na posição {posicao}")
            break

import os
from datetime import datetime

def gerarRelatorio(jogador1, jogador2):
    # Obtém a data e hora atuais
    data_hora_atual = datetime.now()
    data_formatada = data_hora_atual.strftime("%d_%m_%Y_%H_%M")

    # Cria o nome do arquivo no formato solicitado
    nome_arquivo = f"{descricaoJogador(jogador1)}_{descricaoJogador(jogador2)}_{data_formatada}.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("Relatorio do Jogo da Velha\n")
        arquivo.write("===========================\n")
        arquivo.write(f"Jogador 1: {descricaoJogador(jogador1)}\n")
        arquivo.write(f"Jogador 2: {descricaoJogador(jogador2)}\n")
        arquivo.write("===========================\n")
        arquivo.write(f"Vitorias do Jogador 1: {tabuleiro[12]}\n")
        arquivo.write(f"Vitorias do Jogador 2: {tabuleiro[14]}\n")
        arquivo.write(f"Empates: {tabuleiro[13]}\n")
        arquivo.write("===========================\n")
        arquivo.write("Obrigado por jogar!\n")

    print(f"Relatório gerado com sucesso em: {os.path.abspath(nome_arquivo)}")

def descricaoJogador(tipoJogador):
    if tipoJogador == 'h':
        return "humano"
    elif tipoJogador == 'a':
        return "aleatorio"
    elif tipoJogador == 'c':
        return "campeao"
    else:
        return "desconhecido"

def jogadorHumano(quemJoga):
    while True:
        try:
            posicao = int(input(f"Jogador {quemJoga} ({'X' if quemJoga == 1 else 'O'}), escolha uma posição de 1 a 9: "))
            if posicao < 1 or posicao > 9:
                print("Posição inválida! Escolha um número de 1 a 9.")
                continue
            if tabuleiro[posicao] != 0:
                print("Posição já ocupada! Escolha outra posição.")
                continue
            tabuleiro[posicao] = quemJoga
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número de 1 a 9.")

def game(jogador1, jogador2, quantidadePartidas):
    global quemJoga, maxJogadas, vitoria

    while tabuleiro[10] < quantidadePartidas:
        print(f"\nJogo {tabuleiro[10] + 1}")
        limpaTabuleiro()
        exibeTabuleiro()
        vitoria = False
        quemJoga = 1  # Sempre começa com o jogador 1

        while tabuleiro[0] < maxJogadas:
            if quemJoga == 1:
                if jogador1 == 'h':
                    jogadorHumano(quemJoga)
                elif jogador1 == 'a':
                    jogadorAleatorio()
            else:
                if jogador2 == 'h':
                    jogadorHumano(quemJoga)
                else:
                    jogadorAleatorio()

            exibeTabuleiro()
            vencedor = checaVencedor()
            if vencedor != 0:
                print(f"Jogador {'1 (X)' if vencedor == 1 else '2 (O)'} venceu!")
                tabuleiro[11] = vencedor
                if vencedor == 1:
                    tabuleiro[12] += 1  # Vitória do jogador 1
                else:
                    tabuleiro[14] += 1  # Vitória do jogador 2
                vitoria = True
                break

            tabuleiro[0] += 1
            quemJoga = 1 if quemJoga == 2 else 2  # Alterna entre os jogadores

        if not vitoria:
            tabuleiro[11] = 0
            tabuleiro[13] += 1  # Empate
            print("Empate!")

        tabuleiro[10] += 1

    print("\nFim das partidas!")
    print(f"Vitórias Jogador 1: {tabuleiro[12]}, Empates: {tabuleiro[13]}, Vitórias Jogador 2: {tabuleiro[14]}")

    gerarRelatorio(jogador1, jogador2)  # Chama a função para gerar o relatório



menu()
