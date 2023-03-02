print('==============================================ATIVIDADE===========================================================')
print('Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. ')
print('Seu programa deverá ler um programa pelo teclado (entre 0 e 20) e mostra-lá por extenso.')
print('>>'*40)
extenso = ('um' , 'dois' , 'tres' , 'quatro' , 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    count_number = int(input('Digite um número entre 0 e 20: '))
    if count_number <= 0 and count_number <= 20:
        break
    print('Tente novamente. ', end = '')
print(f'Você digitou o número {extenso[count_number]}')
while True:
    pergunta = str(input('Você quer continuar [S/N]:')).strip().upper()
    if pergunta == 'Ss':
    while True:
        count_number = int(input('Digite um número entre 0 e 20:'))
    elif count_number <= 0 and count_number <= 20:
        break
    print('Tente novamente.', end ='')
    print(f'Você digitou o número {extenso[count_number]}')
    if  pergunta == 'Nn':
        print('FIM DO PROGRAMA...')
        print('Volte sempre.')
        break

                        
            
        
                
