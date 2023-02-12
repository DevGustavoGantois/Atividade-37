print('                                                ATIVIDADE                                      ')
print('-=-'*40)
print('Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar')
print('o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma')
print('entre eles, desconsiderando o flag.')
print('-=-'*40)
from time import sleep
numero = cont = soma = 0
while True != 999:
    numero = int(input('Digite um valor [999 para parar ]:'))
    soma = numero + numero
    cont += 1
    if numero == 999:
        break
    cont += 1
    soma += numero
sleep(2)
print('=='*20)
print(f'A soma dos {cont} valores {soma}.')
print('=='*20)








