print('                                                      ATIVIDADE ')
print('Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:')

print('-O primeiro valor é maior.')

print('-O segundo valor é maior.')

print('-Não existe valor maior, os dois são iguais')
print('------------------------------------------------------------------------------------------------------------')
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um segundo valor:'))
if n1 > n2:
    print('O primeiro valor é maior que o segundo valor.... valor = {}'.format(n1 , n2 ))
elif n1 < n2:
    print('O segundo valor é maior que o primeiro valor... valor = {}'.format(n2 , n1))
elif n1 == n2 :
    print('Não existe valor maior. Os dois valores são iguais... valor = {}'.format(n1 , n2))
