import random
num_secreto=random.randrange(1,100)
numero=0

while num_secreto != numero:
    numero = int(input("digite um numero de 1 a 100 é aleatorio: "))

    if num_secreto != numero:
        print("voce errou")
    else:
        if num_secreto == numero:
            print("voce ganhou")

    if num_secreto < numero:
        print("o numero secreto é menor")
    else:
        num_secreto > numero
        print("o numero secreto é maior")









































