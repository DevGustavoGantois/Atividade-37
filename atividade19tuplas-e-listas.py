#Faça um programa que leia 10 números e depois mostre o maior e o menor números lidos
numbers=[int(input(f"Enter a number {i + 1}:"))for i in range (10)]

higher_number=max(numbers)
smallest_number=min(numbers)
print("<----------------------------------------------->")
print(f"The bigger number is {higher_number}.")
print(f"The smaller number is {smallest_number}.")

#EXPLICAÇÃO DO CÓDIGO:
#1.Criei uma lista e dentro dessa lista um input para o usuário digitar os 10 números que ele escoler com a variável numbers e dentro dessa lista usei o laço de repetição for para contar perguntar 10 vezes.
#2.Criei uma variável higher_number para mostrar o maior valor da lista e atribui a ele a função max que é usado para pegar o maior valor.
#3.Criei uma variável smallest_number para mostrar o menor valor da lista e atribui a ele a função min que é usada para pegar o menor valor.
#4.Usei o print para mostrar o maior valor da lista no terminal...
#5.Usei o print para mostrar o menor valor da lista no terminal... 


