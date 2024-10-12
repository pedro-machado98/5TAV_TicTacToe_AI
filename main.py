import random
import os
from datetime import datetime

maxJogadas = 9
vitoria = False
tabuleiro = [0] * 15

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
            return tabuleiro[pos1]

    return 0

def limpaTabuleiro():
    for i in range(1, 10):
        tabuleiro[i] = 0
    tabuleiro[11] = 0

def limpaTabuleiroFinal():
    for i in range(1, 10):
        tabuleiro[i] = 0
    tabuleiro[10] = 0  # Número de partidas
    tabuleiro[11] = 0  # Resultado da partida atual
    tabuleiro[12] = 0  # Vitórias do jogador 1
    tabuleiro[13] = 0  # Empates
    tabuleiro[14] = 0  # Vitórias do jogador 2

# Funções de jogadores
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

def jogadorAleatorio(quemJoga):
    while True:
        posicao = random.randint(1, 9)
        if tabuleiro[posicao] == 0:
            tabuleiro[posicao] = quemJoga
            break

def jogadorCampeao(quemJoga):
    # 1. Ganhar: Se houver duas peças numa linha, coloque a terceira.
    for combinacao in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
        valores = [tabuleiro[pos] for pos in combinacao]
        if valores.count(quemJoga) == 2 and valores.count(0) == 1:
            tabuleiro[combinacao[valores.index(0)]] = quemJoga
            return

    # 2. Bloquear: Se o oponente tiver duas peças numa linha, bloqueie.
    oponente = 2 if quemJoga == 1 else 1
    for combinacao in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
        valores = [tabuleiro[pos] for pos in combinacao]
        if valores.count(oponente) == 2 and valores.count(0) == 1:
            tabuleiro[combinacao[valores.index(0)]] = quemJoga
            return

    # 3. Triângulo: Criar uma situação onde seja possível ganhar de duas formas.
    cantos = [1, 3, 7, 9]
    for canto in cantos:
        if tabuleiro[canto] == 0:
            tabuleiro[canto] = quemJoga
            if criaTriangulo(quemJoga):
                return
            tabuleiro[canto] = 0

    # 4. Bloquear Triângulo do oponente.
    for canto in cantos:
        if tabuleiro[canto] == 0:
            tabuleiro[canto] = oponente
            if criaTriangulo(oponente):
                tabuleiro[canto] = quemJoga
                return
            tabuleiro[canto] = 0

    # 5. Centro: Se o centro estiver livre, ocupe-o.
    if tabuleiro[5] == 0:
        tabuleiro[5] = quemJoga
        return

    # 6. Canto vazio: Jogue em um canto vazio.
    for canto in cantos:
        if tabuleiro[canto] == 0:
            tabuleiro[canto] = quemJoga
            return

    # 7. Lado vazio: Jogue em um lado vazio.
    lados = [2, 4, 6, 8]
    for lado in lados:
        if tabuleiro[lado] == 0:
            tabuleiro[lado] = quemJoga
            return

def criaTriangulo(quemJoga):
    # Checa se o jogador pode ganhar em mais de uma linha com uma jogada
    combinacoesVitoria = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    possibilidades = 0
    for combinacao in combinacoesVitoria:
        valores = [tabuleiro[pos] for pos in combinacao]
        if valores.count(quemJoga) == 2 and valores.count(0) == 1:
            possibilidades += 1
    return possibilidades >= 2



# Função para gerar o relatório do jogo
def gerarRelatorio(jogador1, jogador2):
    data_hora_atual = datetime.now()
    data_formatada = data_hora_atual.strftime("%d_%m_%Y_%H_%M")
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

def game(jogador1, jogador2, quantidadePartidas):
    global vitoria

    for partida in range(quantidadePartidas):
        limpaTabuleiro()
        jogadas = 0
        vitoria = False

        while jogadas < maxJogadas:
            # Jogador 1 faz a jogada nas rodadas ímpares (1ª, 3ª, 5ª, etc.)
            if jogadas % 2 == 0:
                if jogador1 == 'h':
                    jogadorHumano(1)
                elif jogador1 == 'a':
                    jogadorAleatorio(1)
                elif jogador1 == 'c':
                    jogadorCampeao(1)
            # Jogador 2 faz a jogada nas rodadas pares (2ª, 4ª, 6ª, etc.)
            else:
                if jogador2 == 'h':
                    jogadorHumano(2)
                elif jogador2 == 'a':
                    jogadorAleatorio(2)
                elif jogador2 == 'c':
                    jogadorCampeao(2)

            vencedor = checaVencedor()
            if vencedor != 0:
                tabuleiro[11] = vencedor
                if vencedor == 1:
                    tabuleiro[12] += 1
                else:
                    tabuleiro[14] += 1
                vitoria = True
                break

            jogadas += 1

        if not vitoria:
            tabuleiro[11] = 0
            tabuleiro[13] += 1  # Empate

        tabuleiro[10] += 1

    gerarRelatorio(jogador1, jogador2)


def descricaoJogador(tipoJogador):
    if tipoJogador == 'h':
        return "humano"
    elif tipoJogador == 'a':
        return "aleatorio"
    elif tipoJogador == 'c':
        return "campeao"
    else:
        return "desconhecido"


# Função de menu
def menu():
    continuar = 1
    while continuar == 1:
        quantidadePartidas = int(input("Digite a quantidade de partidas: "))
        jogador1 = input("Escolha o tipo de jogador 1: ['h', 'a', 'c']: ")
        jogador2 = input("Escolha o tipo de jogador 2: ['h', 'a', 'c']: ")
        game(jogador1, jogador2, quantidadePartidas)
        limpaTabuleiroFinal()
        continuar = int(input("Digite 1 para continuar ou outro número para sair: "))

# Executa o menu
menu()
