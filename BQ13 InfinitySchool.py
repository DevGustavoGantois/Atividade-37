print('===============================================ATIVIDADE================================================')
print('##'*40)
print('Faça um programa que receba 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve aparecer com uma frase que diga se o número é: ')
print('-par ou impar.')
print('-positivo ou negativo.')
print('Inteiro ou decimal.')
print('>>'*40)
numero1  =  float ( input ( "Digito ou numero 1: " ))
numero2  =  float ( input ( "Digito ou numero 2: " ))
operação  =  input ( "Digite a operação que deseja realizar: [+, -, /, *]: " )
print('=='*40)
if operação == '/':
    if numero1 and numero2 != 0:
        print('Esse número é inteiro.')
    else:
        print('O número é decimal.')
elif operação == '+':
    operação = numero1 + numero2
    print(f'A soma de {numero1} + {numero2} é = {operação}.')
elif operação == '-':
    operação = numero1 - numero2
    print(f'a subtração de {numero1} - {numero2} é = {operação}.')
elif operação == '*':
    operação = numero1 * numero2
    print(f'a multiplicação de {numero1} * {numero2} é = {operação}.')
print('=='*40)
print('FIM DO PROGRAMA, VOLTE SEMPRE!')




