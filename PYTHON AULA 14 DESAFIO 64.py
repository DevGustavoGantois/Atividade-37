print('-=-'*40)
print('                                                 ATIVIDADE                        ')
print('-=-'*40)
print('Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar')
print('o valor 999, que é a condição parada. No final mostre quantos números foram digitados e qual foi a soma entre eles')
print('(desconsiderando o flag).')
print('-=-'*40)
numero = cont = soma = 0
numero = int(input('Digite um número [999 para parar]:'))
while numero != 999:
        soma += numero
        cont += 1
        numero = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

