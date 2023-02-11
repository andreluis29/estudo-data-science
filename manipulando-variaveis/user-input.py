print("====================")
print("Seja bem vindo ao jogo de adivinhação!")
print("====================")

numero_secreto = 42

chute = int(input("Digite seu número: \n"))

print("Você digitou: ", chute)

if (numero_secreto == chute):
    print("====================")
    print("====================")
    print("====================")
    print("====================")
    print("Você acertou o número secreto!\n\n")
    print("====================")
    print("====================")
    print("PARABÉNS!")
    print("====================")
    print("====================")
else:
    print("====================")
    print("====================")
    print("====================")
    print("====================")
    print("Você errou!\n\n")
