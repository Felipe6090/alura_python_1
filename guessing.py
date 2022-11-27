import random

def execute():
    print('************************************')
    print('bem vindo, escolha sua dificuldade: ')
    print('************************************')


    secret_num = int(random.randrange(1, 101))
    shots = 0
    round = 1

    score = 1000

    level = int(input("Dificuldade: "))

    if (level == 1):
        shots = 20
    elif (level == 2):
        shots = 10
    elif (level == 3):
        shots = 5

    for round in range(1, shots + 1):

        print("Tentativa {} de {}".format(round, shots))

        chute = int(input("digite seu número: "))

        print("Você digitou: ", chute)

        penalty = abs(secret_num - chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        isRight = chute == secret_num
        maior = chute > secret_num
        menor = chute < secret_num

        if (isRight):
            print("Você acertou!")
            break

        elif (maior):
            print("Você chutou para cima")
            score = score - penalty

        elif (menor):
            print("Você chutou para baixo")
            score = score - penalty

    round += 1
