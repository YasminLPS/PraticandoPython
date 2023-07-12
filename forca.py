
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de Forca!")
    print("*******************************")

    palavra_forca = "banana"
    enforcado = False
    acertou = False
    palavra = []
    chutes = []

    for letra in  palavra_forca:
        palavra.append("_")

    print(palavra[0:])


    while not enforcado and not acertou:
        letra_chute = input("Digite uma letra: ")
        chute = letra_chute.lower().strip()
        chutes.append(chute)
        print(f"Chutes: {chutes}")
        index = 0
        for letra in palavra_forca:
            if chute == letra:
                palavra[index] = chute
            index += 1
        print(palavra)


    print("Fim do Jogo!")


if __name__ == "__main__":
    jogar()