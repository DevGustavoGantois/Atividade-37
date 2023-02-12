print('-=-'*40)
print('                                                           ATIVIDADE             ')
print('-=-'*40)
print('Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos')
print('os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')
print('-=-'*40)
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número:'))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e menor foi {]'.format(maior, menor))
