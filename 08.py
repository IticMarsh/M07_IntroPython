import random

# Escollir aleatòriament un número entre 1 i 100
numero_aleatori = random.randint(1, 100)

# Inicialitzar el comptador d'intents
intents = 0

while True:
    # Demanar a l'usuari que introdueixi un número
    guess = int(input("Introdueix un número entre 1 i 100: "))
    
    # Incrementar el comptador d'intents
    intents += 1

    # Comprovar si l'usuari ha encertat
    if guess == numero_aleatori:
        print(f"Has encertat! El número era {numero_aleatori}. Nombre d'intents: {intents}")
        break
    elif guess < numero_aleatori:
        print("El número és més gran. Torna-ho a provar.")
    else:
        print("El número és més petit. Torna-ho a provar.")
