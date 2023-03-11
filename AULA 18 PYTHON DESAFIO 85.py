print('===========================================ATIVIDADE======================================================')
print("""Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
pares e impares em ordem crescente.""")
print('-='*40)
numero = [[], []]
valor = 0
for cont in range(1,8):
    valor = int(input(f'Digite o {cont}o número:'))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-='*40)
print(f'Todos os valores: {numero}')
numero[0].sort()
numero[1].sort()
print(f'Os valores pares diigtados foram: {numero[0]}.')
print(f'Os valores ímpares digitados foram: {numero[1]}.')



