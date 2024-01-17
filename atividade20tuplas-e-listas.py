#Faça um programa que leia 10 números inteiros e separe os mesmos em pares e ímpares. Mostre
#quantos pares foram lidos, bem como o maior e o menor número par. Faça o mesmo para os ímpares.
pair_numbers=[]
odd_numbers=[]


for i in range (10):
    numbers=int(input(F"Enter a number {i + 1} -> "))

    if numbers % 2==0:
        pair_numbers.append(numbers)
    elif numbers % 2==1:
        odd_numbers.append(numbers)

print(f"The biggest number in pair numbers is {max(pair_numbers)}")
print(f"The smallest number in pair numbers is {min(pair_numbers)}")
print(f"The biggest number in odd numbers is {max(odd_numbers)}")
print(f"The smallest numbers in odd number is {min(odd_numbers)}")
print(f"The total pair numbers -> {len(pair_numbers)}")
print(f"The total odd numbers -> {len(odd_numbers)}")

#################################################################
#EXPLICAÇÃO DO CÓDIGO:
#1.Criei 2 listas vazias uma para colocar os números pares e uma para colocar os números ímpares.
#2.Usei o laço de repetição for para criar 10 perguntas.
#3.Os números que fossem pares ele colocaria na lista vazia através do método append que criei la em cima. E com os números impares usei a mesma lógica. 
#4.Usei os prints para mostrar os maiores números pares com a função max do Python, e fiz isso também para os menores números pares com a função min
#5.Usei a mesma lógica para os números ímpares, usei a função max e min
#6.No final dei um print e usei a função len para percorrer a lista toda para contar quantos pares a nessa lista. Fiz a mesma coisa com os números ímpares