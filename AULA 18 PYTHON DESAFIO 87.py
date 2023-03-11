print('=================================================ATIVIDADE======================================================')
print("""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
Aprimore esse Desafio, mostrando no final 
A)A soma de todos os valores digitados.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha.""")
print('-='*40)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]:'))
print('-='*40)
for l in range(0, 3):
    for c in range(0, 3):
       print(f'{matriz[l][c]:^5}', end='')
       if matriz[l][c] % 2 == 0:
           spar += matriz[l][c]
    print() 
print('-='*40)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O valor da segunda linha é {mai}.')
