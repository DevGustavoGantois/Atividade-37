#Faça um programa que leia o nome de uma pessoa e imprima o mesmo invertido

name = input("Enter your username:")

inverse_name=name[::-1]

print(inverse_name)

#Faça um programa que leia 4 notas de um aluno e imprima sua média. Após a média ser calculada, informe se o aluno foi ou não aprovado.
#a.Aprovado ---média maior ou igual a 7
#b.Reprovado ---média menor que 5
#c.Em recuperação -- média entre 5 e 7

notes=[]

for i in range (4):
    note = float(input(f"Please. Enter your note student {i + 1}:"))
    notes.append(note)

average =+ sum(notes) / len(notes)

if average >= 7:
    print(f'Your average = {average}. You were Approved.')
elif average <= 5:
    print(f"Your average = {average}. You were Recovery.")
else:
    print(f"Your average = {average}. You were Repproved.")

#Faça um programa que leia 10 números e depois mostre o maior e o menor números lidos.

numbers =[]

for i in range(10):
    number = int(input(f"Enter a number {i + 1}:"))
    numbers.append(number)

bigger_number = max(numbers) 
smallest_number =min(numbers) 

print(f"The Bigger number is = {bigger_number}")
print(f"The Smallest number is = {smallest_number}")

#Faça um programa que leia 10 números inteiros e separe os mesmos em pares e ímpares. Mostre quantos pares foram lidos, bem como o maior e o menor número par. Faça o mesmo para os ímpares.

numbers=[]
odd_numbers=[]
pair_numbers=[]

for i in range(10):
    number = int(input(f"Enter number {i + 1}:"))
    numbers.append(number)

    if number % 2 == 0:
        pair_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"The bigger pair numbers in list -> {max(pair_numbers)}.")
print(f"The smallest pair numbers in list -> {min(pair_numbers)}.")
print(f"The bigger odd numbers in list -> {max(odd_numbers)}.")
print(f"The smallest odd numbers in list -> {min(odd_numbers)}.")
print(f"The numbers in pair -> {pair_numbers}.")
print(f"The number in odd -> {odd_numbers}.")
print(f"The list -> {numbers}.")

#Faça um programa que leia 10 número inteiros e imprima a lista ordenada em ordem crescente e descrescente.
numbers=[]

for i in range(10):
    number = int(input(f"Enter a number {i + 1}:"))
    numbers.append(number)

inverse_order = sorted(numbers, reverse=True) 
ascending_order = sorted(numbers)

print("Ascending order:",ascending_order)
print("Inverse order:",inverse_order)

#Faça um programa que leia o nome de 4 vendedores e o valor total de venda que cada um realizou.
#Imprima na tela os 2 vendedores que mais venderam, ordem decrescente.
names=[]
total_sale=[]

for i in range(4):
    name = input(f"Enter your name {i + 1}:")
    sale = float(input(f"Enter your total sale ="))
    names.append(name)
    total_sale.append(sale)

#Econtrar os dois vendedores que mais venderam em ordem decrescente:
sorted_sellers = sorted(zip(names, total_sale), ley=lambda x: x[1], reverse=True)

#Imrpimir os dois vendedores que mais venderam:
print("Top 2 sellers in descending order:")
for seller, sale in sorted_sellers[:2]:
    print(f"{seller} -> Total Sale: {sale}.")


#faça um programa que leia os nomes de 3 nadadores que subirão ao pódio na ordem do primeiro colocado para o terceiro. Imprima na tela a posição do nadador e seu nome.

namesOfSwimmers=[]

for i in range(3):
    names = input(f"Enter your name Swimmer {i + 1}:")
    namesOfSwimmers.append(names)

positions = sorted(namesOfSwimmers, reverse=True)

for i, swimmer in enumerate(positions, start=1):
    print(f"The position -> {i}: {swimmer} ")

#Crie uma lista com valores variados e envie a mesma para uma função que irá imprimir essa lista.

def print_list(list):
    print("Print list:", list)

list = [11 ,32 ,44 ,18 ,56 ,90 ,182 ,222 ,89328, 4444]

print_list(list)

#Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.

list=[]

for i in range(5):
    numbers=int(input(f"Enter a number {i + 1} ->"))
    list.append(numbers)

print(f"The list is -> {list}")

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. (Use lista para armazenar as notas).

notes=[]

for i in range(4):
    note=float(input(f"Enter a note {i + 1}, student {i + 1} ->"))
    notes.append(note)
    average=sum(notes)/len(notes)

print(f"The average of class = {average:.2f}")
print(f"The value of 4 notes = {len(notes)}")

#Crie uma função que receberá duas listas de valores inteiros e irá imprimir a soma do item do primeiro índice da primeira lista, com o último item da segunda lista.

def print_lists(list1,list2):
    print(f"The value 1 is -> {list1}")
    print(f"The value 2 is -> {list2}")
    sum = list1[0] + list2[7]
    return sum

list1=[11,22,33,55,44,66,77,88,100]
list2=[43,1,2,23,4,3,200,40000]

result=print_lists(list1,list2)

print(f"The values of list 1 is -> {list1}")
print(f"The values of list 2 is -> {list2}")
print(f"The sum of lists = {result}")

#Crie uma lista com 5 valores inteiros variados. E crie uma função que irá receber essa lista e imprimir a soma de todos os valores da lista.
def print_List(list):
    print(f"The values of list = {list}")
    sum_list = sum(list_values)
    return sum_list

list_values=[22,40,95,11,100]

result_sum = print_List(list_values)

print("The result of sun:", result_sum)

#Escreva uma função que recebe uma lista x e retorna x concatenada com ela mesma.

def print_list(list):
    print(f"The list -> {list}")
    concatenad_list=list + list
    return concatenad_list

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

result_list = print_list(list)

print(f"The result of concatenad list --> {result_list} ")

#Crie uma lista com 5 valores inteiros e escreva uma função que receberá essa lista que irá retornar a soma dos três últimos itens da lista.
def print_list(my_list):
    print(f"The list --> {my_list}")
    sum_last_of_three= sum(my_list[-3:])
    return sum_last_of_three

my_list=[32,44,76,88,100]

result_sum_list=print_list(my_list)
print(f"The sum of three last items list is = {result_sum_list}.")

#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. (Use laços de repetição)

list_characters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
consonants_count=0

for char in list_characters:
    if char.lower() not in ['a','e','i','o','u']:
        consonants_count += 1

print(f"The consonant in list = {consonants_count}.")

#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

list_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pair_list_numbers=[]
odd_list_numbers=[]

for num in list_numbers:
    if list_numbers % 2 == 0:
        pair_list_numbers.apppend(num)
    else:
        odd_list_numbers.append(num)

print(f"The list of numbers = {list_numbers} ")
print(f"The list of pair numbers = {pair_list_numbers}")
print(f"The list of odd numbers = {odd_list_numbers}")

#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vector1= [1,2,3,4,5,6,7,8,9,10]
vector2=[11,12,13,14,15,16,17,18,19,20]
vector3=[]

for i in range(len(vector1)):
    vector3.append(vector1[i])
    vector3.append(vector2[i])

print(f"The vector 1 = {vector1}")
print(f'The vector 2 = {vector2}')
print(f"The vector 3 = {vector3}")

#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
list_age=[]
list_height=[]

for i in range(5):
    age = int(input(f"Enter your age {i + 1}:"))
    height = float(input(f"Enter your height {i + 1}"))
    list_age.append(age)
    list_height.append(height)


list_age.reverse()
list_height.reverse()

print(f"The Age in reverse order -> {list_age}")
print(f"The height in reverse order -> {list_height}")

#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em uma lista. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use uma lista de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.

import random

data_list=[]
counter_list=[0 ,0 ,0 ,0 ,0 ,0]

for _ in range(100):
    result = random.randint(1,6)
    data_list.append(result)
    counter_list[result - 1] += 1

print(f"Results of the 100 launches: {data_list}")
print("\n Number of times each value was obtained:")
for i in range(6):
    print(f"Value {i + 1}: {counter_list[i]} times.")