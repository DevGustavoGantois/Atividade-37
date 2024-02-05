#Crie uma função que receba dois números e retorne a soma deles:

def numbers_sum(num1,num2,sum_numbers):
    #Está função retorna a soma de 2 números escolhidos pelo usuário.
    sum_numbers = num1 + num2
    return sum_numbers

num1 = float(input('Enter a first number:'))
num2 = float(input('Enter a second number:'))

result_sum = numbers_sum(num1,num2, numbers_sum)
print(f'The sum of {num1} + {num2} = ',result_sum)