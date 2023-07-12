
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de Forca!")
    print("*******************************")

    palavra_forca = "maça".upper()
    palavra = ["_" for letra in palavra_forca]
    chutes = []

    enforcado = False
    acertou = False
    tentativas = 0

    print(palavra[0:])

    while not enforcado and not acertou:

        letra_chute = input("Digite uma letra: ")
        chute = letra_chute.upper().strip()
        chutes.append(chute)
        index = 0
        tentativas += 1

        print(f"Chutes: {chutes}")

        for letra in palavra_forca:
            if chute == letra:
                palavra[index] = chute
            index += 1

        enforcado = tentativas == 6
        acertou = "_" not in palavra
        print(palavra)


    if acertou:
        print("Você acertou!")
    else:
        print("Enforcado! Você perdeu!")
    print("Fim do Jogo!")


if __name__ == "__main__":
    jogar()