import random

def jogar():
    
    apresentacao()
    palavra_secreta = carregar_palavra_secreta()
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

        enforcado = tentativas == 6
        acertou = "_" not in palavra
        print(palavra)


    if acertou:
        print("Você acertou!")
    else:
        print("Enforcado! Você perdeu!")
    print("Fim do Jogo!")



def apresentacao():
    print("*******************************")
    print("Bem vindo ao jogo de Forca!")
    print("*******************************")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras_forca = []

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

if __name__ == "__main__":
    jogar()