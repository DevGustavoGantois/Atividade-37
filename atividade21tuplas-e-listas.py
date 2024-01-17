#Faça um programa que leia 10 números inteiros e imprima a lista ordenada em ordem crescente e
#decrescente.

numbers=[]

for i in range(10):
    number=int(input(f"Enter a number {i + 1} ->"))
    numbers.append(number)


ascending_order=sorted(numbers)
descending_order=sorted(numbers,reverse=True)

print(f"List in ascending order -> {ascending_order}")
print(f"List in descending order -> {descending_order}")

#EXPLICAÇÃO DO CÓDIGO:
#1.Criei uma variável numbers com uma lista vazia
#2.Usei um laço de repetição for para o usuário ter a entrada de 10 números
#3.Usei a variável numbers com a lista vazia para botar os numbers dentro com a função append
#4.Criei uma variável ascending order para mostrar os números da lista em ordem crescente com o método sorted(numbers)
#5.Criei uma variável descending order para mostar os números da lista em ordem decrescente com o método reserve=True
#6.Dei um print para mostrar a ordem crescente dos números.
#7.Dei um print para mostrar a ordem decrescente dos números.