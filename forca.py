
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de Forca!")
    print("*******************************")

    palavra_forca = "banana"
    enforcado = False
    acertou = False
    palavra = []
    chutes = []
    tentativas = 6

    for letra in palavra_forca:
        palavra.append("_")

    print(palavra[0:])

    while not enforcado and not acertou:
        tentativas += 1

        if tentativas > 6:
            enforcado = True

        letra_chute = input("Digite uma letra: ")
        chute = letra_chute.lower().strip()
        chutes.append(chute)
        index = 0

        print(f"Chutes: {chutes}")

        for letra in palavra_forca:
            if chute == letra:
                palavra[index] = chute

            index += 1
        print(palavra)


    print("Fim do Jogo!")


if __name__ == "__main__":
    jogar()