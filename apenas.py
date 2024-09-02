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

# Função para tratar erros consecutivos
def tratar_erro_consecutivo(erros_consecutivos, vida):
    if erros_consecutivos >= 2:
        vida -= 1
        erros_consecutivos = 0
        print(f"Você perdeu uma vida! Vidas restantes: {vida}\n")
    return erros_consecutivos, vida

# Função para verificar se o jogador desvendou o enigma
def verificar_enigma(dados, num, coin, xp, nivel):
    if dados == num:
        print("Parabéns, você desvendou o enigma!")
        coin += 10
        xp += 2
        if xp >= 4:
            nivel += 1
            xp -= 4
            print(f"Você subiu para o nível {nivel}!")
        return coin, xp, nivel, True
    else:
        print("Você errou!")
        return coin, xp, nivel, False

# Inicializando o jogador
nome_avatar, nivel, xp, vida, coin = inicializar_jogador()
erros_consecutivos = 0
primeira_tentativa = True

# Exibir ficha inicial
exibir_ficha(nome_avatar, nivel, xp, vida, coin)

# Loop principal do jogo
while vida > 0:
    if primeira_tentativa:
        print(f"Bem-vindo, {nome_avatar}! Sua jornada começa agora.\n")
        primeira_tentativa = False

    dados, num = rolar_dados()
    print(f"Role os dados! O valor dos seus dados: {dados}")
    print(f"Número sorteado: {num}\n")

    coin, xp, nivel, sucesso = verificar_enigma(dados, num, coin, xp, nivel)
    
    if sucesso:
        continuar = input("Deseja sair com os espólios ou continuar para outro cofre? (sair/continuar): ").lower()
        if continuar == 'sair':
            print("Você saiu do jogo com seus espólios.")
            break
    else:
        erros_consecutivos += 1
        erros_consecutivos, vida = tratar_erro_consecutivo(erros_consecutivos, vida)
        
        if vida == 0:
            print("Você perdeu todas as suas vidas! Fim de jogo.")
            break
        
        continuar = input("Deseja tentar novamente ou sair do jogo? (tentar/sair): ").lower()
        if continuar == 'sair':
            print("Você decidiu sair do jogo.")
            break
        elif continuar == 'tentar':
            print()
