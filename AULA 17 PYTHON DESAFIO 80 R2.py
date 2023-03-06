print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=ATIVIDADE-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("""Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.""")
print('-='*40)
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-=-'*40)
print(f'Os valores digitados em ordem foram {lista}.') 
print('FIM DO PROGRAMA...')