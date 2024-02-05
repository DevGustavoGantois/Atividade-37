#Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo.

def subtract_numbers(number1, number2):
    #Essa função retorna a subtração dos números solicitados pelo usuário.
    subtract = number1 - number2
    return subtract

number1 = float(input('Enter a number 1:'))
number2 = float(input('Enter a number 2:'))

result_subtract = subtract_numbers(number1, number2)
print(f'The number -> {number1} - {number2} =',result_subtract)