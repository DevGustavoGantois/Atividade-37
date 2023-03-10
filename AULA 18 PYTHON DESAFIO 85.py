print("""Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
pares e impares em ordem crescente.""")
print('-='*40)
resp = []
numero = []
for cont in range(1,8):
    numero = int(input(f'Digite o {cont}o número:'))
    resp.append(numero)
print(f'Os valores pares são {resp % 2}')
print(f'Os valores ímpares são {resp % 3}')
resp.sort()




