import random

def jogar():
    print()
    print("*******************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*******************************")

    print("Qual nivel de dificuldade você quer?")
    nivel = int(input("(1) Fácil  (2) Medio  (3) Dificil : "))

    niveis = [1, 2, 3]

    while not nivel in niveis :
        print("*******************************")
        print("Nivel não conhecido, por favor digite o nivel correto!")
        nivel = int(input("(1) Fácil  (2) Medio  (3) Dificil : "))


    if nivel == 1:
        numero_secreto = random.randrange(1, 51)
        jogo(50, 7, numero_secreto)
    elif nivel == 2:
        numero_secreto = random.randrange(1, 101)
        jogo(100, 5, numero_secreto)
    elif nivel == 3:
        numero_secreto = random.randrange(1, 201)
        jogo(200, 3, numero_secreto)



    print("*******************************")
    print("Fim de Jogo!")
    print("*******************************")

def jogo(nivel,tentativas, numeroS):
    pontos = 1000
    print("*******************************")
    for rodada in range(1, tentativas + 1):
        print(f"Pontos atuais: {pontos}")
        print(f"Tentativa {rodada} de {tentativas}")
        chute = int(input(f"Digite um número entre 1 e {nivel}: "))
        print(f"Voce chutou: {chute}")

        while not chute > 1 or chute > nivel:
            print("*******************************")
            print(f"Número invalido! Digite o numero de 1 a {nivel}")
            print(f"Tentativa {rodada} de {tentativas}")
            chute = int(input(f"Digite um número entre 1 e {nivel}: "))
            print(f"Voce chutou: {chute}")

        if (numeroS == chute):
            print("*******************************")
            print(f"Você acertou e terminou com {pontos} pontos!")
            break
        else:

            if (chute > numeroS):
                print("*******************************")
                print("Você errou! Seu numero é maior que o secreto!")
            elif (chute < numeroS):
                print("*******************************")
                print("Você errou! Seu numero é menor que o secreto")

            pontos_perdidos = abs(numeroS - chute)
            pontos -= pontos_perdidos

            if (rodada == tentativas and numeroS != chute):
                print("*******************************")
                print("Não possui mais tentativas!")
                print(f"O número secreto era: {numeroS}")

if __name__ == "__main__":
    jogar()