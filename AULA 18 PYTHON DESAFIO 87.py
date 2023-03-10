print('=================================================ATIVIDADE======================================================')
print("""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
Aprimore esse Desafio, mostrando no final 
A)A soma de todos os valores digitados.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha.""")
print('-='*40)
matriz = [[0, 0, 0] [0, 0, 0] [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l} {c}]:'))
        