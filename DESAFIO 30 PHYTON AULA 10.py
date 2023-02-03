print('===================================Atividade================================================================')
print('=============================================================================================================')
print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR...')
print('========================================================================================')
numero = int(input('Digite um número qualquer:'))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número é {} IMPAR!'.format(numero))