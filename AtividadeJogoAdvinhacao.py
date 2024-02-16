#Desenvolva um jogo de adivinhação em que o programa
#escolhe um número aleatório e desafia o jogador a
#adivinhá-lo. Forneça dicas ao jogador, indicando se o
#número é maior ou menor do que a adivinhação atual.

import random 

random_numbers = random.randint(0,40)

print("GAME OF NUMBER")
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print("Try to guess beetwen a number from 0 to 40")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
name = input("Please enter your name:")
welcome = print(f"Welcome {name}!!")
are_you_ready = input("Are you ready(yes/no):")

while are_you_ready.lower() == 'no':
    print(f'Bye {name}. Thanks for you playing.')
    break
else:
    print("LETS GOO!")
    
    attempts = 0

    while True:
        #Solicita a tentativa do jogador
        guess = int(input("Type your guess:"))
        #Conta o número de vezes até o jogador acertar.
        attempts += 1
        #Verificando se a tentativa está correta.
        if guess == random_numbers:
            print(f"Congratulations {name}! You guessed the correct number in {attempts}attempts.")
            break
        else:
            if guess < random_numbers:
                print("Try a higher number. ")
            else:
                print("Try a lower number.")


