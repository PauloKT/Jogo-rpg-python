from random import randint

# Função para inicializar atributos do jogador
def inicializar_jogador():
    nome_avatar = input("Digite o nome do seu avatar: ")
    nivel = 1
    xp = 0
    vida = 3
    coin = 0
    return nome_avatar, nivel, xp, vida, coin

# Função para exibir a ficha do jogador
def exibir_ficha(nome_avatar, nivel, xp, vida, coin):
    print(f"\n--- Ficha de {nome_avatar} ---")
    print(f"Nível: {nivel}")
    print(f"Experiência: {xp}")
    print(f"Vidas: {vida}")
    print(f"Moedas: {coin}\n")

# Função para rolar os dados
def rolar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dado3 = randint(1, 6)
    dados = dado1 + dado2 + dado3
    num = randint(3, 18)
    return dados, num

# Inicializando o jogador
nome_avatar, nivel, xp, vida, coin = inicializar_jogador()
erros_consecutivos = 0

# Loop principal do jogo
while True:
    exibir_ficha(nome_avatar, nivel, xp, vida, coin)
    print(f"Bem-vindo, {nome_avatar}! Sua jornada começa agora.\n")

    dados, num = rolar_dados()
    print(f"Role os dados! O valor dos seus dados: {dados}")
    print(f"Número sorteado: {num}\n")

    if dados == num:
        print("Parabéns, você desvendou o enigma!")
        coin += 10
        xp += 2
        erros_consecutivos = 0  # Reinicia os erros consecutivos

        # Verifica se o jogador sobe de nível
        if xp >= 4:
            nivel += 1
            xp -= 4
            print(f"Você subiu para o nível {nivel}!")

        # Pergunta se o jogador quer continuar ou sair com os espólios
        continuar = input("Deseja sair com os espólios ou continuar para outro cofre? (sair/continuar): ").lower()
        if continuar == 'sair':
            print("Você saiu do jogo com seus espólios.")
            break

    else:
        print("Você errou!\n")
        erros_consecutivos += 1

        # Se o jogador errar duas vezes, ele perde uma vida
        if erros_consecutivos == 2:
            vida -= 1
            erros_consecutivos = 0
            print(f"Você perdeu uma vida! Vidas restantes: {vida}\n")

        # Verifica se o jogador ainda tem vidas
        if vida == 0:
            print("Você perdeu todas as suas vidas! Fim de jogo.")
            break

        # Pergunta se o jogador quer continuar jogando após um erro
        continuar = input("Deseja tentar novamente ou sair do jogo? (tentar/sair): ").lower()
        if continuar == 'sair':
            print("Você decidiu sair do jogo.")
            break

        if continuar == 'tentar':
            dados, num = rolar_dados()
            print(f"Role os dados! O valor dos seus dados: {dados}")
            print(f"Número sorteado: {num}\n")

            if dados == num:
                print("Parabéns, você desvendou o enigma!")
                coin += 10
                xp += 2
                erros_consecutivos = 0  # Reinicia os erros consecutivos

                # Verifica se o jogador sobe de nível
                if xp >= 4:
                    nivel += 1
                    xp -= 4
                    print(f"Você subiu para o nível {nivel}!")
            else:
                print("Você errou novamente!\n")
                erros_consecutivos += 1

                if erros_consecutivos == 2:
                    vida -= 1
                    erros_consecutivos = 0
                    print(f"Você perdeu uma vida! Vidas restantes: {vida}\n")

                if vida == 0:
                    print("Você perdeu todas as suas vidas! Fim de jogo.")
                    break

    # Exibir ficha atualizada após cada enigma
    exibir_ficha(nome_avatar, nivel, xp, vida, coin)
