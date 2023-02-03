print('                                                 ATIVIDADE                                                     ')
print('Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule e o preço da passagem, cobrando R$')
print('0,50 por KM para viagens de até 200KM e R$ 0,45 para viagens mais longas.')
print('==============================================================================================================')
print('==============================================================================================================')
print('RESPONDA:')
distancia = float(input('Qual a distancia da viagem em KM:'))
print('Você está prestes a começar uma viagem de {}KM.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('É o preço da sua passagem será de R$ {:.2f}'.format(preço))



