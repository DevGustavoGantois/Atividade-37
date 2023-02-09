print('                                                     ATIVIDADE                                             ')
print('===============================================================================================================')
print('Crie um programa que leia dois valores e mostre um menu na tela:')

print('[1]somar')

print('[2]multiplicar')

print('[3]maior')

print('[4]novos números')

print('[5]sair do programa')

print('Seu programa deverá realizar a operação solicitada em cada caso.')
print('---------------------------------------------------------------------------------------------------------------')
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('[1] SOMAR')
    print('[2]MULTIPLICAR')
    print('[3]MAIOR')
    print('[4]NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    int(input('>>>Qual sua opção:'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opção == 2:
        multipilicar = n1 * n2
        print('A multiplicação de {} x {} é {}'.format(n1, n2, multipilicar))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior =n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Informe o primeiro valor:'))
        n2 = int(input('Informe o segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=-'*10)
print('Fim do programa! Volte sempre!!')





