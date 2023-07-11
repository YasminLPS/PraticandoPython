import forca
import adivinhacao

def escolherJogo():
    print("*******************************")
    print("******Escolha o seu jogo!******")
    print("*******************************")

    jogoEscolhido = int(input("(1) Forca  (2)Adivinhação: "))
    jogos = [1,2]

    while not jogoEscolhido in jogos :
        print("*******************************")
        print("Jogo não conhecido, por favor digite o jogo correto!")
        jogoEscolhido = int(input("(1) Forca  (2)Adivinhação:"))

    if jogoEscolhido == 1:
        forca.jogar()
    elif jogoEscolhido == 2:
        adivinhacao.jogar()

if __name__ == "__main__":
    escolherJogo()