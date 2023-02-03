print('======================================================ATIVIDADE==================================================')
print('que ele foi multado...')
print('A multa vai custar R$ 7,00 por cada Km acima do limite.')
print('================================================================================================================')
print('================================================================================================================')
carro = int(input('Qual a velocidade que o carro está andando?'))
if carro > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (carro-80) * 7
    print('Você deve pagar uma multa de R${:.2f}...'.format(multa))

