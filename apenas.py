from random import randint
lista = []
i = 0

print("A lenda do cofre de Eldoria: Uma Aventura Personalizada\n")

#função inicializar atributos do jogador
def inicializarJogador():
    nomeAvatar = input("Digite o nome do seu avatar: ")
    nivel = 1
    xp = 0
    vida = 3
    coin = 0
    return nomeAvatar, nivel, xp, vida, coin

def exibirFicha(nomeAvatar, nivel, xp, vida, coin):
    print("Ficha de " + nomeAvatar + ":")
    print("NIvel: ", nivel)
    print("Experiencia: ", xp)
    print("Vidas: ", vida)
    print("Moedas: ", coin)

def rolarDados():
    num = randint(3, 18)
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dado3 = randint(1, 6)
    dados = dado1 + dado2 + dado3

    return dados, num

def Jogo():
    nomeAvatar, nivel, xp, vida, coin = inicializarJogador()

while True:
    exibirFicha(nomeAvatar, nivel, xp, vida, coin)
    print("Bem vindo", nomeAvatar + "! Sua jornada começa agora.\n")

    dados, num = rolarDados()
    print("Role os dados! o valor dos seus dados: \n", dados)

    if dados == num:
        print("Parabens voce desvendou o enigma!")
        coin += 10
        xp += 2
    elif dados != num:
        print("Voce errou!")

        




    break