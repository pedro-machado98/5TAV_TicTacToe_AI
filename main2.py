maxJogadas = 9
jogadas = 0
quemJoga = 2
vitoria = False
tabuleiro = [0] * 14

def menu():
    continuar = 1
    quantidadePartidas = 0
    jogador1 = 'h'  # 'h' = humano / 'a' = aleatório / 'v' = vencedor
    jogador2 = 'h'  # 'h' = humano / 'a' = aleatório / 'v' = vencedor

    while continuar:
        print("Menu do Jogo da Velha")
        print("1. Selecionar Jogador 1")
        print("2. Selecionar Jogador 2")
        print("3. Selecionar Quantidade de Partidas")
        print("4. Jogar")
        print("0. Sair")

        continuar = int(input("Escolha uma opção: "))

        if continuar == 1:
            jogador1 = input("Escolha o tipo de Jogador 1 (h = humano / a = aleatório / v = vencedor): ").lower()
        elif continuar == 2:
            jogador2 = input("Escolha o tipo de Jogador 2 (h = humano / a = aleatório / v = vencedor): ").lower()
        elif continuar == 3:
            tabuleiro[10] = int(input("Digite a quantidade de partidas que deseja jogar: "))
        elif continuar == 4:
            print(f"\n\nIniciando o jogo com Jogador 1 ({jogador1}) e Jogador 2 ({jogador2}) para {tabuleiro[10]} partida(s).")
            game(jogador1, jogador2, tabuleiro[10])
        elif continuar == 0:
            print("Saindo...")
        else:
            print("Opção inválida! Tente novamente.")



def exibeTabuleiro():
    print(str(tabuleiro[1]) + " | " + str(tabuleiro[2]) + " | " + str(tabuleiro[3]) + "      " + "1|2|3")
    print(str(tabuleiro[4]) + " | " + str(tabuleiro[5]) + " | " + str(tabuleiro[6]) + "      " + "4|5|6")
    print(str(tabuleiro[7]) + " | " + str(tabuleiro[8]) + " | " + str(tabuleiro[9]) + "      " + "7|8|9")

def limpaTabuleiro():
    for i in range(1, 10):
        tabuleiro[i] = 0

def jogadorAleatorio():
    print("Lógica do jogo da velha aqui...")


def jogadorCampeao():
    print("Lógica do jogo da velha aqui...")


def jogadorHumano(quemJoga):
    while True:
        try:
            # Solicita uma posição para o jogador humano
            posicao = int(input(f"Jogador {quemJoga} ({'X' if quemJoga == 1 else 'O'}), escolha uma posição de 1 a 9: "))

            # Verifica se a posição é válida
            if posicao < 1 or posicao > 9:
                print("Posição inválida! Escolha um número de 1 a 9.")
                continue

            # Verifica se a posição está livre
            if tabuleiro[posicao] != 0:
                print("Posição já ocupada! Escolha outra posição.")
                continue

            # Marca a posição no tabuleiro para o jogador atual
            tabuleiro[posicao] = 'X' if quemJoga == 1 else 'O'
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número de 1 a 9.")

def game(jogador1, jogador2, quantidadePartidas):
    global quemJoga, jogadas, maxJogadas, vitoria

    while tabuleiro[0] < quantidadePartidas:
        print(f"\nJogo {tabuleiro[0] + 1}")
        limpaTabuleiro()
        exibeTabuleiro()
        jogadas = 0
        vitoria = False

        while jogadas < maxJogadas and not vitoria:
            if quemJoga == 1:
                if jogador1 == 'h':
                    jogadorHumano(quemJoga)
                else:
                    jogadorAleatorio()  # Ou outro tipo de jogador
            else:
                if jogador2 == 'h':
                    jogadorHumano(quemJoga)
                else:
                    jogadorAleatorio()  # Ou outro tipo de jogador

            exibeTabuleiro()
            jogadas += 1
            quemJoga = 1 if quemJoga == 2 else 2  # Alterna entre os jogadores

        tabuleiro[0] += 1

    print("\nFim das partidas!")


########################################################
menu()