print('                                     ATIVIDADE                                                                 ')
print('Escreva um programa que leia um número inteiro qualquer e peça para o usúario escolher qual será a base de conversão')
print('1 para binário, 2 para octal e 3 para hexadecimal.')
print('===================================================================================================================')
numero = int(input('Digite um número qualquer:'))
print('Converter para Binário: [1]')
print('Converter para Octal:[2]')
print('Converter para Hexadecimal:[3]')
opçao = int(input('Escolha qual será a base de conversão com as opções dadas acima:'))


if opçao == 1:
    print('{} convertido para Binário é igual a {}'.format(numero , bin(numero)[2:]))
elif opçao == 2:
    print('{} convertido para decimal é igual a {}'.format(numero , oct(numero)[2:]))
elif opçao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero , hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente...')