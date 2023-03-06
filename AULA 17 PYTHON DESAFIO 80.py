print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=ATIVIDADE-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("""Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.""")
print('-='*40)
valores = []
for cadastro in range (1, 6):
    numeros = int(input(f'Digite o {cadastro} números:'))
    print(f'Adicionado a lista o valor {cadastro}')
    valores.append(numeros)
valores.sort()
print('-=-=-'*40)
print(f'O valores cadastrados são {valores}')