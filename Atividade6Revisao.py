#Receba uma lista de números e use funções agregadoras
#para contar quantos valores são ímpares e quantos são
#pares.

list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def number_odd_pair(numbers):
    odd_count = sum(1 for number in numbers if number % 2 == 1 )
    pair_count = sum(1 for number in numbers if number % 2 == 0 )
    return odd_count, pair_count

result_odd, result_pair = number_odd_pair(list_numbers)
print("Quantity of Odds:", result_odd)
print("Quantity of Pair:", result_pair)