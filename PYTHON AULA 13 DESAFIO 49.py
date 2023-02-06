print('                                              ATIVIDADE                   ')
print('------------------------------------------------------------------------------------------')
print('Mostre a tabuada de um número que o usuário escolha usando somente o Laço de Repetição FOR.')
print('-------------------------------------------------------------------------------------------------')
print('TABUADA DE UM NÚMERO.')
numero = int(input('Digite um número:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, numero * c))

