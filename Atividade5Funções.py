#Crie uma função que receba dois números e retorne a multiplicação deles.

def multiplication_numbers(num1,num2):
    #Essa função retorna a multiplicação dos números solicitados pelo usuário
    multiplication = num1 * num2

    return multiplication

num1 = float(input('Enter a number 1:'))
num2 = float(input('Enter a number 2:'))

result_multiplication = multiplication_numbers(num1, num2)

print(f'The result of multiplication is -> {num1}x{num2}=',result_multiplication)