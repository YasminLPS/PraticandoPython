import random

def jogar():
    
    apresentacao()
    nivel = int(input("(1) Fácil  (2) Medio  (3) Dificil : "))
    print()
    validar_entrada_nivel(nivel)



    palavra_secreta = carregar_palavra_secreta(nivel)

    palavra = ["_" for letra in palavra_secreta]
    print(palavra[0:])

    enforcado = False
    acertou = False
    tentativas = 0
    chutes_lista = []

    while not enforcado and not acertou:

        chute = pede_letra()

        chutes_lista.append(chute)
        print(f"Chutes: {chutes_lista}")

        if chute in palavra_secreta:
            adiciona_letra_na_linha(palavra_secreta, chute, palavra)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcado = tentativas == 7
        acertou = "_" not in palavra
        print(palavra)


    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)



def apresentacao():
    print()
    print("*******************************")
    print("Bem vindo ao jogo de Forca!")
    print("*******************************")
    print("Qual nivel de dificuldade você quer?")

def validar_entrada_nivel(nivel):
    niveis = [1, 2, 3]

    while not nivel in niveis :
        print("*******************************")
        print("Nivel não conhecido, por favor digite o nivel correto!")
        nivel = int(input("(1) Fácil  (2) Medio  (3) Dificil : "))
        print()


def carregar_palavra_secreta(nivel):
    palavras_forca = []

    if nivel == 1:
        arquivo = open("palavras.txt", "r")
    elif nivel == 2:
        arquivo = open("palavrasMedias.txt", "r", encoding="utf8")
    elif nivel == 3:
        arquivo = open("palavrasDificeis.txt", "r", encoding="utf8")


    for linha in arquivo:
        linha = linha.strip()
        palavras_forca.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras_forca))
    palavras_secreta = palavras_forca[numero].upper()
    
    return palavras_secreta

def pede_letra():
    letra_chute = input("Digite uma letra: ")
    chute = letra_chute.upper().strip()
    return chute

def adiciona_letra_na_linha(palavra_secreta, chute, palavra):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavra[index] = letra
        index += 1

def desenha_forca(erros):
    print()
    print("*******************************")
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |       0   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |       0   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |       0   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |       0   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |       0   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |       0   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |       0  ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("*******************************")
    print()

def imprime_mensagem_perdedor(palavra_secreta):
    print()
    print("*******************************")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("*******************************")

def imprime_mensagem_vencedor():
    print()
    print("*******************************")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("*******************************")

if __name__ == "__main__":
    jogar()