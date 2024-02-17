#Dada uma lista de números, crie uma nova lista contendo
#apenas os números pares.

list_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_pair = []

for numbers in list_numbers:
    if numbers % 2== 0:
        list_pair.append(numbers)

print(list_pair)

