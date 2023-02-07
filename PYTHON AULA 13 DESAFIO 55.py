print('                                                    ATIVIDADE                               ')
print('=================================================================================================')
print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.')
print('==============================================================================================================')
pesomaior = 0
pesomenor = 0
for p in range(1, 6):
        peso = float(input('Qual é o peso da {} pessoa:'.format(p)))
        if p == 1:
                pesomaior = peso
                pesomenor = peso
else:
        if peso > pesomaior:
                pesomaior = peso
        if peso < pesomenor:
                pesomenor = peso
print('O peso maior lido foi {}Kg'.format(pesomaior))
print('O peso menor lido foi {}Kg'.format(pesomenor))

